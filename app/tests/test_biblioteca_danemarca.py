import logging
from app.lib.biblioteca_danemarca import descriere_danemarca, capitala_danemarca, steag_danemarca

logger = logging.getLogger(__name__)

def test_descriere_danemarca():
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
            padding: 12px 24px;
            font-size: 16px;
            margin-right: 10px;
            background-color: #c62828;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s, transform 0.2s;
        }
        button:hover {
            background-color: #b71c1c;
            transform: scale(1.05);
        }
    </style>

    <div class="button-group">
        <a href="/danemarca/capitala">
            <button>Capitala</button>
        </a>
        <a href="/danemarca/steag">
            <button>Steag</button>
        </a>
    </div>

    <h1>Danemarca</h1> 
    <p> 
       Danemarca este o țară situată în nordul Europei, făcând parte din Scandinavia. Este formată din Peninsula Iutlanda și numeroase insule, cele mai mari fiind Zealand și Funen. Capitala Danemarcei este Copenhaga, un oraș modern și vibrant, situat pe insula Zealand. Danemarca are un sistem politic de tip monarhie constituțională și este cunoscută pentru democrația sa stabilă și nivelul ridicat de trai. Limba oficială este daneza, iar moneda națională este coroana daneză (DKK). Țara are o economie puternică, bazată pe servicii, industrie și agricultură. Este un lider global în energie regenerabilă, în special eoliană. Danemarca face parte din Uniunea Europeană, dar nu a adoptat euro. Cultura daneză este cunoscută pentru design-ul minimalist, literatura, și gastronomia modernă. Populația daneză este recunoscută pentru stilul de viață echilibrat și pentru conceptul de „hygge” – confort și bunăstare.
    </p>
    """
     if descriere_danemarca().strip() == expected_descriere.strip():
        logger.info("Functioneaza descriere_danemarca")
        assert True
    else:
        logger.error("Nu functioneaza descriere_danemarca")
        assert False

 

def test_capitala_danemarca():
    expected_html = """
    <style>
        h1 { color: #1a237e; margin-bottom: 10px; }
        p { font-size: 18px; line-height: 1.6; }
        .button-group { margin-bottom: 30px; }
        button {
            padding: 12px 24px;
            font-size: 16px;
            margin-right: 10px;
            background-color: #c62828;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s, transform 0.2s;
        }
        button:hover {
            background-color: #b71c1c;
            transform: scale(1.05);
        }
    </style>

    <div class="button-group">
        <a href="/danemarca">
            <button>Descriere</button> 
        </a>
        <a href="/danemarca/steag">
            <button>Steag</button> 
        </a>
    </div>

    <h1>Capitala Danemarcei: COPENHAGA</h1> 
    <p>
        Copenhaga este capitala Danemarcei și un important centru cultural, economic și politic al țării, situat pe insulele Zealand și Amager. Este cunoscută pentru calitatea vieții               
ridicată, infrastructura verde și atmosfera relaxată. Orașul atrage milioane de turiști anual datorită numeroaselor obiective turistice. Printre cele mai faimoase se numără statuia Micii Sirene, inspirată de basmul lui Hans Christian Andersen, simbol al orașului. Castelul Rosenborg, cu bijuteriile coroanei daneze, și Palatul Amalienborg, reședința familiei regale, sunt atracții istorice majore. Grădinile Tivoli, unul dintre cele mai vechi parcuri de distracții din lume, oferă distracție pentru toate vârstele. Nyhavn, cu casele sale colorate și restaurantele de pe malul canalului, este un loc ideal pentru plimbări. Alte puncte de interes includ Turnul Rotund, Muzeul Național al Danemarcei și cartierul alternativ Christiania. Copenhaga este și un paradis al bicicliștilor, cu peste 390 km de piste dedicate. Atmosfera cosmopolită, combinată cu moștenirea nordică, face din Copenhaga o destinație de neuitat.
    </p>
    """
    if capitala_danemarca().strip() == expected_html.strip():
        logger.info("Functioneaza capitala_danemarca")
        assert True
    else:
        logger.error("Nu functioneaza capitala_danemarca")
        assert False



def test_steag_danemarca():
    expected_html = """
    <style>
        h1 { color: #00695c; margin-bottom: 10px; }
        .button-group { margin-bottom: 30px; }
        button {
            padding: 12px 24px;
            font-size: 16px;
            margin-right: 10px;
            background-color: #c62828;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s, transform 0.2s;
        }
        button:hover {
            background-color: #b71c1c;
            transform: scale(1.05);
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
        <a href="/danemarca/capitala">
            <button>Capitala</button> 
        </a>
        <a href="/danemarca">
            <button>Descriere</button> 
        </a>
    </div>

    <h1>Steagul Danemarcei</h1>
    <img src="/static/Drapelul-Danemarcei.png" alt="Drapelul Danemarcei">
    """
    if steag_danemarca().strip() == expected_html.strip():
        logger.info("Functioneaza steag_danemarca")
        assert True
    else:
        logger.error("Nu functioneaza steag_danemarca")
        assert False
