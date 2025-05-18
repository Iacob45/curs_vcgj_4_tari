import logging
from app.lib.biblioteca_egipt import descriere_egipt, capitala_egipt, steag_egipt

logger = logging.getLogger(__name__)


def test_descriere_egipt():
    expected_descriere = """
    <style>
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #ffffff, #e53935);
            font-family: 'Segoe UI', sans-serif;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .card {
            background: rgba(255, 255, 255, 0.5);
            border-radius: 16px;
            padding: 2em;
            backdrop-filter: blur(12px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            max-width: 850px;
        }
        h1 {
            color: #b71c1c;
        }
        p {
            font-size: 18px;
            color: #4e0000;
            line-height: 1.7;
        }
        .btn-group {
            margin-top: 1.5em;
        }
        a button {
            padding: 10px 18px;
            font-size: 15px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            margin-right: 10px;
            background-color: #c62828;
            color: white;
        }
        a button:hover {
            background-color: #8e0000;
        }
    </style>

    <div class="card">
        <h1>Egipt</h1>
        <p>
            Egiptul are o populație de circa 114,5 milioane de locuitori, iar capitala și cel mai mare oraș este Cairo.
            
            Egiptul este o țară arabă din nordul Africii și din Orientul Mijlociu, limitată la nord de Marea Mediterană, la est de Fâșia Gaza, de Israel, de Golful Aqaba (prin intermediul căruia are contact cu Iordania și cu Arabia Saudită) și de Marea Roșie, la sud de Sudan iar la vest de Libia.
        </p>
        <div class="btn-group">
            <a href="/egipt/capitala"><button>Capitala</button></a>
            <a href="/egipt/steag"><button>Steag</button></a>
        </div>
    </div>
    """

    if descriere_egipt().strip() == expected_descriere.strip():
        logger.info("Functioneaza descriere_egipt")
        assert True
    else:
        logger.error("Nu functioneaza descriere_egipt")
        assert False


def test_capitala_egipt():
    expected_html = """
    <style>
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #ffffff, #e53935);
            font-family: 'Segoe UI', sans-serif;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .card {
            background: rgba(255, 255, 255, 0.5);
            border-radius: 16px;
            padding: 2em;
            backdrop-filter: blur(12px);
            box-shadow: 0 8px 18px rgba(0,0,0,0.1);
            max-width: 800px;
        }
        h1 {
            color: #c62828;
        }
        p {
            font-size: 18px;
            color: #6d0000;
            line-height: 1.6;
        }
        .btn-group {
            margin-top: 1.5em;
        }
        a button {
            padding: 10px 18px;
            font-size: 15px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            margin-right: 10px;
            background-color: #e53935;
            color: white;
        }
        a button:hover {
            background-color: #b71c1c;
        }
    </style>

    <div class="card">
        <h1>Capitala Egiptului: Cairo</h1>
        <p>
            Cairo este capitala Egiptului cu o populație estimată între 16 și 20 de milioane de locuitori și este al doilea cel mai mare oraș din Africa.
        </p>
        <div class="btn-group">
            <a href="/egipt"><button>Descriere</button></a>
            <a href="/egipt/steag"><button>Steag</button></a>
        </div>
    </div>
    """

    if capitala_egipt().strip() == expected_html.strip():
        logger.info("Functioneaza capitala_egipt")
        assert True
    else:
        logger.error("Nu functioneaza capitala_egipt")
        assert False


def test_steag_egipt():
    expected_html = """
    <style>
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #ffffff, #e53935);
            font-family: 'Segoe UI', sans-serif;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .card {
            background: rgba(255, 255, 255, 0.5);
            border-radius: 16px;
            padding: 2em;
            backdrop-filter: blur(12px);
            box-shadow: 0 8px 18px rgba(0,0,0,0.1);
            max-width: 700px;
            text-align: center;
        }
        h1 {
            color: #b71c1c;
        }
        .btn-group {
            margin-bottom: 1.5em;
        }
        a button {
            padding: 10px 18px;
            font-size: 15px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            margin: 0 10px;
            background-color: #ef5350;
            color: white;
        }
        a button:hover {
            background-color: #d32f2f;
        }
        img {
            margin-top: 20px;
            max-width: 100%;
            height: auto;
            border: 4px solid #ccc;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
    </style>

    <div class="card">
        <h1>Steagul Egiptului</h1>
        <div class="btn-group">
            <a href="/egipt/capitala"><button>Capitala</button></a>
            <a href="/egipt"><button>Descriere</button></a>
        </div>
        <img src="/static/Drapelul-Egiptului.png" alt="Drapelul Egiptului">
    </div>
    """

    if steag_egipt().strip() == expected_html.strip():
        logger.info("Functioneaza steag_egipt")
        assert True
    else:
        logger.error("Nu functioneaza steag_egipt")
        assert False

