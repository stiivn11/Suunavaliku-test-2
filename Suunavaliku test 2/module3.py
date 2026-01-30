import math

def start():
    while True:
        print("\n--- Kalkulaator ---")
        print("1) +")
        print("2) -")
        print("3) *")
        print("4) /")
        print("5) Pythagoras")
        print("0) Tagasi")

        v = input("Vali: ")

        if v == "0":
            return
        if v == "5":
            a = float(input("a: "))
            b = float(input("b: "))
            c = math.sqrt(a*a + b*b)
            print("c =", c)
            continue

        x = float(input("1. arv: "))
        y = float(input("2. arv: "))

        if v == "1":
            print("Tulemus:", x + y)
        elif v == "2":
            print("Tulemus:", x - y)
        elif v == "3":
            print("Tulemus:", x * y)
        elif v == "4":
            if y == 0:
                print("Viga: jagamine nulliga!")
            else:
                print("Tulemus:", x / y)
        else:
            print("Vale valik!")

        
