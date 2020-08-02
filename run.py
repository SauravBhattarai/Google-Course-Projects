# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:28:23 2020

@author: Saurav
"""
    
#!/usr/bin/env python3
    
import os
import requests
    
directory = "supplier-data/descriptions/"
    
for infile in os.listdir(directory):
        
    f,e = os.path.splitext(infile)
    if e == ".txt":
        image_name = f + ".jpeg"
        fruits_catalog = dict()
        with open(os.path.join(directory, infile), "r") as f:
            count = 1
            for line in f:
                line = line.strip()
                if count == 1:
                    fruits_catalog['name'] = line
                    count += 1
                elif count == 2:
                    fruits_catalog['weight'] = line.strip(" lbs")
                    count += 1
                elif count == 3:
                    fruits_catalog['description'] = line
                    count += 1
            fruits_catalog['image_name'] = image_name

        r = requests.post("http://104.155.186.129/fruits/", json = fruits_catalog)
