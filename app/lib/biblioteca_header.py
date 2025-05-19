def header_descriere() -> str:
    return """
    <a href="/egipt/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a>
    <a href="/egipt/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
    </a><br>
    <h1>Descrierea Egiptului</h1>
    """

def header_capitala() -> str:
    return """
    <a href="/egipt">
        <button style="padding: 10px 15px; font-size: 16px;">Vezi Descriere</button>
    </a>
    <a href="/egipt/steag">
        <button style="padding: 10px 15px; font-size: 16px;">Vezi Steag</button>
    </a><br>
    <h1>Capitala Egiptului este :</h1>
    """

def header_steag() -> str:
    return """
    <a href="/egipt">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descriere</button>
    </a>
    <a href="/egipt/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a><br><br>
    <h1>Steagul Egiptului</h1>
    """
