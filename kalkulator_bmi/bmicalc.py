def calculate_bmi(weight, height):
    height /= 100
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Masz niedowagę. Rozważ konsultację z dietetykiem."
    elif 18.5 <= bmi < 24.9:
        return "Masz wagę prawidłową. Tak trzymaj!"
    elif 25 <= bmi <= 29.9:
        return "Masz nadwagę. Może warto zwiększyć aktywność fizyczną?"
    else:
        return "Masz otyłość. Warto skonsultować się z lekarzem."

def main():
    print("--- Kalkulator BMI ---")
    try:
        weight = float(input("Podaj swoją wagę (w kg): "))
        height = float(input("Podaj swój wzrost (w cm): "))
        if weight <= 0 or height <= 0:
            print("Waga i wzrost muszą być liczbami dodatnimi.")
            return
        bmi = calculate_bmi(weight, height)
        print(f"Twoje BMI: {bmi:.2f}")
        print(f"Kategoria: {bmi_category(bmi)}")
    except ValueError:
        print("Proszę podać prawidłowe liczby.")

if __name__ == "__main__":
    main()