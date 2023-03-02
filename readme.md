LOCUST
---

HERRAMIENTA PARA LOAD TESTING

EJECUCION:

    virtualenv venv && venv\Scripts\activate && pip install -r requirements.txt
    cd locust_file  && locust --headless --users 20000 --spawn-rate 99 -H http://localhost:5000

--- 
Test the locust app 
---

SERVER UP :
    
    python flask_app_sample\flask_server.py
    cd locust_file && locust --headless --users 20000 --spawn-rate 99 -H http://localhost:5000


*ACOTACIONES SOBRE LA FORMA COMO TOMA LOS DATOS, SE ESTARIA EMULANDO LA TOMA DE INFORMACION DE LA CANTIDAD DE REGISTROS DESDE UNA BASE DE DATOS, SE PUEDE REALIZAR EL USO CON UNA DB EN SQLITE*