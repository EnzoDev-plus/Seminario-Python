def clean_country (country):
    """Solamente probando cosas"""

    if country is None:
        return None
    
    clean_country = country.strip().capitalize()
    if clean_country in ["Argentina","Bolivia","Chile"]:
        return clean_country
    else:
        return "Resto del mundo"