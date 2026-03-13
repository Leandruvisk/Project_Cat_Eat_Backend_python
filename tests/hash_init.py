from argon2 import PasswordHasher
import bcrypt
import time

password = 'password123'


t_bcrypy_start = time.time()
bytes = password.encode('utf-8')
salt = bcrypt.gensalt()
hash_bcrypt = bcrypt.hashpw(bytes, salt)
print("hash bcrypt: ", hash_bcrypt)

t_bcrypy_stop = time.time()

ph = PasswordHasher()
hash_argon2 = ph.hash(password)
print("hash argon: ", hash_argon2)


t_bcrypy_argon = time.time()


print("tempo do bcrypt: ", (t_bcrypy_stop - t_bcrypy_start))
print("tempo do argon2: ", (t_bcrypy_argon - t_bcrypy_stop))



# hash bcrypt:  b'$2b$12$Dpz0yHpLX1Fm4TynbE0azuV0BO7FH2uu7OV5L9Hp/tR8ox.34pmLG'
# hash argon:  $argon2id$v=19$m=65536,t=3,p=4$j35J8RgX9RlOZZSTfB8uWA$R2H7ZWIdL+Ri5cOM3PHzYKRu+OM1xstIaN/I0/IUfTc
# tempo do bcrypt:  0.21196961402893066
# tempo do argon2:  0.04369187355041504
