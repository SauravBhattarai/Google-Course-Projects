# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:28:21 2020

@author: Saurav
"""
                    
#!/usr/bin/env python3

import os
from PIL import Image

directory = "supplier-data/images/"
size = (600,400)

for infile in os.listdir(directory):
    f,e = os.path.splitext(infile)
    if e == ".tiff":
        infile = os.path.join(directory, infile)
        file = f + ".jpeg"
        outfile = os.path.join(directory, file)
        if infile != outfile:
            try:
                with Image.open(infile) as im:
                    new_im = im.resize(size)
                    new_im.convert("RGB").save(outfile, "JPEG")
            except:
                print("{} could not be converted.".format(os.path.basename(infile)))