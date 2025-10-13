#definir função

def torre(n,t_inicial, t_auxiliar, t_final):
    if n == 0:
        return
    torre(n-1,t_inicial, t_final, t_auxiliar)
    print(f'Mova disco {n} da {t_inicial} para a {t_final}')
    torre(n-1, t_auxiliar, t_inicial, t_final)


n = int(input("Digite o número de discos: "))
t_inicial = "Torre Inicial"
t_auxiliar = "Torre Auxiliar"
t_final = "Torre Destino"
torre(n,t_inicial, t_auxiliar, t_final)
