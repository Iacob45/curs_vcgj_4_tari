import logging
from app.lib.biblioteca_header import header_descriere, header_capitala, header_steag
logger = logging.getLogger(__name__)

def test_header_descriere():
    expected_result = "Descrierea Portugaliei"
    result = header_descriere()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției header_descriere() este: {result}"
    logger.info("Merge functia header_descriere")

def test_header_capitala():
    expected_result = "Capitala Portugaliei"
    result = header_capitala()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției header_capitala() este: {result}"
    logger.info("Merge functia header_capitala")

def test_header_steag():
    expected_result = "Steagul Portugaliei"
    result = header_steag()
    assert result == expected_result, f"Test eșuat! Rezultatul funcției header_steag() este: {result}"
    logger.info("Merge functia header_steag")

if __name__ == "__main__":
    test_header_descriere()
    test_header_capitala()
    test_header_steag()
