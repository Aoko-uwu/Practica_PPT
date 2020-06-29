#piedra papel o tijeras

import random
print("Juego de Piedra, Papel o tijeras")
print("Escoje entre Piedra, Papel o Tijeras \n 1.Piedra \n 2.Papel \n 3.Tijeras")
opc_j=int(input())
resj=""
if opc_j==1:
    resj="piedra"
elif opc_j==2:
    resj="papel"
elif opc_j==3:
    resj="tijeras"
         
def opc_pc():
    listaJ=["piedra","papel","tijeras"]
    pc_al=random.choice(listaJ)
    print(pc_al)
    return pc_al
resupc=opc_pc()
def comparacion( rpc):
        if resj==rpc:
            print("Ganaste")
        elif resj!=rpc:
            print("Perdiste")
        
comparacion(resupc)