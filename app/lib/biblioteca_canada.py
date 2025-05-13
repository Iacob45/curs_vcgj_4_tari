
def descriere_canada() -> str:
    text = """
    <a href="/canada/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a>
    <a href="/canada/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
    </a><br><br>
    <h1>Aceasta este descrierea Canadei</h1><br><br>
    """
    text += "<p>Canada este cea mai misto tara</p>"
    return text

def capitala_canada() -> str:
    text = """
        <a href="/canada">
            <button style="padding: 10px 20px; font-size: 16px;">Vezi Dexcriere</button>
        </a>
        <a href="/canada/steag">
            <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
        </a><br><br>
        <h1>Aceasta este capitala Canadei</h1><br><br>
        """
    text += "<p>Ottawa</p>"
    return text

def steag_canada() -> str:
    text = """
        <a href="/canada/capitala">
            <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
        </a>
        <a href="/canada">
            <button style="padding: 10px 20px; font-size: 16px;">Vezi Descriere</button>
        </a><br><br>
        <h1>Aceasta este steagul Canadei</h1><br><br>
        """
    text += """<img src="/static/Drapelul-Canadei.png" alt="Drapelul Canadei" width="1000" height="600">"""
    return text