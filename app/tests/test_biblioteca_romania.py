import logging
logger = logging.getLogger(__name__)
from app.lib.biblioteca_romania import descriere_romania, capitala_romania, steag_romania

def test_descriere_romania():
    if descriere_romania() == """România este un stat național unitar, o republică semiprezidențială situată în Europa Centrală și de Est, mărginită de Marea Neagră la sud-est, între Bulgaria și Ucraina. De asemenea, se învecinează cu Ungaria la vest, cu Serbia la sud-vest și cu Republica Moldova la est. Se întinde pe 238.397 de kilometri pătrați, reprezentând 4,8% din teritoriul Europei și 5,4% din suprafața Uniunii Europene și are un climat temperat-continental.
Cu o populație de 19.053.815 locuitori (la începutul anului 2022), România este al șaselea cel mai populat stat membru al Uniunii Europene. Capitala și cel mai mare oraș al său, București, era în ianuarie 2024 al optulea oraș ca mărime din UE, având o populație de 1.716.961 locuitori. Teritoriul național cuprinde regiunile istorice Valahia sau Țara Românească (inclusiv Dobrogea), Moldova (inclusiv Bucovina), Transilvania (inclusiv Banat, Maramureș și Crișana). Numele România și român derivă din latinescul romanus, adică „cetățean al Romei”.
România se află pe locul zece în lume în ceea ce privește diversitatea mineralelor produse în țară, în România fiind extrase și prelucrate aproximativ 80 de tipuri de resurse minerale, de la alabastru, ape geotermale și naturale, până la minereuri auro-argentifere, cuarț, lignit și minereuri de molibden sau de uraniu.""":
        logger.info(f"Merge functia descriere_romania")
        print("Merge functia descriere_romania")
        assert True
    else:
        logger.info(f"Nu merge functia descriere_romania")
        print("Nu merge functia descriere_romania")
        assert False

def test_capitala_romania():
    if capitala_romania() == "Bucuresti":
        logger.info(f"Merge functia capitala_romania")
        print("Merge functia capitala_romania")
        assert True
    else:
        logger.info(f"Nu merge functia capitala_romania")
        print("Nu merge functia capitala_romania")
        assert False
def test_steag_romania():
    if steag_romania() == """<img src="/static/Drapelul-Romaniei.jpg" alt="Drapelul Romaniei" width="1000" height="600">""":
        logger.info(f"Merge functia steag_romania")
        print("Merge functia steag_romania")
        assert True
    else:
        logger.info(f"Nu merge functia steag_romania")
        print("Nu merge functia steag_romania")
        assert False

if __name__ == "__main__":
    test_descriere_romania()
    test_capitala_romania()
    test_steag_romania()
