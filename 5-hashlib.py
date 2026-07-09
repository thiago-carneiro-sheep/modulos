import hashlib

# # 1 - Verificar os algoritmos disponíveis
# print(hashlib.algorithms_available)

# # 2 - Verificar algoritmos de acordo com SO
# print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o SHA256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "Tco_1793".encode()
algorithm.update(message)
print(algorithm.hexdigest())

# 4 - Utilizando o MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())


senha = input("Digite a Senha \n ")
message1 = senha.encode()
senha1 = hashlib.md5()
senha1.update(message1)

if senha1.hexdigest() == md5.hexdigest():
    print("Senha correta")
else:
    print("Senha incorreta")