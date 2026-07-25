
#function to convert C to F
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
#function to convert F to C
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
#function to convert C to K
def celsius_to_kelvin(c):
    return c + 273.15
#function to convert K to C
def kelvin_to_celsius(k):
    return k - 273.15
#function to convert F to K
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15
#function to convert K to F
def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Conversion Map also calls the function
conversion_map = {
    "1": ("Celsius to Fahrenheit", celsius_to_fahrenheit, "°F"),
    "2": ("Fahrenheit to Celsius", fahrenheit_to_celsius, "°C"),
    "3": ("Celsius to Kelvin", celsius_to_kelvin, "K"),
    "4": ("Kelvin to Celsius", kelvin_to_celsius, "°C"),
    "5": ("Fahrenheit to Kelvin", fahrenheit_to_kelvin, "K"),
    "6": ("Kelvin to Fahrenheit", kelvin_to_fahrenheit, "°F"),
}

# main function
def main():
    while True:
        print("\n--- Temperature Converter ---")
        for key, (label, _, _) in conversion_map.items():
            print(f"{key}. {label}")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "7":
            print("Exiting the program. Goodbye!")
            break
        elif choice in conversion_map:
            try:
                value = float(input("Enter the temperature value: "))
                label, func, unit = conversion_map[choice]
                result = func(value)
                print(f"\n{label}: {value:.2f} → {result:.2f} {unit}")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        else:
            print("Invalid choice! Please select a number from 1 to 7.")
    #calling main function
main()
