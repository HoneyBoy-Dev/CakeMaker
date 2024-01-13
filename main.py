import pygame
import src.config as config
import src.editor as editor
from libs import cakemaker


while config.running:
    # Close game
    config.update()

    config.screen.fill((255, 127, 80))
    cakemaker.render(editor.obj)#editor.texting.config(text=str(cakemaker.cursor_layer))
    editor.texting.render()
    pygame.display.flip()
    config.clock.tick(60)