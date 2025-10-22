import os
import re
import subprocess
import sys
import shutil
import logging
import platform

MARPS_PATH = 'marps'
DOCS_PATH = 'docs'
THEMES_PATH = 'themes'
TEMPLATE_PATH = 'template.html'
CURRENT_DIR = os.getcwd()

def check_docker():
    """Check if Docker is installed and the daemon is running."""

    try:

        result = subprocess.run(['docker', '--version'], capture_output=True, text=True)

        if result.returncode != 0:
            logging.error("Docker is not installed or not found in PATH.")
            return False

        logging.info(f"Docker found: {result.stdout.strip()}")

        info = subprocess.run(['docker', 'info'], capture_output=True, text=True)
        if info.returncode != 0:
            logging.error("Docker daemon is not running or you do not have permission to access Docker.")
            return False

    except FileNotFoundError:
        logging.error("Docker command not found. Please install Docker and ensure it is in your PATH.")
        return False

    except Exception as e:
        logging.error(f"Unexpected error checking Docker: {e}")
        return False

    return True

def marp_to_html(md_file_list):
    """Convert markdown files to HTML using Marp CLI in Docker."""

    logging.info(f"Processing: {md_file_list}")

    # Convert file list names to absolute paths using /home/marp/app/
    # replace backslashes to forward slashes for Docker compatibility
    arg_file_list = [os.path.join('/home/marp/app', os.path.relpath(md_file, CURRENT_DIR)).replace('\\', '/') for md_file in md_file_list]

    arguments = [
        'docker', 'run', '--rm',
        '-v', f'{CURRENT_DIR}:/home/marp/app',
        '-e', f'LANG={os.environ.get("LANG", "C.UTF-8")}',
    ]

    # Only set MARP_USER on Linux/Mac (GitHub Actions, etc.)
    if platform.system() != 'Windows':
        arguments.extend(['-e', f'MARP_USER={os.getuid()}:{os.getgid()}'])

    arguments.extend([
        'marpteam/marp-cli',
        *arg_file_list
    ])

    line = ' '.join(f'"{arg}"' if ' ' in arg else arg for arg in arguments)
    logging.info(f"Running command: {line}")

    if subprocess.run(arguments, encoding='utf-8', cwd=os.getcwd()).returncode != 0:
        raise RuntimeError(f"Marp CLI failed")

def move_html_to_docs(md_file_list):
    """Move generated HTML files to DOCS_PATH and return a map of HTML file to Marp folder."""

    html_folder_map = {}

    # Go through the list of files and move the generated HTML files to DOCS_PATH
    for md_file in md_file_list:
        generated_html = os.path.splitext(md_file)[0] + '.html'
        if not os.path.isfile(generated_html):
            logging.error(f"Expected generated HTML not found: {generated_html}")
            continue

        target_html = os.path.join(CURRENT_DIR, DOCS_PATH, os.path.basename(generated_html))

        html_folder_map[target_html] = os.path.dirname(md_file)

        logging.info(f"Moving {generated_html} to {target_html}")
        shutil.move(generated_html, target_html)

    return html_folder_map

def rewrite_image_links(html, marp_folder, base_url=None):
    """Rewrite image links in the HTML content."""

    # Normalize path separators for URLs
    marp_folder = marp_folder.replace('\\', '/')

    def src_repl(match):
        """Rewrite src="..." links."""
        quote = match.group(1)
        src = match.group(2)
        if src.startswith(('http://', 'https://', 'data:')):
            return match.group(0)

        url = f'{base_url}/{marp_folder}/{src}' if base_url else f'../{marp_folder}/{src}'
        logging.info(f"Rewriting image src '{src}' to '{url}'")
        return f'src={quote}{url}{quote}'

    def bg_quoted_repl(match):
        """Rewrite background-image:url("...") with quotes."""
        quote = match.group(1)
        src = match.group(2)
        if src.startswith(('http://', 'https://', 'data:')):
            return match.group(0)

        url = f'{base_url}/{marp_folder}/{src}' if base_url else f'../{marp_folder}/{src}'
        logging.info(f"Rewriting quoted background-image url '{src}' to '{url}'")
        return f'background-image:url({quote}{url}{quote})'

    def bg_entity_repl(match):
        """Rewrite background-image:url(&quot;...&quot;) with HTML entities."""
        src = match.group(1)
        if src.startswith(('http://', 'https://', 'data:')):
            return match.group(0)

        url = f'{base_url}/{marp_folder}/{src}' if base_url else f'../{marp_folder}/{src}'
        logging.info(f"Rewriting entity-quoted background-image url '{src}' to '{url}'")
        return f'background-image:url(&quot;{url}&quot;)'

    def bg_unquoted_repl(match):
        """Rewrite background-image:url(...) without quotes."""
        src = match.group(1)
        if src.startswith(('http://', 'https://', 'data:')):
            return match.group(0)

        url = f'{base_url}/{marp_folder}/{src}' if base_url else f'../{marp_folder}/{src}'
        logging.info(f"Rewriting unquoted background-image url '{src}' to '{url}'")
        return f'background-image:url({url})'

    # Handle quoted src attributes
    html = re.sub(r'src=(["\'])([^"\']+)\1', src_repl, html)

    # Handle QUOTED background-image URLs (double or single quotes)
    html = re.sub(r'background-image:url\((["\'])([^"\']+)\1\)', bg_quoted_repl, html)

    # Handle HTML ENTITY quoted background-image URLs (&quot; or &#39;)
    html = re.sub(r'background-image:url\(&quot;([^&]+)&quot;\)', bg_entity_repl, html)
    html = re.sub(r'background-image:url\(&#39;([^&]+)&#39;\)', bg_entity_repl, html)

    # Handle UNQUOTED background-image URLs
    html = re.sub(r'background-image:url\(([^)"\'\s&]+)\)', bg_unquoted_repl, html)

    return html

def find_marps():
    """Find all markdown files in MARPS_PATH."""
    md_files = []
    for folder in os.listdir(MARPS_PATH):
        folder_path = os.path.join(MARPS_PATH, folder)
        if not os.path.isdir(folder_path):
            continue
        md_file = os.path.join(folder_path, f'{folder}.md')
        if os.path.isfile(md_file):
            md_files.append(md_file)
            logging.info(f"Found markdown file: {md_file}")
    return md_files

def process_images(html_folder_map, base_url=None):
    """Update image addresses in the generated HTML files."""

    presentations = []
    for html_file, folder in html_folder_map.items():
        logging.info(f"Updating image links in: {html_file}")
        # Rewrite image links
        with open(html_file, encoding='utf-8') as f:
            html = f.read()
        html = rewrite_image_links(html, folder, base_url)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        # Extract title
        m = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        title = m.group(1) if m else folder
        presentations.append((os.path.basename(html_file), title))


    # Sort presentations by title
    presentations.sort(key=lambda x: x[1].lower())
    return presentations


def clear_docs():
    """Clear the docs directory or create it if it doesn't exist."""

    if os.path.isdir(DOCS_PATH):
        logging.info(f"Clearing docs directory: {DOCS_PATH}")
        for fname in os.listdir(DOCS_PATH):
            fpath = os.path.join(DOCS_PATH, fname)
            if os.path.isfile(fpath):
                logging.debug(f"Removing file: {fpath}")
                os.remove(fpath)
            elif os.path.isdir(fpath):
                logging.debug(f"Removing directory: {fpath}")
                shutil.rmtree(fpath)
    else:
        logging.info(f"Creating docs directory: {DOCS_PATH}")
        os.makedirs(DOCS_PATH)

def generate_index_html(presentations):
    """Generate index.html from the list of presentations."""

    with open(TEMPLATE_PATH, encoding='utf-8') as f:
        template = f.read()

    items = [f'<li><a href="{fname}">{title}</a></li>' for fname, title in presentations]

    html = template.replace('{{PRESENTATIONS}}', '\n        '.join(items))

    output_path = os.path.join(DOCS_PATH, 'index.html')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    logging.info(f"Created main index at {output_path}")

def main():
    """Main function to generate presentations and index.html"""

    # Setup logging
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

    # Parse base_url from command line
    base_url = None
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
        logging.info(f"Using base URL for images: {base_url}")
    else:
        logging.info("No base URL provided, using relative image links.")

    if not check_docker():
        logging.critical("Docker is required to generate presentations. Exiting.")
        sys.exit(1)

    clear_docs()
    marp_files = find_marps()
    marp_to_html(marp_files)
    html_folder_map = move_html_to_docs(marp_files)
    presentations = process_images(html_folder_map, base_url)
    generate_index_html(presentations)

    logging.info("Documentation generation complete.")

if __name__ == '__main__':
    main()