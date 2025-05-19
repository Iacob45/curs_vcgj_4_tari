import logging
from app.lib.biblioteca_bulgaria import descriere_bulgaria, capitala_bulgaria, steag_bulgaria
import pytest

# Configurare logare
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_descriere_bulgaria():
	expected_descriere = """Bulgaria este o țară situată în sud-estul Europei, pe malul vestic al Mării Negre. Are un relief variat, cu munți, câmpii și litoral. Capitala sa este Sofia, un important centru cultural și economic. Bulgaria are o istorie bogată, influențată de civilizațiile tracică, romană și bizantină. Este membră a Uniunii Europene din 2007. """
	
	descriere = descriere_bulgaria()
	assert descriere == expected_descriere, f"Test esuat"

def test_capitala_bulgaria():
	assert capitala_bulgaria() == "Sofia", "Test esuat"

def test_steag_bulgaria():
	expected_steag = """<img src="/static/Steag_bulgaria.png" alt="Drapel Bulgaria" width="1000", height="600"> """
	assert steag_bulgaria() == expected_steag, "Test esuat"

if __name__ == "__main__":
	test_descriere_bulgaria()
	test_capitala_bulgaria()
	test_steag_bulgaria()
