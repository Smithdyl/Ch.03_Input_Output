'''
TEMPERATURE PROGRAM
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test with the following:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: -40

'''

print("Hello welcome to Smith's Fahrenheit to Celsius Converter")
F=int(input("What is the Fahrenheit you would like to convert?"))
print("The celsius is.......",((F-32)*5)/9)
print("Thank you, please come again")


