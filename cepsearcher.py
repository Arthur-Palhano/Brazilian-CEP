#cep de teste 37503130
import pycep_correios

def cepSanatize(cep):
    print("Tratando CEP...")

    unexpectedChars = ["-","_"," "]

    for i in range(0,len(unexpectedChars)):
        cep = cep.split(unexpectedChars[i])
        cep = "".join(cep)

    if len(cep) != 8:
        print("ERRO[01] => Desculpe, um CEP só pode possuir 8 caracteres, verifique e tente novamente.")
        cep = "Reinicie o programa"

    return cep

def getInfo(cep):
    info = pycep_correios.get_address_from_cep(cep)
    return info

print("""
#######    ######    #######
###        ###       ###    ##
#######    #####     ### ###
#######    #######   ###
""")

cep = str(input("Digite o CEP => "))
print("")

adress = getInfo(cepSanatize(cep))

print("Endereço Detectado")
print("")
print(f"CEP: {adress['cep']}")
print(f"Bairro: {adress['bairro']}")
print(f"Cidade: {adress['cidade']}")
print(f"Logradouro: {adress['logradouro']}")
print(f"Estado: {adress['uf']}")
print(f"Complemento: {adress['complemento']}")
