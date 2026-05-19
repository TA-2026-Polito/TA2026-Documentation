# Assignment 3 - Cinematics

🎯 Crea una cinematica in Unreal Engine 5 composta da almeno 5 shot e documenta le scelte di regia e gli strumenti utilizzati. L’obiettivo è dimostrare la padronanza degli strumenti cinematici di UE5  (Sequencer, CineCamera, e Control Rig) non la qualità delle animazioni né la complessità dell’ambiente.

🔥 Questo assignment valuta la cinematografia: il framing delle inquadrature, il blocking della scena e la padronanza degli strumenti dell’engine. La qualità delle animazioni non è oggetto di valutazione, quello che conta è come avete saputo utilizzare e orchestrare il materiale a disposizione.

---

## 🎬 La Cinematica

La cinematica deve avere una durata minima di **10 secondi** ed essere composta da **almeno 5 shot**, tra cui:

▸ **Establishing shot** → inquadratura che introduce lo spazio scenico
▸ **Master shot** → inquadratura d’insieme che mostra la scena nella sua totalità
▸ **3 o più inquadrature a scelta** → qualsiasi tipologia: close-up, over the shoulder, insert, POV, dolly, ecc.

All’interno della cinematica deve essere presente **almeno un personaggio in movimento,** non una scena completamente statica.

---

## ⚙️ Requisiti Tecnici

> Tutti i seguenti elementi devono essere presenti e dimostrati nella consegna.
> 

---

### 🎞️ Sequencer

▸ La sequenza deve essere strutturata con una **MasterSequence** contenente **SequenceShots** e **SubSequences**
▸ Almeno una SubSequence deve essere dedicata al dipartimento di **Lighting,** la struttura deve riflettere un workflow di lavoro multidipartimentale realistico
▸ L’export finale deve essere prodotto con **Movie Render Queue**

---

### 📷 CineCamera

▸ Tutte le inquadrature devono essere realizzate con **CineCamera Actor,** non con la camera di default del viewport
▸ Le scelte di focal length, apertura e profondità di campo devono essere motivate nel post-mortem

---

### 🧍 Personaggi e Animazione

▸ Almeno un personaggio deve essere **in movimento** nella sequenza
▸ La fonte dell’animazione deve essere documentata nel post-mortem, che sia Take Recorder, mocap, libreria, manuale o ibrida
▸ Non è richiesta una qualità di animazione elevata, è richiesta la capacità di integrare e orchestrare il personaggio nella sequenza

> Se avete scelto di lavorare in continuità con l’Assignment 2 e i personaggi e le animazioni sono gli stessi già consegnati lì, non è necessario ridocumentare il processo di creazione o di animazione in questo post-mortem. È sufficiente un riferimento all’Assignment 2, il focus qui è interamente sulla regia e sulla struttura cinematica.
> 

---

### 🌍 Ambiente

L’ambiente non viene valutato in questo assignment. Potete usare:
▸ L’ambiente prodotto nell’Assignment 1
▸ Un environment scaricato da Fab o da qualsiasi altra fonte
▸ Qualsiasi scena pre-esistente di vostra produzione

Non è necessario documentare come è stato costruito l’ambiente.

---

<aside>
🔕

**Una nota sull'audio**

L'audio non è un elemento di valutazione per questo assignment: la cinematica può essere consegnata completamente muta senza alcuna penalità.

Se volete aggiungere audio, siete liberi di farlo nel modo che ritenete più efficace: musica di sottofondo, rumori ambientali, voci. Non ci sono vincoli su come farlo né su cosa usare: scegliete quello che secondo voi valorizza meglio il lavoro. La qualità dell'audio non contribuisce alla valutazione.

</aside>

---

## 🗺️ Workflow Suggerito

1. **Preproduzione** → reference, script, storyboard. Definisci i tuoi shot prima di aprire l’engine.
2. **Dressing dello spazio scenico** → definisci la zona dell’environment dove si svolgerà la scena
3. **Sequencer setup** → MasterSequence, SequenceShots, SubSequences, SubSequence Lighting
4. **Blocking** → posiziona personaggi e camere, definisci i movimenti principali
5. **Animazione** → integra o crea le animazioni necessarie (Take Recorder, libreria, mocap)
6. **Camera framing** → focal length, apertura, profondità di campo, movimento camera
7. **Editing e polish** → timing dei tagli, transizioni, ritmo della sequenza
8. **Export** → Movie Render Queue, compressione, documentazione

---

## 📌 Una Nota su Portata e Impegno

Questo assignment valuta la **cinematografia e la padronanza degli strumenti UE5,** Sequencer, CineCamera, blocking, struttura multidipartimentale. Non valuta la qualità delle animazioni, la complessità dell’ambiente né le capacità di modellazione o di character art.

🚫 Investire tempo nella creazione di un ambiente nuovo o nel miglioramento delle animazioni è tempo sottratto a ciò che viene valutato. Una scena semplice con inquadrature ben ragionate vale più di una scena elaborata con shot generici.

✅ Le scelte di regia devono essere motivate, non basta che un’inquadratura sia tecnicamente corretta, deve essere spiegato perché è stata scelta e cosa comunica.

---

## 🔗 Continuità con gli Altri Assignment

I personaggi e le animazioni prodotte per l’Assignment 2 sono il punto di partenza naturale per questa cinematica. Se avete già un MetaHuman animato, avete già il materiale principale, questo assignment aggiunge la regia e la struttura cinematica sopra di esso.

Allo stesso modo, l’ambiente dell’Assignment 1 può servire da location senza alcuna modifica. La continuità tra i tre assignment non è obbligatoria, ma è il percorso più efficiente, e alla fine produce una scena che dimostra l’intero pipeline di un technical artist.

<aside>
💡

**Bonus** → strutturare la cinematica come l’inizio di un opening, un FTUE o un frammento narrativo. In questo caso, includi nel post-mortem una breve sinossi dell’idea, ,non più di 5 righe.

</aside>

---

## 📬 Consegna

🗓️ **Scadenza** → 20 Maggio @14.00 nella giornata del Showcase 2

Consegna un singolo file zip, **massimo 300MB**, contenente:

---

### 📄 1. File di presentazione

Una presentazione autonoma che copre il tuo technical post-mortem (vedi sotto).

✅ Formati accettati: qualsiasi formato **esportato localmente** — PDF, PPTX, HTML. Se usate Canva, Google Slides o strumenti simili, esportate in uno di questi formati prima di consegnare.
🚫 Non accettati: link a presentazioni online. Il file consegnato deve essere autonomo e apribile senza connessione internet o account esterni.

---

### 🎥 2. Video

▸ Il **video finale** della cinematica esportato con Movie Render Queue — questo è il deliverable principale
▸ Eventuale materiale supplementare (storyboard, reference, varianti di shot) può essere incluso ma non è obbligatorio

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

TA-GXX-Assignment-03.zip
├── 📄 Presentation/
│ └── TA-GXX-Assignment-03-Presentation.pdf (o .pptx / .html)
│
│──   🎥 Supplementary/

     ├── body-animation-01-sidebyside.mp4
     ├── body-animation-02-sidebyside.mp4

</aside>

Sostituisci `GXX` con il numero del tuo gruppo (es. `G01`, `G02`, …).

<aside>
📭

Indirizzo a cui sottomettere il file:
https://www.dropbox.com/request/hso53gpsbfe2zm76hjcx

Vi consiglio di sottomettere su dropbox dopo esservi loggati (con le credenziali polito). In questo modo riceverete mail di avvenuto upload. 

</aside>

---

## 🎤 Technical Post-Mortem (5 minuti)

La tua presentazione è un **technical post-mortem** — un resoconto strutturato di cosa hai realizzato, come lo hai realizzato e cosa hai imparato. Copri i seguenti punti:

▸ 🎬 **Panoramica della cinematica** → di cosa parla la scena, qual è la reference di ispirazione, quanti shot e quanto dura
▸ 🎞️ **Struttura del Sequencer** → come è organizzata la MasterSequence, le SequenceShots e le SubSequences; come è stata gestita la SubSequence di Lighting
▸ 📷 **Shot breakdown** → per ogni inquadratura: tipo di shot, focal length, motivazione della scelta. Quale è stato lo shot più complesso da realizzare e perché
▸ 🧍 **Animazione** → quale strumento è stato usato per creare o reperire le animazioni (Take Recorder, mocap, libreria, manuale, ibrido) e come sono state integrate nella sequenza (**SOLO SE NON TRATTATI nell’Assignment 2**)
▸ 🎯 **Decisioni chiave** → due o tre scelte tecniche o registiche specifiche che hanno definito il carattere della cinematica
▸ 🔥 **La sfida più grande** → cosa ha dato più difficoltà e come è stata affrontata

> 💡 Sii onesto. Una cinematica semplice con scelte di regia consapevoli e ben documentate vale più di una sequenza elaborata senza riflessione sul processo.
> 

---

### 📚 Risorse Consigliate

Indica **2 risorse** (tutorial, video o articoli) che hai trovato particolarmente utili durante questo assignment e che consiglieresti senza esitazione ai tuoi colleghi. Per ognuna specifica:

▸ Titolo e link
▸ Una riga su perché è stata utile e a che punto del workflow ti ha aiutato di più

---

## 🌟 Ispirazione e Visibilità

### 📖 Prima di iniziare

Se non hai le idee chiare su cosa vuoi realizzare, prima di aprire l’engine, guarda almeno una scena di un film o di un videogioco che vuoi usare come reference. Analizza le inquadrature: perché il regista ha scelto quel focal length, quel movimento, quel taglio. Porta questa analisi nel tuo storyboard e poi nel tuo post-mortem.

Non serve una reference elaborata, basta una scena di qualche secondo analizzata con attenzione.

---

### 🎨 Pubblica il tuo lavoro

Una cinematica realizzata in UE5 è un ottimo pezzo da portfolio. Se hai un profilo ArtStation, Behance o YouTube, pubblica il video con un breakdown delle tue scelte registiche. Non è obbligatorio, ma è il tipo di lavoro che vale la pena mostrare.

> 💡 Se pubblichi, condividi il link sul canale Discord del corso.
>