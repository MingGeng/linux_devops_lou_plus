#!/usr/bin/env python3

import sys

#input_income = sys.argv[1];
input_list = sys.argv[1:]
income_dict = {}
def get_netincome(input_income): 
    if input_income <= 0:
        return 0
    insure = input_income * (0.08 + 0.02 + 0.005 + 0.06)
    taxing_income = input_income - 3500 - insure
    if taxing_income <= 0:
        return 0

    discount = 0
    rate = 0

    if taxing_income > 80000:
        rate = 0.45
        discount = 13505
    elif taxing_income >= 55000:
        rate = 0.35
        discount = 5505
    elif taxing_income >= 35000:
        rate = 0.3
        discount = 2755 
    elif taxing_income >= 9000:
        rate = 0.25
        discount = 1005
    elif taxing_income >= 4500:
        rate = 0.2
        discount = 555
    elif taxing_income >= 1500:
        rate = 0.1
        discount = 105
    else:
        rate = 0.03
    
    tax = taxing_income*rate - discount

    if tax <= 0:
        return input_income 
    else:
        return input_income - tax

for data in input_list:
    try:
        income_dict[data.split(":")[0]] = int(float(data.split(":")[1]))
    except ValueError:
        print("Parameter Error")
        exit()


for k in income_dict:
    print(k + ":" + format(get_netincome(income_dict[k]), ".2f"))



