# APIS A APLICAR 
Despues de diversos inconvenientes con las anteriores APIS a aplicar, se aplico por utilizar:
- W.App API, es una API basada en la nube lo que disminuye el tiempo de implementación y la necesidad de usar recursos de desarrollo de manera continua ( https://w.app/dashboard/)
- Api Google Maps, La API de Google Maps es una de las soluciones más completas y versátiles para integrar mapas en aplicaciones web y móviles. (https://developers.google.com/maps/documentation?hl=es-419)
- Api localStorage, En lo que respecta al almacenamiento del lado del cliente en aplicaciones web, la API localStorage se destaca como una solución simple y ampliamente compatible. Permite a los desarrolladores almacenar pares clave-valor directamente en el navegador del usuario. (https://rxdb.info/articles/localstorage.html)
# Descripcción
## W.App Api
### Funcionalidades:
- Plataforma basada en la nube que facilita la implementación rápida.
- Permite la integración con WhatsApp para automatización de mensajes.
- Proporciona herramientas para gestionar interacciones con clientes.
### Requisitos:
-Registro y configuración en el dashboard de W.App.
- Obtener una clave de API para autenticación.
- Conexión estable a internet para comunicación en la nube.
### Limitaciones:
- Dependencia total de la nube; si el servicio se cae, afecta el funcionamiento.
- Puede tener restricciones de uso y costos según el plan elegido.
## API de Google Maps
### Funcionalidades:
- Muestra mapas interactivos en aplicaciones web y móviles.
- Proporciona direcciones, cálculos de rutas y tráfico en tiempo real.
- Permite la búsqueda y autocompletado de lugares con Google Places API.
### Requisitos:
- Cuenta en Google Cloud Platform.
- Clave de API con permisos configurados.
- Configuración de facturación para acceder a niveles de uso gratuito y pagos.
### Limitaciones:
- Modelo de pago por uso: puede ser costoso en aplicaciones con alto tráfico.
- Restricciones en la cantidad de solicitudes por segundo según el plan.
- Necesidad de cumplir con los términos de uso de Google, lo que impide almacenar datos localmente sin permisos específicos.
##  API localStorage

### Funcionalidades:
- Permite almacenar datos en el navegador del usuario en pares clave-valor.
- Los datos persisten incluso después de cerrar y reabrir el navegador.
- Funciona sin necesidad de servidores ni bases de datos externas.
### Requisitos:
- Aplicación web que ejecute JavaScript.
- Acceso al objeto window.localStorage.
- No necesita conexión a internet, ya que el almacenamiento es local.
### Limitaciones:
- Capacidad de almacenamiento limitada 
# PROPUESTA 
En primer lugar, incorporaremos la API de Google Maps, lo que permitirá a los clientes localizar fácilmente el restaurante, visualizar su ubicación en un mapa interactivo y calcular la mejor ruta para llegar desde su posición actual. Además, en caso de contar con varias sucursales, se podrán mostrar todas en un solo mapa, facilitando la elección del punto más cercano. Por otro lado, para agilizar la comunicación y mejorar la atención al cliente, implementaremos la API de W.App, que permitirá a los usuarios realizar pedidos, reservas o consultas directamente a través de WhatsApp. Esta integración ofrecerá una comunicación más fluida y rápida, asegurando que los clientes puedan resolver sus dudas o gestionar sus pedidos de manera sencilla. Asimismo, se podrá automatizar la respuesta a preguntas frecuentes mediante un chatbot, optimizando la interacción sin requerir intervención humana constante y por ultimo vamos a utilizar el API de localStorage la cual implementamos con el fin de que actue como un tipo de base de datos, ya que esta utiliza algunas funcionalidades de la base de datos predeterminada de Pycharm es decir SQL Lite, esta nos sirve para la autentificación del usuario al momento de que se registre e inicie sesión 
# Implementación

## W.App Api
1.- Lo primero que realizamos en este caso es registrarnos dentro de la plataforma de la API 

![Captura de Pantalla 2025-02-07 a la(s) 01 29 16](https://github.com/user-attachments/assets/3bcb94da-e1c4-4b8f-a890-862abfe89ee9)

2.- Luego se aplica el API key y se configura 

![Captura de Pantalla 2025-02-07 a la(s) 01 34 39](https://github.com/user-attachments/assets/bf88d4b5-63bd-4bc6-81c6-dd8d2f0f1e44)

## API de Google Maps
1.- Lo primero que se realiza es el inicio de sesion y aplicar el periodo de prueba de 90 Dias 

![Captura de Pantalla 2025-02-07 a la(s) 01 37 15](https://github.com/user-attachments/assets/96edfe19-7806-441a-9d8c-95d2d2d1b7f2)

2.-  Luego creamos una App, para configurar el forms, para crear los templates donde ira la Api

![Captura de Pantalla 2025-02-07 a la(s) 01 43 31](https://github.com/user-attachments/assets/959f491a-97e8-4509-8dba-0b0ccb21271e)

3.-  Ahora hacemos los templates, para cargar el mapa y la información 
![Captura de Pantalla 2025-02-07 a la(s) 01 45 26](https://github.com/user-attachments/assets/ae28b235-e8c9-4085-bb07-08ab18c16a73)

4.- Configuramos las URLS y compilamos 

![WhatsApp Image 2025-02-06 at 09 55 20](https://github.com/user-attachments/assets/f7343935-ed7c-43ae-9bb2-2ec160fca201)



