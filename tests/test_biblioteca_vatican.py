import logging
from app.lib.biblioteca_vatican import descriere_vatican, capitala_vatican, steag_vatican

logger = logging.getLogger(__name__)


def test_descriere_vatican():
    expected_descriere = """
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #000000;
            color: #FFD700;
            padding: 40px;
        }
        h1 {
            color: #FFD700;
            font-size: 32px;
            margin-bottom: 20px;
        }
        p {
            font-size: 18px;
            line-height: 1.8;
            max-width: 800px;
            background-color: #111;
            padding: 20px;
            border-left: 5px solid #FFD700;
            border-radius: 6px;
        }
        .button-group {
            margin-bottom: 30px;
        }
        a button {
            padding: 10px 20px;
            font-size: 16px;
            margin-right: 10px;
            background-color: #FFD700;
            color: #000;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: 0.3s;
        }
        a button:hover {
            background-color: #e6c200;
        }
    </style>

    <div class="button-group">
        <a href="/vatican/capitala">
            <button>Capitala</button>
        </a>
        <a href="/vatican/steag">
            <button>Steag</button>
        </a>
    </div>

    <h1>Vatican</h1>
    <p>
        Vaticanul este cel mai mic stat independent din lume, ca suprafata si populatie.
        Este situat in interiorul Romei si este sediul Bisericii Catolice si resedinta Papei.
        Aici se gasesc Capela Sixtina, Basilica Sf. Petru si multe opere de arta celebre.
    </p>
    """

    if descriere_vatican().strip() == expected_descriere.strip():
        logger.info("Functioneaza descriere_vatican")
        assert True
    else:
        logger.error("Nu functioneaza descriere_vatican")
        assert False


def test_capitala_vatican():
    expected_html = """
    <style>
        body {
            background-color: #000;
            color: #FFD700;
            font-family: 'Segoe UI', sans-serif;
            padding: 40px;
        }
        h1 {
            font-size: 30px;
            color: #FFD700;
            margin-bottom: 20px;
        }
        p {
            font-size: 18px;
            line-height: 1.8;
            background-color: #111;
            padding: 20px;
            border-radius: 6px;
            border-left: 5px solid #FFD700;
            max-width: 800px;
        }
        .button-group {
            margin-bottom: 30px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin-right: 10px;
            background-color: #FFD700;
            color: #000;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #e6c200;
        }
    </style>

    <div class="button-group">
        <a href="/vatican">
            <button>Descriere</button>
        </a>
        <a href="/vatican/steag">
            <button>Steag</button>
        </a>
    </div>

    <h1>Capitala Vaticanului: Vatican</h1>
    <p>
        Vaticanul este un oras-stat suveran. Capitala este chiar orasul Vatican.
        Aici se afla centrul administrativ si spiritual al Bisericii Catolice, cu locuri precum
        Palatul Apostolic si Muzeele Vaticanului.
    </p>
    """

    if capitala_vatican().strip() == expected_html.strip():
        logger.info("Functioneaza capitala_vatican")
        assert True
    else:
        logger.error("Nu functioneaza capitala_vatican")
        assert False


def test_steag_vatican():
    expected_html = """
    <style>
        body {
            background-color: #000;
            color: #FFD700;
            font-family: 'Segoe UI', sans-serif;
            padding: 40px;
        }
        h1 {
            color: #FFD700;
            font-size: 32px;
            margin-bottom: 20px;
        }
        .button-group {
            margin-bottom: 30px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin-right: 10px;
            background-color: #FFD700;
            color: #000;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        button:hover {
            transform: scale(1.05);
        }
    </style>

    <div class="button-group">
        <a href="/vatican/capitala">
            <button>Capitala</button> 
        </a>
        <a href="/vatican">
            <button>Descriere</button> 
        </a>
    </div>

    <h1>Steagul Vaticanului</h1>
    <img src="/static/flag.png" alt="Steagul Vaticanului">
    """

    if steag_vatican().strip() == expected_html.strip():
        logger.info("Functioneaza steag_vatican")
        assert True
    else:
        logger.error("Nu functioneaza steag_vatican")
        assert False


if __name__ == "__main__":
    test_descriere_vatican()
    test_capitala_vatican()
    test_steag_vatican()