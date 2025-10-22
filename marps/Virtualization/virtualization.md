---
marp: true
theme: custom
paginate: true
header: 'Virtualization • Nackademin IoT'
footer: 'Niklas Åkerlund &lt;<a href="mailto:niklas.akerlund@nackademin.se">niklas.akerlund@nackademin.se</a>&gt;'
class: invert
---


# 🧭 Från Hårdvara till Moln

Vi använder Docker, VM, Wokwi, Kubernetes, WASM, Node.js...

Men var passar de egentligen in i stacken?

<!--
Målet: hjälpa studenter bygga en mental modell så de kan välja rätt verktyg för jobbet och felsöka snabbare.
-->

---

# 7-Lagersmodellen

```text
L6: Runtime          → Node.js, Python, JVM
L5: WASM Sandbox     → Wasmtime, Wasmer
L4: Container        → Docker, Snap
L3: Orkestrering     → Kubernetes, Compose
L2: Virtualisering   → VM, KVM, QEMU
L1: Emulering        → Wokwi, Renode
L0: Hårdvara         → ESP32, Pico, Arduino
```

WASM sitter mellan runtimes och containers som en portabel sandbox.

<!--
Tänk på det som OSI-modellen men för deployment. Varje lager bygger på det under. Studenter blandar ofta ihop dessa - att veta lagret hjälper förutsäga beteende.
-->

---

# Lager 0: Hårdvara

Fysiska enheter du kan röra vid.

- ESP32, Raspberry Pi Pico, Arduino
- Nativ hastighet (snabbast möjligt)
- Ingen isolering
- Produktionsmål

<!--
Det är här din kod faktiskt körs i IoT-projekt. Allt annat är antingen testning/utveckling eller gateway/molninfrastruktur.
-->

---

# Lager 1: Emulering

Testa firmware utan hårdvara.

| Verktyg | Syfte                  |
|---------|------------------------|
| Wokwi   | Arduino/ESP-simulering |
| Renode  | Komplex SoC-simulering |
| QEMU    | CPU-emulering          |

Mycket långsamt men deterministiskt. Bra för CI och tidig prototypning.

<!--
Studenter bör börja här innan de köper hårdvara. Wokwi är den enklaste ingången. Renode är för mer komplexa scenarion som nätverk mellan enheter.
-->

---

# Wokwi i Praktiken

- Webbaserad Arduino/ESP32-simulator
- Visuella komponenter (LED, sensorer, displayer)
- Delningsbara länkar för felsökning
- Integreras med VS Code
- Gratis för utbildningsbruk

Använd när: prototypning av kretsar, undervisning, CI-tester.

<!--
Visa studenter en snabb Wokwi-demo om möjligt. Den visuella feedbacken är utmärkt för lärande. Projekt kan delas via URL vilket är perfekt för fjärrhjälp.
-->

---

# Lager 2: Virtualisering

En komplett dator inuti din dator.

- Fullständigt OS med egen kärna
- KVM, QEMU, VirtualBox, Proxmox
- Stark isolering, långsam uppstart
- Måste boota hela OS

Använd när du behöver komplett OS-separation.

<!--
VM är overkill för de flesta studentprojekt men viktigt att förstå. Proxmox är vad du kan använda för att hantera en labbmiljö med flera VM.
-->

---

# Lager 3: Orkestrering

Hantera containers i skala.

| Verktyg        | Användningsfall     |
|----------------|---------------------|
| Docker Compose | Enskild host        |
| Kubernetes     | Multi-host kluster  |
| K3s            | Lätt K8s            |

Sitter ovanför containers, koordinerar dem.

<!--
Studenter hoppar ofta till K8s för tidigt. Börja med Compose. K3s är en bra mellanväg - det är riktig Kubernetes men lätt nog för Raspberry Pi.
-->

---

# Docker Compose Fördjupning

En enda YAML-fil beskriver flercontainer-appar:

```yaml
services:
  web:
    image: nginx
  db:
    image: postgres
  cache:
    image: redis
```

Ett kommando: `docker-compose up`

<!--
Det är här studenter bör börja för flerserviceprojekt. Mycket enklare än K8s. Bra för gateway-projekt med databas, API och frontend.
-->

---

# Lager 4: Containers

Snabb isolering med värdkärnan.

- Docker, Snap, Flatpak
- Delar värdkärna (inget separat OS)
- Namespaces, cgroups för gränser
- Startar på millisekunder

Varför det är snabbt: bara processkapande, ingen boot.

<!--
Docker är det viktigaste verktyget i denna presentation för studenter att bemästra. Det överbryggar utveckling och produktion. Snap är liknande men mer låst - nämn det så studenter förstår mönstret.
-->

---

# Docker i Praktiken

Vad studenter bör veta:

- `Dockerfile` → recept för image
- Image → mall (oföränderlig)
- Container → körande instans
- Volume → persistent data
- Network → containerkommunikation

Docker är inte en VM - den delar värdkärnan.

<!--
Vanlig förvirring: studenter tror Docker är som VirtualBox. Betona att det bara är isolerade processer. Visa hur snabb `docker run` är jämfört med att boota en VM.
-->

---

# Lager 5: WASM Sandbox

WebAssembly ger portabel, säker sandboxing.

| Egenskap  | WASM          | Container    |
|-----------|---------------|--------------|
| Uppstart  | Sub-ms        | ~0.5–1s      |
| Isolering | Stark         | OS-nivå      |
| Overhead  | Mycket låg    | Låg          |
| Syscalls  | Explicit bara | Full access  |

Använd för: plugins, edge compute, serverless-funktioner.

<!--
WASM är nyare och mer specialiserat. Studenter kommer inte använda det ofta än, men det växer inom edge computing. Bra när du behöver sandboxing utan Docker-overhead.
-->

---

# WASM Användningsfall

När WASM är meningsfullt:

- Pluginsystem (utöka appar säkert)
- Edge-funktioner (Cloudflare Workers)
- Flerspråksstöd (kompilera C/Rust till WASM)
- Opålitlig kodexekvering
- Sub-sekund cold starts krävs

Inte idealisk för: traditionella webbappar, full systemaccess.

<!--
WASM briljerar i scenarion där Docker är för tungt men du behöver mer isolering än en runtime ger. Cloudflare Workers är ett bra verkligt exempel.
-->

---

# Lager 6: Runtime

Där din kod exekverar.

| Runtime     | Isolering | Användningsfall |
|-------------|-----------|-----------------|
| Node.js     | Låg       | Webbappar, API  |
| Python venv | Låg       | Script, ML      |
| JVM         | Medel     | Enterprise      |

npm och venv isolerar beroenden, inte exekvering.

<!--
Studenter bör förstå: venv förhindrar beroendekonflikt, men sandboxar inte koden. För riktig isolering behöver du Docker eller WASM.
-->

---

# Hastighet vs Isolering

| Lager         | Uppstart  | Isolering   | Overhead    |
|---------------|-----------|-------------|-------------|
| Runtime       | <100ms    | Låg         | Ingen       |
| WASM          | <10ms     | Hög         | Mycket låg  |
| Container     | <1s       | Hög         | Låg         |
| VM            | 10-60s    | Mycket hög  | Hög         |
| Emulering     | Minuter+  | Mycket hög  | Mycket hög  |

WASM erbjuder nästan runtime-hastighet med container-nivå isolering.

<!--
Det här är den viktiga avvägningen. Börja högst upp (lättast) och gå nedåt bara när du behöver mer isolering. De flesta studentprojekt behöver containers som mest.
-->

---

# Lager Stackas

Verkliga system använder flera lager:

```text
Node.js-app
  → inuti Docker
    → på Kubernetes
      → på VM
        → på bare metal
```

Ett annat exempel:

```text
ESP32-firmware
  → testad i Wokwi
  → gateway i Docker
  → WASM-plugins på edge
  → backend på K8s
```

<!--
Betona: dessa är inte alternativ, de stackas. En produktionsapp kan använda 4-5 av dessa lager samtidigt. Varje löser ett olika problem.
-->

---

# IoT Exempel

| Komponent     | Lager | Teknik         |
|---------------|-------|----------------|
| Sensorkod     | L0    | Pico 2 W       |
| Testning      | L1    | Wokwi          |
| Edge-plugins  | L5    | WASM           |
| Gateway       | L4    | Docker Compose |
| Moln          | L3    | Kubernetes     |
| Dashboard     | L6    | Node.js        |

Varje komponent använder rätt lager för jobbet.

<!--
Gå igenom detta exempel: sensor samlar data (L0), du testar firmware först i Wokwi (L1), gateway aggregerar data i Docker (L4), molnet skalar med K8s (L3), dashboard byggd med Node (L6). Valfritt: edge-processning i WASM (L5).
-->

---

# Välja Lager

Fråga:

- Hårdvaruinteraktion? → L0 eller L1
- Beroeendeisolering? → L6 (venv, npm)
- Portabel sandbox? → L5 (WASM)
- Processisolering? → L4 (Docker)
- Flera tjänster? → L3 (K8s)
- OS-separation? → L2 (VM)

Börja på det lättaste lager som fungerar.

<!--
Det här är beslutsträdet. De flesta studentprojekt börjar på L6 för utveckling, flyttar till L4 (Docker) för deployment. L0/L1 för IoT-firmware. VM behövs sällan.
-->

---

# Pipelines & Automation

CI/CD-pipelines arbetar över flera lager:

```text
Git push
  → Testa firmware i Wokwi (L1)
  → Bygg Docker image (L4)
  → Testa i container (L4)
  → Deploy till K8s (L3)
  → Flash till hårdvara (L0)
```

Verktyg: GitHub Actions, GitLab CI, Jenkins

<!--
Moderna pipelines automatiserar hela flödet. Samma kod testas i emulering, containers och slutligen hårdvara. Detta ger snabb feedback och minskar manuellt arbete.
-->

---

# Pipeline Exempel

Typiskt IoT-projekt:

1. Kod committas → GitHub Actions triggas
2. Firmware testas i Wokwi (CI)
3. Gateway-kod byggs som Docker image
4. Integration tests körs i containers
5. Deploy till K3s på staging
6. Manuell godkännande
7. Deploy till produktion
8. OTA-uppdatering till ESP32-enheter

<!--
Pipelines gör repeaterbara deployments möjliga. Studenter bör lära sig grundläggande CI/CD tidigt. Börja enkelt: testa → bygg → deploya.
-->