from math import sqrt
from sympy import randprime

MAX_PRIME = 500
MIN_PRIME = 100

def char_from_int(number):
  return chr(number + ord('a') - 1)

def int_from_char(char):
  position = ord(char) - ord('a') + 1
  return int(f"{position:02d}")

def is_prime(number):
  n = number
  prime_flag = 0
  if (n > 1):
    for i in range(2, int(sqrt(n)) + 1):
      if (n % i == 0):
        prime_flag = 1
        break
    if (prime_flag == 0):
      return True
    else:
      return False
  else:
    return False

def get_phi(p, q):
  return (p - 1) * (q - 1)

def find_p_and_q():
  return randprime(MIN_PRIME, MAX_PRIME), randprime(MIN_PRIME, MAX_PRIME)

def find_e(totient):
  number = 1
  while True:
    if is_prime(number) and number < totient and totient % number != 0:
      return number
      break
    else:
      number += 1

def find_d(totient, e, count_aim):
  number = 1
  count_current = 0
  while True:
    if (number * e) % totient == 1:
      if count_current == count_aim:
        return number
        break
      else:
        count_current += 1
        number += 1
        continue
    else:
      number += 1

def generate_keys():
  p, q = find_p_and_q()
  n = p * q
  e = find_e(get_phi(p, q))
  d = find_d(get_phi(p, q), e, 1)
  return ((e, n), (d, n))

def algorithm_encrypt(message, public_key):
  return (message**public_key[0]) % public_key[1]

def algorithm_decrypt(plaintext, private_key):
  return (plaintext**private_key[0]) % private_key[1]

def main_encrypt(message, public_key):
  return_string = ''
  for character in message:
    if character == " ":
      return_string += ": "
      continue
    else:
      character_int = int_from_char(character)
    encrypted = algorithm_encrypt(character_int, public_key)
    return_string += str(encrypted)
    return_string += " "
  return return_string

def main_decrypt(message, private_key):
  return_string = ''
  message_split = message.split(" ")
  for character in message_split:
    if character == ":":
      character_decrypted = " "
    elif character == "":
      continue
    else:
      character_decrypted = char_from_int(
        algorithm_decrypt(int(character), private_key))
    return_string += character_decrypted
    
  return return_string
