import math

def hx(TdegC: float, dewPtC: float) -> float:
    """
    Calculates the humidex, given
    TdegC: the temp in degrees C
    dewPtC: the dewpoint in degrees C

    Returns:
    hTemp: humidex in degrees C
    """
    p = 5417.753 * (1 / 273.15 - 1 / (273.15 + dewPtC))
    hTemp = TdegC + (5/9) * (6.11 * math.exp(p) - 10)
    return hTemp

def humidex_warning(humidex: float) -> str:
    if humidex < 30:
        return "Normal"
    elif 30 <= humidex < 39:
        return "Causes some discomfort"
    elif 40 <= humidex < 44:
        return "Causes great discomfort"
    elif 45 <= humidex < 49:
        return "Considered dangerous"
    else:  # humidex >= 50
        return "Heat stroke is very likely"

# Main program (do not modify)
T = 28.0
D = 26.0
h_val = hx(T, D)
print("H=%6.3f T=%6.3f D=%6.3f" % (h_val, T, D))
print(humidex_warning(h_val))

T = 30.0
D = 20.0
h_val = hx(T, D)
print("H=%6.3f T=%6.3f D=%6.3f" % (h_val, T, D))
print(humidex_warning(h_val))

T = 26.0
D = 28.0
h_val = hx(T, D)
print("H=%6.3f T=%6.3f D=%6.3f\n" % (h_val, T, D))
print(humidex_warning(h_val))