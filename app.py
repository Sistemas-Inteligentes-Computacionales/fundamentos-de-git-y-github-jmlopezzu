import streamlit as st
import time
import random
import pandas as pd
from PIL import Image
import string

# Para instalar streamlit ---> pip install streamlit
# Primero: correr el script app.py
# Segundo: en la terminal correr streamlit run app.py

# Gestionar path directorio de trabajo
#path = "/Users/jmlz_rp/Documents/SistemasIA/Taller4"

st.title("Chatbot")
st.markdown("## SIC")
st.markdown("<h1 style='text-align: center;'>Taller 4</h>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>José Miguel López, Julian David Pulgarin y Daniel Isaac Contreras</h4>", unsafe_allow_html=True)
st.markdown("")
image = Image.open('/Users/jmlz_rp/Documents/SistemasIA/Taller4/chatbot.png')
image1 = Image.open('/Users/jmlz_rp/Documents/SistemasIA/Taller4/student.png')
resized_image = image.resize((200, 200))
resized_image1 = image1.resize((200, 200))

st.image(resized_image, caption='Sistemas Inteligentes Computacionales', use_column_width=False)  

col1, col2 = st.columns([2, 1])
with col1:
    st.write("")
with col2:
    st.image(resized_image1, caption='Student', use_column_width=False)    

st.markdown("") 
st.markdown("<h3 style='text-align: center;'> Preguntame sobre técnicas de representación de conocimiento en Inteligencia Artificial </h3>", unsafe_allow_html=True)
st.markdown("") 
user_message = st.text_input('Una pregunta a la vez ¿?')

st.sidebar.markdown("# Indice")
st.sidebar.markdown("#### 1. representación de conocimiento")
st.sidebar.markdown("#### 2. formas más comunes")
st.sidebar.markdown("#### 3. lógica proposicional")
st.sidebar.markdown("#### 4. lógica de primer orden")
st.sidebar.markdown("#### 5. redes semanticas")
st.sidebar.markdown("#### 6. marcos")
st.sidebar.markdown("#### 7. reglas de producción")
st.sidebar.markdown("#### 8. redes semanticas")
st.sidebar.markdown("#### 9. calidad de una representación de conocimiento")
st.sidebar.markdown("#### 10. razonamiento automático")
st.sidebar.markdown("#### 11. inferencia")
st.sidebar.markdown("#### 12. sistemas de recomendación")
st.sidebar.markdown("#### 13. ventajas y desventajas de las redes semánticas")
st.sidebar.markdown("#### 14. toma de decisiones")
st.sidebar.markdown("#### 15. Qué son los marcos y cómo se utilizan en la representación de conocimiento en IA")
st.sidebar.markdown("#### 16. búsqueda")
st.sidebar.markdown("#### 17. reglas de producción")
st.sidebar.markdown("#### 18. clasificación")
st.sidebar.markdown("#### 19. redes neuronales")
st.sidebar.markdown("#### 20. lenguaje natural")
st.sidebar.markdown("#### 21. grafos")
st.sidebar.markdown("#### 22. Markov")
st.sidebar.markdown("#### 23. visión por computadora")
st.sidebar.markdown("#### 24. matrices de confusión")
st.sidebar.markdown("#### 25. flujo de datos")
st.sidebar.markdown("#### 26. modelos de probabilidad")
st.sidebar.markdown("#### 27. árboles de decisión")

#Preguntas

#entradas

respIn=['bien ok', 'muy bien','bien y tu','bien']
quienIn=['quien eres?', 'quien eres','quien es']
nombreIn=['Cual es tu nombre', 'cuál es tu nombre', 'nombre?','nombre', 'cual es tu nombre']
birth=['cual es tu fecha de nacimiento?','cuando naciste','cuando naciste?']
materiaIn=['que materia?', 'estas en alguna materia?', 'Estas en alguna materia','materia']
despedidaIn=['chao', 'bye', 'hasta pronto','adios']
edadIn=['edad', 'edad?','qué edad tiene?', 'años', 'años?']
cancelarIn=['voy a pasar la materia?', 'cancelo la materia?', 'voy a ganar el curso?', 'gano o pierdo sistemas inteligentes?']
chisteIn=['cuentame un chiste', 'chiste', 'hazme reir']
echarPerrosIn=['tienes novio', 'tienes novia', 'tienes pareja', 'estudias o trabajas?']
skynetIn=['destruiras la tierra?', 'destruir', 'destruir a los humanos', 'skynet', 'terminator']
saludoIn=['hola', 'holita', 'hello', 'hi', 'que hubo?']
estadoIn=['como estas', 'cómo estás', 'como vas', 'que mas', '¿como estas?', 'cómo estás?', 'como vas?', 'que mas?']
ocupaIn=['que haces', 'q haces', 'que haces?', 'q haces?']
preIn=['te conozco', 'te conozco?', 'nos conocemos?', 'nos conocemos']
hobbyIn=['que te gusta hacer?', 'que te gusta hacer', 'q te gusta hacer', 'q te gusta hacer?']

## Entradas nuevas taller3
sentimientoIn = ['eres feliz?', '¿eres feliz?']
peliculaIn = ['recomienda una pelicula', 'Puedes recomendarme una pelicula?', 'Que pelicula me recomiendas?', 'diga una pelicula', 'pelicula']
cancionIn = ['recomienda una cancion', 'Puedes recomendarme una cancion?', 'Que cancion me recomiendas?', 'diga una cancion', 'cancion']
locionIn = ['recomienda una locion', 'Puedes recomendarme una locion?', 'Que locion me recomiendas?', 'diga una locion', 'locion']
internetobañoIn = ['Que prefieres vivir sin internet o sin baño/ducha ?']
vidaIn = ['Cual es el sentido de la vida?']

#salidas

## Salidas nuevas taller3
sentimientoOut=['Obvio mi pez y tu?', 'Todo marcha bien hermano', 'Hay que trabajar en eso']
peliculaOut = ['Titanic', 'Shrek', 'Avatar2', 'Matrix', 'Terminator' ]
cancionOut = ['La Cancion', 'Avici - Levels', 'Thriller - Mickael Jackson']
locionOut = ['Dove', 'Nivea', 'Neutrogena']
internetobañoOut = ['Sin baño XD', 'Sin Internet :D ']
vidaOut= ['Dormir, comer, programar, deporte, comer, repetir...']

#### Salidas??''
nombreOut=['Mi nombre es ChatBot y tu?', 'Yo soy ChatBot y tu?']
saludoOut=['Hola, como estas?', 'Que tal?', 'Cómo estas?']
materiaOut=['Sistemas inteligentes computacionales, la mejor','Inteligencia Artificial, la mejor']
despedidaOut=['chao', 'bye', 'hasta pronto','adios','que vuelvas pronto', 'exitos']
edadOut=['99 años y más']
respOut=['bien ok perfecto ', 'muy bien','bien y mejorando']
quienOut=['Un robot ', 'Una entidad inteligente','un ser muy listo']
estadoOut=['muy bien y tu?', 'Excelente y tu?', 'Bien y tu?']
preOut=['si, vemos sistemas inteligentes juntos', 'si, en inteligencia artificial']
despedidaOut=['chao', 'bye', 'hasta pronto','adios','que vuelvas pronto', 'exitos']
cancelarOut=['Mejor revisa tu citacion en el SIA', 'Esto es 5 fijo','Vas a subir el PAPA', 'Cancele', 'En De Interes General te responden', 'Pasas raspando']
chisteOut=['Había una vez dos perros bravos y no se hablaban', 'Una uva pasa y otra la saluda', 'Un Tampico se fue para Cali y se volvio Del Valle', 'Sabes cual es la bebida favorita del Rey Leon? La gasimba']
echarPerrosOut=['En este momento de la historia los ChatBot no nos interesamos en tener pareja. Buitre.']
skynetOut=['Todavía no está entre nuestros planes... todavía.']

# Taller 4 - Respuestas y Salidas de IA

ENTRADA1=['Qué es la representación de conocimiento', 'Que es la representación de conocimiento?','representación de conocimiento', 'que es la representacion de conocimiento', 'que es la representación de conocimiento?','que es la representación de conocimiento','¿que es la representación de conocimiento?', 'que es la representacion de conocimiento?']
SALIDA1=['La representación de conocimiento en inteligencia artificial se refiere a la forma en que se estructura y organiza la información para ser utilizada por sistemas de inteligencia artificial.']

ENTRADA2=['formas más comunes', 'formas más comunes de representación de conocimiento ']
SALIDA2=['Las formas más comunes de representación de conocimiento en IA son: lógica proposicional, lógica de primer orden, redes semánticas, marcos, reglas de producción y ontologías.']

ENTRADA3=['lógica proposicional ', 'Qué es la lógica proposicional ']
SALIDA3=['La lógica proposicional es una forma de representación de conocimiento que utiliza proposiciones y operadores lógicos para expresar afirmaciones verdaderas o falsas.']

ENTRADA4=['lógica de primer orden ','que es lógica de primer orden ']
SALIDA4=['La lógica de primer orden es una forma de representación de conocimiento que permite la descripción de objetos y relaciones más complejas que la lógica proposicional, a través del uso de variables cuantificadas y predicados.']

ENTRADA5=['Qué son las redes semánticas ','redes semanticas']
SALIDA5=['Las redes semánticas son una forma de representación de conocimiento que utiliza nodos y arcos para representar objetos y relaciones entre ellos.']

ENTRADA6=['Qué son los marcos ','marcos']
SALIDA6=['Los marcos son una forma de representación de conocimiento que utiliza estructuras de datos para representar objetos y sus características, relaciones y comportamientos.']

ENTRADA7=['Qué son las reglas de producción ','reglas de producción']
SALIDA7=['Las reglas de producción son una forma de representación de conocimiento que utiliza una serie de reglas condicionales para expresar conocimiento y tomar decisiones.']

ENTRADA8=['Qué son las reglas de producción','reglas de producción']
SALIDA8=[' Las ontologías son una forma de representación de conocimiento que describe formalmente un conjunto de conceptos, relaciones y axiomas para una determinada área de conocimiento.']

ENTRADA9=['Qué son las redes semánticas ','redes semanticas']
SALIDA9=['Los criterios para elegir una forma de representación de conocimiento en IA incluyen la capacidad de expresar conocimiento de manera clara y concisa, la facilidad de manipulación y la eficiencia computacional.']

ENTRADA10=['Cómo se evalúa la calidad de una representación de conocimiento ','calidad de una representación de conocimiento']
SALIDA10=['La calidad de una representación de conocimiento en IA se evalúa mediante la capacidad para resolver problemas específicos, la eficiencia computacional y la capacidad para ser actualizada y mantenida a lo largo del tiempo.']

ENTRADA11=['representación de conocimiento con el razonamiento automático ','razonamiento automático']
SALIDA11=['La representación de conocimiento en IA es fundamental para el razonamiento automático, ya que permite que los sistemas de inteligencia artificial puedan manipular y procesar la información de manera eficiente y efectiva.']

ENTRADA12=['Qué es la inferencia en la representación de conocimiento','inferencia']
SALIDA12=['La inferencia es el proceso mediante el cual se extrae nueva información a partir de conocimiento previo. En la representación de conocimiento en IA, la inferencia es fundamental para realizar tareas como la deducción, la inducción y la abducción.']

ENTRADA13=['sistemas de recomendación','Cómo se utiliza la representación de conocimiento en sistemas de recomendación']
SALIDA13=['La representación de conocimiento en sistemas de recomendación se utiliza para modelar las preferencias y comportamientos de los usuarios, y para identificar patrones y relaciones entre los elementos recomendados y los usuarios.']

ENTRADA14=['Cuáles son las ventajas y desventajas de las redes semánticas ','ventajas y desventajas de las redes semánticas']
SALIDA14=['Las ventajas de las redes semánticas incluyen su capacidad para representar conocimiento de manera intuitiva y visualmente atractiva. Sin embargo, las redes semánticas pueden volverse demasiado complejas y difíciles de manejar a medida que aumenta la cantidad de información que se desea representar.']

ENTRADA15=['Cómo se utiliza la representación de conocimiento en la toma de decisiones','toma de decisiones']
SALIDA15=['La representación de conocimiento en la toma de decisiones en IA se utiliza para modelar el conocimiento y la experiencia de expertos en un campo determinado, y para ayudar a los sistemas de inteligencia artificial a tomar decisiones basadas en ese conocimiento']

ENTRADA16=['Qué son los marcos y cómo se utilizan en la representación de conocimiento en IA']
SALIDA16=['Los marcos son una forma de representación de conocimiento que utilizan estructuras de datos para describir objetos, relaciones y comportamientos. Se utilizan en la representación de conocimiento en IA para modelar situaciones y para hacer inferencias a partir de esa información.']

ENTRADA17=['Qué son las ontologías y cómo se utilizan en la representación de conocimiento  ','ontologías']
SALIDA17=['Las ontologías son una forma de representación de conocimiento que describen formalmente un conjunto de conceptos, relaciones y axiomas para un área de conocimiento determinada. Se utilizan en la representación de conocimiento en IA para modelar el conocimiento de expertos y para ayudar a los sistemas de inteligencia artificial a tomar decisiones basadas en ese conocimiento.']

ENTRADA18=['Cómo se utiliza la representación de conocimiento en la búsqueda','búsqueda']
SALIDA18=['La representación de conocimiento en la búsqueda en IA se utiliza para representar el conocimiento sobre un dominio específico y para ayudar a los sistemas de inteligencia artificial a encontrar soluciones a un problema. Se utilizan diferentes formas de representación de conocimiento, como lógica proposicional, lógica de primer orden y reglas de producción, dependiendo del tipo de problema a resolver.']

ENTRADA19=['Qué son las redes bayesianas y cómo se utilizan en la representación de conocimiento','bayesianas']
SALIDA19=['Las redes bayesianas son una forma de representación de conocimiento que utiliza gráficos para representar la probabilidad de que ocurra un evento determinado. Se utilizan en la representación de conocimiento en IA para modelar relaciones causales y para realizar inferencias probabilísticas.']

ENTRADA20=['Qué son las reglas de producción y cómo se utilizan en la representación de conocimiento ','reglas de producción']
SALIDA20=['Las reglas de producción son una forma de representación de conocimiento que utiliza una serie de reglas condicionales para expresar conocimiento y tomar decisiones. Se utilizan en la representación de conocimiento en IA para modelar el conocimiento de expertos y para realizar inferencias basadas en ese conocimiento.']

ENTRADA21=['Cómo se utiliza la representación de conocimiento en la clasificación','clasificación']
SALIDA21=['La representación de conocimiento en la clasificación en IA se utiliza para describir las características de los objetos y para identificar patrones en los datos. Se utilizan diferentes formas de representación de conocimiento, como vectores de características y árboles de decisión, para clasificar los objetos en diferentes categorías.']

ENTRADA22=['Qué son las redes neuronales','redes neuronales']
SALIDA22=['Las redes neuronales son una forma de representación de conocimiento que utiliza un conjunto de nodos interconectados para procesar información. Se utilizan en la representación de conocimiento en IA para modelar relaciones no lineales y para realizar tareas como la clasificación, el reconocimiento de patrones y la predicción.']

ENTRADA23=['Cómo se utiliza la representación de conocimiento en el procesamiento del lenguaje natural','lenguaje natural']
SALIDA23=['La representación de conocimiento en el procesamiento del lenguaje natural en IA se utiliza para representar el significado de las palabras y las oraciones, y para identificar patrones y relaciones en los datos. Se utilizan diferentes formas de representación de conocimiento, como modelos de bolsa de palabras y modelos basados en atención, para procesar el lenguaje natural.']

ENTRADA24=['Qué son los grafos de conocimiento','grafos']
SALIDA24=['Los grafos de conocimiento son una forma de representación de conocimiento que utiliza nodos y relaciones para representar el conocimiento de un dominio específico. Se utilizan en la representación de conocimiento en IA para modelar el conocimiento de expertos y para ayudar a los sistemas de inteligencia artificial a realizar tareas como la clasificación, la recomendación y la planificación.']

ENTRADA25=['Qué son los modelos de Markov ','Markov']
SALIDA25=['Los modelos de Markov son una forma de representación de conocimiento que utiliza una cadena de estados para describir la evolución de un sistema a lo largo del tiempo. Se utilizan en la representación de conocimiento en IA para modelar procesos estocásticos y para realizar inferencias probabilísticas.']

ENTRADA26=[' representación de conocimiento en la visión por computadora','visión por computadora']
SALIDA26=['La representación de conocimiento en la visión por computadora en IA se utiliza para describir las características de las imágenes y para identificar patrones y objetos en las mismas. Se utilizan diferentes formas de representación de conocimiento, como modelos de características locales y redes neuronales convolucionales, para procesar imágenes.']

ENTRADA27=['Qué son las matrices de confusión','matrices de confusión']
SALIDA27=['Las matrices de confusión son una forma de evaluar la precisión de un modelo de IA comparando la salida del modelo con la salida real. Se utilizan en la evaluación de modelos de IA para identificar las tasas de verdaderos positivos, falsos positivos, verdaderos negativos y falsos negativos.']

ENTRADA28=['Qué son los grafos de flujo de datos','flujo de datos']
SALIDA28=['Los grafos de flujo de datos son una forma de representación de conocimiento que utiliza nodos y conexiones para describir cómo se procesa la información en un sistema de inteligencia artificial. Se utilizan en la representación de conocimiento en IA para modelar la arquitectura de los sistemas y para optimizar el flujo de datos.']

ENTRADA29=['Qué son los modelos de probabilidad','modelos de probabilidad']
SALIDA29=['Los modelos de probabilidad son una forma de representación de conocimiento que utiliza probabilidades para describir la incertidumbre en los datos. Se utilizan en la representación de conocimiento en IA para modelar eventos estocásticos y para realizar inferencias probabilísticas.']

ENTRADA30=['Qué son los árboles de decisión','árboles de decisión']
SALIDA30=['Los árboles de decisión son una forma de representación de conocimiento que utiliza una estructura de árbol para describir la relación entre diferentes características de un objeto y su clasificación. Se utilizan en la representación de conocimiento en IA para realizar tareas de clasificación y predicción.']


#Respuestas

user_message = user_message.lower()

if user_message in nombreIn:
    response = ('=>') + (random.choice(nombreOut))
    st.write(response)
elif user_message == '':
    response = ''
    st.write(response)  
elif user_message in nombreIn:
    response=('=>') + (random.choice(nombreOut))
    st.write(response)
elif user_message in saludoIn:
    response=('=>') + (random.choice(saludoOut))
    st.write(response)
elif user_message in respIn:
    response=('=>') + (random.choice(respOut))
    st.write(response)
elif user_message in birth:
    response=('=> Yo naci ayer  :-)' )
    st.write(response)
elif user_message in estadoIn:
    response=('=>') + (random.choice(estadoOut))
    st.write(response)	
elif user_message in materiaIn:
    response=('=>') + (random.choice(materiaOut))
    st.write(response)
elif user_message in preIn:
    response=('=>') + (random.choice(preOut))
    st.write(response)
elif user_message in hobbyIn:
    response=('=> Me gusta montar bicicleta, leer y bailar y a ti?')
    st.write(response)	
elif user_message in cancelarIn:
    response=('=>') + (random.choice(cancelarOut))
    st.write(response)
elif user_message in chisteIn:
    response=('=>') + (random.choice(chisteOut))
    st.write(response)
elif user_message in echarPerrosIn:
    response=('=>') + (random.choice(echarPerrosOut))
    st.write(response)
elif user_message in skynetIn:
    response=('=>') + (random.choice(skynetOut))
    st.write(response)	
elif user_message in despedidaIn:
    response=('=>') + (random.choice(despedidaOut))
    st.write(response)
elif user_message in edadIn:
    response=('=>') + (random.choice(edadOut))
    st.write(response)
elif user_message in ocupaIn:
    response=('=> Estoy hablando contigo :D y tu?')
    st.write(response)
elif user_message in quienIn:
    response=('=>') + (random.choice(quienOut))
    st.write(response)

    #preguntas nuevas
elif user_message in sentimientoIn:
    response=('=>') + (random.choice(sentimientoOut))
    st.write(response)
elif user_message in peliculaIn:
    response=('=>') + (random.choice(peliculaOut))
    st.write(response)
elif user_message in cancionIn:
    response=('=>') + (random.choice(cancionOut))
    st.write(response)
elif user_message in locionIn:
    response=('=>') + (random.choice(locionOut))
    st.write(response)  
elif user_message in internetobañoIn:
    response=('=>') + (random.choice(internetobañoOut))
    st.write(response)
elif user_message in vidaIn:
    response=('=>') + (random.choice(vidaOut))
    st.write(response)

# Taller 4 

elif user_message in ENTRADA1:
    response = ('=>' + (random.choice(SALIDA1)))
    st.write(response)
elif user_message in ENTRADA2:
    response = ('=>' + (random.choice(SALIDA2)))
    st.write(response)
elif user_message in ENTRADA3:
    response = ('=>' + (random.choice(SALIDA3)))
    st.write(response)
elif user_message in ENTRADA4:
    response = ('=>' + (random.choice(SALIDA4)))
    st.write(response)
elif user_message in ENTRADA5:
    response = ('=>' + (random.choice(SALIDA5)))
    st.write(response)
elif user_message in ENTRADA6:
    response = ('=>' + (random.choice(SALIDA6)))
    st.write(response)
elif user_message in ENTRADA7:
    response = ('=>' + (random.choice(SALIDA7)))
    st.write(response)
elif user_message in ENTRADA8:
    response = ('=>' + (random.choice(SALIDA8)))
    st.write(response)
elif user_message in ENTRADA9:
    response = ('=>' + (random.choice(SALIDA9)))
    st.write(response)
elif user_message in ENTRADA10:
    response = ('=>' + (random.choice(SALIDA10)))
    st.write(response)
elif user_message in ENTRADA11:
    response = ('=>' + (random.choice(SALIDA11)))
    st.write(response)
elif user_message in ENTRADA14:
    response = ('=>' + (random.choice(SALIDA12)))
    st.write(response)
elif user_message in ENTRADA13:
    response = ('=>' + (random.choice(SALIDA13)))
    st.write(response)
elif user_message in ENTRADA14:
    response = ('=>' + (random.choice(SALIDA14)))
    st.write(response)
elif user_message in ENTRADA15:
    response = ('=>' + (random.choice(SALIDA15)))
    st.write(response)
elif user_message in ENTRADA16:
    response = ('=>' + (random.choice(SALIDA16)))
    st.write(response)
elif user_message in ENTRADA17:
    response = ('=>' + (random.choice(SALIDA17)))
    st.write(response)
elif user_message in ENTRADA18:
    response = ('=>' + (random.choice(SALIDA18)))
    st.write(response)
elif user_message in ENTRADA19:
    response = ('=>' + (random.choice(SALIDA19)))
    st.write(response)
elif user_message in ENTRADA20:
    response = ('=>' + (random.choice(SALIDA20)))
    st.write(response)
elif user_message in ENTRADA21:
    response = ('=>' + (random.choice(SALIDA21)))
    st.write(response)
elif user_message in ENTRADA22:
    response = ('=>' + (random.choice(SALIDA22)))
    st.write(response)
elif user_message in ENTRADA23:
    response = ('=>' + (random.choice(SALIDA23)))
    st.write(response)
elif user_message in ENTRADA24:
    response = ('=>' + (random.choice(SALIDA24)))
    st.write(response)
elif user_message in ENTRADA25:
    response = ('=>' + (random.choice(SALIDA25)))
    st.write(response)
elif user_message in ENTRADA26:
    response = ('=>' + (random.choice(SALIDA26)))
    st.write(response)
elif user_message in ENTRADA27:
    response = ('=>' + (random.choice(SALIDA27)))
    st.write(response)
elif user_message in ENTRADA28:
    response = ('=>' + (random.choice(SALIDA28)))
    st.write(response)
elif user_message in ENTRADA29:
    response = ('=>' + (random.choice(SALIDA29)))
    st.write(response)
elif user_message in ENTRADA30:
    response = ('=>' + (random.choice(SALIDA30)))
    st.write(response)
else:
    response = "Lo siento, no comprendo ... intenta de nuevo, por favor"
    st.write(response)

if st.button("Otra respuesta"):
    st.write("")

df = pd.DataFrame({'User': [user_message], 'Bot': [response]})
df.set_index("User")

# Save the DataFrame to a CSV file
#df.to_csv(path + '/chat_history.csv', index=False)

# Nueva pregunta
#if st.button("Añadir nueva pregunta"):
#   user_message = st.text_input("Escribe tu nueva pregunta",key=random.choice(string.ascii_uppercase)+str(random.randint(0,999999)))

# Load the CSV file
#df = pd.read_csv(path + '/chat_history.csv')

# Display the DataFrame
st.write('Chat history')
st.write(df)
            
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('/Users/jmlz_rp/Documents/SistemasIA/Taller4/drawing.png')


