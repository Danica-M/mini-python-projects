def convert(value, scale):
    if scale == "C":
        print(f'{round((value - 32)/1.8,2)}' + " celsius") 
    elif scale == "F":
        print(f'{round((value * 1.8)+32,2)}' +" fahrenheit" )
    else:
        print("you have entered an invalid scale")


while True:
    #Ask user the length of password they prefer
    scale = str(input("Enter the scale that you want to convert to (F-Fahrenheint/C-Celsius): ")).upper()
    value = int(input("Enter the temperature: "))
    convert(value, scale)
    again = str(input("Do you want to convert another? Y/N: "))
    if again.upper() == "N":
        break
