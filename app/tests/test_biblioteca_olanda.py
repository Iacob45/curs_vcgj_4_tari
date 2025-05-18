import logging
from app.lib.biblioteca_olanda import descriere_olanda, capitala_olanda, steag_olanda
import pytest

# Configurare logare
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_descriere_olanda():
    expected_descriere = """Olanda, cunoscută oficial ca Regatul Țărilor de Jos, este o țară din Europa de Vest, renumită pentru lalele, morile de vânt și canalele sale. Capitala, Amsterdam, este un important centru cultural, iar Rotterdam găzduiește unul dintre cele mai mari porturi din Europa. Cu o economie puternică bazată pe comerț, agricultură și tehnologie, Olanda este un lider în sustenabilitate și inovație. Cultura sa este influențată de mari artiști precum Rembrandt și Van Gogh. Turismul prosperă datorită orașelor pitorești, muzeelor și tradițiilor autentice."""

    descriere = descriere_olanda()
    assert descriere == expected_descriere, f"Test eșuat! Rezultatul funcției descriere_olanda() este: {descriere}"

def test_capitala_olanda():
    assert capitala_olanda() == "Amsterdam", "Test eșuat! Capitala nu este corectă."

def test_steag_olanda():
    expected_steag = """<img src="/static/steag_olanda.png" alt="Drapel Olanda" width="1000", height="600">"""
    assert steag_olanda() == expected_steag, "Test eșuat! Codul HTML pentru steag nu este corect."

if __name__ == "__main__":
    test_descriere_olanda()
    test_capitala_olanda()
    test_steag_olanda()
