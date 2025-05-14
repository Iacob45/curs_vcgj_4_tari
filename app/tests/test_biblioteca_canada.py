import logging
from app.lib.biblioteca_canada import descriere_canada, capitala_canada, steag_canada

logger = logging.getLogger(__name__)


def test_descriere_canada():
    expected_descriere = """
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #eef2f7;
            color: #2c3e50;
            padding: 40px;
        }
        h1 {
            color: #d32f2f;
            margin-bottom: 10px;
        }
        p {
            font-size: 18px;
            line-height: 1.8;
            max-width: 800px;
        }
        .button-group {
            margin-bottom: 30px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin-right: 10px;
            background-color: #d32f2f;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #a52727;
        }
    </style>

    <div class="button-group">
        <a href="/canada/capitala">
            <button>Capitala</button>
        </a>
        <a href="/canada/steag">
            <button>Steag</button>
        </a>
    </div>

    <h1>Canada</h1> 
    <p> 
        Canada este a doua cea mai mare țară din lume, situată în nordul Americii de Nord. Este renumită pentru peisajele sale spectaculoase, 
        pădurile vaste, munții impunători și lacurile cristaline. Cu o populație diversă și tolerantă, Canada promovează multiculturalismul 
        și oferă unul dintre cele mai ridicate standarde de viață din lume. Este o țară bilingvă, cu engleza și franceza ca limbi oficiale.
    </p>
    """

    if descriere_canada().strip() == expected_descriere.strip():
        logger.info("Functioneaza descriere_canada")
        assert True
    else:
        logger.error("Nu functioneaza descriere_canada")
        assert False


def test_capitala_canada():
    expected_html = """
    <style>
        h1 { color: #1a237e; margin-bottom: 10px; }
        p { font-size: 18px; line-height: 1.6; }
        .button-group { margin-bottom: 30px; }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin-right: 10px;
            background-color: #3949ab;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #283593;
        }
    </style>

    <div class="button-group">
        <a href="/canada">
            <button>Descriere</button> 
        </a>
        <a href="/canada/steag">
            <button>Steag</button> 
        </a>
    </div>

    <h1>Capitala Canadei: OTTAWA</h1> 
    <p>
        Ottawa este capitala Canadei și se află în provincia Ontario. Este un oraș elegant, 
        cu clădiri guvernamentale impresionante, muzee naționale, parcuri și canale. 
        Reprezintă centrul politic al țării și reflectă diversitatea culturală canadiană.
    </p>
    """

    if capitala_canada().strip() == expected_html.strip():
        logger.info("Functioneaza capitala_canada")
        assert True
    else:
        logger.error("Nu functioneaza capitala_canada")
        assert False


def test_steag_canada():
    expected_html = """
    <style>
        h1 { color: #00695c; margin-bottom: 10px; }
        .button-group { margin-bottom: 30px; }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin-right: 10px;
            background-color: #00897b;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #004d40;
        }
        img {
            margin-top: 20px;
            max-width: 100%;
            height: auto;
            border: 4px solid #ccc;
            border-radius: 8px;
        }
    </style>

    <div class="button-group">
        <a href="/canada/capitala">
            <button>Capitala</button> 
        </a>
        <a href="/canada">
            <button>Descriere</button> 
        </a>
    </div>

    <h1>Steagul Canadei</h1>
    <img src="/static/Drapelul-Canadei.png" alt="Drapelul Canadei">
    """

    if steag_canada().strip() == expected_html.strip():
        logger.info("Functioneaza steag_canada")
        assert True
    else:
        logger.error("Nu functioneaza steag_canada")
        assert False

