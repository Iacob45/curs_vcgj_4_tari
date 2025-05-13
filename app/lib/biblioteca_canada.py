def descriere_canada() -> str:
    text = """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            color: #333;
        }
        h1 {
            color: #2c3e50;
        }
        p {
            font-size: 18px;
            line-height: 1.6;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin-right: 10px;
            background-color: #d32f2f;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #b71c1c;
        }
    </style>

    <a href="/canada/capitala">
        <button>Vezi Capitala</button>
    </a>
    <a href="/canada/steag">
        <button>Vezi Steag</button>
    </a><br><br>

    <h1>Descrierea Canadei</h1>
    <p>Canada este a doua cea mai mare țară din lume ca suprafață și este cunoscută pentru peisajele sale vaste, 
    multiculturalism, sistemul educațional de calitate și un nivel ridicat de trai. Este situată în America de Nord și 
    se învecinează cu Statele Unite. Canada are zece provincii și trei teritorii, iar limba oficială este atât engleza, cât și franceza.</p>
    """
    return text


def capitala_canada() -> str:
    text = """
    <style>
        h1 { color: #2c3e50; }
        p { font-size: 18px; }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin-right: 10px;
            background-color: #1976d2;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0d47a1;
        }
    </style>

    <a href="/canada">
        <button>Vezi Descriere</button>
    </a>
    <a href="/canada/steag">
        <button>Vezi Steag</button>
    </a><br><br>

    <h1>Capitala Canadei</h1>
    <p>Ottawa este capitala Canadei și este situată în provincia Ontario. Este un important centru politic, 
    cultural și tehnologic.</p>
    """
    return text


def steag_canada() -> str:
    text = """
    <style>
        h1 { color: #2c3e50; }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin-right: 10px;
            background-color: #388e3c;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #1b5e20;
        }
    </style>

    <a href="/canada/capitala">
        <button>Vezi Capitala</button>
    </a>
    <a href="/canada">
        <button>Vezi Descriere</button>
    </a><br><br>

    <h1>Steagul Canadei</h1>
    <img src="/static/Drapelul-Canadei.png" alt="Drapelul Canadei" width="1000" height="600">
    """
    return text







































