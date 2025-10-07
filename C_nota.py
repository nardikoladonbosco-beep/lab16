def ne_interval_0_10(v: float) -> bool:
    return 0 <= v <= 10

def pesho_notat(p1: float, p2: float, provim: float) -> float:
    if not (ne_interval_0_10(p1) and ne_interval_0_10(p2) and ne_interval_0_10(provim)):
        return -1
    return p1 * 0.3 + p2 * 0.3 + provim * 0.4

def etiketa(mes: float) -> str:
    if mes < 5:
        return 'Dobët'
    elif mes < 7:
        return 'Mjaftueshëm'
    elif mes < 9:
        return 'Mirë'
    else:
        return 'Shkëlqyeshëm'

def nota_finale(p1: float, p2: float, provim: float) -> tuple:
    mes = pesho_notat(p1, p2, provim)
    if mes == -1:
        return (-1, "")
    mes_rounded = round(mes, 2)
    return (mes_rounded, etiketa(mes_rounded))

# Main
try:
    p1 = float(input("p1: "))
    p2 = float(input("p2: "))
    provim = float(input("provim: "))

    mes, etik = nota_finale(p1, p2, provim)

    if mes == -1:
        print("Gabim")
    else:
        print(f"Mes: {mes:.2f} | Etiketa: {etik}")
except:
    print("Gabim")
