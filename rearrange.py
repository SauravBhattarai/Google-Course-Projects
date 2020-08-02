# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:15:04 2020

@author: Saurav
"""


import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])    