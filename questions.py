import random
import sys
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# El usuario deberá contestar 3 preguntas
puntaje = 0
# Se selecciona una pregunta aleatoria, ayuda de la práctica
questions_to_ask = random.choices(list(zip(questions,answers, correct_answers_index)), k=3)
# Se muestra la pregunta y las respuestas posibles, se deben contestar 3 preguntas
for pregunta,opciones,respuesta in questions_to_ask:
    print(pregunta)
    for i, answer in enumerate(opciones):
        print(f"{i + 1}. {answer}")
# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ") 
        if user_answer in ["1","2","3","4"]:
            user_answer = int(user_answer)-1
# Se verifica si la respuesta es correcta
            if user_answer == respuesta:
                print("¡Correcto!")
                puntaje+=1
                break
            else:
# Si el usuario no responde correctamente después de 2 intentos, 
# # se muestra la respuesta correcta
                puntaje+=-0.5
        else:
            print("Respuesta no valida")
            sys.exit(1)
    else: 
        print("Incorrecto. La respuesta correcta es: ")
        print(opciones[respuesta])

# Se imprime un blanco al final de la pregunta
print()
print("El puntaje final obtenido fue: ",puntaje)