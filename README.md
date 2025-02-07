# Grupo 5
# Programación Orientada a Objetos - Evaluación Unidad 3
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
# Descripción 
El siguiente diagrama de clases continen los siguientes requerimientos:
- Registrar todos los insumos del restaurante, con información como nombre, cantidad, unidad de medida y nivel de reorden.
- Permitir registrar entradas al inventario (compras de insumos) y salidas del inventario (uso de insumos).
- Actualizar en tiempo real la cantidad disponible de cada insumo según el uso en los pedidos.
- Generar alertas automáticas cuando la cantidad de un insumo está por debajo del nivel de reorden.
- Generar reportes sobre el consumo de insumos en un período determinado, permitiendo identificar los más utilizados.
- Mantener un historial de las entradas y salidas para fines de auditoría y control.


# Diagrama Visual Paradimg 

![Captura de pantalla 2024-11-26 090338](https://github.com/user-attachments/assets/c7749dbe-1b60-4093-b966-77a0b0499ded)


*Link del diagrama para ver más claro*

https://drive.google.com/file/d/1WnKVkikT2FHkUT9_u0Pv7kQjc8qsrlUT/view?usp=sharing

# APIS A UTILIZAR EN EL MENUBOARD
- Api para delibery de dos funciones " PICKER "  https://www.pickerexpress.com/es/desarrollador/documentacion-api-delivery
- Api para pago con tarjetas de credito y facturación " RAMPAGO " https://rapidapi.com/RampagoHub/api/rampago-seamless-fiat-to-usdc-fiat-ramp

#  API PICKER 
La API Picker es una interfaz utilizada en aplicaciones web para permitir a los usuarios seleccionar archivos de su dispositivo o de servicios en la nube de manera eficiente.


Picker te permitirá conectar tus plataformas y/o comercios a distintos proveedores de delivery de la región en la que te encuentras. La integración con Picker a través de su API te ofrece las siguientes capacidades:

- Administración de locales.
- Automatizar la creación de pedidos desde tu plataforma.
- Realizar consultas de tarifas.
- Recibir en tiempo real las actualizaciones de tu pedido.

 Funciona en 2 partes, es decir 2 APIS en una sola, que se pueden usar y combinar a la vez:
 - Primera parte para crear un pedido
 - La segunda parte para calcuar el costo de entraga por pedido
# Crear un pedido
Para entender un poco la lógica que maneja Picker, una cuenta se la denomina Empresa. Cada empresa puede tener N locales (que pueden representar tiendas, restaurantes, puntos de despacho). Cada local obligatoriamente debe estar referenciado con una dirección y una geolocalización (se las requiere al momento de crearlas). Por ejemplo: Si tu empresa va a manejar 2 sucursales, deberás crear 2 locales, Todo pedido creado en la plataforma de Picker es determinado por un estado. El estado de un pedido es una parte importante del ciclo de vida del mismo. Estos estados pueden indicar si el pedido esta terminado, cancelado o aun en proceso. Es importante que en la integración que se vaya a desarrollar se mapeen todos los estados posibles, para que el cliente tenga muy claro lo que significa cada estado.

## Estados de Pedido

### ON_HOLD: 
Es el estado inicial del pedido si existe un tiempo de preparación. Durante este estado, el pedido aún no busca conductor. Pasa automáticamente a READY_FOR_PICKUP si:
- Se cumple el tiempo de preparación o cooktime.
- Se activa manualmente la búsqueda desde dashboard.
- Se activa mediante el endpoint de Start Search.


### READY_FOR_PICKUP

En este estado se inicia la búsqueda de motorizados en los distintos proveedores activados para el local. Este estado se puede disparar en los siguientes escenarios.

- Se termina tiempo de preparación de pedido en ON_HOLD
- Se inicia una búsqueda manualmente
- Si un pedido ya con conductor ejecuta una nueva búsqueda de conductores. (Por ejemplo: Pedido en ACCEPTED con conductor vuelve a READY_FOR_PICKUP).
- Si el pedido se crea sin tiempo de preparación, será el estado inicial del pedido.
   
### ACCEPTED
Este estado se guarda en el pedido al momento que un proveedor asigna un motorizado al pedido. Este estado únicamente llega por medio del webhook de DRIVER_ASSIGNED 

### ARRIVED_AT_PICKUP
Cuando el conductor notifica que el conductor llego al local y esta esperando que local le entregue el pedido

### WAY_TO_DELIVER
Cuando el conductor indica que abandono el local y va en dirección al punto de entrega

### ARRIVED_AT_DELIVERY
Cuando el conductor llega donde el cliente y esta por terminar el pedido

### COMPLETED
Pedido fue completado satisfactoriamente

### PROVIDER_NOT_FOUND
Cuando ningún proveedor activado para tu local no puede atender tu pedido. No se ejecuta ninguna búsqueda

### CANCELLED_BY_BUSINESS
Negocio dispara la cancelación del pedido. Esto puede suceder cuando:

- Pedido es cancelado desde dashboard
- Pedido es cancelado vía API por medio del endpoint de Cancel Booking

### CANCELLED_BY_ADMIN
Cuando la cancelación es disparada por el área de Soporte de Picker

### CANCELLED_BY_DELIVERY_PROVIDER
Cuando la cancelación es disparada por el proveedor de delivery


### NOT_DELIVERED
Cuando el pedido no pudo ser entregado al cliente; y el paquete de entrega no puede ser devuelto al negocio


### RETURNING
Cuando el pedido no pudo ser entregado al cliente y el pedido esta en camino a ser retornado al negocio

### RETURNED
Cuando el pedido fue retornado exitosamente al negocio

# Costo de Pedido
El endpoint de Pre Checkout te permitirá consultar precios y valores del pedido que necesites realizar. Además de eso, te indicará si es posible que podamos atender tu pedido (si el pedido cubre una distancia muy larga entre el local y el punto de entrega; o el punto de entrega esta fuera de cobertura, devolveremos un mensaje de error).

Para este endpoint es obligatorio la locación del punto de entrega. La ubicación del local ya la obtenemos automáticamente por el Api Key del negocio que usas en la autorización.

# Reflexión 
La elaboración de el proyecto general, fue una motivación para nosotros como grupo, por que nos ayudo a entender lo básico de una creación de página web, desde lo que es la creación del diagrama de clase, la códificación de cada clase a java, la codificación a python para la implementación de DJANGO el cual en esta ultima unidad se ha venido trabajando arduamente para crear la página principal en HTML.
Esto ayuda mucho a entender lo escencial de la programación orientada a objetos, el como se implemento la base de datos de SQLite para el almacen de datos ingresados sean usuarios, pedidos, alertas, reservaciones, etc.
También nos ayudo a poder trabajar en grupo el cuál al inicio fue complicado, pero poco a poco se logro interactuar de la mejor manera sin dejar de lado el compañerismo.
