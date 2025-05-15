def descriere_vatican() -> str:
    text = """
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
    return text


def capitala_vatican() -> str:
    text = """
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
    return text


def steag_vatican() -> str:
    text = """
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
    return text

