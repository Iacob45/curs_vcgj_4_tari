import logging
from app.lib.biblioteca_header import header_descriere, header_capitala, header_steag
logger = logging.getLogger(__name__)

def test_header_descriere():
    result = header_descriere()
    if "Luxembourg" in result and "Vezi Capitala" in result and "Vezi Steag" in result:
        logger.info("Merge functia header_descriere")
        assert True
    else:
        logger.info("Nu merge functia header_descriere")
        assert False

def test_header_capitala():
    result = header_capitala()
    if "Luxembourg" in result and "Vezi Descriere" in result and "Vezi Steag" in result:
        logger.info("Merge functia header_capitala")
        assert True
    else:
        logger.info("Nu merge functia header_capitala")
        assert False

def test_header_steag():
    result = header_steag()
    if "Luxembourg" in result and "Vezi Descriere" in result and "Vezi Capitala" in result:
        logger.info("Merge functia header_steag")
        assert True
    else:
        logger.info("Nu merge functia header_steag")
        assert False

if __name__ == "__main__":
    test_header_descriere()
    test_header_capitala()
    test_header_steag()