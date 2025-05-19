import logging
logger = logging.getLogger(__name__)

from app.lib.biblioteca_header import header_descriere, header_capitala, header_steag

def test_header_descriere():
    expected = """
    <a href="/egipt/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a>
    <a href="/egipt/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
    </a><br>
    <h1>Descrierea Egiptului</h1>
    """

    if header_descriere().strip() == expected.strip():
        logger.info(f"Merge functia header_descriere")
        print("Merge functia header_descriere")
        assert True
    else:
        print("Așteptat:", expected)
        print("Primit:", header_descriere())
        logger.error(f"Nu merge functia header_descriere")
        assert False


def test_header_capitala():
    expected = """
    <a href="/egipt">
        <button style="padding: 10px 15px; font-size: 16px;">Vezi Descriere</button>
    </a>
    <a href="/egipt/steag">
        <button style="padding: 10px 15px; font-size: 16px;">Vezi Steag</button>
    </a><br>
    <h1>Capitala Egiptului este :</h1>
    """


    if header_capitala().strip() == expected.strip():
        logger.info(f"Merge functia header_capitala")
        print("Merge functia header_capitala")
        assert True
    else:
        print("Așteptat:", expected)
        print("Primit:", header_capitala())
        logger.error(f"Nu merge functia header_capitala")
        assert False


def test_header_steag():
    expected = """
    <a href="/egipt">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descriere</button>
    </a>
    <a href="/egipt/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a><br><br>
    <h1>Steagul Egiptului</h1>
    """


    if header_steag().strip() == expected.strip():
        logger.info(f"Merge functia header_steag")
        print("Merge functia header_steag")
        assert True
    else:
        print("Așteptat:", expected)
        print("Primit:", header_steag())
        logger.error(f"Nu merge functia header_steag")
        assert False

if __name__ == "__main__":
    test_header_descriere()
    test_header_capitala()
    test_header_steag()
