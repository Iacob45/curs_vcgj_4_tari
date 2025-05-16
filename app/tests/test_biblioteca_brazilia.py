import logging
from app.lib.biblioteca_brazilia import descriere_brazilia, capitala_brazilia, steag_brazilia
logger = logging.getLogger(__name__)

def test_descriere_brazilia():
    if descriere_brazilia() == """
    <a href="/brazilia/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a>
    <a href="/brazilia/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
    </a><br><br>
    <h1>Aceasta este descrierea Braziliei</h1><br><br>
    Brazilia este cea mai mare țară din America de Sud și una dintre cele mai populate din lume. Este renumită pentru diversitatea sa naturală, inclusiv pădurea Amazoniană, și pentru cultura bogată, influențată de tradiții africane, europene și indigene. Este recunoscută internațional pentru fotbal, dansul samba, carnavalurile spectaculoase și peisajele sale exotice.""":
        logger.info("Merge functia descriere_brazilia")
        assert True
    else:
        logger.info("Nu merge functia descriere_brazilia")
        assert False

def test_capitala_brazilia():
    if capitala_brazilia() == """
    <a href="/brazilia">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descriere</button>
    </a>
    <a href="/brazilia/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
    </a><br><br>
    <h1>Aceasta este capitala Braziliei</h1><br><br>
    Brasília""":
        logger.info(f"Merge functia capitala_brazilia")
        assert True
    else:
        logger.info("Nu merge functia capitala_brazilia")
        assert False
def test_steag_brazilia():
    if steag_brazilia() == """
    <a href="/brazilia">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descriere</button>
    </a>
    <a href="/brazilia/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a><br><br>
    <h1>Acesta este steagul Braziliei</h1><br><br>
    <img src="/static/Steagul-Braziliei.png" alt="Steagul Braziliei" width="1000" height="600">""":
        logger.info("Merge functia steag_brazilia")
        assert True
    else:
        logger.info("Nu merge functia steag_brazilia")
        assert False

if __name__ == "__main__":
    test_descriere_brazilia()
    test_capitala_brazilia()
    test_steag_brazilia()
