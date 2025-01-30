def parallel(resistors):
    total = 0
    for r in resistors:
        total += 1 / r
    effective_resistance = 1 / total
    print(f"{effective_resistance:.3f} ohms") 

# Testing the parallel function
parallel([330, 1000, 2200])

def potential_divider(voltage, resistors):
    total_resistance = sum(resistors)  
    for resistor in resistors:
        voltage_drop = (resistor / total_resistance) * voltage  
        print(f"{voltage_drop:.2f}v")  

# Test the voltage divider function
potential_divider(9, [3000, 1000])



def temperature_check(temperature, unit):
    # Statements with conditions for temperature check in Celsius
    if unit == "C":
        if temperature < 35:
            print("the patient is hypothermic")
        elif temperature > 38:
            print("the patient is hyperthermic")
        else:
            print("the patient's temperature is normal")
    
    # Statements with conditions for temerature check in Fahrenheit
    elif unit == "F":
        if temperature < 95:
            print("the patient is hypothermic")
        elif temperature > 100:
            print("the patient is hyperthermic")
        else:
            print("the patient's temperature is normal")
    
    else:
        print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")

# Test the temperature check 
temperature_check(14, "C")  # "the patient is hypothermic"
temperature_check(37, "C")  # "the patient's temperature is normal"
temperature_check(37, "F")  # "the patient is hypothermic"


