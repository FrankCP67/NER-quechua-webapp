
# NER Quechua con Web App

El presente trabajo de investigación planteará una metodología a seguir según la revisión del estado del arte concerniente a BERT y su uso en NER. Se realizará un modelo pre entrenado BERT a partir de un conjunto de datos no anotados en quechua con tal de obtener una base sobre la cual aplicar ajustes. A su vez, se utilizará un conjunto de datos anotado para NER de otro idioma traducido al quechua con tal de ajustar el modelo. Finalmente se elabora una propuesta de un aplicativo con tal de mostrar resultados claros.

## Demostración del Web App

Ingrese a este enlace: https://ner-quechua.streamlit.app/

## Ejecución

Ejecutamos el archivo *app_NER_quechua.ipynb*

Tenemos la siguientes partes:

En la sección 1, se encarga de cargar los datos.
En la sección 2, se instancia el modelo, luego se entrena y se evalua los resultados.
En la sección 3, se realiza algunas prediciones luego de entrenar el modelo.

Para desplegar tendremos que ejecutar la sección 4 **Desplegar Aplicativo Web**.
Aquí es necesario ejecutar la sección 1 y de la sección 2 solo la primera linea de codigo
y posteriormente la sección 4.

En esta línea de código generamos la url temporal:
```bash
  url = ngrok.connect(8501)
  url.public_url
```
Luego ejecutamos este codigo y entramos al enlace anterior:
```bash
  !simple-viewer
```
    
