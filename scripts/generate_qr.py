#!/usr/bin/env python3
"""Genera il QR code vCard per il biglietto da visita TruScreen (Valeria Negrini)."""
from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_M

VCARD = "\r\n".join([
    "BEGIN:VCARD",
    "VERSION:3.0",
    "N:Negrini;Valeria;;;",
    "FN:Valeria Negrini",
    "ORG:TruScreen Pty Limited",
    "TITLE:Field Training Manager EU",
    "TEL;TYPE=CELL:+393381477262",
    "EMAIL;TYPE=WORK:valeria.negrini@truscreen.com",
    "URL:https://www.truscreen.com",
    r"ADR;TYPE=WORK:;;Level 1\, 1 Jamison Street;Sydney;NSW;2000;Australia",
    r"ADR;TYPE=POSTAL:GPO Box 3904;;;Sydney;NSW;2001;Australia",
    "END:VCARD",
])

OUT = Path(__file__).resolve().parent.parent / "assets" / "negrini_vcard_qr.png"


def main() -> None:
    qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_M, box_size=10, border=4)
    qr.add_data(VCARD)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(f"QR salvato: {OUT}  ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
