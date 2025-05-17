def descriere_canada() -> str:
    text = """
    <style>
        body {
            background-color: #f5f7fa;
            font-family: 'Helvetica Neue', sans-serif;
            color: #333;
            margin: 0;
            padding: 2em;
        }
        .card {
            background: white;
            padding: 2em;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            max-width: 900px;
            margin: auto;
        }
        h1 {
            color: #e53935;
            margin-top: 0;
        }
        .btn-group {
            margin-top: 1em;
        }
        a button {
            background-color: #e53935;
            color: white;
            border: none;
            padding: 10px 16px;
            font-size: 15px;
            margin-right: 10px;
            border-radius: 6px;
            cursor: pointer;
        }
        a button:hover {
            background-color: #c62828;
        }
    </style>

    <div class="card">
        <h1>Canada 🇨🇦</h1>
        <p>
            Canada este a doua cea mai mare țară din lume, cunoscută pentru peisajele sale vaste, 
            natura sălbatică, multiculturalismul și nivelul ridicat de trai. Este o țară bilingvă, 
            cu engleza și franceza ca limbi oficiale.
        </p>
        <div class="btn-group">
            <a href="/canada/capitala"><button>Capitala</button></a>
            <a href="/canada/steag"><button>Steag</button></a>
        </div>
    </div>
    """
    return text

def capitala_canada() -> str:
    text = """
    <style>
        body {
            background-color: #eef2f3;
            font-family: 'Verdana', sans-serif;
            color: #2e3c4e;
            padding: 2em;
        }
        .card {
            background: #ffffff;
            border-radius: 10px;
            padding: 2em;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            max-width: 800px;
            margin: auto;
        }
        h1 {
            color: #3949ab;
            margin-bottom: 1em;
        }
        .btn-group a button {
            background-color: #3949ab;
            color: white;
            border: none;
            padding: 10px 15px;
            margin-right: 10px;
            border-radius: 5px;
            cursor: pointer;
        }
        .btn-group a button:hover {
            background-color: #283593;
        }
    </style>

    <div class="card">
        <h1>Capitala Canadei: Ottawa</h1>
        <p>
            Ottawa este capitala Canadei, situată în provincia Ontario. Este un oraș elegant, cu clădiri oficiale, muzee naționale și spații verzi extinse.
        </p>
        <div class="btn-group">
            <a href="/canada"><button>Descriere</button></a>
            <a href="/canada/steag"><button>Steag</button></a>
        </div>
    </div>
    """
    return text

def steag_canada() -> str:
    text = """
    <style>
        body {
            background-color: #fafafa;
            font-family: 'Arial', sans-serif;
            color: #1b2a3b;
            padding: 2em;
        }
        .card {
            background: white;
            padding: 2em;
            border-radius: 12px;
            box-shadow: 0 6px 14px rgba(0,0,0,0.08);
            max-width: 750px;
            margin: auto;
            text-align: center;
        }
        h1 {
            color: #00796b;
            margin-bottom: 1em;
        }
        .btn-group {
            margin-bottom: 1.5em;
        }
        a button {
            background-color: #009688;
            color: white;
            padding: 10px 16px;
            border: none;
            border-radius: 6px;
            margin-right: 10px;
            cursor: pointer;
        }
        a button:hover {
            background-color: #00695c;
        }
        img {
            margin-top: 20px;
            max-width: 100%;
            height: auto;
            border: 4px solid #ccc;
            border-radius: 10px;
        }
    </style>

    <div class="card">
        <h1>Steagul Canadei</h1>
        <div class="btn-group">
            <a href="/canada/capitala"><button>Capitala</button></a>
            <a href="/canada"><button>Descriere</button></a>
        </div>
        <img src="/static/Drapelul-Canadei.png" alt="Drapelul Canadei">
    </div>
    """
    return text

