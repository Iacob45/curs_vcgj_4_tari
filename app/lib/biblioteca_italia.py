def descriere_italia() -> str:
    text = """
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
        <h1>Italia 🇮🇹</h1>
        <p>
            Italia este o țară situată în sudul Europei, cunoscută pentru forma sa de cizmă și pentru bogata sa moștenire culturală, istorică și artistică.
             Italia a fost leagănul Imperiului Roman și al Renașterii, influențând profund arta, arhitectura, literatura și știința europeană.
        </p>
        <div class="btn-group">
            <a href="/italia/capitala"><button>Capitala</button></a>
            <a href="/italia/steag"><button>Steag</button></a>
        </div>
    </div>
    """
    return text
def capitala_italia() -> str:
    text = """
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
        <h1>Capitala Italiei: Roma</h1>
        <p>
            Roma este capitala Italiei și unul dintre cele mai vechi și mai importante orașe din lume. Supranumită "Orașul Etern", Roma are o istorie de peste 2.700 de ani și a fost centrul Imperiului Roman, care a influențat decisiv civilizația occidentală.
        </p>
        <div class="btn-group">
            <a href="/italia"><button>Descriere</button></a>
            <a href="/italia/steag"><button>Steag</button></a>
        </div>
    </div>
    """
    return text

def steag_italia() -> str:
    text = """
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
        <h1>Steagul Italiei</h1>
        <div class="btn-group">
            <a href="/italia/capitala"><button>Capitala</button></a>
            <a href="/italia"><button>Descriere</button></a>
        </div>
        <img src="/static/Drapelul-Italiei.png" alt="Drapelul Italiei">
    </div>
    """
    return text

