import logging
from app.lib.biblioteca_andorra import descriere_andorra, capitala_andorra, steag_andorra
logger = logging.getLogger(__name__)

def test_descriere_andorra():
    if descriere_andorra() == """Andorra, ofcial Principatul Andorra (Catalana:Principat d'Andorra), este un mic stat situat in sud-vestul Europei, intre Franta la nord si Spania la sud.Aflat in Muntii Pirinei, Andorra are o populatie de aproximtiv 80.000 de locuitori, fiind una din cele mai mici tari din Europa, aatat ca suprafata, cat si ca populatie.Andorra este un principat parlamentar condus de doi co-printi: presedintele Frantei si episcopul de Urgel(din Spania).Capitala tarii este Andorra la Vella, cel mai inalt oras-capitala din Europa, situat la o altitudine de peste 1000m.Numele de "Andorra" ar proveni, potrivit unei traditii locale, din cuvantul arab "al-Darra" care inseamna "padure", reflectand peisajul montan si impadurit al regiunii.""":
        logger.info("Merge functia descriere_andorra")
        assert True
    else:
        logger.info("Nu merge functia descriere_andorra")
        assert False

def test_capitala_andorra():
    if capitala_andorra() == "Andorra la Vella":
        logger.info(f"Merge functia capitala_andorra")
        assert True
    else:
        logger.info("Nu merge functia capitala_andorra")
        assert False
def test_steag_andorra():
    if steag_andorra() == """<img src="/static/Drapelul-Andorrei.png" alt="Drapelul Andorrei" width="1000" height="600">""":
        logger.info("Merge functia steag_andorra")
        assert True
    else:
        logger.info("Nu merge functia steag_andorra")
        assert False

if __name__ == "__main__":
    test_descriere_andorra()
    test_capitala_andorra()
    test_steag_andorra()
