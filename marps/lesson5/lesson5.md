---
marp: true
theme: custom
paginate: true
header: 'Linux Foundation & Embedded Linux - Nackademin IoT • 2025'
footer: 'Niklas Åkerlund &lt;<a href="mailto:niklas.akerlund@nackademin.se">niklas.akerlund@nackademin.se</a>&gt;'
class: invert
---

# Linux Foundation & Embedded Linux

[linuxfoundation.org](https://www.linuxfoundation.org/)

<!--

Linux foundation har tre uppdrag:

1. Stödja utvecklingen av Linux-kärnan
2. Främja användningen av Linux i företag
3. Utbilda nästa generations Linux-utvecklare

...och sponsrar Linus Torvald och andra utvecklare.

--->

---

## Platium, Gold & Silver members

- Linux Foundation sponsras av företag som använder Linux i stor skala.
- Dessa företag är med och styr utvecklingen av Linux.
- Exempel på medlemmar:
    - Platinum: Ericsson, Microsoft, Meta
    - Gold: Google, Sony, Toyota
    - Silver: AWS, IKEA, Spotify

<!--
 - Dessa företag bär en stor del av kostnaden för konferenser, utveckling, och infrastruktur.
 - Vilket gör det relativt billigt för enskilda utvecklare eller små företag att hänga på.
-->

---

## Enskilda utvecklare kan också bli medlemmar

- Individualt medlemskap kostar $99/år
- Får tillgång till kurser, certifieringar, och events

---

## Linux Foundation - Certifieringar

Linux Foundation erbjuder certifieringar för systemadministratörer och utvecklare:

**LFCS** - Linux Foundation Certified System Administrator

- Grundläggande Linux-administration
- Filsystem, användare, processer, nätverk

**LFCE** - Linux Foundation Certified Engineer

- Avancerad systemadministration
- Kubernetes, Docker, networking

**Mer info:** <https://training.linuxfoundation.org/certification/>

---

## Öva mer på Linux?

[linuxjourney.com](https://linuxjourney.com/) är en gratis, interaktiv guide för att lära sig Linux.
[labex.io](https://labex.io/) erbjuder praktiska labs i en virtual Linux-miljö.
[overthewire.org](https://overthewire.org/wargames/bandit/) har utmaningar för att lära sig Linux-kommandon.

---

## Mer allmän kodövning

[adventofcode.com](https://adventofcode.com/) - Årliga kodutmaningar i december.

---

## Vad är Yocto Project?

**Yocto Project** är ett build-system för att skapa custom Linux-distributioner för embedded systems.

- Full kontroll över vad som inkluderas
- Optimerat för specifik hardware
- Reproducerbara builds
- Industri-standard

**URL:** <https://www.yoctoproject.org/>

---

## YoctoRPI - Ett exempel-projekt

**YoctoRPI** är ett Git-repo som visar hur man bygger en custom Linux-image för Raspberry Pi.

**GitHub:** <https://github.com/nakerlund/YoctoRPI>

**Vad innehåller det?**

- Yocto layers för Raspberry Pi
- Custom recipes för IoT-applikationer
- Exempel på Bluetooth LE integration
- Build-instruktioner

**OBS:** Detta är ett **showcase-projekt** - inte en övning vi gör nu.
Yocto är avancerat och tar lång tid att bygga.

---

## Varför visa YoctoRPI?

**För att illustrera:**

1. Linux kan anpassas helt för din hardware
2. IoT-enheter kör ofta custom Linux-distributioner
3. Det finns verktyg för att bygga från grunden
4. Open source ecosystem är kraftfullt

---

## Cellulära nätverk

    - GSM: Global System for Mobile Communications (2G, äldre standard som stängs ner)
    - UMTS: Universal Mobile Telecommunications System (3G, fortfarande i bruk)
    - LTE: Long Term Evolution (4G, helt IP-baserat till skillnad från 3G)
    - 5G: Fifth Generation (New Radio, högre hastigheter och lägre latens)
    - NB-IoT: Narrowband IoT (för lågdata, del av LTE och 5G)
    - eMTC: Enhanced Machine Type Communication (Cat-M1, del av LTE och 5G)

---

## Dyra IoT Abonnemang?

- 1nce (<https://1nce.com/>) erbjuder global täckning med en fast kostnad på 10€ för 10 år.
- Passar bra för IoT-enheter med låg dataanvändning.

---

## Roaming och IoT

- I hemlandet sker inte roaming och man är fast i ett nätverk.
- Utomlands kan enheten automatiskt byta till ett lokalt nätverk.
- Bästa täckingen i Svergie för IoT får man därför med ett utländskt SIM-kort i teorin.

---

## Modem moduler

- Kör egna firmware och hanterar radiokommunikation.
- Kommunicerar med host via AT-kommandon över seriell port (UART, USB).
- Qualcomm baserade moduler är vanliga.

---

## Moduler på Linux

- Strömsätting och styrning av SIM-kort sker ofta via GPIO.
- AT -kommandon skickas via seriell terminal (minicom, screen).
- ModemManager och NetworkManager kan hantera modemet automatiskt.

---

## Extra resurser - srsRAN

[srsRAN](https://docs.srsran.com/) är en open source 4G/5G software radio stack.

<!--

Lagstifting tvingade operatörer att jobba med open source för att möjliggöra konkurrens och transparens.
-->

---

## Raspberry Pi 4G / 5G basstation

<https://docs.srsran.com/projects/4g/en/next/app_notes/source/pi4/source/index.html>

- Sätta upp ett eget 4G-nätverk (för labb-syfte)
- Testa cellular connectivity utan operatör
- Lära dig hur 4G/5G fungerar på djupet
- Kräver SDR hårdvara (t.ex. USRP B200)
