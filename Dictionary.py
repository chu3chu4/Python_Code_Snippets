# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:30:09 2024

@author: yanwu
"""

cats = {"Jane":16, "Tom":29, "Meow":99}

print (cats["Tom"]) #print the value corresponding to key Tom. expected result = 29
print (cats["Tom"], cats["Meow"]) #print the value corresponding to two keys Tom and Meow. expected result = 29 99

Int_Boolean = {1:True, 2:False, 4:False}
print (Int_Boolean[4])