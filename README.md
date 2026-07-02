# Conexión de Base de Datos y Backend

## Descripción

Se realizó la configuración e integración entre la base de datos PostgreSQL y el backend desarrollado en FastAPI, utilizando Docker como herramienta de contenedorización. Esta configuración permite que ambos servicios se ejecuten de manera independiente pero comunicándose entre sí dentro de una misma red de Docker.

---

## Objetivo

Implementar y verificar la conexión entre la base de datos y el backend, garantizando el correcto funcionamiento de la aplicación y la persistencia de la información.

---

## Tecnologías Utilizadas

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker
* Docker Compose

---

## Proceso Realizado

### 1. Configuración de la Base de Datos

Se utilizó PostgreSQL como sistema gestor de base de datos, configurado dentro de un contenedor Docker mediante Docker Compose.

### 2. Configuración del Backend

El backend fue desarrollado con FastAPI y configurado para ejecutarse dentro de un contenedor Docker independiente.

### 3. Configuración de Variables de Entorno

Se definieron las variables necesarias para la conexión a la base de datos, incluyendo:

* Nombre de la base de datos.
* Usuario.
* Contraseña.
* Dirección del servidor.
* Clave secreta de la aplicación.

### 4. Integración mediante SQLAlchemy

Se configuró SQLAlchemy como ORM para gestionar la comunicación entre el backend y PostgreSQL, permitiendo realizar operaciones sobre la base de datos mediante modelos de Python.

### 5. Comunicación entre Contenedores

Se estableció la comunicación entre los servicios utilizando la red interna creada automáticamente por Docker Compose, permitiendo que el backend accediera a la base de datos mediante el nombre del servicio configurado.

### 6. Ejecución del Proyecto

Se construyeron y ejecutaron los contenedores utilizando Docker Compose, verificando que tanto la base de datos como el backend iniciaran correctamente.

---

## Comandos Ejecutados

### Verificar contenedores activos

```bash
docker ps
```

Permite visualizar los contenedores que se encuentran en ejecución.

---

### Detener contenedores existentes

```bash
docker compose down
```

Detiene y elimina los contenedores creados previamente.

---

### Construir y levantar los servicios

```bash
docker compose up --build
```

Construye las imágenes y levanta los servicios definidos en el archivo `docker-compose.yml`.

---

### Verificar los registros del backend

```bash
docker logs backend_sihs
```

Permite identificar errores o confirmar el correcto inicio del backend.

---

### Verificar los registros de PostgreSQL

```bash
docker logs postgres_sihs
```

Permite verificar que la base de datos se encuentre funcionando correctamente.

---

### Ingresar a PostgreSQL

```bash
docker exec -it postgres_sihs psql -U postgres -d sistema_sihs
```

Permite acceder a la consola de PostgreSQL para realizar consultas sobre la base de datos.

---

### Listar tablas existentes

```sql
\dt
```

Muestra todas las tablas creadas en la base de datos.

---

### Salir de PostgreSQL

```sql
\q
```

Finaliza la sesión en PostgreSQL.

---

### Acceder a la documentación de la API

```text
http://localhost:8000/docs
```

Permite visualizar y probar los servicios disponibles mediante Swagger.

---

### Resultado

Después de actualizar la cadena de conexión y reconstruir los contenedores, el backend logró conectarse correctamente a PostgreSQL, permitiendo el inicio exitoso de la aplicación y el acceso a la documentación Swagger.


## Verificación de Funcionamiento

Para validar la integración se realizaron las siguientes comprobaciones:

* Inicio correcto del contenedor de PostgreSQL.
* Inicio correcto del contenedor del backend.
* Conexión exitosa entre FastAPI y PostgreSQL.
* Disponibilidad de la API mediante Swagger.
* Acceso a los endpoints expuestos por el backend.

---

## Resultado Obtenido

Se logró establecer correctamente la conexión entre la base de datos PostgreSQL y el backend desarrollado en FastAPI. La aplicación quedó operativa dentro de un entorno Dockerizado, permitiendo la administración de la información y el acceso a los servicios mediante la documentación interactiva de Swagger.

---

## Conclusión

La implementación permitió integrar satisfactoriamente la base de datos con el backend, garantizando una arquitectura organizada, escalable y portable gracias al uso de Docker. Esta configuración facilita el despliegue del proyecto y asegura un entorno de ejecución consistente para todos los integrantes del equipo.
