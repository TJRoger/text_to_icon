#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: rogerluo[r@zingfront.com]
# Created At: 2018-06-14 11:39:00
# File: image.py
# desc:
#########################################################################
import os
import pygame
from pygame.locals import *
import csv
import os.path as path

width = 100
height = 100

csv_path = "./csv/animation.csv"
OUT_PATH = "./imgs/"
FONT_PATH = './font/NotoSansMonoCJKsc-Bold.otf'

def generate(name, text):
    #设置字体和字号
    # font = pygame.font.SysFont('STHeitiSC-Light', 64)
    length = len(text)
    if length <= 0:
        print("length is zero for "+name)
        return
    # 64pixel是48磅字体，(48/72)*96
    font_size = min(64, width // length)
    font = pygame.font.Font(FONT_PATH, font_size)
    ftext = font.render(text, True, (100, 100, 100))
    #渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
    # ftext = font.render(text, True, (0, 0, 0),(255, 255, 255, 0))
    #保存图片
    if not path.exists(OUT_PATH):
        os.mkdir(OUT_PATH)
    pygame.image.save(ftext, OUT_PATH + name + ".png")
    #图片保存地址

def csv_2_dict():
    csv_dict = {}
    with open(csv_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            print(row[0])
            print(row[1])
            csv_dict[row[0]] = row[1]
    del csv_dict['name']
    return csv_dict

def main():
    #pygame初始化
    pygame.init()
    csv_dict = csv_2_dict()
    for key, value in csv_dict.items():
        print(key, value)
        generate(key, value)
    #  generate(text)

if __name__ == '__main__':
    main()
# vim: set expandtab ts=4 sts=4 sw=4 :
