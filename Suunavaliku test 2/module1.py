import module2
import module3
import module4

def run():
    while True:
        print("\n=== MENÜÜ ===")
        print("1) Logi salvestamine")
        print("2) Kalkulaator + Pythagoras")
        print("3) Kolmnurk")
        print("0) Välju")

        v = input("Vali: ").strip()

        if v == "1":
            module2.save()
        elif v == "2":
            module3.start()
        elif v == "3":
            module4.draw()
        elif v == "0":
            print("Head aega!")
            break
        else:
            print("Vale valik!")

