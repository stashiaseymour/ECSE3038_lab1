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
