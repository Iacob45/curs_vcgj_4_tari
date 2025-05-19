
def header_descriere() -> str:
    return """
    <a href="/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitale</button>
    </a>
    <a href="/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steaguri</button>
    </a><br><br>
    <h1>Acestea sunt descrierile tarilor</h1><br><br>
    """

def header_capitala() -> str:
    return """
    <a href="/">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descrieri</button>
    </a>
    <a href="/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steaguri</button>
    </a><br><br>
    <h1>Acestea sunt capitalele tarilor</h1><br><br>
    """

def header_steag() -> str:
    return """
    <a href="/">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descrieri</button>
    </a>
    <a href="/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a><br><br>
    <h1>Acestea sunt steagurile tarilor</h1><br><br>
    """