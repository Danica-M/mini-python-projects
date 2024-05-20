#function that will calculate the bmi with height and weight parameter from user input
def calculate(h,w):
    #weight divided by height squared
    bmi = w/(h*h)
    #rounding the Bmi into 2 decimal format
    rounded = format(bmi,".2f")
    #if lower than 0 then invalid input will be printed
    if bmi<0 :
        print("looks like you've entered invalid height or weight")
    else:
        if bmi<=16:
            print(f"your BMI is {rounded} & you are severely underweight")
        elif bmi<=18.5:
            print(f"your BMI is {rounded} & you are underweight")
        elif bmi<=25:
            print(f"your BMI is {rounded} & you are Healthy")
        elif bmi<=30:
            print(f"your BMI is {rounded} & you are overweight")
        else: print(f"your BMI is {rounded} & you are severely overweight")


height = float(input("Enter your height in cm: "))
weight = float(input("Enter your height in kg: "))

# dividing height by 100 to get convert it into meter from cm
calculate(height/100, weight)