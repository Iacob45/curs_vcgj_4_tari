def header_descriere() -> str:
    return """
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Luxembourg - Descriere</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="container">
            <header>
                <div class="flag-colors">
                    <div class="color-bar color-red"></div>
                    <div class="color-bar color-white"></div>
                    <div class="color-bar color-blue"></div>
                </div>
                <h1>Luxembourg - Marele Ducat</h1>
                <nav>
                    <a href="/luxembourg/capitala">
                        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
                    </a>
                    <a href="/luxembourg/steag">
                        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
                    </a>
                </nav>
            </header>
            <div class="country-info">
                <h1>Aceasta este descrierea Luxembourg</h1>
                <div class="info-box">
                    <p><strong>Nume oficial:</strong> Marele Ducat de Luxembourg</p>
                    <p><strong>Continent:</strong> Europa</p>
                    <p><strong>Membru UE:</strong> Da (membru fondator)</p>
                </div>
    """

def header_capitala() -> str:
    return """
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Luxembourg - Capitală</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="container">
            <header>
                <div class="flag-colors">
                    <div class="color-bar color-red"></div>
                    <div class="color-bar color-white"></div>
                    <div class="color-bar color-blue"></div>
                </div>
                <h1>Luxembourg City</h1>
                <nav>
                    <a href="/luxembourg">
                        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descriere</button>
                    </a>
                    <a href="/luxembourg/steag">
                        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
                    </a>
                </nav>
            </header>
            <div class="capital-info">
                <h1>Aceasta este capitala Luxembourg</h1>
    """

def header_steag() -> str:
    return """
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Luxembourg - Steag</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="container">
            <header>
                <div class="flag-colors">
                    <div class="color-bar color-red"></div>
                    <div class="color-bar color-white"></div>
                    <div class="color-bar color-blue"></div>
                </div>
                <h1>Steagul Național</h1>
                <nav>
                    <a href="/luxembourg">
                        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descriere</button>
                    </a>
                    <a href="/luxembourg/capitala">
                        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
                    </a>
                </nav>
            </header>
            <div class="flag-info">
                <h1>Acesta este steagul Luxembourg</h1>
    """