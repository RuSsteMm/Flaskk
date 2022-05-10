# -*- coding: utf-8 -*-

import os


def putb():
    p = os.path.abspath('main.py')
    path = '\\'.join(p.split(f'\\')[:-1]) + '\\static\\img'
    print(path)
    filelist = []

    for root, dirs, files in os.walk(path):
        for file in files:
            filelist.append(os.path.join(root, file))

    for i in range(len(filelist)):
        filelist[i] = '/'.join(filelist[i].split('\\')[5:])

    return filelist
