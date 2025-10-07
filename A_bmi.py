def valido_pozitiv(x: float) -> bool:
    return x > 0

def llogarit_bmi(pesha_kg: float, gjatesia_m: float) -> float:
    if not (valido_pozitiv(pesha_kg) and valido_pozitiv(gjatesia_m)):
        return -1
    return pesha_kg / (gjatesia_m ** 2)

def kategorizo_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return 'Nën peshë'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Mbi peshë'
    else:
        return 'Obez'

# Main
try:
    pesha = float(input("Pesha (kg): "))
    gjatesia = float(input("Gjatësia (m): "))
    bmi = llogarit_bmi(pesha, gjatesia)

    if bmi == -1:
        print("Gabim")
    else:
        print(f"BMI: {round(bmi, 2)} - {kategorizo_bmi(bmi)}")
except:
    print("Gabim")
