height = float(input("your height (cm)  :"))
print(height )

weight = float(input("your weight (kg)  :"))
print(weight )

#BMI = mass (kg) / (height(m) x height(m)
print("Body Mass Index")
BMI = (weight)/((height*0.01)*(height*0.01))

print(BMI)

if BMI<16:
    print("weight loss")
elif 16<=BMI<18.5 :
    print("Lack of weight")
elif 18.5<=BMI<25 :
    print("normally")
elif 25<=BMI<=30 :
    print("Overweight")
else :
    print("Obesity") 
print("done!")                   


