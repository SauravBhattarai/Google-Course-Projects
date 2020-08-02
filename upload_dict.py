# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:08:48 2020

@author: Saurav
"""
#! /usr/bin/env python3

import os
import requests

directory = "<............>"

for file in os.listdir(directory):
    f,e = os.path.splitext(file)
    if e == ".txt":
        feedback_dict = dict()
        with open(os.path.join(directory, file), "r") as f:
            count = 1
            for line.strip() in f:
                if count == 1:
                    feedback_dict['title'] = line
                    count += 1
                elif count == 2:
                    feedback_dict['name'] = line
                    count += 1
                elif count == 3:
                    feedback_dict['date'] = line
                    count += 1
                else:
                    feedback_dict['feedback'] = line
                
            r = requests.post("http://<........>/feedback", json = feedback_dict)