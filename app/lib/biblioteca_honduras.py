def descriere_honduras():
    "Descriere honduras"
    text = """
            <a href="/honduras/capitala">
                <button style="font-size: 20px;">Capitala</button>
            </a>
            <a href="/honduras/steag">
                <button style="font-size: 20px;">Steag</button>
            </a><br>
            <h1>Honduras</h1><br>
            """
    text += "Honduras este o țară situată în America Centrală, având graniță cu Guatemala, El Salvador și Nicaragua,"
    text += "precum și deschidere la Marea Caraibilor și Oceanul Pacific. Capitala sa este Tegucigalpa."
    text += "Țara are un relief variat, format din munți, câmpii fertile și zone de coastă,"
    text += "iar clima este în general tropicală."
    return text

def capitala_honduras():
    "Capitala honduras"
    text = """
            <a href="/honduras">
                <button style="font-size: 20px;">Descriere</button>
            </a>
            <a href="/honduras/steag">
                <button style="font-size: 20px;">Steag</button>
            </a><br>
            <h1>Honduras</h1><br>
            """
    text += "Tegucigalpa"
    return text

def steag_honduras():
    "Steag honduras"
    text = """
            <a href="/honduras/capitala">
                <button style="font-size: 20px;">Capitala</button>
            </a>
            <a href="/honduras">
                <button style="font-size: 20px;">Descriere</button>
            </a><br>
            <h1>Honduras</h1><br>
            """
    text += """<img src="/static/honduras__42861.jpg" alt="Steagul Hondurasului">"""
    return text
