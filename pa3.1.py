# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 11:45:22 2026

@author: Sneha
"""
num=int(input("Enter a number:"))        
def factorial(num):
    facto=1
    if (num==0 or num==1):
        facto= 1
    else:
        for i in range(1,num+1):
            facto*=i
    return facto
print(factorial(num))
