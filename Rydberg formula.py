# write a python program to calculate the wavelenghts of emission lines in the spectrum of the Hydrogen atom based on the rydberg formula

R = 1.097e-2


for i in range(1,4,1):
    m = i
    n = m + 1
    print("for value of m = " + str(m) + ", value of n = " + str(n))
    wavelength_inverse = R*((1/(m**2))-(1/(n**2)))
    wavelength = 1/(wavelength_inverse)
    print("wavelength inverse : " + str(wavelength_inverse))
    print("wavelength : " + str(wavelength))
    print("")
    
    
    
