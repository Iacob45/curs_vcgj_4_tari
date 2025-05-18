def descriere_brazilia() -> str:
    text="""
    <a href="/brazilia/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a>
    <a href="/brazilia/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
    </a><br><br>
    <h1>Aceasta este descrierea Braziliei</h1><br><br>
    """
    text+= "Brazilia este cea mai mare țară din America de Sud și una dintre cele mai populate din lume. Este renumită pentru diversitatea sa naturală, inclusiv pădurea Amazoniană, și pentru cultura bogată, influențată de tradiții africane, europene și indigene. Este recunoscută internațional pentru fotbal, dansul samba, carnavalurile spectaculoase și peisajele sale exotice."
    return text

def capitala_brazilia() -> str:
    text= """
    <a href="/brazilia">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descriere</button>
    </a>
    <a href="/brazilia/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Steag</button>
    </a><br><br>
    <h1>Aceasta este capitala Braziliei</h1><br><br>
    """
    text+="Brasília"
    return text

def steag_brazilia() -> str:
    text ="""
    <a href="/brazilia">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Descriere</button>
    </a>
    <a href="/brazilia/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Vezi Capitala</button>
    </a><br><br>
    <h1>Acesta este steagul Braziliei</h1><br><br>
    """
    text += """<img src="/static/Steagul-Braziliei.png" alt="Steagul Braziliei" width="1000" height="600">"""
    return text
