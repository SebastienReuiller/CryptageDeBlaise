#!/usr/bin/env python
import binascii
import argparse

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ. :/'

parser = argparse.ArgumentParser()

parser.add_argument('-k', '--key', help='The key', default='')
parser.add_argument('-m', '--msg', help='The message', default='')
parser.add_argument('--mode', help='The mode : crypt or decrypt', default='decrypt')

args = parser.parse_args()

my_message = args.msg
my_key = args.key

# la cle est hexa (indice 0x), on la remet en alpha numerique pour notre algorithme
if my_key.find('0x') != -1:
    my_key = binascii.unhexlify(my_key.lstrip('0x'))

translated = []
key_index = 0

for letter in my_message:  # parcours du message lettre a lettre
    num = LETTERS.find(letter.upper())
    if num != -1:  # -1 signifie que la lettre n'est pas trouvee dans LETTERS

        gap = LETTERS.find(my_key[key_index])

        if args.mode == 'crypt':
            num += gap  # addition pour crypter
        else:
            num -= gap  # soustraction pour decrypter

        num %= len(LETTERS)  # modulo selon la taille de LETTERS

        # on ajout au message traduit
        translated.append(LETTERS[num])

        # on passe a la lettre suivante de la cle
        key_index += 1
        if key_index == len(my_key):
            key_index = 0
    else:
        # on n'a pas trouve la lettre donc on la remet tel quel
        translated.append(letter)

translated_message = ''.join(translated)

print(translated_message)
