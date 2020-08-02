# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:28:24 2020

@author: Saurav
"""

#!/usr/bin/env python3

import os                  
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date
            
def generate_report():
    
    today = date.today().strftime("%B %d, %Y")
    
    styles = getSampleStyleSheet()
    
    report = SimpleDocTemplate("/tmp/processed.pdf")
    
    report_title = Paragraph("Processed Update on " + today, styles["h1"])
    empty_line = Spacer(1,20)
    
    directory = "supplier-data/descriptions/"
    
    report_list = [report_title, empty_line]
    
    for infile in os.listdir(directory):
        
        f,e = os.path.splitext(infile)
        
        if e == ".txt":
            with open(os.path.join(directory, infile), "r") as f:
                count = 1
                for line in f:
                    line = line.strip()
                    if count == 1:
                        report_list.append(Paragraph("name"+ ": " + line, styles["BodyText"]))
                        count += 1
                    elif count == 2:
                        report_list.append(Paragraph("weight" + ": " + line, styles["BodyText"]))
                        report_list.append(empty_line)
                        count += 1
        
    report.build(report_list)