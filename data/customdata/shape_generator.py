#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:40:39 2020

@author: rameshveer
"""

import PIL.Image as image

files = ["train.txt", "test.txt"]

for file in files:
    finp = open(file, 'r')
    with open(file.split(".")[0] + ".shapes", 'w') as fout:
        
        i = 0
        
        for line in finp.readlines():
            line = line.replace("./data/customdata", ".")
            line = line.replace("\n", "")
            
            try:    
                img = image.open(str(line))
            except OSError as e:
                print(e.errno)

            width, height = img.size
            o_line = str(width) + " " + str(height)
            fout.write("%s\n" % o_line)
                
            i += 1
            
        print("Generated shapes for " + str(i) + " " + file.split(".")[0] + " images!")
        print("Generated shapes for " + str(i) + " " + file.split(".")[0] + " images!")