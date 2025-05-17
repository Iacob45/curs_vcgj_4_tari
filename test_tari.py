from tari import descriere, capitala, steag

def test_descriere():
    assert "Norvegia" in descriere()

def test_capitala():
    assert "Oslo" in capitala()

def test_steag():
    assert "<img" in steag()
