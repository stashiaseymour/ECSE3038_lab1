def parallel(resistors):
    total = 0
    for r in resistors:
        total += 1 / r
    effective_resistance = 1 / total
    print(f"{effective_resistance:.3f} ohms") 

# Testing the function
parallel([330, 1000, 2200])
