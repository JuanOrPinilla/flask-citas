## Primero, crear un entorno virtual:

python3 -m virtualenv env

pip3 install virtualenv

sudo apt install python3-venv

## Activar el entorno virtual:

### Linux
 . venv/bin/activate
### Windows
 .venv\Scripts\activate

## Para instalar los paquetes necesarios:

pip install -r requirements.txt

## Configuracion para VM app.run:

app.run(host='0.0.0.0', port=8080)

## Crear un archivo .env (en la raíz del proyecto) para las variables de entorno:

SECRET_KEY=SECRET_KEY

PGSQL_HOST=10.128.0.10

PGSQL_USER=monitoring_user

PGSQL_PASSWORD=rasi

PGSQL_DATABASE=monitoring_db
