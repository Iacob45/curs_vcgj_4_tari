import logging
from app.lib.biblioteca_kosovo import descriere_kosovo, capitala_kosovo, steag_kosovo
logger = logging.getLogger(__name__)

def test_descriere_kosovo():
    if descriere_kosovo() == """osovo, oficial Republica Kosovo (Albaneză: Republika e Kosovës, Sârbă: Република Косово), este o țară situată în sud-estul Europei, în regiunea Balcanilor, care se învecinează cu Serbia la nord și est, Muntenegru la vest, Albania la sud-vest și Macedonia de Nord la sud. Are o populație de aproximativ 1,8 milioane de locuitori, majoritatea de etnie albaneză. Kosovo este o republică parlamentară cu un sistem democratic, iar capitala și cel mai mare oraș este Pristina. Statutul său de independență, declarat în 2008, este recunoscut de peste 100 de țări, deși nu de toți membrii ONU. Numele „Kosovo” provine din cuvântul sârb „kos” care înseamnă „mierlă” și se referă la Câmpia Mierlei (Kosovo Polje), loc important din punct de vedere istoric pentru regiune.""":
        logger.info("Merge functia descriere_kosovo")
        assert True
    else:
        logger.info("Nu merge functia descriere_kosovo")
        assert False

def test_capitala_kosovo():
    if capitala_kosovo() == "Prishtina":
        logger.info(f"Merge functia capitala_kosovo")
        assert True
    else:
        logger.info("Nu merge functia capitala_kosovo")
        assert False
def test_steag_kosovo():
    if steag_kosovo() == """<img src="/static/Flag_of_Kosovo.png" alt="Steag Kosovo" width="1000" height="600">""":
        logger.info("Merge functia steag_kosovo")
        assert True
    else:
        logger.info("Nu merge functia steag_kosovo")
        assert False

if __name__ == "__main__":
    test_descriere_kosovo()
    test_capitala_kosovo()
    test_steag_kosovo()
