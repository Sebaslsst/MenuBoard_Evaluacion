# IMPLEMENTACIÓN DE LOCALSTORAGE
Para el proyecto elaborada se ha seleccionado usar la API de LocalStorage
## ¿Qué es LocalStorage?
Es una parte de la Web Storage API, cuya función permite almacenar información dentro del navegador del usuario, los cuales se conservan incluso cuando el usuario navega a otra página o cierra el navegador. El API utiliza un sistema de pares clave-valor, donde los datos se almacenan como cadenas asociadas a una clave única, lo que facilita recuperar y manejar datos directamente en el navegador, esto garantiza un almacenamiento de datos de forma indefinida, hasta que el usuario borra los datos del navegador o borra la información de forma remota, además presentan métodos de almacenamiento simples desde y hacia un formato .json, recibiendo datos de hasta 5-10 MB, siendo accesibles desde cualquier página del mismo dominio, esta API presenta muchas funciones y utilidades en el almacenamiento de datos, asi como algunas limitaciones para su almacenamiento.
## ¿Por qué elegimos LocalStorage?
LocalStorage representa mucha facilidad para la implementación y conservación de datos(parte fundamental para cualquier programa en muchas de las funciones) gracias a su facilidad de almacenar datos simples como arreglos de datos que se pueden conservar de manera indefinida aun cuando se presentan ciertos inconvenientes que obliguen al usuario a abandonar la página, siendo su función similar a la de una base de datos, con algunas limitaciones y restricciones, pero que a conveniencia no presentan problema alguno en el almacenamiento de información para el proyecto propuesto, por si fuera poco, su implementación en Django no es muy complicada para implementarse dentro de un template de una página, para finalizar este apartado queda concluir que LocalStorage proporciona mucha facilidad de acceso para almacenar, conservar y reutilizar cualquier tipo de información simple sin mucha complicación y existe mucha información que permite darle un gran uso a esta función
## Implementación de LocalStorage en el proyecto

![image](https://github.com/user-attachments/assets/f75a41a5-3331-48d0-a46a-32034a8e4902)

Recogida de los valores del formulario: Primero, se recuperan los valores ingresados por el usuario en los campos de nombre de usuario (newUsername), contraseña (newPassword) y rol (role). Esto se hace mediante:

![image](https://github.com/user-attachments/assets/e269522e-9242-42f1-93c0-4dd540139c44)

Verificación de los campos: Luego, el código verifica si todos los campos del formulario están completos (es decir, que no estén vacíos). Si los campos están completos, se procede a almacenar la información en localStorage. Si no se han completado todos los campos, se muestra un mensaje de error.
Redirección y mensaje: Después de guardar los datos en localStorage, se muestra un mensaje de alerta indicando que el registro fue exitoso, y luego redirige al usuario a la página de inicio de sesión (/login/)
Guardado en localStorage: Si todos los campos están completos, se crea un objeto user que contiene los datos del usuario:
##Exportación de LocalStorage
Almacenar datos en localStorage: Guardar los datos en localStorage es como exportarlos de la memoria del navegador a un lugar persistente dentro del mismo navegador. Este almacenamiento permite que los datos sobrevivan incluso si el usuario cierra la página o el navegador.

Para hacer una exportación de los datos almacenados en localStorage (por ejemplo, exportarlos como un archivo descargable o enviarlos a un servidor), necesitas agregar una funcionalidad adicional.
