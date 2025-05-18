import logging
from app.lib.biblioteca_Luxembourg import descriere_luxembourg, capitala_luxembourg, steag_luxembourg
logger = logging.getLogger(__name__)

def test_descriere_luxembourg():
    result = descriere_luxembourg()
    if "Luxembourg este un stat suveran" in result and "634.730 locuitori" in result:
        logger.info("Merge functia descriere_luxembourg")
        assert True
    else:
        logger.info("Nu merge functia descriere_luxembourg")
        assert False

def test_capitala_luxembourg():
    result = capitala_luxembourg()
    if "Orașul Luxembourg" in result and "124.500 de locuitori" in result:
        logger.info("Merge functia capitala_luxembourg")
        assert True
    else:
        logger.info("Nu merge functia capitala_luxembourg")
        assert False

def test_steag_luxembourg():
    result = steag_luxembourg()
    if '<img src="https://upload.wikimedia.org/wikipedia/commons/d/da/Flag_of_Luxembourg.svg"' in result:
        logger.info("Merge functia steag_luxembourg")
        assert True
    else:
        logger.info("Nu merge functia steag_luxembourg")
        assert False

if __name__ == "__main__":
    test_descriere_luxembourg()
    test_capitala_luxembourg()
    test_steag_luxembourg()