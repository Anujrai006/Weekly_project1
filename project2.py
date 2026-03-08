#Linear Regression with one independent variable
import pyttsx3
engine=pyttsx3.init()
import numpy as np
x=np.array([1,2,3,4,5]) #independent variable
y=np.array([2,4,6,8,10]) #dependent variable
x_mean=np.mean(x)
y_mean=np.mean(y)
numerator=np.sum((x-x_mean)*(y-y_mean)) #numerator of the slope formula
denominator=np.sum((x-x_mean)**2) #denominator of the slope formula
slope=numerator/denominator
intercept=y_mean-slope*x_mean #intercept of the line
print("the slope of the line is:",slope)
print("the intercept of the line is:",intercept)
print("the equation of the line is: y =",slope,"x +",intercept)
x_predict=float(input("Enter a value of x to predict y:"))
y_predict=slope*x_predict+intercept #predicting the value of y for the given x
print(f"The predicted value of y for x={x_predict} is {y_predict}")
