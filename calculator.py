#!/usr/bin/env python3

import sys

input_income = sys.argv[1];

try:
    input_income = int(float(input_income))
except ValueError:
    print("Parameter Error")   
    exit()

    
taxing_income = input_income - 3500
discount = 0
rate = 0

if taxing_income > 0:
    rate = 0.3
else:
    taxing_income = 0


if taxing_income > 80000:
    rate = 0.45
    discount = 13505
elif taxing_income > 55000:
    rate = 0.35
    discount = 5505
elif taxing_income > 35000:
    rate = 0.3
    discount = 2755 
elif taxing_income > 9000:
    rate = 0.25
    discount = 1005
elif taxing_income > 4500:
    rate = 0.2
    discount = 555
elif taxing_income > 1500:
    rate = 0.1
    discount = 105
else:
    rate = 0.03

print(format(taxing_income*rate - discount, ".2f"))




