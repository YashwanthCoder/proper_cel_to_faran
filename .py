print ("  Celcius | Fahrenheit")
print("-"*20)
for celcius in range(0,100+1,10):
    fahrenheit = ((celcius*(9/5))+32)
    print("{:>7} C | {:>9.2f} F".format(celcius,fahrenheit))
