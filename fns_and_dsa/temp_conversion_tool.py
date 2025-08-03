# Define global conversion factors at the top
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Implement conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main interaction
def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)  # If this fails, it will raise ValueError

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        elif unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
