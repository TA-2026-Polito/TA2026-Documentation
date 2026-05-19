# Assignment 2 — Virtual Humans & Animation

🎯 Crea due MetaHuman originali, animali con fonti diverse e documenta il processo. L'obiettivo è dimostrare la padronanza del pipeline di creazione e animazione di personaggi digitali in Unreal Engine 5, non le capacità di recitazione o di regia.

<aside>
🔥

Un MetaHuman scaricato direttamente dalla libreria senza alcun processo di authoring non è accettabile. Ogni personaggio deve essere stato costruito, anche se il punto di partenza è un preset, le scelte di aspetto, materiali e identità devono essere documentate e motivate.

</aside>

---

## 👤 I Personaggi

L'assignment richiede **almeno due MetaHuman distinti**, entrambi creati attraverso il pipeline di authoring in MetaHuman Creator. La scena di sfondo non viene valutata, può essere l'ambiente dell'Assignment 1, un asset scaricato da Fab, oppure un semplice stage neutro.

🎨 **Requisito estetico** → i personaggi devono essere fotorealistici e tecnicamente credibili. L'aspetto finale (pelle, occhi, capelli) deve dimostrare attenzione alle scelte di rendering, non solo l'uso dei preset di default.

---

<aside>
🥻

**Una nota sul vestiario**

Il clothing è uno degli aspetti tecnicamente più complessi dell'intero pipeline MetaHuman  (simulazione fisica, fitting su mesh animate, compatibilità con il retargeting) e **non viene valutato in questo assignment**. Qualsiasi soluzione troviate è accettabile: un asset di default, qualcosa di free su Fab, un abito che non si abbina perfettamente al personaggio o al contesto. L'importante è l'aspetto generale, la comprensione del pipeline di animazione e la qualità del processo documentato.

Detto questo, è molto probabile che i vostri MetaHuman finiscano nell'Assignment 3 e in generale potenzialemtne nel vostro portfolio. Un personaggio ben vestito fa differenza nell'immagine finale molto più di quanto ne faccia in un semplice test di animazione.

Per questo motivo, se ritenete che sia rilevante per i vostri personaggi, potete acquistare asset di abbigliamento da Fab o store equivalenti  (alcuni di voi mi hanno segnalato prezzi anche intorno a 1€). In alternativa, se volete investire tempo nel clothing come percorso tecnico, documentate il processo: cosa avete provato, cosa ha funzionato, cosa no. Non è un requisito, è lavoro extra, e verrà riconosciuto come tale.

</aside>

---

## ⚙️ Requisiti Tecnici

> Tutti i seguenti elementi devono essere presenti e dimostrati nella consegna.
> 

---

### 👥 Creazione dei Personaggi

▸ **Due MetaHuman** creati attraverso MetaHuman Creator: face controls, body, skin, eyes, hair
▸ Il processo di authoring di entrambi i personaggi deve essere documentato nel post-mortem
▸ **Bonus** → uno dei due personaggi tenta di replicare una persona reale utilizzando il pipeline Mesh to MetaHuman (foto, scan, o mesh come input)

---

### 🏃 Animazione del Corpo

Ogni personaggio deve avere almeno una body animation. Le due animazioni devono provenire da fonti diverse:

▸ **Animazione da libreria** → retargetata da una fonte esistente (Game Animation Sample, Mixamo o equivalente). 
▸ **Animazione da video mocap** → generata da voi usando uno strumento di motion capture video-based (DeepMotion, Move.ai o equivalente). Il gruppo realizza una performance, la processa e la retargeta sul MetaHuman

Le due animazioni possono essere distribuite liberamente tra i due personaggi, entrambe sullo stesso personaggio, una per ciascuno, o qualsiasi altra combinazione. L'importante è che entrambe le fonti siano presenti e documentate.

> Se il pipeline ha richiesto un passaggio di retargeting (IK Rig, chain mapping, retarget pose), documentalo nel post-mortem. Non è un requisito separato, è parte naturale del processo di animazione e va raccontato se è stato fatto.
> 

---

### 😐 Animazione Facciale

▸ **Almeno un personaggio** deve avere una facial animation
▸ L’animazione può essere catturata con uno dei seguenti metodi, in ordine decrescente di qualità:

- iPhone con Live Link Face App o MetaHuman Animator (depth data) → massima qualità
- Android compatibile con Live Link Face (Beta) → real-time streaming
- Video monoscopico con MetaHuman Animator (webcam, DSLR, smartphone) → accessibile senza hardware dedicato
- Audio-driven animation via MetaHuman Animator → ultima risorsa, ma accettabile
▸ **Bonus** → la performance facciale è eseguita dal gruppo stesso (non generata da audio sintetico o clip pre-esistenti)

---

### 🎬 Video di Consegna

▸ Per ogni body animation, consegnare un video **side-by-side** che mostri in parallelo la fonte originale (video di riferimento o clip dalla libreria) e il MetaHuman animato nel risultato finale
▸ Per la facial animation, consegnare un video che mostri il MetaHuman con la performance applicata
▸ I video devono essere compressi prima di essere inclusi nello zip (vedi sotto)

---

## 🗺️ Workflow Suggerito

1. 🧑‍🎨 **Creazione dei personaggi** → MetaHuman Creator, scelte di aspetto, eventuale Mesh to MetaHuman
2. 📥 **Integrazione in UE5** → download via Quixel Bridge o assembly pipeline in UE5.6+, verifica LODSync e plugin attivi
3. 🎭 **Cattura facciale** → Live Link, MetaHuman Animator o audio-driven secondo disponibilità hardware
4. 🏃 **Acquisizione body animation** → download da libreria + video mocap con strumento AI
5. 🔄 **Retargeting** → IK Rig setup, chain mapping, retarget pose, export
6. 🎬 **Montaggio video side-by-side** → affianca source e risultato per ogni body animation
7. ✨ **Polish e documentazione** → post-mortem, verifica requisiti, compressione video

---

## 📌 Una Nota su Portata e Impegno

Questo assignment valuta il **pipeline di creazione e animazione di personaggi digitali** — le scelte tecniche, la comprensione del sistema e la qualità del risultato. Non valuta le capacità di recitazione, la qualità cinematografica delle inquadrature, né la complessità della scena di sfondo.

🚫 Il tempo dedicato a costruire un ambiente elaborato per questo assignment è tempo sottratto alla parte che viene valutata. Un personaggio ben animato su uno stage neutro vale più di un personaggio mal animato in un ambiente ricercato.

✅ Documentare onestamente i problemi incontrati — un retargeting imperfetto con una chiara spiegazione di cosa non ha funzionato e perché vale più di un risultato rifinito senza alcuna riflessione tecnica.

---

## 🔗 Continuità con gli Altri Assignment

L'ambiente dell'Assignment 1 può essere riutilizzato come sfondo — è un'opportunità naturale per popolare lo spazio che avete già costruito con dei personaggi. Non è obbligatorio, e non porta punti aggiuntivi.

Allo stesso modo, i personaggi e le animazioni prodotte per questo assignment sono esattamente il materiale di partenza per l'Assignment 3 (Cinematics). Montare le animazioni in una sequenza con più inquadrature è il passo naturale successivo. Se volete lavorare su A2 e A3 in parallelo o in combinazione — perché no?

---

## 📬 Consegna

🗓️ **Scadenza** → 20 Maggio @14.00 nella giornata del Showcase 2

Consegna un singolo file zip, **massimo 300MB**, contenente:

---

### 📄 1. File di presentazione

Una presentazione autonoma che copre il tuo technical post-mortem (vedi sotto).

✅ Formati accettati: qualsiasi formato **esportato localmente** — PDF, PPTX, HTML. Se usate Canva, Google Slides o strumenti simili, esportate in uno di questi formati prima di consegnare.
🚫 Non accettati: link a presentazioni online. Il file consegnato deve essere autonomo e apribile senza connessione internet o account esterni.

> Il file consegnato è la versione di riferimento — ciò che mostri in classe deve corrispondere a ciò che hai consegnato e deve servire per fare il confronto con quanto verrà presentato all’esame. Si ricorda che il lavoro può essere migliorato successivamente in vista dell’esame (vedi dettagli nella guida)
> 

<aside>
📭

Indirizzo a cui sottomettere il file:
https://www.dropbox.com/request/kz2m3jkgsufduzlio0lq

Vi consiglio di sottomettere su dropbox dopo esservi loggati (con le credenziali polito). In questo modo riceverete mail di avvenuto upload. 

</aside>

---

### 🎥 2. Video

▸ Un video **side-by-side** per ogni body animation (source vs MetaHuman)
▸ Un video della facial animation applicata al personaggio

<aside>
🔥

La compressione video è **obbligatoria** e viene verificata. File video non compressi che fanno sforare il limite di 300MB comportano una penalità sulla valutazione. Usa FFmpeg:

</aside>

```
ffmpeg -i input.mp4 -vcodec libx264 -crf 28 -preset slow output.mp4
```

---

### 📁 3. Struttura del file zip

<aside>
⚠️

TA-GXX-Assignment-02.zip
├── 📄 Presentation/
│   └── TA-GXX-Assignment-02-Presentation.pdf  (o .pptx / .html)
│──   🎥 Supplementary/
          ├── body-animation-01-sidebyside.mp4
          ├── body-animation-02-sidebyside.mp4
          ├── facial-animation.mp4
          └── ... (qualsiasi altro materiale media)

</aside>

Sostituisci `GXX` con il numero del tuo gruppo (es. `G01`, `G02`, ...).

---

## 🎤 Technical Post-Mortem (5 minuti)

La tua presentazione è un **technical post-mortem** — un resoconto strutturato di cosa hai costruito, come lo hai costruito e cosa hai imparato. Copri i seguenti punti:

▸ 👤 **Panoramica dei personaggi** → chi sono i due MetaHuman, quali scelte sono state fatte in Creator, cosa li rende distinti
▸ 🧑‍🎨 **Creation pipeline** → il processo di authoring di ciascun personaggio — face controls, body, skin, eyes, hair. Se è stato tentato un Mesh to MetaHuman, documenta il processo e il risultato
▸ 🏃 **Body animation breakdown** → le due fonti usate, il processo seguito per ciascuna, i problemi incontrati e come sono stati risolti. Se è stato necessario un passaggio di retargeting, descrivilo.
▸ 😐 **Facial animation** → il metodo di cattura usato, perché è stato scelto (o perché non è stato possibile usarne uno migliore), qualità del risultato
▸ 🎯 **Decisioni chiave** → due o tre decisioni tecniche specifiche che hanno definito il risultato
▸ 🔥 **La sfida più grande** → cosa ha dato più difficoltà e come è stata affrontata

> 💡 Sii onesto. Un retargeting imperfetto con una spiegazione chiara di cosa non ha funzionato è più prezioso di un risultato rifinito senza alcuna riflessione tecnica.
> 

---

### 📚 Risorse Consigliate

Indica **2 risorse** (tutorial, video o articoli) che hai trovato particolarmente utili durante questo assignment e che consiglieresti senza esitazione ai tuoi colleghi. Per ognuna specifica:

▸ Titolo e link
▸ Una riga su perché è stata utile e a che punto del workflow ti ha aiutato di più

---

## 🌟 Ispirazione e Visibilità

### 📖 Articoli di riferimento

Prima di iniziare, esplora questi breakdown di pipeline reali con MetaHuman — non come template da copiare, ma come esempi del livello di riflessione tecnica che ci aspettiamo nel post-mortem:

▸ [Drip Fit for a King: Realistic Game-Ready Character Made with UE5.5](https://80.lv/articles/drip-fit-for-a-king-realistic-game-ready-character-made-with-ue5-5) (80.lv). Breakdown completo di un personaggio realistico in UE5.5: creation pipeline, skin, hair, ottimizzazione
▸ [Character Production in Unreal Engine's MetaHuman + XGen](https://80.lv/articles/character-production-in-unreal-engine-s-metahuman-xgen)  (80.lv) Pipeline di produzione di un personaggio con MetaHuman e XGen per i capelli

---

### 🎨 Pubblica il tuo lavoro

Un MetaHuman ben riuscito è un ottimo pezzo da portfolio. Se hai un profilo ArtStation o simile, pubblica i tuoi personaggi con un breakdown del processo. Non è obbligatorio, ma è esattamente il tipo di lavoro che vale la pena mostrare.

> 💡 Se pubblichi, condividi il link sul canale Discord del corso.
>