#IMPORTAR FUNCIONES SI MAIN FUERA DE LA CARPETA SRC
from cleaner import clean_data


dataset = [
        { "name": "Carlos",
         "age": "25",
         "email":"carlos@example.com",
         "country":"argentina",
         }
        ]


print(clean_data(dataset))
