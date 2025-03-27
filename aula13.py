import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  
        data = response.json()
        
        user = data['results'][0]
        nome = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        pais = user['location']['country']
        
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

gerar_usuario()
