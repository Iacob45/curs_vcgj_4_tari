import logging
from app.lib.biblioteca_honduras import descriere_honduras, capitala_honduras, steag_honduras
logger = logging.getLogger(__name__)

def test_descriere_honduras():
    "Test descriere"
    text = """
            <a href="/honduras/capitala">
                <button style="font-size: 20px;">Capitala</button>
            </a>
            <a href="/honduras/steag">
                <button style="font-size: 20px;">Steag</button>
            </a><br>
            <h1>Honduras</h1><br>
            """
    text += "Honduras este o țară situată în America Centrală, având graniță cu Guatemala, El Salvador și Nicaragua,"
    text += "precum și deschidere la Marea Caraibilor și Oceanul Pacific. Capitala sa este Tegucigalpa."
    text += "Țara are un relief variat, format din munți, câmpii fertile și zone de coastă,"
    text += "iar clima este în general tropicală."
    if descriere_honduras() == text:
        logger.info("Merge functia descriere_honduras")
        assert True
    else:
        logger.info("Nu merge functia descriere_honduras")
        assert False

def test_capitala_honduras():
    "Test capitala"
    text = """
            <a href="/honduras">
                <button style="font-size: 20px;">Descriere</button>
            </a>
            <a href="/honduras/steag">
                <button style="font-size: 20px;">Steag</button>
            </a><br>
            <h1>Honduras</h1><br>
            """
    text += "Tegucigalpa"
    if capitala_honduras() == text:
        logger.info(f"Merge functia capitala_honduras")
        assert True
    else:
        logger.info("Nu merge functia capitala_honduras")
        assert False

def test_steag_honduras():
    "Test steag"
    text = """
            <a href="/honduras/capitala">
                <button style="font-size: 20px;">Capitala</button>
            </a>
            <a href="/honduras">
                <button style="font-size: 20px;">Descriere</button>
            </a><br>
            <h1>Honduras</h1><br>
            """
    text += """<img src="/static/honduras__42861.jpg" alt="Steagul Hondurasului">"""
    if steag_honduras() == text:
        logger.info("Merge functia steag_honduras")
        assert True
    else:
        logger.info("Nu merge functia steag_honduras")
        assert False

if __name__ == "__main__":
    test_descriere_honduras()
    test_capitala_honduras()
    test_steag_honduras()
