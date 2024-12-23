

"""
def mostra_o_doubro(num):
    return 2*num
resultado = mostra_o_doubro(num=int(input(f"\nEnter a number: ")))

print(resultado)


def data(dia=1, mes=1, ano=2024):
    return f"{dia} de {str(mes)} de {ano}"


leitura_data = data(dia=int(input("\nEnter the day: ")), mes=int(input(f"\nEnter the month: ")),
                    ano=int(input(f"\nEnter the year: ")))

print(leitura_data)
"""
import requests

url = "https://desafio-endpoint-hashcode-n2.onrender.com/passo3"
headers = {"Content-Type": "application/json"}
data = {
    "cpf": "098.730.491-77",  # Substitua pelo seu CPF
    "respostaQuestaoObjetiva": "6"
}

response = requests.post(url, json=data, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.json())
