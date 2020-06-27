# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 17:11:24 2020

@author: JessicaCabral

JPG to PDF
"""

from PIL import Image

path = 'path'
image1 = Image.open(path + '/file_name.png')
im1 = image1.convert('RGB')
im1.save(path + '/new_file_name.pdf')