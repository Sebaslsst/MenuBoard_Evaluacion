# Programación Orientada a Objetos - Evaluación Unidad 3
# Grupo 5
Este repositorio contiene la Evaluación Final de Programación Orientada a Objetos.
# Docente de la materia:
Ing. Edison Coronel.
# Los integrantes del grupo son: 
- Tayron Morales.
  tayron.morales@unl.edu.ec
- Mathias Medina. 
  mathias.medina@unl.edu.ec
- Santiago Villamagua.
  santiago.villamagua@unl.edu.ec
- Leonardo Sánchez.
  leonardo.sanchez@unl.edu.ec
- Luis Blacio.
  luis.blacio@unl.edu.ec
  
# Modulos que se emplearon dentro del proyecto

## Modulos de Mesas y Reservaciones
Este módulo gestiona la disponibilidad y uso de las mesas dentro del restaurante. Las mesas pueden estar en diferentes estados, tales como libre, ocupada o reservada. Los clientes pueden hacer reservaciones de mesas con antelación, especificando la fecha y hora de la reserva. Es necesario gestionar las características de cada mesa, como el número de asientos y su ubicación en el restaurante. Cuando un cliente llega, una mesa puede ser asignada, y al finalizar su uso, la mesa debe ser liberada para otros clientes. Las reservaciones pueden ser modificadas o canceladas por el cliente o el personal del restaurante.

![Captura de Pantalla 2025-02-06 a la(s) 22 18 35](https://github.com/user-attachments/assets/5836db12-3c08-4a56-b57f-2fd0efaeca21)



## Modulo de Reporte y Estadistica 
Este módulo proporciona información sobre el desempeño del restaurante a través de reportes y estadísticas. Los reportes incluyen datos sobre las ventas diarias, productos más vendidos, mesas más utilizadas, ingresos generados, y el desempeño de los empleados. El sistema debe permitir generar reportes personalizados por rango de fechas y categorías específicas, como ventas por categoría de producto o por empleado. Además, se deben generar gráficos y tablas que faciliten la interpretación de los datos.

![Captura de Pantalla 2025-02-06 a la(s) 22 13 28](https://github.com/user-attachments/assets/0310ed90-8fc9-4ef1-a60e-cde8e357f347)


## Modulo de Menus y productos
Este módulo permite gestionar los productos y platos que se ofrecen en el restaurante. Cada producto tiene atributos como nombre, descripción, categoría, precio y disponibilidad. El menú puede estar organizado en categorías, como entradas, platos principales, postres y bebidas. El sistema debe permitir agregar nuevos productos al menú, modificarlos o eliminarlos cuando sea necesario. Además, se requiere que los productos puedan estar temporalmente fuera de stock o deshabilitados para su venta si los ingredientes no están disponibles. También se debe mantener un control de precios, permitiendo actualizarlos según sea necesario.

![Captura de Pantalla 2025-02-06 a la(s) 22 24 30](https://github.com/user-attachments/assets/503fcb3a-dfdb-4b9d-bc5e-784a0ccdadfe)


## Modulo de inventario
El módulo de inventario permite gestionar los insumos y productos necesarios para la preparación de los platos del restaurante. Cada insumo debe ser registrado con información como nombre, cantidad disponible y unidad de medida. El sistema debe permitir registrar entradas de nuevos insumos y salidas de los mismos cuando se utilizan en la preparación de los productos del menú. Además, es necesario generar alertas cuando el inventario de un insumo esté bajo o agotado. También debe permitir generar reportes de consumo de insumos y de stock disponible para facilitar la reposición.

![Captura de Pantalla 2025-02-06 a la(s) 22 21 39](https://github.com/user-attachments/assets/a6fec96f-4beb-4f6a-a11c-a7668357c73a)


## Modulo de Facturación y Pagos 
Este módulo es responsable de generar la factura para los clientes al finalizar su pedido. La factura debe calcular automáticamente el total del pedido, incluyendo impuestos y descuentos aplicables. Además, debe permitir seleccionar el método de pago, ya sea en efectivo, tarjeta de crédito o débito, entre otros. El sistema debe generar un comprobante de pago que puede ser impreso o enviado al correo del cliente. También es necesario mantener un registro de todas las facturas emitidas para efectos contables y de auditoría.

![Captura de Pantalla 2025-02-06 a la(s) 22 16 06](https://github.com/user-attachments/assets/a1f98f40-3366-4c20-a341-90bd463b8117)


## Modulo de pedidos 
El módulo de pedidos permite gestionar los pedidos de los clientes, desde que se realiza el pedido hasta que es servido y pagado. Cada pedido puede contener uno o más productos del menú, y es posible agregar o eliminar productos mientras el pedido no haya sido servido. El sistema debe permitir modificar cantidades de productos en los pedidos, así como su estado (pendiente, en preparación, servido, pagado). El personal del restaurante puede visualizar y actualizar el estado de cada pedido. Además, se requiere tener un registro histórico de todos los pedidos realizados en el restaurante para futuras consultas.

![Captura de Pantalla 2025-02-06 a la(s) 22 25 20](https://github.com/user-attachments/assets/4581139f-9722-4c04-852b-a90172ae2428)

# Interfaz Grafica del Usuario
En esta parte nosotros implementamos esta interfaz grafica del usuario, mediante templates, donde previamente en la Unidad 1 y 2 planificamos lo que es el diagrama UML, despues de su revisión, se comenzo a codificar las clases para que se implemente la logica del diagrma de clases tipo UML, y por ultimo se añadieron los templates donde hacemos funcionar los diferentes atributos aplicados a una pagina Web

### Utilizamos colores llamativos, aparte de que nuestro proyecto de restaurante tiene diferentes cuestiones, ya que aplica: 
- Formularios (Para registro y inicio de sesion)

  ![Captura de Pantalla 2025-02-06 a la(s) 23 34 07](https://github.com/user-attachments/assets/354dc56b-1e03-4e24-85fa-ecc99643c5f7)

- Botones (Revisar Menu, Reservar mesas, Pedidos)

![Captura de Pantalla 2025-02-06 a la(s) 23 34 51](https://github.com/user-attachments/assets/64ddeaa8-8d2e-4535-bb11-0a2d73c56272)


- Menu (Para inventario, para añadir un insumo )
![WhatsApp Image 2025-02-07 at 00 03 37](https://github.com/user-attachments/assets/3bbef64b-c0c4-4ff0-ae20-c4c1ac97b185)

# Reflexión 

Lo primero que se realizo en este caso fue configurar en parte las bases de la interfaz grafica, como definir los colores base y escoger detalladamente que templates vamos a utilizar para llevar a cabo nuestro proyecto, luego fue implementar la logica de las clases de la segunda unidad a los templates HTML, y la configuración basica de la interfaz de usuario, se opto por mejorar los templates, generando formularios como para el inicio de sesion o registro, luego se opto por tambien implementar botones que rediriguen las Urls, y por ultimo tambien se implemento menus, sobre todo para la parte de insumos del inventario , aparte de diferentes funcionalidades en si, puesto que la aplicación que queremos entregar o presentar sea muy completa, despues de todo ese proceso llegamos a la parte de las APIS, donde primero se penso en implementar la API de picker que era una APi para servicio de Delibery, pero por temas de autentificación no se pudo lograr, luego se optmo por un sistema de facturación llamado Stripe, que tampoco se implemento dedibo a un problema con la autentificación tambien, por ultimo se optmo por utilizar la Api de google maps, donde se pudo implementar como un medio para que el cliente sepa la posicicón o ubicación del restaurante, y calcula la manera mas rapida de llegar, tambien se implemento una API de contacto, puesto que se pudo añadir un boton que atraves de un API que funciona con datos en la Nube, se implemento el numero de WhatsApp de los administradores del restaurante, asi el usuario tendria mas formas de interacción dentro de la pagina, luego tuvimos problemas con la base de datos y como solución mediante la investigación fue aplicar un API que tome en cuenta las funciones de la base de datos MSQL Lite, se pudo crear una simultanea base de datos donde se guardan en el mismo archivo del proyecto los datos de los usuarios, al final se volvio a configurar los templates dandoles otra forma mas sofisticada y mas formal.

