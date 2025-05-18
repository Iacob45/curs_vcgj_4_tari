def base_css() -> str:
    return """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;500;700&display=swap');
      :root {
        --primary: #d62828;           /* roșu principal */
        --background-start: rgba(214, 40, 40, 0.85);  /* roșu intens */
        --background-end: rgba(255, 255, 255, 0.4);    /* alb semi-transparent */
        --card-bg: rgba(255, 255, 255, 0.6);           /* alb semi-transparent pentru card */
        --dark: #1d3557;
        --accent: #e63946;
      }
      * { box-sizing: border-box; margin: 0; padding: 0; }
      body {
        font-family: 'Montserrat', sans-serif;
        color: var(--dark);
        /* gradient din roșu în alb transparent */
        background: linear-gradient(
          135deg,
          var(--background-start) 0%,
          var(--background-end) 100%
        );
        min-height: 100vh;
        line-height: 1.6;
      }
      .container {
        max-width: 960px;
        margin: 2em auto;
        padding: 0 1em;
      }
      .card {
        background: var(--card-bg);
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        margin-bottom: 2em;
        transition: transform .2s;
      }
      .card:hover { transform: translateY(-5px); }
      .hero {
        position: relative;
        height: 300px;
        background-size: cover;
        background-position: center;
      }
      .hero::after {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(0,0,0,0.3), rgba(0,0,0,0.6));
      }
      .hero h1 {
        position: absolute;
        bottom: 1em;
        left: 1em;
        color: white;
        font-size: 2.5rem;
        z-index: 1;
      }
      .content {
        padding: 1.5em;
      }
      .content p {
        margin-bottom: 1.5em;
      }
      .buttons {
        display: flex;
        gap: 1em;
        flex-wrap: wrap;
        margin-top: 1.5em;
      }
      .buttons a { text-decoration: none; }
      .buttons button {
        background: var(--primary);
        border: none;
        padding: .8em 1.2em;
        border-radius: 6px;
        color: white;
        font-weight: 500;
        cursor: pointer;
        transition: background .2s;
      }
      .buttons button:hover {
        background: var(--accent);
      }
      img.inline {
        max-width: 100%;
        border-radius: 8px;
        margin-top: 1em;
      }
    </style>
    """

def descriere_malta() -> str:
    return f"""
    {base_css()}
    <div class="container">
      <div class="card">
        <div class="hero" style="background-image:url('/static/malta_bg.jpg')">
          <h1>Malta 🇲🇹</h1>
        </div>
        <div class="content">
          <p>
            Republica Malta este un stat insular independent, situat în inima Mării Mediterane,
            la sud de Sicilia. Arhipelagul cu o suprafață de doar 316 km² are o importanță
            strategică recunoscută de-a lungul mileniilor, fiind stăpânit succesiv de fenicieni,
            romani, arabi, normanzi și Cavalerii Ioaniți, care au lăsat în urmă o moștenire
            culturală și arhitecturală unică.
          </p>
          <p>
            Clima mediteraneană, cu veri calde și uscate și ierni blânde, face din Malta o
            destinație turistică de prim rang. Capitala, Valletta, inclusă în patrimoniul
            UNESCO, impresionează prin fortificații baroce, palate impunătoare și biserici
            decorate cu fresce elaborate. Insulele Gozo și Comino completează peisajul,
            oferind situri megalitice antice, precum Ġgantija, plaje izolate și rezervații naturale.
          </p>
          <p>
            Economia Maltei este diversificată, bazându-se atât pe turism și servicii financiare,
            cât și pe industrii de valoare adăugată, precum tehnologia informației și producția
            farmaceutică. Politica lingvistică reflectă bogăția culturală: malteza și engleza
            sunt limbi oficiale, iar comunitățile locale mențin vii tradiții precum festivalurile
            religioase și concertele de fanfară.
          </p>
          <div class="buttons">
            <a href="/malta/capitala"><button>Vezi Capitala</button></a>
            <a href="/malta/steag"><button>Vezi Steagul</button></a>
          </div>
        </div>
      </div>
    </div>
    """

def capitala_malta() -> str:
    return f"""
    {base_css()}
    <div class="container">
      <div class="card">
        <div class="hero" style="background-image:url('/static/valletta.jpg')">
          <h1>Valletta</h1>
        </div>
        <div class="content">
          <p>
            Valletta, capitala Republicii Malta, a fost fondată în 1566 de către Cavalerii 
            Ordinului Sfântului Ioan, după planurile inginerului militar Pietro Paolo Floriani.
            Orașul-fortăreață este înscris în patrimoniul UNESCO și se distinge printr-o arhitectură 
            barocă excepțională, cu palate impunătoare, biserici somptuoase și bastioane de piatră.
          </p>
          <p>
            Centrul istoric, cu străzi pietruite dispuse pe un sistem de grid, găzduiește repere 
            culturale de excepție: Co-Catedrala Sfântului Ioan, cu interioare decorate de Caravaggio, 
            și Grădinile Upper Barrakka, care oferă panorame impresionante asupra Marelui Port.
          </p>
          <p>
            În prezent, Valletta este și inima administrativă și economică a insulei: aici 
            funcționează Parlamentul Maltei, ministerele și numeroase instituții culturale, 
            festivaluri de teatru și concerte clasice animând viața urbană pe tot parcursul anului.
          </p>
          <img class="inline" src="/static/valletta_strazi.jpg" alt="Străzi în Valletta">
          <div class="buttons">
            <a href="/malta"><button>Înapoi la Descriere</button></a>
            <a href="/malta/steag"><button>Vezi Steagul</button></a>
          </div>
        </div>
      </div>
    </div>
    """

def steag_malta() -> str:
    return f"""
    {base_css()}
    <div class="container">
      <div class="card">
        <div class="hero" style="background-image:url('/static/steag_malta_banner.jpg')">
          <h1>Steagul Maltei</h1>
        </div>
        <div class="content">
          <p>
            Steagul Republicii Malta este compus din două benzi verticale de culoare albă și roșie, 
            plasate în proporție de 1:1. În colțul superior al benzii albe apare Crucea Sfântului Gheorghe, 
            conferită insulei de Regele George al VI-lea în 1942, pentru vitejia locuitorilor în timpul celui 
            de-al Doilea Război Mondial.
          </p>
          <p>
            Banda albă semnifică pacea și puritatea, iar cea roșie reprezentă curajul și sacrificiul. Crucea, 
            cu contur argintiu, evocă tradiția cavalerilor ioaniți și rolul lor central în apărarea creștinătății 
            în bazinul mediteranean.
          </p>
          <img class="inline" src="/static/steag_malta.png" alt="Steagul Maltei">
          <div class="buttons">
            <a href="/malta"><button>Descriere</button></a>
            <a href="/malta/capitala"><button>Vezi Capitala</button></a>
          </div>
        </div>
      </div>
    </div>
    """

