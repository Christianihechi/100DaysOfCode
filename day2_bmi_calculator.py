print('BMI - Body Mass Index Calculator\n')
weight = float(input("What is your weight in kg: "))
height = float(input('What is your height in m: '))
bmi = weight / (height ** 2)
bmi = round(bmi, 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}. You're underweight!")
elif bmi < 25:
    print(f"Your BMI is {bmi}. You have a normal weight!")
elif bmi < 30:
    print(f"Your BMI is {bmi}. You're slightly overweight!")
elif bmi < 35:
    print(f"Your BMI is {bmi}. You're obese!")
else:
    print(f"Your BMI is {bmi}. You're clinically obese!")

