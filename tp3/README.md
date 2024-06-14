    TPN3: Consultas de APIs con Django
    Índice
    Descripción de la API
    Funcionamiento
    Modo de trabajo
    Bibliografía

    Descripción de la API: Georef-ar API
    La API Georef-ar proporciona datos geográficos y administrativos de Argentina. Permite consultar información detallada sobre provincias, como nombres, ID, coordenadas del centroide, población y superficie.

    

    Funcionamiento
    La aplicación comienza en la página de inicio (index.html), donde se presenta un menú desplegable para seleccionar entre consultar datos generales de provincias o información detallada de una provincia específica.

    Búsqueda de Provincias: El usuario puede ingresar el nombre de la provincia o una parte de él para obtener sugerencias mediante autocompletado.
    Resultados de la Búsqueda: Después de seleccionar una provincia y realizar la búsqueda, se muestran los detalles como ID, nombre, coordenadas del centroide, población y superficie en la página resultados.html.
    Modo de trabajo
    Configuración inicial:

    Clonar el repositorio desde GitHub.
    Configurar el entorno virtual y instalar las dependencias necesarias.
    Configurar el archivo settings.py con la configuración de la base de datos y otros ajustes.
    Ejecución de la aplicación:

    Aplicar las migraciones.
    Iniciar el servidor Django local.
    Navegación en la aplicación:

    Acceder a http://localhost:8000 para iniciar la búsqueda de provincias.
    Seleccionar una provincia desde el autocompletado o ingresar directamente el nombre completo.
    Visualizar los resultados detallados en una tabla organizada en resultados.html.
    Bibliografía
    Documentación oficial de Django: https://docs.djangoproject.com/
    API Georef-ar: https://datosgobar.github.io/georef-ar-api/
    Bootstrap Documentation: https://getbootstrap.com/docs/4.0/getting-started/introduction/