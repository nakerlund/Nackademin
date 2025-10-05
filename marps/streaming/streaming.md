---
marp: true
theme: custom
paginate: true
title: "Streaming Data • 2025"
header: 'Streaming Data • 2025'
footer: 'Niklas Åkerlund &lt;<a href="mailto:niklas.akerlund@nackademin.se">niklas.akerlund@nackademin.se</a>&gt;'
class: invert
---

# Allt blir SQL till slut

![bg](assets/crab-684881.jpg)

<!--
-Pipes, generatorer, LINQ och deklarativa pipelines
- Biologer skämtar: *“allt utvecklas till krabbor.”*
- Inom datavetenskap utvecklas allt till **pipelines och SQL-liknande språk.**
- Låt oss följa denna konvergenta evolution.
 -->

---

## POSIX-pipes (1970-talet)

```bash
cat logs.txt | grep error | sort | uniq
```

- Små verktyg, kopplade med `|`
- Strömmar text vänster → höger
- Komponerbara, minnessnåla
- Tidigt exempel på *dataflödesprogrammering*

---

## SQL (1970-talet)

```sql
SELECT DISTINCT name
FROM customers
WHERE city = 'Stockholm'
ORDER BY name;
```

- Baserat på **relationell algebra** (Codd, 1970)
- Operatorer: selektion, projektion, join, gruppering
- Deklarativt: ange *vad*, inte *hur*

---

## Python-generatorer (2001) / Iterators / Coroutines

```python
def count_up(n):
    for i in range(1, n+1):
        yield i
```

- `yield` = pausa & återuppta → **korutin som generator**
- **lazy evaluation** (värden beräknas vid behov)
- Funktioner med *instance state*

---

## C#, LINQ (Language Integrated Query, 2007)

```csharp
// C# query syntax alternativ till dot-chaining
var q =
    from c in customers
    where c.City == "Stockholm"
    orderby c.Name
    select c.Name;
```

- Stöd för både **query syntax** och **dot-chaining** av **comprehensions** (ofta med lambda-uttryck)
- Använder generators (IEnumerable<T>) för att bygga **streams** med **lazy evaluation**

<!--
- LINQ är SQL-liknande syntax för att skapa **strömmande pipelines** i kod
- Använder generators (IEnumerable<T>) för **lazy evaluation**
- Finns nu i många språk: Java Streams, JavaScript (RxJS), Python (Pandas), m.fl.
-->

---

## Java Streams (2014)

```java
// Dot-chaining style med LINQ-liknande funktioner och lambda-uttryck
List<String> names = customers.stream()
    .filter(c -> c.getCity().equals("Stockholm"))
    .map(Customer::getName)
    .distinct()
    .sorted()
    .collect(Collectors.toList());
```

---

## NoSQL-omvägen (2000-talet)

- Hadoop (MapReduce) och NoSQL-system (MongoDB, Cassandra, DynamoDB)
- Uppstod ur skalbarhetsproblem i relationsdatabaser
- Tidiga system exponerade **lågnivå-API:er** (map/reduce-funktioner, nyckel-värde-åtkomst)
- Snart återkom högre **deklarativa lager**:
    - HiveQL (SQL över Hadoop)
    - Spark SQL (deklarativa frågor på DataFrames)
    - CQL (Cassandra Query Language)
- Mönster: systemen övergav SQL men återinförde **SQL-liknande abstraktioner** för användbarhet och optimering

---

## Streama data över nätverk

- Om möjligt, streamad data i stället för att buffra hela filer
- T.ex. med **gRPC** (Google Remote Procedure Call) som bygger på HTTP/2 och Protobuf
- gRPC stödjer både **unary** (enkel förfrågan/svaret) och **streaming** (flera meddelanden i båda riktningar)
- Praktiskt för ljud/video som lätt blir för stort att skicka i en enda bit och realtidsdata som sensordata

---

![bg](assets/crab-684881.jpg)

<!--
    Konvergens mot SQL-liknande språk
    Allt blir SQL till slut
-->
