import logging
from app.lib.biblioteca_portugalia import descriere_portugalia, capitala_portugalia, steag_portugalia
import pytest

# Configurare logare
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_descriere_portugalia():
    expected_descriere = """Portugalia (în portugheză Portugal), oficial Republica Portugheză (în portugheză República Portuguesa, pronunțat /ʁɨ'publikɐ puɾtu'ɣezɐ/), este o țară în Peninsula Iberică din Europa de Sud-Vest. Este cea mai vestică țară din Europa continentală. La vest și sud are coastă la Oceanul Atlantic, iar la est și nord se învecinează cu Spania. Frontiera dintre Portugalia și Spania⁠(d) are 1.214 km lungime și este considerată cea mai lungă graniță neîntreruptă în cadrul Uniunii Europene. Republica include, de asemenea, arhipelagurile Azore și Madeira din Atlantic, ambele regiuni autonome cu propriile lor guverne regionale⁠."""

    descriere = descriere_portugalia()
    assert descriere == expected_descriere, f"Test eșuat! Rezultatul funcției descriere_portugalia() este: {descriere}"

def test_capitala_portugalia():
    assert capitala_portugalia() == "Lisabona", "Test eșuat! Capitala nu este corectă."

def test_steag_portugalia():
    expected_steag = """<img src="/static/Flag_of_Portugal.svg.png" alt="Drapel Portugalia" width="1000", height="600">"""
    assert steag_portugalia() == expected_steag, "Test eșuat! Codul HTML pentru steag nu este corect."

if __name__ == "__main__":
    test_descriere_portugalia()
    test_capitala_portugalia()
    test_steag_portugalia()
