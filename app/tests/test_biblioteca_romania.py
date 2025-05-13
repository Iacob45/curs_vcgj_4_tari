import logging
logger = logging.getLogger(__name__)
from app.lib.biblioteca_canada import descriere_canada, capitala_canada, steag_canada

def test_descriere_romania():
    if descriere_canada() == """
    <a href="/canada/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a>
    <a href="/canada/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
    </a><br><br>
    <h1>Aceasta este descrierea Canadei</h1><br><br>
    <p>Canada este cea mai misto tara</p>""":
        logger.info(f"Merge functia descriere_romania")
        assert True
    else:
        logger.info(f"Nu merge functia descriere_romania")
        assert False

def test_capitala_romania():
    if capitala_canada() == "Bucuresti":
        logger.info(f"Merge functia capitala_romania")
        assert True
    else:
        logger.info(f"Nu merge functia capitala_romania")
        assert False
def test_steag_romania():
    if steag_canada() == """<img src="/static/Drapelul-Romaniei.jpg" alt="Drapelul Romaniei" width="1000" height="600">""":
        logger.info(f"Merge functia steag_romania")
        assert True
    else:
        logger.info(f"Nu merge functia steag_romania")
        assert False

if __name__ == "__main__":
    test_descriere_romania()
    test_capitala_romania()
    test_steag_romania()
