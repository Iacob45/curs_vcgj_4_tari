def header_descriere() -> str:
     return """
    <div style="background: linear-gradient(to right, #0055A4 33.33%, #ffffff 33.34% 66.66%, #EF4135 66.67%); min-height: 100vh; padding: 40px 20px; font-family: 'Playfair Display', serif; color: #002654;">
        <div style="display: flex; justify-content: flex-end; margin-bottom: 20px;">
            <a href="/franta/capitala">
                <button style="padding: 12px 24px; margin-right: 10px; font-size: 17px; background-color: white; color: #0055A4; border: 2px solid #0055A4; border-radius: 8px;">
                    Capitala Franței
                </button>
            </a>
            <a href="/franta/steag">
                <button style="padding: 12px 24px; font-size: 17px; background-color: white; color: #EF4135; border: 2px solid #EF4135; border-radius: 8px;">
                    Steagul Franței
                </button>
            </a>
        </div>
        <h1 style="text-align: center; font-size: 48px; margin-bottom: 10px;">
            Aceasta este descrierea Franței
        </h1>
    """

def header_capitala() -> str:
   return """
    <div style="background-color: #f5f5f5; min-height: 100vh; padding: 40px; font-family: 'Playfair Display', serif;">
        <div style="text-align: right; margin-bottom: 20px;">
            <a href="/franta">
                <button style="padding: 14px 28px; font-size: 18px; background-color: #0055A4; color: white; border: none; border-radius: 10px; margin-right: 10px;">
                    Descrierea Franței
                </button>
            </a>
            <a href="/franta/steag">
                <button style="padding: 14px 28px; font-size: 18px; background-color: #EF4135; color: white; border: none; border-radius: 10px;">
                    Steagul Franței
                </button>
            </a>
        </div>
        <h1 style="font-size: 54px; color: #002654; text-align: center; margin-bottom: 20px; font-weight: 600;">
            Paris
        </h1>
        <p style="max-width: 800px; margin: 0 auto; font-size: 20px; color: #333; text-align: center;">
            Paris, capitala Franței, este un simbol al eleganței, artei și arhitecturii rafinate. Este cunoscut drept „Orașul Luminilor” și găzduiește obiective emblematice precum Turnul Eiffel, Luvrul și Catedrala Notre-Dame.
        </p>
    </div>
    """


def header_steag() -> str:
     return """
    <div style="background-color: #ffffff; min-height: 100vh; padding: 40px 20px; font-family: 'Playfair Display', serif;">
        <div style="display: flex; justify-content: flex-end; margin-bottom: 20px;">
            <a href="/franta">
                <button style="padding: 12px 24px; margin-right: 10px; font-size: 17px; background-color: #0055A4; color: white; border: none; border-radius: 8px;">
                    Descrierea Franței
                </button>
            </a>
            <a href="/franta/capitala">
                <button style="padding: 12px 24px; font-size: 17px; background-color: #EF4135; color: white; border: none; border-radius: 8px;">
                    Capitala Franței
                </button>
            </a>
        </div>
        <h1 style="text-align: center; font-size: 42px; color: #002654; margin-bottom: 10px;">
            Acesta este steagul Franței
        </h1>
    """
  

def descriere_franta() -> str:
      return """
        <div style="max-width: 900px; margin: 0 auto; font-size: 20px; line-height: 1.6; color: #111; font-family: 'Georgia', serif; text-align: center;">
            Franța este o țară situată în Europa de Vest, cunoscută pentru istoria, cultura și gastronomia sa. Este membră fondatoare a Uniunii Europene și are un sistem de guvernare semi-prezidențial. Franța se învecinează cu Belgia, Luxemburg, Germania, Elveția, Italia, Monaco, Spania și Andorra.
            <br><br>
            Teritoriul Franței include regiuni metropolitane și teritorii de peste mări. Are o populație de aproximativ 67 de milioane de locuitori și o economie dezvoltată. Limba oficială este franceza, iar moneda este euro. Franța este renumită pentru contribuțiile sale în artă, știință, modă și gastronomie.
        </div>
    </div> <!-- închidem DIV-ul deschis în header_descriere -->
    """
def capitala_franta() -> str:
    return "Paris"

def steag_franta() -> str:
    return """
        <div style="text-align: center; margin-top: 0;">
            <img src="/static/Drapelul-Frantei.jpg" alt="Drapelul Franței" width="600" height="360"
                 style="border: 5px solid #002654; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
        </div>
    </div> <!-- închidem DIV-ul deschis în header_steag -->
    """
