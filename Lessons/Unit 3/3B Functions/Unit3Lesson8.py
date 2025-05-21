import math

def wc(TdegC: float, windKPH: float) -> float:
    """
    Calculates the wind chill, given
    TdegC: the temp in degrees C
    windKPH: the wind speed in km/h

    Returns:
    vTemp: Wind chill in degrees C
    """
    vTemp = 13.12 + 0.6215 * TdegC - 11.37 * math.pow(windKPH, 0.16) + 0.3965 * TdegC * math.pow(windKPH, 0.16)
    return vTemp

def risk_level(wind_chill: float) -> str:
    if wind_chill >= 0:
        return "No risk"
    elif 0 > wind_chill >= -9:
        return "Low risk"
    elif -10 >= wind_chill >= -27:
        return "Moderate risk of hypothermia"
    elif -28 >= wind_chill >= -39:
        return "High risk of frostbite"
    elif -40 >= wind_chill >= -47:
        return "Severe risk of frostbite: exposed skin freezes in 5-10 minutes"
    elif -48 >= wind_chill >= -54:
        return "Severe risk of frostbite: exposed skin freezes in 2-5 minutes"
    else:  # below -55
        return "Extreme risk: exposed skin freezes in under 2 minutes"

# Main program
temps_and_winds = [(-5.0, 10.0), (-20.0, 20.0), (-45.0, 40.0)]

for T, W in temps_and_winds:
    wc_value = wc(T, W)
    print("WC=%8.3f T=%8.3f W=%6.3f km/h" % (wc_value, T, W))
    print(risk_level(wc_value))
