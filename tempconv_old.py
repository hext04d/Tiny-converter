
def f_to_c_conv(f): #converts fahrenheit to celsius
    celsius = (5/9) * (float(f)-32)
    result = round (celsius,2)
    return float(result)

def lbs_to_kg(lbs):#converts lbs to kg
    kg = (float(lbs)) / 2.205
    return float(round(kg, 2))

def ftin_to_mcm(ft, inch):#converts feet and inch to meters and centimeters
    ftin = (inch / 12) + ft
    mtrs = ftin / 3.281
    cm = (mtrs - int(mtrs)) * 100  # Calculate remaining centimeters
    return int(mtrs), cm  # Return meters and centimeters as a tuple
