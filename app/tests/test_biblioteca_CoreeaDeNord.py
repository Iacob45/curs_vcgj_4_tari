import logging
logger = logging.getLogger(__name__)
from app.lib.biblioteca_CoreeaDeNord import descriere_CoreeaDeNord, capitala_CoreeaDeNord, steag_CoreeaDeNord

def test_descriere_CoreeaDeNord() -> None:
    if descriere_CoreeaDeNord() == """
       <p style="font-size: 20px; line-height: 1.6;">
           CoreeaDeNord este o tara care respecta cetatenii si valorile libere ale acestora.Poti sa faci tot ce vrei
           daca te lasa grasutul.
       </p>
       """:
        logger.info(f"Merge functia descriere_CoreeaDeNord")
        print("Merge functia descriere_CoreeaDeNord")
        assert True
    else:
        logger.info(f"Nu merge functia descriere_CoreeaDeNord")
        print("Nu merge functia descriere_CoreeaDeNord")
        assert False

def test_steag_CoreeaDeNord():
    if steag_CoreeaDeNord() == """<img src="/static/CoreeaDeNordsteag.jpg" alt="Drapelul CoreeaDeNord" width="1000" height="600">""":
        logger.info(f"Merge functia steag_CoreeaDeNord")
        print("Merge functia steag_CoreeaDeNord")
        assert True
    else:
        logger.info(f"Nu merge functia steag_CoreeaDeNord")
        print("Nu merge functia steag_CoreeaDeNord")
        assert False

def test_capitala_CoreeaDeNord():
    if capitala_CoreeaDeNord() == """
           <p style="font-size: 50px; line-height: 1.6;">
               Pyongyang
           </p>
           """:
        logger.info(f"Merge functia capitala_CoreeaDeNord")
        print("Merge functia capitala_CoreeaDeNord")
        assert True
    else:
        logger.info(f"Nu merge functia capitala_CoreeaDeNord")
        print("Nu merge functia capitala_CoreeaDeNord")
        assert False

if __name__ == "__main__":
    test_descriere_CoreeaDeNord()
    test_steag_CoreeaDeNord()
    test_capitala_CoreeaDeNord()