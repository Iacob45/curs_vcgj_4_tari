import logging
from app.lib.biblioteca_spania import descriere_spania, capitala_spania, steag_spania
logger = logging.getLogger(__name__)

def test_descriere_spania():
    if descriere_spania() == """Spania este un stat național unitar, organizat ca monarhie constituțională, situat în sud-vestul Europei, în Peninsula Iberică. Se învecinează cu Franța și Andorra la nord-est, cu Portugalia la vest și cu Gibraltar la sud, fiind mărginită de Marea Mediterană și Oceanul Atlantic. Are o suprafață de 505.990 km² (aprox. 10% din teritoriul Uniunii Europene) și un climat variat, predominant mediteranean.
Cu o populație de aproximativ 47,6 milioane de locuitori (în 2023), Spania este al patrulea stat ca populație din UE. Capitala este Madrid, iar alte orașe mari includ Barcelona, Valencia și Sevilla. Teritoriul cuprinde 17 comunități autonome și 2 orașe autonome, reflectând o diversitate culturală bogată. Numele Spaniei provine din latinescul Hispania.
Spania are o economie puternică, bazată pe turism, agricultură, industrie și energie regenerabilă. Resursele naturale includ minereuri, cărbune, marmură și apă geotermală.""":
        logger.info("Merge functia descriere_spania")
        assert True
    else:
        logger.info("Nu merge functia descriere_spania")
        assert False

def test_capitala_spania():
    if capitala_spania() == "Madrid":
        logger.info(f"Merge functia capitala_spania")
        assert True
    else:
        logger.info("Nu merge functia capitala_spania")
        assert False
def test_steag_spania():
    if steag_spania() == """<img src="/static/Steag-Spania-768x512-3700220658.png" alt="Steagul Spaniei" width="800" height="500">""":
        logger.info("Merge functia steag_spania")
        assert True
    else:
        logger.info("Nu merge functia steag_spania")
        assert False

if __name__ == "__main__":
    test_descriere_spania()
    test_capitala_spania()
    test_steag_spania()
