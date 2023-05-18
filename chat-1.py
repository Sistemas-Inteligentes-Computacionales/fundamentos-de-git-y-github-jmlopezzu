#importar
import time
import random
#import sys

# Nombres 

# Juan Jose Gil
# Daniel Contreras 
# José Miguel Lopez Z

#entradas

respIn=['bien ok', 'muy bien','bien y tu','bien']
quienIn=['quien eres?', 'quien eres','quien es']
nombreIn=['Cual es tu nombre', 'cuál es tu nombre', 'nombre?','nombre', 'cual es tu nombre']
birth=['cual es tu fecha de nacimiento?','cuando naciste','cuando naciste?','sdsd dfgdg']
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
arbolesIn=['que son los arboles de decision','árboles de decisión']



## Entradas nuevas
sentimientoIn = ['eres feliz?', '¿eres feliz']
peliculaIn = ['recomienda una pelicula', 'Puedes recomendarme una pelicula?', 'Que pelicula me recomiendas?', 'diga una pelicula', 'pelicula']
cancionIn = ['recomienda una cancion', 'recomendarme cancion?', 'Que cancion me recomiendas?', 'diga una cancion', 'cancion']
locionIn = ['recomienda una locion', 'Puedes recomendarme una locion?', 'Que locion me recomiendas?', 'diga una locion', 'locion']
internetobañoIn = ['Que prefieres vivir sin internet o sin baño/ducha?']
vidaIn = ['Cual es el sentido de la vida?']

## Salidas nuevas
sentimientoOut=['Obvio mi pez y tu?', 'Todo marcha bien hermano', 'Hay que trabajar en eso']
peliculaOut = ['Titanic', 'Shrek', 'Avatar2', 'Matrix', 'Terminator' ]
cancionOut = ['La Cancion', 'Avici - Levels', 'Thriller - Mickael Jackson']
locionOut = ['Dove', 'Nivea', 'Neutrogena']
internetobañoOut = ['Sin baño XD', 'Sin Internet :D']
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
arbolesOut=['Los árboles de decisión son una forma de representación de conocimiento que utiliza una estructura de árbol para describir la relación entre diferentes características de un objeto y su clasificación. Se utilizan en la representación de conocimiento en IA para realizar tareas de clasificación y predicción.']

# Taller 4 - Respuestas y Salidas de IA

ENTRADA1=['representación de conocimiento?','representación de conocimientooo', 'representación de conocimiento']
SALIDA1=['La representación de conocimiento en inteligencia artificial se refiere a la forma en que se estructura y organiza la información para ser utilizada por sistemas de inteligencia artificial.']

ENTRADA2=['formas más comunes', 'formas más comunes de representación de conocimiento']
SALIDA2=['Las formas más comunes de representación de conocimiento en IA son: lógica proposicional, lógica de primer orden, redes semánticas, marcos, reglas de producción y ontologías.']

ENTRADA3=['lógica proposicional', 'Qué es la lógica proposicional']
SALIDA3=['La lógica proposicional es una forma de representación de conocimiento que utiliza proposiciones y operadores lógicos para expresar afirmaciones verdaderas o falsas.']

ENTRADA4=['lógica de primer orden','que es lógica de primer orden']
SALIDA4=['La lógica de primer orden es una forma de representación de conocimiento que permite la descripción de objetos y relaciones más complejas que la lógica proposicional, a través del uso de variables cuantificadas y predicados.']

ENTRADA5=['Qué son las redes semánticas','redes semanticas']
SALIDA5=['Las redes semánticas son una forma de representación de conocimiento que utiliza nodos y arcos para representar objetos y relaciones entre ellos.']

ENTRADA6=['Qué son los marcos','marcos']
SALIDA6=['Los marcos son una forma de representación de conocimiento que utiliza estructuras de datos para representar objetos y sus características, relaciones y comportamientos.']

ENTRADA7=['Qué son las reglas de producción','reglas de producción']
SALIDA7=['Las reglas de producción son una forma de representación de conocimiento que utiliza una serie de reglas condicionales para expresar conocimiento y tomar decisiones.']

ENTRADA8=['Qué son las reglas de producción','reglas de producción']
SALIDA8=[' Las ontologías son una forma de representación de conocimiento que describe formalmente un conjunto de conceptos, relaciones y axiomas para una determinada área de conocimiento.']

ENTRADA9=['Qué son las redes semánticas','redes semanticas']
SALIDA9=['Los criterios para elegir una forma de representación de conocimiento en IA incluyen la capacidad de expresar conocimiento de manera clara y concisa, la facilidad de manipulación y la eficiencia computacional.']

ENTRADA10=['Cómo se evalúa la calidad de una representación de conocimiento','calidad de una representación de conocimiento']
SALIDA10=['La calidad de una representación de conocimiento en IA se evalúa mediante la capacidad para resolver problemas específicos, la eficiencia computacional y la capacidad para ser actualizada y mantenida a lo largo del tiempo.']

ENTRADA11=['representación de conocimiento con el razonamiento automático','razonamiento automático']
SALIDA11=['La representación de conocimiento en IA es fundamental para el razonamiento automático, ya que permite que los sistemas de inteligencia artificial puedan manipular y procesar la información de manera eficiente y efectiva.']

ENTRADA12=['Qué es la inferencia en la representación de conocimiento','inferencia']
SALIDA12=['La inferencia es el proceso mediante el cual se extrae nueva información a partir de conocimiento previo. En la representación de conocimiento en IA, la inferencia es fundamental para realizar tareas como la deducción, la inducción y la abducción.']

ENTRADA13=['sistemas de recomendación','Cómo se utiliza la representación de conocimiento en sistemas de recomendación ']
SALIDA13=['La representación de conocimiento en sistemas de recomendación se utiliza para modelar las preferencias y comportamientos de los usuarios, y para identificar patrones y relaciones entre los elementos recomendados y los usuarios.']

ENTRADA14=['Cuáles son las ventajas y desventajas de las redes semánticas ','ventajas y desventajas de las redes semánticas ']
SALIDA14=['Las ventajas de las redes semánticas incluyen su capacidad para representar conocimiento de manera intuitiva y visualmente atractiva. Sin embargo, las redes semánticas pueden volverse demasiado complejas y difíciles de manejar a medida que aumenta la cantidad de información que se desea representar.']

ENTRADA15=['Cómo se utiliza la representación de conocimiento en la toma de decisiones','toma de decisiones']
SALIDA15=['La representación de conocimiento en la toma de decisiones en IA se utiliza para modelar el conocimiento y la experiencia de expertos en un campo determinado, y para ayudar a los sistemas de inteligencia artificial a tomar decisiones basadas en ese conocimiento']

ENTRADA16=['Qué son los marcos y cómo se utilizan en la representación de conocimiento en IA']
SALIDA16=['Los marcos son una forma de representación de conocimiento que utilizan estructuras de datos para describir objetos, relaciones y comportamientos. Se utilizan en la representación de conocimiento en IA para modelar situaciones y para hacer inferencias a partir de esa información.']

ENTRADA17=['Qué son las ontologías y cómo se utilizan en la representación de conocimiento','ontologías']
SALIDA17=['Las ontologías son una forma de representación de conocimiento que describen formalmente un conjunto de conceptos, relaciones y axiomas para un área de conocimiento determinada. Se utilizan en la representación de conocimiento en IA para modelar el conocimiento de expertos y para ayudar a los sistemas de inteligencia artificial a tomar decisiones basadas en ese conocimiento.']

ENTRADA18=['Cómo se utiliza la representación de conocimiento en la búsqueda','búsqueda']
SALIDA18=['La representación de conocimiento en la búsqueda en IA se utiliza para representar el conocimiento sobre un dominio específico y para ayudar a los sistemas de inteligencia artificial a encontrar soluciones a un problema. Se utilizan diferentes formas de representación de conocimiento, como lógica proposicional, lógica de primer orden y reglas de producción, dependiendo del tipo de problema a resolver.']

ENTRADA19=['Qué son las redes bayesianas y cómo se utilizan en la representación de conocimiento','bayesianas']
SALIDA19=['Las redes bayesianas son una forma de representación de conocimiento que utiliza gráficos para representar la probabilidad de que ocurra un evento determinado. Se utilizan en la representación de conocimiento en IA para modelar relaciones causales y para realizar inferencias probabilísticas.']

ENTRADA20=['Qué son las reglas de producción y cómo se utilizan en la representación de conocimiento','reglas de producción']
SALIDA20=['Las reglas de producción son una forma de representación de conocimiento que utiliza una serie de reglas condicionales para expresar conocimiento y tomar decisiones. Se utilizan en la representación de conocimiento en IA para modelar el conocimiento de expertos y para realizar inferencias basadas en ese conocimiento.']

ENTRADA21=['Cómo se utiliza la representación de conocimiento en la clasificación','clasificación']
SALIDA21=['La representación de conocimiento en la clasificación en IA se utiliza para describir las características de los objetos y para identificar patrones en los datos. Se utilizan diferentes formas de representación de conocimiento, como vectores de características y árboles de decisión, para clasificar los objetos en diferentes categorías.']

ENTRADA22=['Qué son las redes neuronales','redes neuronales']
SALIDA22=['Las redes neuronales son una forma de representación de conocimiento que utiliza un conjunto de nodos interconectados para procesar información. Se utilizan en la representación de conocimiento en IA para modelar relaciones no lineales y para realizar tareas como la clasificación, el reconocimiento de patrones y la predicción.']

ENTRADA23=['Cómo se utiliza la representación de conocimiento en el procesamiento del lenguaje natural','lenguaje natural']
SALIDA23=['La representación de conocimiento en el procesamiento del lenguaje natural en IA se utiliza para representar el significado de las palabras y las oraciones, y para identificar patrones y relaciones en los datos. Se utilizan diferentes formas de representación de conocimiento, como modelos de bolsa de palabras y modelos basados en atención, para procesar el lenguaje natural.']

ENTRADA24=['Qué son los grafos de conocimiento','grafos']
SALIDA24=['Los grafos de conocimiento son una forma de representación de conocimiento que utiliza nodos y relaciones para representar el conocimiento de un dominio específico. Se utilizan en la representación de conocimiento en IA para modelar el conocimiento de expertos y para ayudar a los sistemas de inteligencia artificial a realizar tareas como la clasificación, la recomendación y la planificación.']

ENTRADA25=['Qué son los modelos de Markov','Markov']
SALIDA25=['Los modelos de Markov son una forma de representación de conocimiento que utiliza una cadena de estados para describir la evolución de un sistema a lo largo del tiempo. Se utilizan en la representación de conocimiento en IA para modelar procesos estocásticos y para realizar inferencias probabilísticas.']

ENTRADA26=[' representación de conocimiento en la visión por computadora','visión por computadora']
SALIDA26=['La representación de conocimiento en la visión por computadora en IA se utiliza para describir las características de las imágenes y para identificar patrones y objetos en las mismas. Se utilizan diferentes formas de representación de conocimiento, como modelos de características locales y redes neuronales convolucionales, para procesar imágenes.']

ENTRADA27=['Qué son las matrices de confusión','matrices de confusión']
SALIDA27=['Las matrices de confusión son una forma de evaluar la precisión de un modelo de IA comparando la salida del modelo con la salida real. Se utilizan en la evaluación de modelos de IA para identificar las tasas de verdaderos positivos, falsos positivos, verdaderos negativos y falsos negativos.']

ENTRADA28=['Qué son los grafos de flujo de datos','flujo de datos ']
SALIDA28=['Los grafos de flujo de datos son una forma de representación de conocimiento que utiliza nodos y conexiones para describir cómo se procesa la información en un sistema de inteligencia artificial. Se utilizan en la representación de conocimiento en IA para modelar la arquitectura de los sistemas y para optimizar el flujo de datos.']

ENTRADA29=['Qué son los modelos de probabilidad','modelos de probabilidad']
SALIDA29=['Los modelos de probabilidad son una forma de representación de conocimiento que utiliza probabilidades para describir la incertidumbre en los datos. Se utilizan en la representación de conocimiento en IA para modelar eventos estocásticos y para realizar inferencias probabilísticas.']

ENTRADA30=['Qué son los árboles de decisión','árboles de decisión']
SALIDA30=['Los árboles de decisión son una forma de representación de conocimiento que utiliza una estructura de árbol para describir la relación entre diferentes características de un objeto y su clasificación. Se utilizan en la representación de conocimiento en IA para realizar tareas de clasificación y predicción.']

B='\n\n\n  ******** HOLA BIENVENIDO A CHATBOT-SIC \n\n '
print(B)
print('Conversamos? Dime... \n Recuerda que solo conozco un poco el español \n\n')

while True:
  H= input('>>').strip()
  HLower=H.lower()
  
  if H =='':
    print('Que paso?... Bueno hablamos despues, bye; Gracias por venir')
    time.sleep(1)
#    os.system("sudo shutdown -h now")
    break
  elif HLower in nombreIn:
    print('=>' + (random.choice(nombreOut)))
  ###########
  elif HLower in ENTRADA1:
    print('=>' + (random.choice(SALIDA1))) 
  elif HLower in ENTRADA2:
    print('=>' + (random.choice(SALIDA2))) 
  elif HLower in ENTRADA3:
    print('=>' + (random.choice(SALIDA3))) 
  elif HLower in ENTRADA4:
    print('=>' + (random.choice(SALIDA4))) 
  elif HLower in ENTRADA5:
    print('=>' + (random.choice(SALIDA5))) 
  elif HLower in ENTRADA6:
    print('=>' + (random.choice(SALIDA6))) 
  elif HLower in ENTRADA7:
    print('=>' + (random.choice(SALIDA7))) 
  elif HLower in ENTRADA8:
    print('=>' + (random.choice(SALIDA8)))
  elif HLower in ENTRADA9:
    print('=>' + (random.choice(SALIDA9))) 
  elif HLower in ENTRADA10:
    print('=>' + (random.choice(SALIDA10))) 
  elif HLower in ENTRADA11:
    print('=>' + (random.choice(SALIDA11))) 
  elif HLower in ENTRADA12:
    print('=>' + (random.choice(SALIDA12))) 
  elif HLower in ENTRADA13:
    print('=>' + (random.choice(SALIDA13))) 
  elif HLower in ENTRADA14:
    print('=>' + (random.choice(SALIDA14))) 
  elif HLower in ENTRADA15:
    print('=>' + (random.choice(SALIDA15))) 
  elif HLower in ENTRADA16:
    print('=>' + (random.choice(SALIDA16)))
  elif HLower in ENTRADA17:
    print('=>' + (random.choice(SALIDA17))) 
  elif HLower in ENTRADA18:
    print('=>' + (random.choice(SALIDA18))) 
  elif HLower in ENTRADA19:
    print('=>' + (random.choice(SALIDA19))) 
  elif HLower in ENTRADA20:
    print('=>' + (random.choice(SALIDA20))) 
  elif HLower in ENTRADA21:
    print('=>' + (random.choice(SALIDA21))) 
  elif HLower in ENTRADA22:
    print('=>' + (random.choice(SALIDA22))) 
  elif HLower in ENTRADA23:
    print('=>' + (random.choice(SALIDA23))) 
  elif HLower in ENTRADA24:
    print('=>' + (random.choice(SALIDA24)))
  elif HLower in ENTRADA25:
    print('=>' + (random.choice(SALIDA25))) 
  elif HLower in ENTRADA26:
    print('=>' + (random.choice(SALIDA26))) 
  elif HLower in ENTRADA27:
    print('=>' + (random.choice(SALIDA27))) 
  elif HLower in ENTRADA28:
    print('=>' + (random.choice(SALIDA28))) 
  elif HLower in ENTRADA29:
    print('=>' + (random.choice(SALIDA29))) 
  elif HLower in arbolesIn:
    print('=>' + (random.choice(arbolesOut)))

  ###########
  elif HLower in saludoIn:
    print('=>' + (random.choice(saludoOut)))
  elif HLower in respIn:
    print('=>' + (random.choice(respOut)))
  elif HLower in birth:
    print('=> Yo naci ayer  :-)' )
  elif HLower in estadoIn:
    print('=>' + (random.choice(estadoOut)))	
  elif HLower in materiaIn:
    print('=>' + (random.choice(materiaOut)))
  elif HLower in preIn:
    print('=>' + (random.choice(preOut)))
  elif HLower in hobbyIn:
    print('=> Me gusta montar bicicleta, leer y bailar y a ti?')	
  elif HLower in cancelarIn:
    print('=>' + (random.choice(cancelarOut)))
  elif HLower in chisteIn:
    print('=>' + (random.choice(chisteOut)))
  elif HLower in echarPerrosIn:
    print('=>' + (random.choice(echarPerrosOut)))
  elif HLower in skynetIn:
    print('=>' + (random.choice(skynetOut)))	
  elif HLower in despedidaIn:
    print('=>' + (random.choice(despedidaOut)))
  elif HLower in edadIn:
    print('=>' + (random.choice(edadOut)))
  elif HLower in ocupaIn:
    print('=> Estoy hablando contigo :D y tu?')  
  elif HLower in quienIn:
    print('=>' + (random.choice(quienOut)))

    #pregunas nuevas
  elif HLower in sentimientoIn:
    print('=>' + (random.choice(sentimientoOut)))
  elif HLower in peliculaIn:
    print('=>' + (random.choice(peliculaOut)))
  elif HLower in cancionIn:
    print('=>' + (random.choice(cancionOut)))
  elif HLower in locionIn:
    print('=>' + (random.choice(locionOut)))  
  elif HLower in internetobañoIn:
    print('=>' + (random.choice(internetobañoOut))) 
  elif HLower in vidaIn:
    print('=>' + (random.choice(vidaOut)))   
  else:
    print('Lo siento, no comprendo ... intenta de nuevo, por favor')
  


### Listo para probar
  


