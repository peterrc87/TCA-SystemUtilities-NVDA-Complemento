## TCA SystemUtilities.

Piccolo add-on che ci consente di eseguire rapidamente alcune azioni di Windows tramite una scorciatoia da tastiera.
È in grado di eseguire una riparazione del sistema con SFC. Puoi copiare le informazioni di sistema negli appunti, accedere al BIOS e molto altro.
Possiamo anche aprire il sito ufficiale per ottenere add-on per NVDA in modo diretto.

* Autore: Peter Reina <peterrc87@gmail.com>
* Compatibilità: NVDA 2018 fino a NVDA 2021.3

## Funzioni di sistema:
* Arresto del sistema: chiude Windows
 Inoltre, emette il classico suono di chiusura di Windows. Ci avverte che il sistema sta per essere spento tramite un messaggio.
 Ci offre la possibilità di chiudere o annullare lo spegnimento per 3 secondi.
* Riavvio del sistema: riavvia Windows
 Inoltre, emette il classico suono di chiusura di Windows. Ci avverte che il sistema si riavvierà tramite un messaggio.
 Ci offre la possibilità di chiudere o annullare il riavvio per 3 secondi.
* Annulla (arresto o riavvio): ci consente di annullare una qualsiasi delle 2 opzioni precedenti (arresto o riavvio)
Inoltre, ci informa con un messaggio che l'arresto/riavvio è stato annullato.
 ! Nota! Abbiamo solo 3 secondi per eseguire questa azione.
* Ibernazione: ci consente di mettere il sistema in modalità ibernazione, comodamente da NVDA.
* Riavvia ed entra in modalità provvisoria con rete: questa funzionalità a volte è molto complicata da inserire, invece con TCA SystemUtilities è un gioco da ragazzi.
Molto facilmente ci permette di entrare in Windows con funzioni limitate senza caricare servizi o programmi non necessari, da dove possiamo fare una pulizia più approfondita, rimuovere programmi indesiderati, malware e molto altro.
! Nota importante!
In questa modalità, nei sistemi precedenti a Windows 10, il servizio audio potrebbe non essere attivato, quindi non possiamo avere la sintesi vocale dello screen reader.
Una volta attivata questa funzione, dobbiamo quindi disabilitarla, possiamo farlo dallo stesso menu TCA-SystemUtilities, nella sezione: "Arresto del sistema".
* Riavvia in modalità normale: ci consente di disabilitare la modalità provvisoria se l'abbiamo attivata, riporta l'avvio di Windows ai suoi valori normali (carica tutti i servizi e i programmi che abbiamo all'avvio).
* Sospendi: consente di sospendere il sistema, comodamente da NVDA.
* Entra nel BIOS-UEFI: Possiamo comodamente da Windows e con NVDA dire al PC di entrare nel BIOS-UEFI al prossimo riavvio.
Non c'è bisogno di premere o conoscere il tasto, direttamente e facilmente.
(Nota importante!) nel BIOS-UEFI non è presente il servizio audio, quindi non potremo utilizzare uno screen reader nella sua interfaccia). Una volta che vogliamo tornare al nostro sistema, possiamo premere la combinazione di tasti: CTRL+ALT+Canc.
* Riavvia Explorer: riavviamo comodamente Windows Explorer da NVDA.
Possiamo farlo tramite una scorciatoia che assegniamo o dal menu TCA-SystemUtilities.* Conoscere l'architettura del sistema: ci dirà qual è l'architettura di Windows (32 o 64 bit).
* Nascondi cartelle: ci consente di inserire l'attributo nascosto nella cartella in cui ci troviamo, ovvero la cartella non verrà mostrata (dobbiamo inserirla affinché abbia effetto).
* Mostra cartelle nascoste: questa funzione ci consente di rendere visibili tutte le cartelle e i file nascosti (validi in chiavette USB, unità esterne e altro), molto utile quando si collega qualsiasi dispositivo esterno. Dobbiamo entrare nella cartella e premere la scorciatoia da tastiera.
 
## Funzioni di riparazione del sistema.
* Esegui una scansione del sistema con SFC: ci consente di eseguire una scansione / riparazione del file system di Windows SFC /SCANNOW.
* Cancella cache DNS: cancella rapidamente e direttamente tutta la cache DNS di Windows (può migliorare i problemi di navigazione in Internet). (
* Pulisci disco: ci consente di avviare Windows Disk Cleaner, ma con opzioni molto più avanzate. Pulirà tutti i dischi e i dispositivi di archiviazione che abbiamo collegato al sistema.
La prima volta che lo eseguiamo, verrà visualizzata una finestra di dialogo per creare un profilo di pulizia, possiamo selezionare tutte le caselle che vogliamo pulire più a fondo. È conveniente che premiamo il pulsante: "Crea profilo" questo è necessario farlo solo una volta. Abbiamo una casella di controllo che possiamo contrassegnare se non vogliamo che questa finestra di dialogo appaia di nuovo. 
* Ripara il sistema con Dism: esegui una scansione approfondita e prova a riparare i problemi in Windows.

## Funzioni dirette degli appunti:
* Copia negli appunti l'elenco delle cartelle o dei file del percorso corrente:
Copia l'elenco degli elementi del percorso in cui ci troviamo direttamente negli appunti, così possiamo incollarlo in qualsiasi posto modificabile.
* Copia negli appunti le informazioni sulle schede audio: ci permette di copiare direttamente negli appunti le informazioni su tutti i dispositivi audio che abbiamo nel sistema.
così possiamo incollarlo in qualsiasi posto modificabile.
* Copia le informazioni dell'intero sistema negli appunti: ci consente di copiare direttamente un riepilogo del nostro sistema.
così possiamo incollarlo in qualsiasi posto modificabile.
* Copia il percorso: copierà il percorso della cartella in cui ci troviamo negli appunti.
 così possiamo incollarlo in qualsiasi posto modificabile. 

## Opzioni di sicurezza di Windows (Windows Defender).
* Analizza avvio del sistema: esegue direttamente un'analisi di virus e malware dei file appartenenti al settore di avvio di Windows (settore di avvio).
* Scansione completa: avvia direttamente una scansione antivirus dell'intero sistema.
* Scansione rapida: avvia direttamente una scansione rapida di virus e malware (di parti di sistema essenziali).
* Scansiona file compressi: attiva direttamente,L'antivirus di Windows può scansionare file compressi (rar, zip, ace, tar, ecc.).
* Non eseguire la scansione di file compressi: disabilita direttamente l'antivirus di Windows dalla scansione di file compressi (rar, zip, ace, tar, ecc.).
* Elenco dei file in quarantena negli appunti: copia negli appunti, un elenco e le informazioni di tutti i file che l'antivirus di Windows ha messo in quarantena.

## Opzioni multimediali.
* Attiva Webcam: Ci permette comodamente da NVDA di attivare la webcam se ce l'abbiamo (lasciarla pronta per essere utilizzata).
* Disattiva Webcam: Ci permette comodamente da NVDA di disabilitare la webcam se ce l'abbiamo (disabilitarla, nessun programma può usarla).
* Mixer del volume: ci consente di aprire facilmente il mixer del volume di Windows da NVDA.
Possiamo farlo dal menu TCA SystemUtilities, nella sezione: "Voce e multimedia", oppure possiamo stabilire una scorciatoia da tastiera.
* Apri opzioni vocali: apre rapidamente le opzioni o le proprietà di sintesi vocale. Qui possiamo scegliere la nostra voce TTS installata di default sul sistema. 
 * Apri opzioni audio: ci consente di aprire direttamente le opzioni audio del pannello di controllo (audio, riproduzione, registrazione, comunicazioni).
 
## Apri rapidamente alcune funzioni di sistema:
* Apri Ottimizza unità: ci consente di aprire direttamente questa interessante funzionalità di Windows, per migliorare le prestazioni dei nostri dischi rigidi.
* Apri mappa caratteri: apre direttamente questa interessante funzionalità di Windows. Ciò ci consente di scegliere e conoscere tutti i segni, i numeri e le lettere esistenti nel sistema.
Molto utile per conoscere segni rari o difficili da ottenere con la tastiera.
* Procedura guidata di salvataggio delle password utente: Apre la procedura guidata di questa utilissima ma poco conosciuta utility di Windows.
Ciò ci consente di salvare le credenziali (nomi, password e altro), degli account utente che abbiamo nel sistema.
* Apri procedura guidata per trasferire file tramite Bluethoot: ci consente di avviare direttamente questa procedura guidata per ricevere o inviare file tramite i nostri dispositivi Bluethoot.
* Apri Opzioni cartella: apre direttamente questa funzione molto utilizzata, per gestire Esplora risorse, visualizzazione di cartelle, visualizzazione di estensioni di file e altro.
* Apri cartella Roaming: apri direttamente la cartella AppData>Roaming (qui troviamo la cartella di configurazione NVDA, e di molti altri programmi).
* Apri Gestione disco: ci permette di aprire direttamente questa interessante funzionalità per gestire i dischi, le partizioni e altri dispositivi di archiviazione installati sul nostro PC.
* Apri password di backup:
Si aprirà questo utile Wizard poco conosciuto che ci permette di fare un backup della password di Windows,per poterlo recuperare da un dispositivo esterno.
* apri Gestione risorse del computer: possiamo aprire direttamente questo potente e poco conosciuto strumento Windows. È come un Gestione attività migliorato, possiamo gestire tutti i servizi, le applicazioni e i processi in esecuzione sul nostro sistema.
Inoltre possiamo sapere quanta memoria, disco, rete e altro i programmi consumano.
* Apri Gestione dispositivi: ci consente di aprire questa utile funzionalità di Windows per gestire l'hardware e i driver del computer.
* Conoscere la versione di Windows: si apriranno le informazioni con la versione del sistema operativo.
* Apri sito ufficiale degli add-on: si aprirà nel browser predefinito, il sito ufficiale per ottenere add-on NVDA.

## Nota importante!
L'add-on è ancora in fase di test (Beta).
Inoltre, tutte le scorciatoie da tastiera possono essere assegnate a gusto personale, dalla finestra di dialogo Preferenze NVDA > Gesti di immissione.

## Modifiche alla versione: 04.
* Nuova funzione per entrare nel BIOS-UEFI del sistema (nella sezione: "Arresto del sistema").
* Modificato il menu: "Suono e voce", in: "Voce e multimedia".
* 2 Nuove funzioni nella sezione: "Voce e multimedia" (Attiva/disattiva la webcam).
* Nuova funzionalità: "Cancella cache DNS" (nella sezione Riparazione e ottimizzazione).
* Ristrutturazione della documentazione degli add-on.
* Correzione di sicurezza (sys.path.remove()).

## Modifiche alla versione 03:
* In questa versione TCA SystemUtilities è già completamente compatibile con il nuovo sistema: Windows 11.
* Nuovo menu: Sicurezza di Windows
con diverse opzioni per quanto riguarda l'antivirus di Windows.
* Un'altra opzione nel menu: Arresto del sistema, l'opzione: "sospendere il sistema".
* In questa versione l'add-on è tradotto nelle seguenti lingue: arabo, portoghese (Portogallo, portoghese Brasile) e rumeno.

## Modifiche alla versione: 02.
* In questa versione l'add-on ha un comodo Menu da cui possiamo eseguire la maggior parte delle sue funzionalità (non tutte).
Si trova nel menu: "Strumenti" di NVDA e ha il nome del plug-in: "TCA SystemUtilities".
* Tutte le scorciatoie preimpostate sono state rimosse in questa versione, quindi ora devi assegnare le scorciatoie a qualsiasi funzione, dal menu: "Gesti di input" di NVDA.
* Altre funzioni nelle sezioni: Arresto del sistema, Esplora risorse, Suono e voce, Ripristino del sistema.
* Ottimizzazione di tutto il codice dell'add-on.

***

Codice del progetto su GitHub:
[https://github.com/peterrc87/TCA-SystemUtilities-NVDA-Complemento](https://github.com/peterrc87/TCA-SystemUtilities-NVDA-Complemento)