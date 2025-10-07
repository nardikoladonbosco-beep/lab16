def trim(s: str) -> str:
    return s.strip()

def normalizo_hapesirat(s: str) -> str:
    rezultat = ""
    ishte_hapesire = False
    for c in s:
        if c == " ":
            if not ishte_hapesire:
                rezultat += " "
                ishte_hapesire = True
        else:
            rezultat += c
            ishte_hapesire = False
    return rezultat

def format_card_title(s: str) -> str:
    s = trim(s)
    s = normalizo_hapesirat(s)
    if s == "":
        return ""
    return s[0].upper() + s[1:]

# Main
teksti = input("Teksti: ")
titulli = format_card_title(teksti)
print(f"Titulli: {titulli}")
