# Flask Store 🛒

¡Bienvenido a **Flask Store**, una aventura digital creada por **VolleyDevByMaubry**! Esta aplicación web, construida con Flask y MongoDB, es tu boleto para gestionar una tienda en línea con estilo. Desde una API REST para manejar productos hasta una interfaz web que te permite crear y editar con un clic, ¡Flask Store es donde las ideas se convierten en código y los productos cobran vida!

## ¿Qué hace especial a Flask Store?

- **API REST ágil**: Crea, lee, actualiza y elimina productos con endpoints claros y potentes.
- **Interfaz web amigable**: Formularios intuitivos para listar, agregar o editar productos, con soporte para subir imágenes (¡sí, fotos en `.jpg`, `.png`, y más!).
- **MongoDB como aliado**: Almacena tus productos en una base de datos flexible y moderna.
- **Código modular**: Una arquitectura limpia que hace fácil añadir nuevas funcionalidades.

## Requisitos

- Python 3.8 o superior
- MongoDB (local o en la nube, como MongoDB Atlas)
- Git para clonar este proyecto

## ¡Pongámoslo en marcha!

1. Clona el repositorio y entra al directorio:

   ```bash
   git clone https://github.com/maubry-ortega/flask_store.git
   cd flask_store
   ```

2. Crea un entorno virtual y actívalo:

   ```bash
   python -m venv venv
   venv/bin/activate  # En Windows: source venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura tu `.env` en la raíz del proyecto:

   ```bash
   MONGO_URI=mongodb://localhost:27017/
   MONGO_DB_NAME=tiendaorm
   ```

5. Lanza la aplicación:

   ```bash
   python app.py
   ```

   ¡Visita `http://localhost:3030` y comienza la magia!

## Explora Flask Store

### Interfaz Web

- **Lista de productos**: Ve todos tus productos en `/pagina`.
- **Añade un producto**: Usa `/pagina/crear` para subir detalles e imágenes.
- **Edita o elimina**: Modifica con `/pagina/editar/<id>` o elimina desde la lista.

### API REST

Prueba estos endpoints con `curl` o tu herramienta favorita:

- **GET /api**: Obtén todos los productos.
- **POST /api**: Crea un producto nuevo:

  ```bash
  curl -X POST -H "Content-Type: application/json" \
       -d '{"codigo": "P001", "nombre": "Gadget Cool", "precio": 15.99, "foto": "/static/img/gadget.jpg", "categoria": "Tech"}' \
       http://localhost:3030/api
  ```

- **GET/PUT/DELETE /api/**: Maneja un producto específico por su ID.

## Estructura del Proyecto

Flask Store está organizado para ser claro y escalable:

- **Rutas**: Conectan tus acciones con la lógica de la app.
- **Servicios**: Orquestan la magia detrás de escena.
- **Repositorios**: Hablan con MongoDB para guardar y recuperar datos.
- **Plantillas**: HTML dinámico para una experiencia visual fluida.
- **Configuración**: Todo listo con variables de entorno.

## Dependencias

- Flask
- PyMongo
- python-dotenv

## Consejos para el Futuro

- **Seguridad**: Añade `Flask-Login` para proteger tu tienda.
- **Validación**: Usa `Flask-WTF` para formularios más robustos.
- **Imágenes**: Valida el contenido de las imágenes con `Pillow` para mayor seguridad.

## Únete al Proyecto

¿Tienes ideas? ¡Abre un _issue_ o envía un _pull request_! Flask Store es un lienzo para creadores como tú.

## Creado por

**VolleyDevByMaubry**\
2025, con pasión y código. Licencia MIT.
