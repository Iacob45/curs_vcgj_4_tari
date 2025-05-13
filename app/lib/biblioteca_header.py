def header_descriere() -> str:
    return """
    <a href="/olanda/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a>
    <a href="/olanda/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steagul</button>
    </a><br><br>
    <h1>Acestea sunt descrierile Olandei</h1><br><br>
    """

def header_capitala() -> str:
    return """
    <a href="/olanda">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descrierea</button>
    </a>
    <a href="/olanda/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steagul</button>
    </a><br><br>
    <h1>Acestea sunt capitalele Olandei</h1><br><br>
    """

def header_steag() -> str:
    return """
    <a href="/olanda">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descrierea</button>
    </a>
    <a href="/olanda/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a><br><br>
    <h1>Acestea sunt steagurile Olandei</h1><br><br>
    """
