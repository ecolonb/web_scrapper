# Web scraepper - python3

### Clonar el repositorio:

        git clone https://github.com/ecolonb/web_scrapper.git

### Instalar ambiente virtual

    python3 -m venv .env

### Activar ambiente virtual:

    source .env/bin/activate

### instalar YAML

    pip install pyyaml

### ejecutar el main

    python3 main.py eluniversal

#### notes

    Para evitar warnings deprecate, utilizar el load de esta manera:
    -->> yaml.load(f, Loader=yaml.FullLoader)
