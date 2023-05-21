from os import walk
import pygame as pg

def import_folder(path):
    surfaceList = []

    for _, __, imgFiles in walk(path):
        for img in imgFiles:
            fullPath = f'{path}/{img}'
            imgSurf = pg.image.load(fullPath).convert_alpha()
            surfaceList.append(imgSurf)

    return surfaceList