---
marp: true
theme: custom
paginate: true
header: 'Bluetooth • 2025'
footer: 'Niklas Åkerlund &lt;<a href="mailto:niklas.akerlund@nackademin.se">niklas.akerlund@nackademin.se</a>&gt;'
class: invert
math: mathjax
---

# Var Kung Harald Blåtands blåa tand svart?

<!--
Kring år 1000 så betydde blå snarare mörk eller svart.
blár hrafn (fornisländska) → “blå korp” = svart korp.
blár kyrtill / blár serkr → mörk (blåsvart) tunika/rock.
-->

---

## 1990s: Wi-Fi och Bluetooth

- 1990 → NCR/AT&T WaveLAN protyper på 900 MHz
- 1991 → NCR/AT&T WaveLAN 2.4 GHz (1 Mbit/s)
- 1994 → IEEE 802.11 arbetsgrupp bildas (från WaveLAN)
- 1994 → Ericson i Lund vill ersätta RS-232 med radio (2.4 GHz FHSS)
- 1995 → Bluetooth-arbetet inleds

<!--
2.4 GHz ISM-bandet → Wi-Fi + Bluetooth pionerades av microvågsugnar.
Microvågsugnar funkar på 2.45 GHz → bandet är öppet och globalt.
Microvågsugnar kom i sin tur från upptäckten av radar på 2.4 GHz under andra världskriget smälte choklad i fickan på vetenskapsmannen Percy Spencer. Han fick trots den upptäckten tre barn.

Används också av trådlösa telefoner, babyvakter, trådlösa möss och tangentbord, Zigbee, Z-Wave, Thread, DECT, vissa satellitkommunikationer och mikrovågsradio.
-->

---

## 1999: Bluetooth 1.0 (IEEE 802.15.1)

- Bandbredd upp till 1 Mbit/s (1mb på 1 sekund)
- Räckvidd upp till 100 m (Class 1)
- Star-topologi med master/slave (1:N)
- 79 kanaler à 1 MHz i 2.4 GHz ISM-bandet

<!--
https://www.aftonbladet.se/teknik/a/oR6zeB/ericsson-utvecklar-ny-hemlig-supermobil
-->

---

## 2001: Bluetooth 1.1

- RFCOMM (serial port emulation)
- L2CAP (Logical Link Control and Adaptation Protocol)
- SDP (Service Discovery Protocol)
- Användes först i T39 med headsettet HBH-10

<!--
 Praktisk funktionalitet för att ersätta RS-232 kablar.
 Tillbehör 2001 med T39: headset, bilkit, skrivare, PDA.
-->

---

## 2003: Bluetooth 1.2

- Snabbare anslutning (snabbare hopphoppning)
- Snabbare datahastighet (1.2 Mbit/s)
- Mer robust mot störningar (adaptive frequency hopping, AFH)
- Stöd för EDR (Enhanced Data Rate, 2–3 Mbit/s)
<!--
 EDR = 2 Mbit/s med GFSK, 3 Mbit/s med π/4-DQPSK
-->
---

## 2004: Bluetooth 2.0 + EDR

- EDR (Enhanced Data Rate) upp till 3 Mbit/s
- Lägre energiförbrukning (EDR = mindre tid i luften)
- Bakåtkompatibel med 1.x
<!--
 EDR = 2 Mbit/s med GFSK, 3 Mbit/s med π/4-DQPSK
-->
---

## 2009: Bluetooth 3.0 + HS

- High Speed (HS) med Wi-Fi (802.11) för dataöverföring
- Bluetooth används för att upprätta och hantera anslutningen
- Upp till 24 Mbit/s med 802.11 (Bluetooth max 3 Mbit/s)
- Används för snabba filöverföringar
<!--
 HS = 802.11 (Wi-Fi) för dataöverföring
-->

---

## 2010: Bluetooth 4.0/4.1/4.2 (BLE)

- Bluetooth Low Energy (BLE) för låg energiförbrukning
- Upp till 1 Mbit/s (1mb på 1 sekund)
- GATT (Generic Attribute Profile) för datautbyte

<!--
    Modern bluetooth för sensorer och IoT
    4.1, 2013: bättre samarbete med LTE
    4.2, 2014: IPv6 över BLE (6LoWPAN)
-->

---

## 2016: Bluetooth 5.0

- Upp till 2 Mbit/s med BLE (1mb på 0.5 sekund)
- Upp till 4× räckvidd (500–1000 m med Coded S=8)
- 8× större annonskapacitet (255 byte)
- Stöd för mesh-nätverk (BLE Mesh)

<!--
    Mer IoT: längre räckvidd, snabbare, mesh
    Bluetooth longrange med Coded PHY (S=2, S=8)
-->

---

## Bluetooth 5.1

- Introducerade riktad annonsering (Direction Finding)
- Förbättrad platsbestämning (Indoor Positioning)
- Stöd för flerkanalsljud (Multi-Stream Audio)

<!--
    Riktad annonsering med AoA (Angle of Arrival) och AoD (Angle of Departure)
    Förbättrad platsbestämning med riktade antenner men kan inte jämföras med UWB som används i Apple AirTags.
-->

---

## 2020: Bluetooth 5.2

- LE Audio med LC3 codec (Low Complexity Communication Codec)
- Multi-Stream Audio (flera samtidiga ljudströmmar)
- Isochronous Channels för synkroniserad dataöverföring
- Förbättrad energihantering (LE Power Control)

<!--
    Nytt ljudlager med LC3 codec. Tidagre har Samsung och Apple egna codecs. Nu finns en standard.
    LE Audio möjliggör också Audio Sharing (1:N) och Broadcast Audio (1:Many) med Auracast.
    Isochronous Channels för synkroniserad dataöverföring, t.ex. för hörselhjälpmedel.
    Förbättrad energihantering med LE Power Control.
-->
---

## Bluetooth familjen

| Category | Data Rate | Range | Power | Topology | Typical Use |
|-----------|-----------|-------|--------|-----------|-------------|
| **Classic** (BR/EDR) | 1–3 Mbit/s | 10–30 m | ⚡ Med | Star | Audio, SPP |
| **BLE 1 M** | 1 Mbit/s | 30–50 m | 🌿 Low | Star | Sensors |
| **BLE Coded S=8** | 125 kbit/s | 500–1000 m | 🌿 Low | Star | Long range IoT |
| **BLE Mesh** | ~10 kbit/s | Multi-hop | 🌿 Low | Many-to-many | Lighting |
| **LE Audio** | ≤ 2 Mbit/s | 10–30 m | ⚡ Med | 1:N | Headsets, etc. |

<!--
Det finns dessutom Bluetooth beacon som aldrig slog igenom.
-->
---

## LE Audio

- Nytt ljudlager med LC3 codec (Low Complexity Communication Codec)
- Multi-Stream Audio (flera samtidiga ljudströmmar)
- Audio Sharing (1:N) och Broadcast Audio (1:Many) med Auracast
- Stöd för hörselhjälpmedel (Hearing Aids Profile, HAP)
- Isochronous Channels för synkroniserad dataöverföring (ljud syncar så det inte blir eko)
- Funkar på IOS 17, Android 13+, Windows 11, Linux (BlueZ)

<!--
    LC3 codec: bättre ljudkvalitet vid lägre bitrates än SBC (Classic Bluetooth)
    Audio Sharing: dela ljud från en källa till flera mottagare, t.ex. i ett flygplan eller gym.
    Auracast: sändare kan skicka ljud till alla som vill lyssna, t.ex. i en butik eller på en konsert.
    Hearing Aids Profile (HAP): direkt stöd för hörapparater utan mellanliggande enhet.

    Men, inte okomprimerat perfekt ljud som med trådbundna hörlurar. I teorin borde man inte betala för mycket för trådlösa audiphil hörlurar om dom ändå begränsas av codec.
-->

---

## Platform Stöd

| Mode | Windows | macOS | Linux | Android | iOS | Embedded |
|------|----------|--------|--------|----------|------|-----------|
| Classic SPP | ✅ Client | ⚠️ | ✅ | ✅ | ❌ | ✅ |
| BLE GATT | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| BLE Mesh | ⚙️ | ⚙️ | ✅ | ✅ Proxy | ✅ Proxy | ✅ |
| LE Audio | ⚙️ | ⚙️ | ✅ Exp | ✅ | ✅ | ✅ |

<!--
 BlueZ är den enda stacken som stödjer allt från Classic, BLE, Mesh och LE Audio.
 Därför är en RPI med BlueZ ett bra val för utveckling och testning av hemmautomation med Bluetooth Mesh och LE Audio.
-->

---

## RFComm: Ersätt serieporthårdvara med mobilen

**Gammal hårdvara → Modern lösning:**

- 📍 **GPS-mottagare (RS-232)** → NMEA Android-app + RFComm
- 📦 **Streckkodsläsare (USB/RS-232)** → [HID Barcode Scanner](https://github.com/Fabi019/hid-barcode-scanner)

```text
Android App (GPS/Camera)
    ↓ NMEA / Barcode data
RFComm (SPP Profile)
    ↓ Virtual COM Port
Windows/Linux App
```

<!--
Demonstrera live: Öppna Google Earth Pro, anslut NMEA-appen, visa realtidsspårning.
Visa HID Barcode Scanner-appen och skanna något i rummet.
-->

---

## Bluetooth HID (Human Interface Devices)

**Bygg egna input-enheter med ESP32/Arduino:**

- ⌨️ **Keyboard/Mouse:** Custom macro keyboards, fotpedaler, switches
- 🎮 **Game Controllers:** Racing wheels, flight sticks, custom gamepads
- 🎵 **MIDI Controllers:** Synth/drum pads → DAW (GarageBand, Ableton)
- 📱 **Media Controls:** Play/pause, volym, skip (utan att ta fram mobilen)
- ♿ **Accessibility:** Custom switches för funktionsnedsättning

<!--
    ESP32 har inbyggt stöd för Bluetooth HID.
    Använd Arduino IDE med ESP32-biblioteket.
    Exempel:

    Jag har alltid haft en idé med anslagskänsligt tangentbord som skriver stora bokstäver när man trycker hårt.
-->

---

## GATT Profiles

- ❤️ Heart Rate Profile (0x180D)
- 🩸 Blood Pressure Profile
- 🍬 Glucose Profile
- ⚖️ Weight Scale Profile (0x181D)
- 🚴 Cycling Speed & Cadence
- 🔋 Battery Service (0x180F)
- 🌡️ Environmental Sensing (0x181A)
- 🕰️ Current Time Service (0x1805)

<https://www.bluetooth.com/specifications/gatt/services>

<!--
    Standardiserade profiler för hälsosensorer och andra vanliga enheter.
    Används ofta i wearables och fitness trackers.
    Bluetooth SIG har en fullständig lista:
    https://www.bluetooth.com/specifications/gatt/services/
-->
---

## Men GATT standarder följs inte alltid

1. 🔒 **Vendor lock-in** - Tvinga till deras app
2. 📊 **Data mining** - Samla användardata
3. 💰 **Ecosystem** - Sälja fler produkter
4. 😴 **Lathet** - Enklare att kopiera egen kod

**Undantag:** HID - funkar eftersom OS kräver standarden

<!--
Detta är frustrerande för både utvecklare och användare
Standarderna FINNS men följs inte konsekvent
Apple kräver att keyboards/möss använder HID, därför funkar det
Men för health devices finns ingen enforcement
-->

---

## IoT Protokoll - Energiförbrukning & Användning

| Protokoll | Strömförbrukning | Räckvidd | Data Rate | Batteriliv | Topologi |
|-----------|------------------|----------|-----------|------------|----------|
| **BLE** | 10-50 mW (TX) | 10-100m | 1-2 Mbps | 1-5 år | Star/Mesh |
| **Zigbee** | 15-60 mW (TX) | 10-100m | 250 kbps | 1-3 år | Mesh |
| **Thread** | 15-60 mW (TX) | 10-100m | 250 kbps | 1-3 år | Mesh (IPv6) |
| **LoRaWAN** | 10-100 mW (TX) | 2-15 km | 0.3-50 kbps | 5-10 år | Star |
| **Wi-Fi** | 100-300 mW (TX) | 50-100m | 1-600 Mbps | Dagar | Star |
| **NB-IoT** | 100-500 mW (TX) | 10+ km | 20-200 kbps | 3-10 år | Star (Cellular) |

<!--
Strömförbrukning varierar enormt beroende på duty cycle
Sleep current är ofta viktigare än TX current för batteriliv
BLE Mesh konkurrerar direkt med Zigbee/Thread
LoRaWAN för långdistans sensorer (parkering, jordbruk)
NB-IoT/LTE-M för mobila enheter
-->

---

## Mesh och batteridrivna noder

- **Mesh-nätverk** (Zigbee, Thread, BLE Mesh) använder multi-hop routing för att öka räckvidden och pålitligheten.
- **Batteridrivna noder** kan vara "sleepy" och bara vakna för att skicka/ta emot data, vilket sparar energi men gör att de inte kan routa trafik hela tiden.
- **Router-noder** är ofta nätanslutna och alltid vakna för att hantera trafik i nätverket.
- **Wakeup window**: batteridrivna noder måste ha ett schema för när de är vakna för att ta emot meddelanden.

---

## Hitta enheter: Bluetooth Classic

Bluetooth Classic - Device Discovery

- Söker efter **alla** enheter i närheten
- Enhet måste vara i "discoverable mode"
- Returnerar: Name, MAC address, Device Class
- Långsam: 10-12 sekunder per scan
- Hög energiförbrukning

---

## Hitta enheter: Bluetooth Low Energy (BLE)

BLE - Advertising Scan

- Lyssnar på **advertising packets**
- Enheter broadcastar kontinuerligt (passiv)
- Returnerar: Name, MAC, RSSI, Service UUIDs, Manufacturer data
- Snabb: Kontinuerlig stream (millisekunder)
- Låg energiförbrukning

<!--
BLE advertising är unidirektionellt tills connection
Classic discovery kräver inquiry response från båda sidor
BLE kan scanna utan att connecta (beacons)
iOS begränsar BLE scanning i bakgrunden
-->

---

## Parkoppling (Pairing & Bonding)

Pairing = Engångsautentisering
Bonding = Spara nycklar för framtida anslutningar

Bluetooth Classic:

- PIN-kod (4-16 siffror)
- SSP (Secure Simple Pairing) - Numeric comparison, Passkey entry

BLE:

- Just Works (ingen användarinteraktion)
- Passkey Entry (6 siffror)
- Numeric Comparison
- Out of Band (NFC, QR-kod)

<!--
Pairing = autentisering, Bonding = spara Long Term Key (LTK)
Just Works = ingen säkerhet, man-in-the-middle möjlig
Passkey Entry = användaren matar in 6-siffrig kod
Numeric Comparison = båda enheter visar samma kod, användaren bekräftar
Out of Band = använd NFC eller QR-kod för att utbyta nycklar
iOS kräver pairing för vissa GATT operations (write)
Android mer flexibelt - kan läsa många services utan pairing
HID kräver alltid pairing (säkerhet)
-->

---

## Python Bluetooth-bibliotek

- BLE: `bleak` - Async, cross-platform, rekommenderas
- Bluetooth Classic: `pybluez` - RFComm/SPP support

| Bibliotek | Windows | macOS | Linux | Classic | BLE |
|-----------|---------|-------|-------|---------|-----|
| **bleak** | ✅ | ✅ | ✅ | ❌ | ✅ |
| **pybluez** | ✅ | ⚠️ | ✅ | ✅ | ❌ |

<!--
Bleak använder native APIs: Windows BLE API, macOS Core Bluetooth, Linux BlueZ
PyBluez på macOS är problematiskt - kompileringsfel vanliga, använd bleak istället
PyBluez är gammalt men funkar bra för Classic RFComm på Windows/Linux
Raspberry Pi: BlueZ ger bäst stöd för både Classic och BLE
pip install bleak
pip install pybluez (eller pybluez2 för nyare version)
-->