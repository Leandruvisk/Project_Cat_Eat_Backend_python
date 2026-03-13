from argon2 import PasswordHasher

ph = PasswordHasher()

my_password = "minha_senha"

hash_password = ph.hash(my_password)

print("hashed password: ", hash_password)