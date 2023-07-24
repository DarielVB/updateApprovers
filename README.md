# updateApprovers
Scrip para actualizar aprobadores

# Como usar?

Este script se compone de tres carpetas, App, json y utils.

1. Para poder actualizar los aprobadores, primero necesitamos y archivo json con el siguiente formato:

aprobadores.json:
[
    {
        "approvers": [
            [
                "correo1@bancodebogota.com.co",  // aprobador principal
                "correo2@bancodebogota.com.co",  // aprobadores secundarios
                "correo3@bancodebogota.com.co"
            ],
            [
                "correo4@bancodebogota.com.co", // aprobador principal
                "correo5@bancodebogota.com.co"  // aprobadores secundarios del 
            ]
        ],
        "team": {
            "prefix": "dt1" // prefijo del equipo
        },
        "deploymentType": {
            "prefix": "cv" // prefijo del tipo de release
        }
    },
]

2. este archivo lo llamaremos aprobadores.json y lo pondremos en la carpeta json  "\updateApprovers\json"

3. ejecutaremos lo siguiente para iniciar un env e instalar las librerias necesarias

- pip install virtualenv

- virtualenv env (windows) - python3 -m venv env(mac o linux)

- env\Scripts\activate
// si en dado caso no llega a servir en windows, y aparece un error tipo  SecurityError: (:) [], PSSecurityException hacer en poweshell como administrador:
// - Get-ExecutionPolicy
// - Set-ExecutionPolicy RemoteSigned

- pip install -r requirements.txt

4. Ejecutar el programa

- py index.py (si no sirve, probar con otros comandos, como - python index.py, etc)