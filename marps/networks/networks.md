---
marp: true
theme: custom
paginate: true
header: 'Nätverk och adresser'
footer: 'Niklas Åkerlund &lt;<a href="mailto:niklas.akerlund@nackademin.se">niklas.akerlund@nackademin.se</a>&gt;'
class: invert
math: mathjax
---

# Nätverk och adresser

![bg](mailboxes-1838667.jpg)

---

## IPv4-adresser: `192.168.0.1`

- 32 bitar, skrivs som 4 bytes i decimalform
- Varje byte representerar ett värde mellan 0 och 255
- Delas in i nätverksdel och värddel med hjälp av en nätmask
- Maximalt 4,3 miljarder unika adresser men betydligt färre praktiskt p.g.a. reserverade adresser och ineffektiv adressallokering

---

## IP Address ranges

| Class | Start      | End              | CIDR-Notation | 4 MSBs | Description           |
|-------|------------|------------------|---------------|--------|-----------------------|
| A     | `0.0.0.0`  |`127.255.255.255` | `0.0.0.0/8`   | 0xxx   | Large networks        |
| B     | `128.0.0.0`|`191.255.255.255` | `128.0.0.0/16`| 10xx   | Medium-sized networks |
| C     | `192.0.0.0`|`223.255.255.255` | `192.0.0.0/24`| 110x   | Small networks        |
| D     | `224.0.0.0`|`239.255.255.255` | `224.0.0.0/4` | 1110   | Multicast             |
| E     | `240.0.0.0`|`255.255.255.255` | `240.0.0.0/4` | 1111   | Experimental          |

---

## Table of special ranges and addresses

| Start         | End              | CIDR-Notation    | Description       |
|---------------|------------------|------------------|-------------------|
| `0.0.0.0`     |`0.0.0.0`         | `0.0.0.0/32`     | This host         |
| `10.0.0.0`    |`10.255.255.255`  | `10.0.0.0/8`     | Private network   |
| `100.64.0.0`  |`100.127.255.255` | `100.64.0.0/10`  | Carrier-Grade NAT |
| `127.0.0.0`   |`127.255.255.255` | `127.0.0.0/8`    | Loopback          |
| `169.254.0.0` |`169.254.255.255` | `169.254.0.0/16` | Link-local        |
| `172.16.0.0`  |`172.31.255.255`  | `172.16.0.0/12`  | Private network   |
| `192.168.0.0` |`192.168.255.255` | `192.168.0.0/16` | Private network   |

---

## CIDR (**C**lassless **I**nter-**D**omain **R**outing) Notation

&nbsp;

$$
\underbrace{192.168.0.2}_{\mathrm{address}} \mathrm{/} \underbrace{24}_{\mathrm{prefix}} \rightarrow\underbrace{255.255.255.0}_{\mathrm{netmask}}
$$

<!--
Prefixet anger hur många bitar som är nätverksdelen. Eller antalet 1:or i nätmasken.
-->

---

## Nätmask: `255.255.255.0`

- Utan nätmask är det svårt att veta vilka IP-adresser som tillhör samma nätverk.
- Värdadressen kan inte hittas utan nätmasken.
- Broadcast-adressen kan inte hittas utan nätmasken.

---

## CIDR Exempel 1: `192.168.0.1/24`

```text
IP = 192.168.0.1
Prefix = 24
Hostmask = 2^(32-24) - 1 = 2^8 - 1 = 256 - 1 = 255 = 0.0.0.255
Nätmask = ~ Hostmask = 255.255.255.0
Nätverksadress = Nätmask & IP = 192.168.0.0
Broadcast = Nätverksadress | Hostmask = 192.168.0.255
Värdadress = Nätverksadress + 1 = 192.168.0.1
Värdadressintervall = 192.168.0.1 - 192.168.0.254
Antal värdar = Hostmask - 1 = 255 - 1 = 254
```

---

## CIDR Exempel 2: `10.0.0.1/8`

```text
IP = 10.0.0.1
Prefix = 8
Hostmask = 2^(32-8) - 1 = 2^24 - 1 = 16777216 - 1 = 16777215 = 0.255.255.255
Nätmask = ~ Hostmask = 255.0.0.0
Nätverksadress = Nätmask & IP = 10.0.0.0
Broadcast = Nätverksadress | Hostmask = 10.255.255.255
Värdadress = Nätverksadress + 1 = 10.0.0.1
Värdadressintervall = 10.0.0.1 - 10.255.255.254
Antal värdar = Hostmask - 1 = 16777215 - 1 = 16777214
```

---

## Ethernet och MAC-adresser, (**M**edia **A**ccess **C**ontrol)

- MAC-adresser används för att identifiera enheter på ett ethernet-nätverk, medan IP-adresser används för att identifiera enheter på internet.
- Wifi och vissa andra nätverksteknologier använder också MAC-adresser, t.ex. Bluetooth, Zigbee och Thread. Men inte, t.ex., LTE och 5G som använder IMEI och IMSI.
- MAC-adresser är 48 bitar/6 bytes och skrivs i hex-form: `00:1A:2B:3C:4D:5E`
- Unik adress för varje nätverkskort (fysisk adress) där de tre första byten identifierar tillverkaren och de tre sista unikt identifierar enheten
- Randomiserade MAC-adresser skapas genom att den näst lägsta biten i det första bytet är satt till 1

<!--  Jobbar man på företag som tillverkar uppkopplade enheter så kan man behöva hantera dessa adresser och se till att de är unika och bränns in vid produktion. -->

---

## Ethernet och PTP (**P**recision **T**ime **P**rotocol)

- Används för att synkronisera klockor i nätverk med hög precision (nanosekund-nivå).
- Viktigt i industriella applikationer där exakt tidssynkronisering är nödvändig för att koordinera processer och dataflöden.
- PTP fungerar genom att skicka tidsstämplade meddelanden mellan en master-klocka och en eller flera slav-klockor.
- PTP kan användas över Ethernet-nätverk och kräver stöd i både nätverkskort och switchar för bästa precision.

---

## Ethernet och PoE (**P**ower **o**ver **E**thernet)

- Används för att leverera både data och ström över samma Ethernet-kabel.
- Vanliga användningsområden inkluderar IP-kameror, trådlösa accesspunkter och VoIP-telefoner.
- Behöver inte särskild kablage, fungerar med vanliga Cat5e/Cat6 kablar.
- Ingen behörighet krävs för installation eftersom spänningen är låg (under 60V).
- Räcker upp till 100 meter med standard Ethernet-kablar.

<!--
Det går att strömmsätta CAN-bussar, RS485, m.m. osv. på liknande sätt.
Ethernet kan också köras över vanliga elnät med Powerline-adaptrar.
Men vanligast är att använda PoE för Ethernet.
Finns hattar till Raspberry Pi och en massa switchar med inbyggd PoE.
Eller injectors som kan kopplas in i en vanlig switch.
Öven RPI 5 som kräver 30W kan drivas över PoE++/Type 3 driver upp till 51w.
PoE++/Type 4 driver upp till 71.3w.
-->

---

## IPv6-adresser

- 128 bitar: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- Grupper med inledande nollor kan förkortas: `2001:db8:85a3::8a2e:370:7334`
- Ranges:
    - Loopback: `::1` = `0000:0000:0000:0000:0000:0000:0001` = localhost
    - Link-local: `fe80::/10` = IPv4 variant: `169.254.0.0/16`
    - Multicast: `ff00::/8` = `1111:1111::/8`, IPv4 variant: `224.0.0.0/4`
    - Global unicast: `2000::/3` = IPv4 variant: `192.0.2.0/24`, till enskild enhet
    - Anycast: Delas av flera enheter, routas till närmaste

---

## IPv6-adresser och NAT (**N**etwork **A**ddress **T**ranslation)

- IPv6 utvecklades på 1990-talet för att hantera adressbristen i IPv4
- Det blev inte så stor brist som befarades tack vare NAT (Network Address Translation) som gjorde att många enheter kunde dela på en offentlig IPv4-adress
- NAT medförde också en viss anonymitet eftersom enheternas privata IP-adresser inte var synliga utåt
- IPv6 knöt i början adresserna direkt till MAC-adresser vilket medförde integritetsproblem
- IPv6 krävde också IPsec-stöd vilket gjorde det mer komplext
- Idag används ofta randomiserade gränssnitt-id:n för att förbättra anonymiteten

---

## IPSec (**IP** **Sec**urity)

- IPSec är en uppsättning protokoll som används för VPN (Virtual Private Network) och säker kommunikation över IP-nätverk.
- Krav i kursen och finns med certifiering och får användas i kritiska system.
- Finns inbyggt i både IPv4 och IPv6 och mycket gammal hårdvara och mjukvara har stöd.
- WireGuard är ett snabbare, säkrare och enklare alternativ som tar över mer och mer.

<!--
Mycket av säkerheten i Wireguard bygger på att den är enkel och har en liten kodbas som är lätt att granska.
Svårare att göra fel i konfigurationen medans IPSec är svårt att konfigurera rätt.
-->

---

## NAT och Port Forwarding och UDP Hole Punching

- NAT (Network Address Translation) gör att flera enheter i ett privat nätverk kan dela på en offentlig IP-adress.
- Port Forwarding gör att trafik från internet kan dirigeras till en specifik enhet i det privata nätverket (inte en NAT-teknik).
- UDP Hole Punching är en teknik som används för att etablera direktkommunikation från en enhet bakom en NAT-router till internet utan att behöva konfigurera portforwarding på routern.

<!--

Datorer och mobiler kan konfigureras för att agera som routrar.
Hotspot i mobiler/på datorer är en enkel router med NAT och DHCP.
Moderna WIFI moduler klarar ofta av att både vara accesspunkt och klient samtidigt så dom kan både ansluta till ett WIFI nätverk och agera som accesspunkt för andra enheter samtidigt.
Kan också använda en dator med två nätverkskort för fysisk ethernet och då gärna med en switch för att få fler portar.
Linux är otroligt bra på att agera router med iptables och dnsmasq och används mycket i inbyggda system.

-->

---

## DHCP (**D**ynamic **H**ost **C**onfiguration **P**rotocol)

- DHCP används för att automatiskt tilldela IP-adresser och andra nätverkskonfigurationsparametrar till enheter i ett nätverk.
- DHCP-servern tillhandahåller IP-adresser från ett fördefinierat intervall (scope) och kan också ge information om DNS-servrar, gateway-adresser och mer.
- DHCP kan fungera med både statiska och dynamiska IP-adresser, där statiska adresser är reserverade för specifika enheter.
- DHCPv6 är versionen av DHCP som används för att hantera IPv6-adresser och nätverkskonfigurationer.
- DHCP är innbyggt i de flesta operativsystem och routrar.
- Hotspot i mobiler och datorer är enkla DHCP-servrar.

---

## DNS (**D**omain **N**ame **S**ystem)

- DNS översätter domännamn (t.ex. <www.example.com>) till IP-adresser (t.ex. 192.0.2.1).
- DNS använder en hierarkisk struktur med olika nivåer av namnservrar för att hantera översättningen av domännamn till IP-adresser.
- Vanliga DNS-servrar är Google DNS (8.8.8.8, 8.8.4.4) och Cloudflare DNS (1.1.1.1).
- Funkar även på interna nätverk där DNS servern ofta är en del av routern. Enheter kan då nå varandra med hostnamn istället för IP-adresser.

<!--
Example.com är en domän som reserverats för dokumentation och exempel. Så använd denna i stället för att hitta på egna. Funkar för mejl också så ni inte råkar spamma någon server på riktigt.

NetBird har en DNS server och namnger klienter i nätverket.
-->

---

## DNS Records

- Samanfogar olika servrar och tjänster under ett och samma domännamn. Som portar fast för tjänster och transparent för användaren.
- Används för subdomäner och tjänster som t.ex. `www`, `mail`, `ftp`, `api`, `iot`, osv.
- För att använda, t.ex., AWS Simple Email Service (SES) för att skicka e-post från en egen domän, krävs det att man lägger till rätt DNS-poster och verifierar domänen.

---

## Wifi

- 802.11 är en samling standarder för trådlösa nätverk utvecklade av IEEE med olika versioner (a/b/g/n/ac/ax/ay) och funktioner.
- MAC-adresser används för att identifiera enheter på ett wifi-nätverk precis som i Ethernet.
- Wifi-nätverk kan vara öppna eller säkrade med olika krypteringsmetoder som WEP, WPA, WPA2 och WPA3.
- Wifi-nätverk kan använda olika frekvensband (2.4 GHz och 5 GHz) med olika kanaler för att undvika störningar.
- Wifi-nätverk kan konfigureras som infrastruktur (med accesspunkt) eller ad-hoc (direkt mellan enheter).

---

## Thread

- Trådlöst mesh-nätverk baserat på IEEE 802.15.4 för IoT-enheter.
- Använder låg effekt och har stöd för många enheter i ett nätverk.
- MAC-adresser används för att identifiera enheter på ett Thread-nätverk.
- Använder IPv6 för adressering och kommunikation.
- Används med Matter för smarta hem och IoT-applikationer.

<!--
Tänk på det som wifi fast mesh och med låg effekt.
Enheterna kan kommunicera direkt med varandra och vidarebefordra trafik för andra enheter i nätverket.
Kan ansluta direkt till internet via en eller flera border routers. Ingen gateway behövs såsom med Zigbee eller Bluetooth.
-->