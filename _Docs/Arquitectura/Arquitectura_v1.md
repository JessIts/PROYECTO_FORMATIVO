#  Justificación de Arquitectura y Tecnologías

##  Justificación de la Arquitectura

La arquitectura de software seleccionada para el desarrollo del proyecto se basa en un enfoque de **API REST** junto con una **arquitectura en capas**, lo cual permite una organización clara, modular y escalable del sistema.

La elección de una API REST facilita la comunicación entre cliente y servidor mediante el uso de estándares ampliamente adoptados, lo que garantiza interoperabilidad, facilidad de integración con otros sistemas y una mayor flexibilidad para futuras expansiones, como aplicaciones móviles o servicios externos.

Por otra parte, la arquitectura en capas permite dividir el sistema en diferentes niveles (por ejemplo: presentación, lógica de negocio y acceso a datos), lo cual favorece la separación de responsabilidades. Esto no solo mejora la mantenibilidad del código, sino que también facilita la detección de errores, la reutilización de componentes y el trabajo colaborativo entre los integrantes del equipo.

Adicionalmente, se opta por el uso de metodologías ágiles debido a su enfoque iterativo e incremental, lo cual resulta especialmente adecuado para un equipo de aprendices del SENA. Estas metodologías permiten adaptarse a cambios, recibir retroalimentación constante y realizar entregas parciales funcionales, facilitando así el aprendizaje progresivo y la mejora continua del proyecto.

En conjunto, la combinación de API REST, arquitectura en capas y metodologías ágiles proporciona una base sólida para el desarrollo del proyecto, asegurando calidad, organización y capacidad de adaptación a futuros requerimientos.

---

##  Tecnologías Recomendadas por Capa

### 1. Capa de Presentación (Frontend)

Encargada de la interacción con el usuario y consumo de la API REST.

**Opciones:**

* React
* Vite
* TypeScript
* TailwindCSS


---

###  2. Capa de Aplicación (Backend)

Encargada de gestionar las solicitudes HTTP (GET, POST, PUT, DELETE).

**Opciones:**

* Fast API
* Python
* JWT

**Buenas prácticas:**

* Validaciones
* Reglas de negocio
* Manejo de datos
* Restricciones

---

###  3. Capa de Acceso a Datos (DB)

Encargada de la comunicación con la base de datos.

**Opciones:**

* Bases de datos:

  * PostgreSQL
  * Docker Compose

---

##  Herramientas Complementarias

* Control de versiones: Git + GitHub
* Pruebas de API: Postman
* Documentación: Visual Estudio Code
* Gestión ágil: Clickup

---

##  Arquitectura Recomendada

* Frontend: React + Vite
* Backend: Fast API
* Base de datos: PostgreSQL
* Pruebas: Postman
* Control de versiones: GitHub

---

## Diagrama de despliegue

```mermaid

flowchart LR
    %% =========================
    %% CLIENTE
    %% =========================
    subgraph Cliente["Cliente (Navegador Web)"]
        FE["Frontend\nReact + Vite\nTypeScript + TailwindCSS"]
    end

    %% =========================
    %% BACKEND PRINCIPAL
    %% =========================
    subgraph Backend_Principal["Servidor Backend Principal"]
        BE1["API REST\nFastAPI (Python)\nJWT\nValidaciones\nReglas de negocio"]
    end

    %% =========================
    %% BACKEND RESPALDO (DOCKER)
    %% =========================
    subgraph Backend_Respaldo["Contenedores Docker (Respaldo)"]
        BE2["Replica API REST\nFastAPI"]
        BE3["Replica API REST\nFastAPI"]
    end

    %% =========================
    %% BASE DE DATOS
    %% =========================
    subgraph DB_Server["Servidor de Base de Datos"]
        DB[(PostgreSQL\nDocker Container)]
    end

    %% =========================
    %% RELACIONES
    %% =========================
    FE -->|HTTP/HTTPS| BE1

    %% Uso de respaldo en caso crítico
    FE -->|Alta carga / Falla| BE2
    FE -->|Alta carga / Falla| BE3

    BE1 --> DB
    BE2 --> DB
    BE3 --> DB
```
---

##  Recomendación Final

Se recomienda utilizar un conjunto de tecnologías que el equipo pueda manejar adecuadamente, priorizando la simplicidad, la correcta implementación y el funcionamiento completo del sistema, en lugar de incorporar herramientas innecesarias que compliquen el desarrollo.

---
## Observaciones

Tenemos en cuenta que probablemente no estamos escogiendo las tecnologias más optimas para desarrollar nuestro sistema de información justo en este momento, no obstante decidimos seguir este planteamiento teniendo en cuenta los temas desarrollado en la formación del tecnólogo.
