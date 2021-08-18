# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 19:33:19 2021

@author: Joseph Thomas
"""
def reverse(s):
  str = ""
  i=5
  for i in s:
    str = i + str
  return str
s = input("Enter the string ")
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string(using loops) is : ",end="")
print (reverse(s))