# vcard-truscreen

Biglietto da visita virtuale statico (HTML/CSS/JS vanilla) per Valeria Negrini
(TruScreen Pty Limited), con QR code vCard generato via script Python.

## Struttura

```
vcard-truscreen/
├── assets/                     logo e QR code generato
├── scripts/generate_qr.py      genera il QR della vCard
├── requirements.txt
└── negrini_vcard.html          biglietto da visita
```

## Installazione dipendenze

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Generare il QR code

```bash
python scripts/generate_qr.py
```

Il PNG viene salvato in `assets/negrini_vcard_qr.png`.

## Aprire il biglietto da visita

Apri `negrini_vcard.html` direttamente nel browser (doppio click o
`file://` locale).

**Importante:** la stringa vCard in `scripts/generate_qr.py` deve restare
identica, carattere per carattere, a quella incorporata nello `<script>`
di `negrini_vcard.html`, in modo che il QR code e il file `.vcf` scaricabile
producano lo stesso contatto.
