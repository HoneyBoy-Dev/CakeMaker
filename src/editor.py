import libs.cakemaker as ck
import pygame
import src.config as config

ck.root = config.screen

obj = {}

obj['label'] = ck.Label(
    text= 'Close',
    gradient= [(255, 255, 255), (62, 156, 188 )], 
    padding = 10,
    border_color= (60, 60, 60),
    border_size=1,
    color=(30, 30, 30),
)



