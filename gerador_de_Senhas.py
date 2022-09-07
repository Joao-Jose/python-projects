import random
import time

user = input('Bem vindo ao Gerador de Senhas. PRESS ENTER... ')
time.sleep(0.2)

chars = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ012345678910*&@%^,.()?'
numbers = input('\n Quantidades de senhas que você quer gerar: ')
numbers = int(numbers)

length = input('\n Insira o comprimento de suas senhas: ')
length = int(length)

print('=' * 50 + '==')
msg = '\n Aguarde suas senhas estão sendo geradas'
print(msg.center(80))
print('=' * 50 + '==')

for pwd in range(numbers):
    passwords = ''
    for c in range(length):
        time.sleep(0.1)
        passwords += random.choice(chars)
    print(passwords)

print('=' * 50 + '==')
