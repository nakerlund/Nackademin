---
marp: true
theme: custom
class: invert
paginate: true
header: IoT Projekt • Nackademin IoT
footer: 'Niklas Åkerlund <niklas.akerlund@nackademin.se>'
---

# IoT Projekt

## Drönare vs 3D-skrivare

- 🛸 Drönare: **Batteri**, **Realtidslager**, **Failsafe**
- 🖨️ Skrivare: **Ström**, **Host-styrd**, kan **pausa**
- Olika krav på **sensorer**, **motorstyrning**, **test**

[PX4](https://px4.io) • [ArduPilot](https://ardupilot.org) • [Klipper](https://www.klipper3d.org) • [Marlin](https://marlinfw.org)

<!-- presenter:
FC måste rädda sig själv; skrivaren kan stoppa säkert. Sätt scenen för resten.
-->

---

## Motorstyrning – jämförelse

- 🛸 BLDC + **FOC** (sinus-PWM ~20–48 kHz) via **ESC**
- 🖨️ Stegmotor + **mikrostegning** (STEP/DIR; intern PWM ~20–50 kHz)
- Gemensamt: **MOSFET-bryggor**, **gate-drivers**, **shuntar**
- Skillnad: **Closed-loop moment** (BLDC) vs **Open-loop position** (stepper)

[VESC/FOC](https://vesc-project.com) • [BLHeli](https://blheli.info) • [Trinamic/TMC](https://www.trinamic.com)

<!-- presenter:
Samma kraftkomponenter, olika styrfilosofi. FOC/observer vs strömprofil i mikrosteg.
-->

---

## Stegfel & feedback (3D-skrivare)

- **Sensorless stall-detect** (TMC), **hall/encoder** vid behov
- **Closed-loop steppers** i avancerade system
- Fel → **pause** & re-home (ej personsäkerhetskritiskt)

<!-- presenter:
Sensorlös detektion vanlig; encoder där kvalitet/hastighet kräver det.
Closed-loop betyder att stegmotorer automatiskt kan korrigera för missade steg.

Sensorless betyder att systemet kan detektera rotorposition via back-EMF utan extra sensorer. Det gör att man måste köra ett par varv för att initialisera rotorpositionen vid start.
-->

---

## Sensorer – jämförelse

- 🛸 IMU, **baro**, **GPS**, **IR/ToF/LiDAR**, magnetometer
- 🖨️ Endstops, **Z-probe**, ev. accelerometer (input shaping)
- Närmark: **IR/ToF** (AGL); baro = relativ AMSL
- Skrivare → **homing** (relativt)

<!-- presenter:
Drönare: kontinuerlig positionsuppskattning. Skrivare: referens + determinism.
-->

---

## Realtidslager vs Planeringslager

- **Realtids-MCU**: FOC/PWM/mikrosteg, sensorfusion, **failsafe**
- **Host**: mål, planering, UI
- **Timing/Jitter**: host stör ej drift → **buffer/lookahead**

<!-- presenter:
All smoothness nära hårdvaran. Host levererar kommandon i god tid, inte “puls för puls”.
-->

---

## Failsafe – exempel (drönare)

- **Low battery** → **Autoland** (hellre vatten än risk)
- **Link-loss** → **Hover/Climb/RTH** enligt batteri + trend
- **Sensorfel** → fallback (IMU↔baro↔GPS), begränsad manöver

<!-- presenter:
Beslut lokalt i FC. Prioritet: personsäkerhet > uppdrag > utrustning.
-->

---

## Batterisäkerhet

- **BMS**: SOC/spänning/cellbalans, cutoff, logg
- **Termiskt skydd**, kortslutning, rusning
- **OTA-energireserv** + rollback (ej brick)
- Standarder: **UN 38.3**, **IEC 62133**, **UL 2054**

[UNECE UN38.3](https://unece.org) • [IEC](https://iec.ch) • [UL](https://ul.com)

<!-- presenter:
Batteri = eget säkerhetsområde. HIL-testa cutoff/OTA/rollback.
-->

---

## Autonomi ⇒ Komplexitet

- Fler **tillstånd** & **övergångar**
- Större **testyta** (fler felvägar)
- Mer **tid** & **risk** om ej planerat

<!-- presenter:
Det är beslutsgrafen som växer – inte antalet motorer i sig.
-->

---

## Komplexitetsbudget

- **Definition**: logik + felvägar + testyta teamet kan bära
- Mät: **taktkvot** (skapade/stängda) < 1.0; **regressioner** ↓
- Vid >1.0: **feature-frys**, **refaktor**, **test**

<!-- presenter:
Som “error budget” men för beslutslogik. När kvoten tippar – frys och köp kapacitet med test/refaktor.
-->

---

## Burndown & budget

- Inom budget → sjunkande kurva
- Nära tak → planar ut
- Över tak → stiger/fryser
- Åtgärd: **frys + refaktor + HIL/automation**

<!-- presenter:
Burndown visar symptom; orsaken är överskriden komplexitetsbudget.
-->

---

## HIL – varför och när

- Fångar **realtidsfel**, **race**, **failsafe** i labb
- Kör HIL vid **varje commit/PR** (autonoma system)
- Ekonomi: tidigt fel ≪ sent fel (fält)

<!-- presenter:
HIL ökar komplexitetsbudgeten. Automatisera riggen och koppla till CI.
-->

---

## Testspecifikation

- **Scenarier** (trigger → förväntat)
- **Failsafe** (low-bat, link-loss, sensorfel)
- **Pass/Fail**, loggning, ansvar
- Driver regression & HIL-automation

<!-- presenter:
Testspec = kontrakt och scope-kontroll. Möjliggör automation och regressionsdisciplin.
-->

---

## Known issues / Deviations

- **Spec-referens**, **riskklass**, **mitigation**, **expiry**
- **HIL-cover** per avvikelse
- Blockerande risker → ej skeppbara

[CISA VEX](https://www.cisa.gov)

<!-- presenter:
Avvikelser ok om kontrollerade, riskklassade, tidsatta och testtäckta.
-->

---

## Säkerhet för alla IoT (generellt)

- **SBOM** (SPDX/CycloneDX), **CVE**-bevakning, **VEX**
- **Secure Boot**, **signerad OTA** (**A/B + rollback**)
- **Incidentprocess**, spårbarhet, supportperiod
- EU-ramverk (ex. **CRA**)

[SPDX](https://spdx.dev) • [CycloneDX](https://cyclonedx.org) • [NVD](https://nvd.nist.gov) • [CRA](https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-factsheet)

<!-- presenter:
Gäller alla uppkopplade produkter – skrivare inklusive. Processen minskar överraskningstickets.
-->

---

## Flygspecifika krav (utöver generellt)

- **Flygsäkerhet** (EASA), riskklassning, geofencing, fjärr-ID
- Dokumenterad **failsafe** + verifiering
- **HIL** = nödvändigt
- Spårbar uppdateringshistorik

[EASA](https://www.easa.europa.eu)

<!-- presenter:
Flygkraven läggs ovanpå de generella IoT-kraven. Hög personsäkerhet ⇒ striktare process.
-->

---

## Drönare vs 3D-skrivare – sammanfattning

- Byggstenar: **MOSFET**, **gate-drivers**, **sensorer**
- Arkitektur: **autonomi** vs **host**
- Test: **HIL obligatoriskt** vs “nice-to-have”
- Säkerhet: **SBOM/CVE/OTA**; flyg har extra lager

<!-- presenter:
Samma teknik – olika ansvar. Autonomin driver komplexitet, test och regulatorik.
-->