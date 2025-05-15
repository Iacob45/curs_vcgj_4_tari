import logging
from app.lib.biblioteca_guatemala import descriere_guatemala, capitala_guatemala, steag_guatemala
logger = logging.getLogger(__name__)

def test_descriere_guatemala():
    if descriere_guatemala() == """Guatemala, oficial Republica Guatemala (Spaniolă: República de Guatemala), este o țară din America Centrală, în partea de sud a Americii de Nord, ce se învecinează cu Mexic la nord-vest, Oceanul Pacific la sud-vest, Belize și Marea Caraibelor la nord-est și cu Honduras și El Salvador la sud-est. Cu o populație de aproximativ 17,6 milioane de locuitori, este cel mai populat stat din America Centrală.
            Guatemala este o republică cu reprezentare democratică; capitala țării și totodată cel mai mare oraș este Nueva Guatemala de la Asunción, mai cunoscut sub numele de Guatemala City.
            Numele de „Guatemala” provine din cuvântul Cuauhtēmallān care în limba nahuatl înseamnă „locul multor pomi”, o traducere a mayanului quiche (k'iche'), „mulți pomi”.""":
        logger.info("Merge functia descriere_guatemala")
        assert True
    else:
        logger.info("Nu merge functia descriere_guatemala")
        assert False

def test_capitala_guatemala():
    if capitala_guatemala() == "Ciudad de Guatemala(Guatemala City)":
        logger.info(f"Merge functia capitala_guatemala")
        assert True
    else:
        logger.info("Nu merge functia capitala_guatemala")
        assert False
def test_steag_guatemala():
    if steag_guatemala() == """<img src="/static/Drapelul-Guatemalei.png" alt="Drapelul Guatemalei" width="1000" height="600">""":
        logger.info("Merge functia steag_guatemala")
        assert True
    else:
        logger.info("Nu merge functia steag_guatemala")
        assert False

if __name__ == "__main__":
    test_descriere_guatemala()
    test_capitala_guatemala()
    test_steag_guatemala()
