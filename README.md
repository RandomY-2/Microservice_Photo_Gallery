# Microservice_Photo_Gallery

A photo gallery website created with TypeScript and React for the  frontend and Python, Flask, Django, and Docker for the backend. 

The Flask server handles the main photo gallery page and the Django server handles the admin page that can create/delete/modify photos. The backend servers further communicate with each other through an event bus created using RabbitMQ.