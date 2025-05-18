import logging
from app.lib.biblioteca_malta import descriere_malta, capitala_malta, steag_malta

logger = logging.getLogger(__name__)


def test_descriere_malta():
    html = descriere_malta()
    # Verifică titlul și elementele principale
    assert '<h1>Malta 🇲🇹</h1>' in html
    assert '<p>' in html
    assert 'Republica Malta' in html
    assert 'background: linear-gradient' in html
    assert '<a href="/malta/capitala"' in html
    assert '<a href="/malta/steag"' in html
    logger.info("descriere_malta conține elementele de bază")


def test_capitala_malta():
    html = capitala_malta()
    # Verifică titlul și elementele principale
    assert '<h1>Valletta</h1>' in html
    assert 'Valletta, capitala Republicii Malta' in html
    assert "background-image:url('/static/valletta.jpg')" in html
    assert '<a href="/malta"' in html
    assert '<a href="/malta/steag"' in html
    logger.info("capitala_malta conține elementele de bază")


def test_steag_malta():
    html = steag_malta()
    # Verifică titlul și elementele principale
    assert '<h1>Steagul Maltei</h1>' in html
    assert 'Steagul Republicii Malta' in html
    assert "background-image:url('/static/steag_malta_banner.jpg')" in html
    assert '<img class="inline" src="/static/steag_malta.png"' in html
    assert '<a href="/malta"' in html
    assert '<a href="/malta/capitala"' in html
    logger.info("steag_malta conține elementele de bază")

