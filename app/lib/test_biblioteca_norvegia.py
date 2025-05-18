from app.lib.biblioteca_norvegia import descriere_norvegia, capitala_norvegia, steag_norvegia

def test_descriere_norvegia():
    assert "Norvegia este o țară nordică" in descriere_norvegia()

def test_capitala_norvegia():
    assert "Oslo" in capitala_norvegia()

def test_steag_norvegia():
    assert "Flag_of_Norway.svg" in steag_norvegia()
