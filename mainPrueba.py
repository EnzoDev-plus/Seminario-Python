data = [
        { "name": "Carlos",
         "age": "25",
         "email":"carlos@example.com",
         "country":"argentina",
         },
        ]





def clean_country (country):
    """solamente probando cosas"""

    if country is None:
        return None
    
    clean_country = country.strip().capitalize()
    if clean_country in ["Argentina","Bolivia","Chile"]:
        return clean_country
    else:
        return "Resto del mundo"
