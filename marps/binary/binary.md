---
marp: true
theme: custom
paginate: true
header: 'Binary and Text'
footer: 'Niklas Åkerlund &lt;<a href="mailto:niklas.akerlund@nackademin.se">niklas.akerlund@nackademin.se</a>&gt;'
class: invert
math: mathjax
---

# Binärdata och Textdata

![bg](technology-2650392.jpg)

---

## Textdata

- Textdata är lätt att läsa och redigera för människor, medan binärdata är mer kompakt och effektiv för maskiner.
- Textdata använder vanligtvis tecken som ASCII eller UTF-8, medan binärdata representeras i ett format som är mer direkt kopplat till maskinens hårdvara.
- Textdata är också binär i grunden men är kodad på ett sätt som gör den läsbar för människor.

---

## Binärdata i MQTT

- MQTT är ett lättviktsprotokoll för meddelandehantering som ofta används i IoT.
- MQTT-meddelanden kan innehålla binärdata i sin nyttolast, vilket gör det möjligt att skicka komprimerade eller specialiserade dataformat.
- Binärdata i MQTT kan vara mer effektivt för överföring av stora datamängder eller realtidsdata.
- Längden på fält för data anges i antal bytes i förväg istället för att använda avgränsare eller 0-terminering som i textdata.

---

## Textdata i HTTP

- HTTP (Hypertext Transfer Protocol) är ett protokoll för överföring av textdata över nätverket.
- HTTP-meddelanden är i allmänhet textbaserade och använder en enkel struktur som gör dem lätta att läsa och förstå.
- Textdata i HTTP kan inkludera HTML, JSON, XML och andra textformat.
- Textdata i HTTP är lätt att felsöka och analysera med verktyg som webbläsare och nätverksanalysatorer.
- För att tolka HTTP söks textdata efter avgränsare som mellanslag, kolon, CRLF och 0-terminering. Det är inte lika effektivt som i strukturerad binärdata.

---

## UTF-8 och multibyte-tecken, Unicode

<style scoped>
    li li { font-size: 70% }
</style>

- Tecken kan vara 1 till 4 bytes långa och använder de högsta bitarna för att indikera längden:
    - 1-byte: `0xxxxxxx` (ASCII)
    - 2-byte: `110xxxxx 10xxxxxx`
    - 3-byte: `1110xxxx 10xxxxxx 10xxxxxx`
    - 4-byte: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`
- För att tolka UTF-8 måste man läsa de högsta bitarna för att avgöra tecknets längd och sedan läsa de efterföljande bitarna för att få det fullständiga tecknet.
- Det går med andra ord inte att slumpmässigt hoppa in i en UTF-8 sträng och börja läsa, utan att först veta var tecknen börjar och slutar.
- XML och JSON är exempel på textformat som använder UTF-8.

---

## "Base64 Encoding!" = "QmFzZTY0IEVuY29kaW5nIQ=="

- Base64 är en metod för att koda binärdata som text och används ofta för att överföra binärdata över textbaserade protokoll som HTTP.
- Base64-kodning delar upp data i 6-bitars block och representerar varje block som ett tecken i en 64-teckens uppsättning.
- Base64-kodning ökar storleken (`(length * 4) / 3`) och `=` tecken används som padding i slutet så man får hela bytes.
