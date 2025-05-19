import logging
logger = logging.getLogger(__name__)
from app.lib.biblioteca_egipt import descriere_egipt, capitala_egipt, steag_egipt

def test_descriere_egipt():
    assert isinstance(descriere_egipt(), str)
    assert len(descriere_egipt()) > 10

def test_capitala_egipt():
    if capitala_egipt() == """
           <p style="font-size: 50px; line-height: 1.6;">
               Cairo
           </p>
           """:
        logger.info(f"Merge functia capitala_egipt")
        print("Merge functia capitala_egipt")
        assert True
    else:
        logger.info(f"Nu merge functia capitala_egipt")
        print("Nu merge functia capitala_egipt")
        assert False

if __name__ == "__main__":
    test_descriere_egipt()
    test_steag_egipt()
    test_capitala_egipt()
