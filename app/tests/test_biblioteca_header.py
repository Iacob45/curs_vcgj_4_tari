import logging
from app.lib.biblioteca_header import header_descriere, header_capitala, header_steag
logger = logging.getLogger(__name__)

def test_header_descriere():
    if header_descriere() == """
    <a href="/romania/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a>
    <a href="/romania/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
    </a><br><br>
    <h1>Aceasta este descrierea României</h1><br><br>
    """:
        logger.info("Merge functia header_descriere")
        assert True
    else:
        logger.info("Nu merge functia header_descriere")
        assert False

def test_header_capitala():
    if header_capitala() == """
    <a href="/romania">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descriere</button>
    </a>
    <a href="/romania/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
    </a><br><br>
    <h1>Aceasta este capitala României</h1><br><br>
    """:
        logger.info("Merge functia header_capitala")
        assert True
    else:
        logger.info("Nu merge functia header_capitala")
        assert False
def test_header_steag():
    if header_steag() == """
    <a href="/romania">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descriere</button>
    </a>
    <a href="/romania/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a><br><br>
    <h1>Acesta este steagul României</h1><br><br>
    """:
        logger.info("Merge functia header_steag")
        assert True
    else:
        logger.info("Nu merge functia header_steag")
        assert False

if __name__ == "__main__":
    test_header_descriere()
    test_header_capitala()
    test_header_steag()
