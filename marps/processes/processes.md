---
marp: true
theme: custom
paginate: true
header: 'Arbetssätt'
footer: 'Niklas Åkerlund &lt;<a href="mailto:niklas.akerlund@nackademin.se">niklas.akerlund@nackademin.se</a>&gt;'
class: invert
math: mathjax

---

# Arbetssätt

---

## Företagstyper

- **Startups**: Små, snabbväxande företag med innovativa idéer; dynamisk miljö med breda yrkesroller.
- **Storföretag**: Etablerade företag med strukturerade processer; tydliga roller och karriärvägar.
- **Enskilda konsulter**: Självständiga specialister som erbjuder tjänster direkt till kunder; hög flexibilitet och självständighet.
- **Tech-hus**: Specialiserade företag som utvecklar produkter åt andra företag; snabba och varierande projekt.
- **Konsultföretag**: Anställer konsulter för kunduppdrag; variation i projekt och branscher, kräver anpassningsförmåga.

---

## Produktlivcykel

- **PoC**: Proof of Concept, som ofta byggs med utvecklingskit och slutar i ett mycket begränsat demo.
- **Utveckling**: Utveckling av hårdvara och mjukvara uppdelat i workpackages.
- **Prototyper**: "Board bring up" är en process där hårdvaruprototyperna startas för första gången, vilket kräver nära samarbete mellan hårdvaru- och mjukvaruteam.
- **Certifiering**: Med en fungerande prototyp kan precompliance tester för CE-märklning påbörjas. Sedan följer slutgiltiga certifieringen.
- **Industrialisering**: Skapande av produktionslinjen inklusive produktionstester och provisionering av enheterna.
- **Underhåll**: Mjukvara måste underhållas och uppdateras under produktens livslängd enligt CRA (Cyber reciliance act)

---

## Dokumentation och kravinsamling

Dokumentation är avgörande för att skapa en tydlig bild av systemets krav och specifikationer.

- **Systemspecifikation**: En övergripande beskrivning av systemet, dess syfte, funktioner och arkitektur.
- **Hårdvaruspecifikation (HW Specifikation)**: Detaljer om hårdvarukomponenter, inklusive processorer, sensorer och andra fysiska enheter som används i systemet.
- **Mjukvaruspecifikation (SW Specifikation)**: Beskrivning av mjukvarans funktionalitet, operativsystem, och gränssnitt mellan olika moduler.
- **Testspecifikation**: Detaljerade tester för att verifiera att både hårdvara och mjukvara fungerar enligt specifikationerna, inklusive testfall och testscenarier.

---

## Agila metoder

- Agila metoder som Scrum och Kanban används för att hantera projekt och förbättra samarbetet inom team. Scrum fokuserar på iterativ utveckling med korta sprintar, medan Kanban betonar kontinuerligt arbetsflöde och visualisering av uppgifter för att optimera produktiviteten.

<https://agilemanifesto.org>
<https://www.atlassian.com/agile/manifesto>

---

### Kanban

- **Kanban** används för kontinuerligt arbetsflöde, med fokus på att visualisera arbetet och begränsa mängden arbete som pågår samtidigt.
- Används ofta i underhålls- och supportteam där arbetsuppgifterna kommer in oregelbundet.
- **Kanban-tavla** med kolumner som "To Do", "In Progress", och "Done" för att spåra uppgifter.

---

### Scrum

- **Scrum** är en ramverk för att hantera komplexa projekt med iterativ utveckling i korta cykler kallade sprintar (vanligtvis 2-4 veckor).
- Teamet arbetar tillsammans för att planera, genomföra och granska arbetet i sprintar.
- Roller i Scrum:
    - **Utvecklingsteamet** utvecklarna som utför arbetet
    - **Scrum Master** planerar och faciliterar Scrum-processen och tar bort hinder samt leder sprintplanning, review och retrospective
    - **Produktägare** ansvarar för produktens vision och prioriteringar och äger produktbackloggen

<https://www.scrum.org/resources/what-is-scrum>

---

### Sprintar

- **Sprintplanering** för att bestämma vilka uppgifter som ska slutföras under sprinten.
- **Sprint review** för att demonstrera vad som har uppnåtts.
- **Sprint retrospective** för att reflektera över processen och identifiera förbättringsområden.
- **Daily stand-ups** för att synkronisera teamet och identifiera hinder.
- **Backloggen** innehåller alla uppgifter som ska utföras men som inte är tidsatta eller prioriterade. Det är inte med i sprinten förrän det är planerat.

---

### Jira

- Jira är ett populärt verktyg för att hantera projekt och uppgifter inom agila team
- Det stödjer både Scrum och Kanban. Det hjälper team att organisera sitt arbete, spåra framsteg och samarbeta effektivt genom att erbjuda funktioner som **backlog management**, **sprint planning**, och **issue tracking**.

<https://ifuckinghatejira.com>
