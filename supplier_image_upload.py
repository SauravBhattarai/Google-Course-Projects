# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:28:23 2020

@author: Saurav
"""
   
#!/usr/bin/env python3
    
import os
import requests
    
url = "http://104.155.186.129/upload/"
directory = "supplier-data/images/"
    
for infile in os.listdir(directory):
    f,e = os.path.splitext(infile)
    if e == ".jpeg":
        try:
            with open(os.path.join(directory, infile), "rb") as f:
                r = requests.post(url, files = {"file": f})
                if r.status_code != 201:
                    raise Exception('POST error status={}'.format(r.status_code))
        except:
            print("{} could not be uploaded.".format(os.path.basename(infile)))
