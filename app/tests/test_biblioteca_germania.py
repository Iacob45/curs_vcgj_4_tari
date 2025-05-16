import logging
from app.lib.biblioteca_germania import descriere_germania, capitala_germania, steag_germania
logger = logging.getLogger(__name__)

def test_descriere_germania():
    if descriere_germania() == """Germania, cu o populație de aproximativ 84 de milioane de locuitori și o suprafață de 357.022 km², este situată în Europa Centrală și reprezintă una dintre cele mai influente puteri economice și politice ale continentului. Capitala sa, Berlin, este un important centru cultural și istoric, iar țara este renumită pentru infrastructura sa modernă, producția industrială avansată, tradițiile bogate și contribuțiile majore în știință, artă și tehnologie.""":
        logger.info("Merge functia descriere_germania")
        assert True
    else:
        logger.info("Nu merge functia descriere_germania")
        assert False

def test_capitala_germania():
    if capitala_germania() == "Berlin":
        logger.info(f"Merge functia capitala_germania")
        assert True
    else:
        logger.info("Nu merge functia capitala_germania")
        assert False
def test_steag_germania():
    if steag_germania() == """<img src="/static/Drapel_Germania.png" alt="Drapel Germania" width="1000", height="600">""":
        logger.info("Merge functia steag_germania")
        assert True
    else:
        logger.info("Nu merge functia steag_germania")
        assert False

if __name__ == "__main__":
    test_descriere_germania()
    test_capitala_germania()
    test_steag_germania()