--Actúa como desarrollador front-end senior, experto en Django (Django Template Language) y Bootstrap 5.Crea el archivo templates/base.html, la plantilla base de mi proyecto, para que el resto de las plantillas hereden de ella con {% extends %}.- Proyecto Django llamado "Huella Austral", un sistema de un centro de rescate de fauna silvestre del sur de Chile (pudú, zorro chilla, chucao, monito del monte).
- App: rescate. Namespace de URLs: 'rescate' (nombres: lista, crear, detalle, editar, eliminar).
- Es un trabajo académico, así que el código debe ser limpio y estar bien comentado.
- Requisitos que debe cumplir:
  1. Bootstrap 5.3 por CDN (CSS y JS bundle).
  2. {% load static %} y enlace a static/css/custom.css (diseño propio, verdes bosque y tonos tierra).
  3. Espacio para un logo en la navbar con {% static 'img/logo.png' %}, junto al nombre "Huella Austral".
  4. Navbar responsive con enlace al catálogo. Visibilidad condicional con {% if user.is_authenticated %}: si hay sesión, mostrar "+ Nuevo ejemplar", el nombre del usuario y un botón "Cerrar sesión" (formulario POST con {% csrf_token %}, porque en Django 5 el logout por GET no funciona). Si no hay sesión, mostrar "Iniciar sesión".
  5. Bloques DTL: {% block title %}, {% block content %} y {% block extra_css %}.
  6. Footer simple con el año y el nombre del proyecto.
Entrégame solo el código completo de base.html en un único bloque de código, con comentarios breves en español. Después, en máximo 5 líneas, indica qué debo agregar en settings.py (MESSAGE_TAGS para que error se convierta en danger, STATICFILES_DIRS, LOGIN_URL, etc.) para que funcione todo.

-templates/rescate/ejemplar_list.html
--Actúa como desarrollador front-end senior, experto en Django (Django Template Language) y Bootstrap 5.
Crea la plantilla templates/rescate/ejemplar_list.html, el catálogo de ejemplares de mi proyecto, que hereda de base.html.
- Proyecto Django "Huella Austral", un centro de rescate de fauna silvestre del sur de Chile.
- La ListView (EjemplarListView) entrega al template la variable "ejemplares", obtenida con select_related('especie').
- Cada ejemplar tiene: especie (ForeignKey a Especie, que tiene el campo nombre), nombre (texto), peso_kg (decimal), fecha_ingreso (fecha) y liberado (booleano).
- Namespace de URLs: 'rescate'. Nombres: detalle, editar y eliminar (los tres reciben pk) y crear.
- Requisitos:
  1. Empezar con {% extends 'base.html' %} y usar {% block title %} y {% block content %}.
  2. Título principal "Ejemplares en el centro de rescate".
  3. Grilla responsive de Bootstrap 5 (row con col-12 col-md-6 col-lg-4) con una card por ejemplar.
  4. Cada card muestra: nombre, nombre de la especie, peso en kg, fecha de ingreso con el formato d/m/Y y un badge verde "Liberado" o amarillo "En recuperación" según el booleano.
  5. Botón "Ver" visible para todos. Los botones "Editar" y "Eliminar" solo deben verse con {% if user.is_authenticated %}.
  6. Usar {% empty %} para mostrar un mensaje cuando no haya ejemplares.
  7. Usar {% url %} con el namespace, sin rutas escritas a mano.
Entrégame solo el código completo del template en un único bloque de código, con comentarios breves en español. No uses CSS inline, solo clases de Bootstrap.

-templates/rescate/ejemplar_detail.html
Actúa como desarrollador front-end senior, experto en Django (Django Template Language) y Bootstrap 5.
Crea la plantilla templates/rescate/ejemplar_detail.html, la ficha de detalle de un ejemplar, que hereda de base.html.
- Proyecto Django "Huella Austral", un centro de rescate de fauna silvestre del sur de Chile.
- La DetailView (EjemplarDetailView) entrega al template la variable "ejemplar" y captura <int:pk> desde la URL (si el registro no existe, Django devuelve 404 automáticamente).
- Campos del ejemplar: especie (ForeignKey a Especie, que tiene el campo nombre), nombre (texto), peso_kg (decimal), fecha_ingreso (fecha) y liberado (booleano).
- Namespace de URLs: 'rescate'. Nombres: lista, editar y eliminar (los dos últimos reciben pk).
- Requisitos:
  1. Empezar con {% extends 'base.html' %} y usar {% block title %} (con el nombre del ejemplar) y {% block content %}.
  2. Mostrar los datos dentro de una card de Bootstrap 5, con el nombre como título (h1) y una lista de descripción (dl con row, dt y dd) para: especie, peso en kg, fecha de ingreso con formato d/m/Y y estado.
  3. El estado debe mostrarse como un badge verde "Liberado" o amarillo "En recuperación" según el booleano.
  4. Botón "Volver" al catálogo visible para todos.
  5. Botones "Editar" y "Eliminar" solo visibles con {% if user.is_authenticated %}.
  6. Usar {% url %} con el namespace, sin rutas escritas a mano.
Entrégame solo el código completo del template en un único bloque de código, con comentarios breves en español. No uses CSS inline, solo clases de Bootstrap.

-templates/rescate/ejemplar_form.html
Actúa como desarrollador front-end senior, experto en Django (Django Template Language, formularios y ModelForm) y Bootstrap 5.
Crea la plantilla templates/rescate/ejemplar_form.html, un único formulario que sirva tanto para crear como para editar un ejemplar, y que herede de base.html.
- Proyecto Django "Huella Austral", un centro de rescate de fauna silvestre del sur de Chile.
- La misma plantilla la usan EjemplarCreateView y EjemplarUpdateView. Ambas entregan la variable "form" (un ModelForm llamado EjemplarForm). En edición existe además "object" con el ejemplar; en creación "object" es None.
- Campos del formulario: especie (Select), nombre (texto), peso_kg (decimal), fecha_ingreso (fecha) y liberado (checkbox). Los widgets ya traen sus clases de Bootstrap definidas en forms.py (form-control, form-select, form-check-input).
- Namespace de URLs: 'rescate'. Nombre para volver: lista.
- Requisitos:
  1. Empezar con {% extends 'base.html' %} y usar {% block title %} y {% block content %}.
  2. Título dinámico con {% if object %}: "Editar ejemplar" si existe, "Registrar ejemplar" si no.
  3. <form method="post"> dentro de una card de Bootstrap 5, con {% csrf_token %}.
  4. Recorrer los campos con {% for campo in form %}, mostrando label y widget con {{ campo }}.
  5. El checkbox debe renderizarse distinto: dentro de un div "form-check", con el input antes del label.
  6. Mostrar los errores de cada campo debajo de él, con clase text-danger small.
  7. Botón "Guardar" (btn-success, type submit) y botón "Cancelar" que vuelva al catálogo con {% url 'rescate:lista' %}.
  8. No usar CSS inline, solo clases de Bootstrap.
Entrégame solo el código completo del template en un único bloque de código, con comentarios breves en español.

-templates/rescate/ejemplar_confirm_delete.html
--Actúa como desarrollador front-end senior, experto en Django (Django Template Language y DeleteView) y Bootstrap 5.
Crea la plantilla templates/rescate/ejemplar_confirm_delete.html, la página de confirmación antes de eliminar un ejemplar, que hereda de base.html.
- Proyecto Django "Huella Austral", un centro de rescate de fauna silvestre del sur de Chile.
- La DeleteView (EjemplarDeleteView) entrega al template la variable "ejemplar" (con context_object_name definido). Al enviar el formulario por POST, la vista elimina el registro y redirige al catálogo con reverse_lazy.
- Campos útiles del ejemplar: nombre y especie (ForeignKey a Especie, que tiene el campo nombre).
- Namespace de URLs: 'rescate'. Nombre para cancelar: lista.
- Requisitos:
  1. Empezar con {% extends 'base.html' %} y usar {% block title %} y {% block content %}.
  2. Card de Bootstrap 5 con borde rojo (border-danger) y un título "Eliminar ejemplar" en color de peligro.
  3. Mensaje de confirmación que incluya el nombre del ejemplar en negrita y su especie, y avise que la acción no se puede deshacer.
  4. <form method="post"> con {% csrf_token %}
  5. Botón "Sí, eliminar" (btn-danger, type submit) y botón "Cancelar" (btn-outline-secondary) que vuelva al catálogo con {% url 'rescate:lista' %}.
  6. No usar CSS inline, solo clases de Bootstrap.
Entrégame solo el código completo del template en un único bloque de código, con comentarios breves en español.