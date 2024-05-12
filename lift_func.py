def test():
    print("test successful")

def is_number(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False

def liftcalc(liftcoeff, density, velocity, wingarea):
    lift = liftcoeff * wingarea * (0.5 * (velocity**2)) * density
    return lift