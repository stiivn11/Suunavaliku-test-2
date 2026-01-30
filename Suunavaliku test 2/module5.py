def non_empty(text):
    s = input(text).strip()
    if s == "":
        print("Viga: tühi sisend!")
        return None
    return s

def get_int(text):
