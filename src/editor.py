import libs.cakemaker as ck
import pygame
import src.config as config

ck.root = config.screen

obj = {}

texting = ck.Label(text='jaja') 
texting.config(text='no', bg=(255, 0, 0))
texting.hover(text='si')
#obj['button'] = ck.Button(x=120, y=100)
#obj['button2'] = ck.Button(x=100, y=100)