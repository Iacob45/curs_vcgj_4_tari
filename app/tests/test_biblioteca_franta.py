import logging
from app.lib.biblioteca_franta import (
    header_descriere,
    header_capitala,
    header_steag,
    descriere_franta,
    capitala_franta,
    steag_franta,
)

logger = logging.getLogger(__name__)


def test_header_descriere():
    content = header_descriere()
    assert "/franta/capitala" in content
    assert "/franta/steag" in content
    assert "Capitala Franței" in content
    assert "Steagul Franței" in content
    assert "Aceasta este descrierea Franței" in content
    logger.info("✅ header_descriere conține elementele așteptate")


def test_header_capitala():
    content = header_capitala()
    assert "/franta" in content
    assert "/franta/steag" in content
    assert "Descrierea Franței" in content
    assert "Steagul Franței" in content
    assert "<h1" in content and "Paris" in content
    logger.info("✅ header_capitala conține elementele așteptate")


def test_header_steag():
    content = header_steag()
    assert "/franta" in content
    assert "/franta/capitala" in content
    assert "Descrierea Franței" in content
    assert "Capitala Franței" in content
    assert "Acesta este steagul Franței" in content
    logger.info("✅ header_steag conține elementele așteptate")


def test_descriere_franta():
    text = descriere_franta()
    assert "Franța este o țară" in text
    assert "Europa" in text
    assert "cultură" in text or "gastronomie" in text
    logger.info("✅ descriere_franta conține informațiile corecte")


def test_capitala_franta():
    assert capitala_franta() == "Paris"
    logger.info("✅ capitala_franta returnează 'Paris'")


def test_steag_franta():
    content = steag_franta()
    assert "Drapelul-Frantei.jpg" in content
    assert "<img" in content
    assert "alt=" in content
    logger.info("✅ steag_franta returnează imaginea corectă")


if __name__ == "__main__":
    test_header_descriere()
    test_header_capitala()
    test_header_steag()
    test_descriere_franta()
    test_capitala_franta()
    test_steag_franta()

