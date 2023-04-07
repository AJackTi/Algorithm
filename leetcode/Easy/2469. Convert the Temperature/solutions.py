def convertTemperature(celsius: float) -> list[float]:
    return [float("{:.5f}".format(celsius + 273.15)), float("{:.5f}".format(celsius * 1.80 + 32.00))]