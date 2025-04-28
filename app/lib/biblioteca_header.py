def header_descriere() -> str:
    return """
    <a href="/lituania/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a>
    <a href="/lituania/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
    </a><br>
    <h1>Descrierea Lituaniei</h1>
    """

def header_capitala() -> str:
    return """
    <a href="/lituania">
        <button style="padding: 10px 15px; font-size: 16px;">Vezi Descriere</button>
    </a>
    <a href="/lituania/steag">
        <button style="padding: 10px 15px; font-size: 16px;">Vezi Steag</button>
    </a><br>
    <h1>Capitala Lituaniei este :</h1>
    """

def header_steag() -> str:
    return """
    <a href="/lituania">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descriere</button>
    </a>
    <a href="/lituania/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a><br><br>
    <h1>Steagul Lituaniei</h1>
    """