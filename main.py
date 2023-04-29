import requests
import json
from json import load
from jsonschema import Draft7Validator


with open('schema.json') as sc:
    schema = load(sc)

link = "https://muriloh-barbosa.github.io/requisicao-HTTP/cadastro.json"

http = requests.get(link)
dados = http.json()

print(type(dados))
print(http) #imprime a resposta do Git Pages, retornando o valor 200 está ativo
print(http.json())


nova_lista = json.dumps(dados)

nome      = http.json()['Nome']
sobrenome = http.json()['Sobrenome']
nomeCompleto = nome + " " + sobrenome
def conca():
    if len(nomeCompleto) > 2:
        return True
    else:
        print("Nome completo deve ter pelo menos 2 caracteres.")
        return False

CPF      =  http.json()['CPF']
def numeros():
    if len(CPF) <= 11:
        return True
    else:
        print("Digite um CPF valido!")


endereco =  ['Endereco']
cidade   =  ['Cidade']
estado   =  ['Estado']
telefone =  ['Telefone']
email    =  ['Email']
hospital =  ['Hospital']
matricula=  ['Matricula']
dataCadastro =['DataCadastro']

validator = Draft7Validator(schema)

print(list(validator.iter_errors(nova_lista)))

print([nomeCompleto, CPF.replace('.','').replace('-',''), endereco, cidade, estado, telefone,email, hospital, matricula,dataCadastro])

