def processing(cadena):
    cadena.split()
    print(cadena)


def clean_country (country):
    """Solamente probando cosas"""

    if country is None:
        return None
    
    clean_country = country.strip().capitalize()
    if clean_country in ["Argentina","Bolivia","Chile"]:
        return clean_country
    else:
        return "Resto del mundo"
    
def clean_email(email):
    """Sigo probando"""

    email = email.lower().strip()
    if email and "@" in email:
        return email
    else:
        return None
    

def clean_data(dataset):
    """Limpia los datos del dataset"""
    for data in dataset:
        data["emial"] = clean_email(["email"])
        data["country"] = clean_country(["country"])
    return dataset 

from . import clean_data, clean_country, clean_email