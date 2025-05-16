import logging
logger = logging.getLogger(__name__)
from app.lib.biblioteca_grecia import descriere_grecia, capitala_grecia, steag_grecia

def test_descriere_grecia():
    if descriere_grecia() == """
      <a href="/grecia/capitala">
        <button style="padding: 10px 20px; font-size: 16px;">Capitala</button>
    </a>
    <a href="/grecia/steag">
        <button style="padding: 10px 20px; font-size: 16px;">Steag</button>
    </a><br><br>
    <h1>Acesta este descrierea Greciei</h1><br><br>
    <p>Grecia este considerata leaganul civilizatei occidentale, o tara situata la rascrucea dintre Europa, Asia si Africa, influentele acesteia fiind vizibile asupra celor trei continente in lingvistica, arta, filosofie, muzica, literatura, politica si sport. Deoarece in acest spatiu s-a dezvoltat o civilizatie atat de bogata, siturile arheologice sunt foarte raspandite, oferind calatorii de mii de ani in istoria lumii.</p> <h3>Așezare geografică</h3><p>Fiind o tara situata in sudul Peninsulei Balcanice, litoralul grecesc se intalneste cu trei mari: in est cu Marea Egee, in vest cu Marea Ionica si cu Marea Mediterana in sud. Se invecineaza cu Bulgaria, Albania si Macedonia la nord, iar la est cu Turcia. Este formata dintr-o parte continentala Peninsula Peloponez (numele se traduce prin Insula lui Pelops, personaj mitologic ce a cucerit toata regiunea, fiul regelui Tantal, care la randul sau era fiul marelui Zeus.) si zona peninsulara (aproximativ 3 000 de insule in Marea Egee, Marea Ionica si Marea Mediterana). Insulele cele mai importante sunt Creta, Rhodos, Corfu, grupele Dodecaneze si Cicladele.</p> <h3>Istorie</h3><p>Cicladele si Insula Creta sunt unele dintre  primele regiuni care au fost populate de catre om, aici regasindu-se si cele mai importante situri arheologice; civilizatia cicladica este renumita pentru bizarii idoli cu aspect modern ce au fost gasiti in aceste insule si care au inspirat arta marelui sculptor Constantin Brancusi; in Creta a inflorit civilizatia minoica, care datorita ordinii sociale armonioase (palatele erau extrem de luxoase, nu aveau armata sau ziduri de aparare si exista egalitate intre sexe) a reprezentat baza pentru legenda celebrei insule scufundate Atlantida, descrisa de catre filosoful Platon ca fiind societatea perfecta, iar palatul din Cnossos, datorita structurii sale labirintice, a dat nastere cunoscutului mit al regelui Minos si al Minotaurului; tot in Creta s-a dezvoltat mai tarziu civilizatia miceniana, renumita pentru natura sa razboinica, micenieni fiind numiti ahei de catre poetul Homer, in celebrul sau poem epic, Iliada.</p>
    """:
        logger.info(f"Merge functia descriere_grecia")
        assert True
    else:
        logger.info(f"Nu merge functia decriere_grecia")
        assert False
def test_capitala_grecia():
    if capitala_grecia()=="Capitala Greciei este Atena":
        logger.info(f"Merge functia capitala_grecia")
        assert True
    else:
        logger.info(f"Nu merge functia capitala_grecia")
        assert False
def test_steag_grecia():
    if steag_grecia() == """<img src='/static/Steag-Grecia.png' alt='Steagul Greciei' width="1000" height="600">""":
        logger.info(f"Merge functia steag_grecia")
        assert True
    else:
        logger.info(f"Nu merge functia steag_grecia")
        assert False
if __name__ == '__main__':
    test_descriere_grecia()
    test_capitala_grecia()
    test_steag_grecia()

