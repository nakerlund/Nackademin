---
marp: true
theme: custom
paginate: true
title: "Async/Await"
description: "Syntaktiskt socker över Tasks"
header: 'Async/Await'
footer: 'Niklas Åkerlund &lt;<a href="mailto:niklas.akerlund@nackademin.se">niklas.akerlund@nackademin.se</a>&gt;'
class: invert
---

# Async / Await

![bg](assets/crab-684881.jpg)
<!--
- Callbacks → Tasks → async/await
- Syntaktiskt socker: ny syntax, samma modell
- C# 5 myntade `async`/`await`
-->

---

# Callbacks (före 2010)

```csharp
client.DownloadStringCompleted += (s,e) => {
    if (e.Error != null) Handle(e.Error);
    else Process(e.Result);
};
````

* Event-driven stil (EAP/APM)
* Splittrad felhantering
* Svår att komponera

---

# C# 4 (2010) – Tasks men utan `await`

```csharp
Task<string> t = client.DownloadStringTaskAsync(url);

t.ContinueWith(done =>
{
    if (done.IsFaulted) Handle(done.Exception);
    else Process(done.Result);
}, TaskScheduler.FromCurrentSynchronizationContext());
```

* Introduktion av **Task Parallel Library (TPL)**
* Asynkrona operationer som **Tasks**
* Kedjning med `ContinueWith`
* Fel via **AggregateException**

---

# C# 5 (2012) – `async` / `await`

```csharp
public async Task RunAsync(string url)
{
    try
    {
        var result = await client.DownloadStringTaskAsync(url);
        Process(result);
    }
    catch (Exception ex)
    {
        Handle(ex);
    }
}
```

* **Syntaktiskt socker** över Tasks
* Kompilatorn bygger en **state machine**
* Vanlig `try/catch` fungerar
* Samma modell som i C# 4 – bara mycket renare

---

# Varför syntaktiskt socker?

## C# 4

```csharp
DownloadAsync()
  .ContinueWith(done =>
  {
      if (done.IsFaulted) Handle(done.Exception);
      else Process(done.Result);
  });
```

## C# 5

```csharp
try { Process(await DownloadAsync()); }
catch (Exception ex) { Handle(ex); }
```

* `await` översätts till en **ContinueWith + state machine**
* Ingen ny runtime-modell – bara ny syntax

---

# Desugar: `await` ⇒ `ContinueWith`

```csharp
// Socker
int x = await DownloadAsync();

// Ungefärlig desugar (C# 4-stil)
DownloadAsync().ContinueWith(task =>
{
    if (task.IsFaulted) throw task.Exception;
    return task.Result;
});
```

* Kompilatorn genererar dold `MoveNext()` med switch-state machine
* Skillnaden är **ergonomi**, inte semantik

---

# Konsekvenser av C# 5

* Async blev **läsbart och idiomatiskt**
* `try/catch/finally` fungerar naturligt
* `Task.WhenAll` + `await` förenklar samkörning
* Men: **deadlocks** möjliga om man blockerar `.Result`
  → `ConfigureAwait(false)` praxis i bibliotek

---

# Spridning till andra språk

* **Python 3.5 (2015):** `async def`, `await`
* **JavaScript ES2017:** `async function`, `await` över Promises
* **Kotlin (2017):** `suspend` + koroutiner (structured concurrency)
* **Java (2014/2021):** `CompletableFuture` + Loom (virtuella trådar)
