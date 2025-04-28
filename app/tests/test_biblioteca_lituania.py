import logging
logger = logging.getLogger(__name__)
from app.lib.biblioteca_lituania import descriere_lituania, capitala_lituania, steag_lituania

def test_descriere_lituania():
    if descriere_lituania() == """
       <p style="font-size: 20px; line-height: 1.6;">
           Lituania are o populație de circa 2,9 milioane de locuitori, iar capitala și cel mai mare oraș este Vilnius. 
           Lituanienii sunt un popor baltic. Limba oficială, lituaniana, este, împreună cu letona, una din singurele două 
           limbi din ramura baltică a familiei de limbi indo-europene care încă se mai vorbesc.
       </p>
       """:
        logger.info(f"Merge functia descriere_lituania")
        print("Merge functia descriere_lituania")
        assert True
    else:
        logger.info(f"Nu merge functia descriere_lituania")
        print("Nu merge functia descriere_lituania")
        assert False

def test_steag_lituania():
    if steag_lituania() == """<img src="/static/Flag_of_Lithuania.png" alt="Drapelul Lituaniei" width="1000" height="600">""":
        logger.info(f"Merge functia steag_lituania")
        print("Merge functia steag_lituania")
        assert True
    else:
        logger.info(f"Nu merge functia steag_lituania")
        print("Nu merge functia steag_lituania")
        assert False

def test_capitala_lituania():
    if capitala_lituania() == """
           <p style="font-size: 50px; line-height: 1.6;">
               Vilnius
           </p>
           """:
        logger.info(f"Merge functia capitala_lituania")
        print("Merge functia capitala_lituania")
        assert True
    else:
        logger.info(f"Nu merge functia capitala_lituania")
        print("Nu merge functia capitala_lituania")
        assert False

if __name__ == "__main__":
    test_descriere_lituania()
    test_steag_lituania()
    test_capitala_lituania()