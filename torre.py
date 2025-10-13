#definir função

def torre(n,t_inicial, t_auxiliar, t_final):
    if n == 1:
        print(f'mova disco {n} de {t_inicial} para {t_final}')
        return
    torre(n-1,t_inicial, t_final, t_auxiliar)
    print(f'mova disco {n} de {t_inicial} para {t_final}')
    torre(n-1, t_auxiliar, t_inicial, t_final)


n = int(input("Digite o número de discos: "))
t_inicial = "Torre 1"
t_auxiliar = "Torre 2"
t_final = "Torre 3"
torre(n,t_inicial, t_auxiliar, t_final)
