class Conversion:
    def __init__(self, fahrenheit, pounds, feet, inches):
        self.fahrenheit = fahrenheit
        self.pounds = pounds
        self.feet = feet
        self.inches = inches
    
    def f_to_celsius(self):
        celsius = (5 / 9) * (float(self.fahrenheit) - 32)
        return round(celsius, 2)
    
    def lbs_to_kg(self):
        kg = float(self.pounds) / 2.205
        return round(kg, 2)
    

    def ftin_to_mcm(self):
        ftin = (self.inches / 12) + self.feet
        meters = ftin / 3.281
        cm = (meters - int(meters)) * 100
        return int(meters), cm
