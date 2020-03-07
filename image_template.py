#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: rogerluo[r@zingfront.com]
# Created At: 2018-06-14 15:02:07
# File: image_template.py
# desc:
#########################################################################
import os
from PIL import Image
import os.path as path


template = "./background/act_bg.png"
img_dir = "./imgs/"
img_out = "./imgs/out/"

def process(filename):
    print("processing ", filename, "---")
    image = Image.open(img_dir+filename, 'r')
    img_w, img_h = image.size
    background = Image.open(template)
    # background = Image.new('RGBA', (240, 150), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(image, offset, image)
    # background.blend(image, offset)
    if not path.exists(img_out):
        os.mkdir(img_out)
    background.save(img_out + filename)
    print("done processing ", filename)

def main():
    filelist = os.listdir(img_dir)
    for filename in filelist:
        if filename.endswith('.png'):
            process(filename)

if __name__ == '__main__':
    main()

# vim: set expandtab ts=4 sts=4 sw=4 :
