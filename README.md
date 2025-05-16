 Proiect SCC - Luxembourg

Descriere

Proiect dedicat temei "Țări" în cadrul cursului SCC, implementând technologii precum Flask, Docker, Jenkins și Git/GitHub.

 Obiectiv

Dezvoltarea unei microaplicații web pentru Luxembourg utilizând Flask, cu 3 endpoint-uri distincte ("/luxembourg", "/luxembourg/capitala", "/luxembourg/steag") pentru afișarea informațiilor relevante. Implementarea CI/CD via Jenkins și containerizare prin Docker.

 Utilitare folosite

- **Flask**: Framework web lightweight pentru Python
- **Docker**: Platformă de containerizare pentru deployment izolat
- **Jenkins**: Server de automatizare pentru CI/CD
- **Git/GitHub**: Sistem VCS pentru managementul codului sursă

 Setup local

Configurare Git:
```bash
git config --global user.name "username"
git config --global user.email "email"
```

Clonare repository:
```bash
git clone https://github.com/<user>/curs_vcgj_4_tari.git
cd curs_vcgj_4_tari
```

Setup environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Structură proiect:
![Structura](/static/structura.png)

Instalare dependencies:
```bash
pip install -r requirements.txt
```

Lansare server:
```bash
export FLASK_APP=tari
flask run -p 5011 --reload
```

## Implementare `tari.py`

`tari.py` configurează aplicația Flask și definește rutele API pentru informațiile despre Luxembourg.

### Import dependencies
- Flask: Core framework 
- Modulele interne: `biblioteca_header` și `biblioteca_luxembourg`

### Server initialization
- Instanțiere Flask app

### Routing implementation

1. **Endpoint principal ("/luxembourg")**
   - Handler pentru requesturi HTTP GET
   - Renderizare template cu descrierea Luxembourg
   - Implementare: `header_descriere()` + `descriere_luxembourg()`

2. **Endpoint capitală ("/luxembourg/capitala")**
   - Handler GET pentru informații despre Luxembourg City
   - Implementare: `header_capitala()` + `capitala_luxembourg()`

3. **Endpoint steag ("/luxembourg/steag")**
   - Handler GET pentru drapelul național
   - Implementare: `header_steag()` + `steag_luxembourg()`

## Containerizare Docker

Build image:
```bash
docker build -t <nume> .
```

Deploy container:
```bash
docker run -dp 5011:5011 <nume>
```

Acces API:
- http://localhost:5011

## Dockerfile specs

Implementare multi-stage build pentru optimizare:

1. **Base image**: `python:3.10-alpine` (lightweight)
2. **ENV config**: Setare variabile FLASK_APP
3. **Security enhancements**: Utilizator non-privilegiat
4. **Workspace setup**: Working directory și copy application files
5. **Dependency management**: Instalare packages via pip
6. **Permission handling**: Configurare ownership și permissions
7. **Network config**: Expunere port 5011
8. **Entrypoint setup**: Script startup pentru lansare server

## Testing framework

### Unit testing via pytest
```bash
pytest app/tests/
```

### pytest.ini configuration

Setări avansate pentru test runner:

1. `pythonpath = .`: Setare import path relativă la root
2. `testpaths = app/tests`: Locație test suite
3. `log_cli = true`: Activare CLI logging
4. `log_cli_level = DEBUG`: Verbose debugging
5. `log_cli_format`: Pattern formatare logs avansate
6. `log_cli_date_format`: Format timestamp ISO 8601

### CI/CD via Jenkins
Automatizare build & deployment pipeline.

Server initialization:
```bash
jenkins
```

Pipeline configuration:
![Jenkins Config 1](/static/1.png)
![Jenkins Config 2](/static/2.png)
![Jenkins Config 3](/static/3.png)

## Jenkinsfile architecture

Pipeline declarativ pentru CI/CD:

1. **Build stage**: Compilare Docker image și tagging cu build number
2. **Code quality**: Static analysis via pylint pentru code quality metrics
3. **Unit testing**: Execuție test suite via pytest framework
4. **Deployment**: Build production-ready Docker image
5. **Runtime**: Lansare container cu port mapping și health checks
6. **Cleanup**: Teardown și resource cleanup post-execution
