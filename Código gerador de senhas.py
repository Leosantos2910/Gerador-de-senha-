import random
import string

def gerar_senha(tamanho, maiusculas=True, minusculas=True, numeros=True, especiais=True):
    caracteres = ''
    
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if especiais:
        caracteres += string.punctuation
    
    if not caracteres:
        raise ValueError("Você deve escolher pelo menos um tipo de caractere.")
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


tamanho = int(input("Digite o tamanho da senha: "))
incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
incluir_numeros = input("Incluir números? (s/n): ").lower() == 's'
incluir_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

senha = gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais)
print(f"A senha gerada é: {senha}")
