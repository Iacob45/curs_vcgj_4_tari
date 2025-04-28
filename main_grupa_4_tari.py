from enum import Enum
import uvicorn
from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import HTMLResponse
from app.lib import biblioteca_header, biblioteca_romania, biblioteca_germania, biblioteca_olanda, biblioteca_franta

api = FastAPI(
    title="Api_Tari_PROIECT_VCGJ",
    version="0.1"
)


@api.get("/", response_class=HTMLResponse)
def index() -> str:
    text = biblioteca_header.header_descriere()
    text += biblioteca_romania.descriere_romania()
    text += biblioteca_germania.descriere_germania()
    text += biblioteca_olanda.descriere_olanda()
    text += biblioteca_franta.descriere_franta()
    return text

@api.get("/capitala", response_class=HTMLResponse)
def capitala() -> str:
    text = biblioteca_header.header_capitala()
    text += biblioteca_romania.capitala_romania()
    text += biblioteca_germania.capitala_germania()
    text += biblioteca_olanda.capitala_olanda()
    text += biblioteca_franta.capitala_franta()
    return text

@api.get("/steag", response_class=HTMLResponse)
def steag() -> str:
    text = biblioteca_header.header_steag()
    text += biblioteca_romania.steag_romania()
    text += biblioteca_germania.steag_germania()
    text += biblioteca_olanda.steag_olanda()
    text += biblioteca_franta.steag_franta()
    return text




if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=5050)