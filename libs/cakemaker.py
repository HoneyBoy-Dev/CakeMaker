import pygame

root = None

def render(main):
    if main:
        for item in main:
            main[item].render()
    pass

class Label:
    def __init__(self, **kwargs):
        # Propierties default.
        self.cake = None 
        self.text = 'text'
        self.font_size = 14         
        self.font_family = 'Arial'
        self.color = (0, 0, 0)
        self.x = 0
        self.y = 0
        self.anti_aliasing = True
        self.limit_str= 0
        self.bg = None
        self.padding = 0
        self.border_size = 0
        self.border_color = (0, 0, 0)
        self.gradient = None

        self.config(**kwargs)
    
    def config(self, **kwargs):
        self.text = kwargs.get('text', self.text)
        self.font_size = kwargs.get('font_size', self.font_size)
        self.font_family = kwargs.get('font_family', self.font_family)
        self.color = kwargs.get('color', self.color)
        self.x = kwargs.get('x', self.x)
        self.y = kwargs.get('y', self.y)
        self.anti_aliasing = kwargs.get('anti_aliasing', self.anti_aliasing)
        self.limit_str =  kwargs.get('limit_str', self.limit_str)
        self.bg = kwargs.get('bg', self.bg)
        self.padding = kwargs.get('padding', self.padding)
        self.border_size = kwargs.get('border_size', self.border_size)
        self.border_color = kwargs.get('border_color', self.border_color)
        self.gradient = kwargs.get('gradient', self.gradient)

        if self.limit_str:
            self.text = self.text[0:self.limit_str] + '...'

        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.font_render = self.font.render(self.text, self.anti_aliasing, self.color)

        # Position finall
        self.X = self.x + (self.padding / 2)
        self.Y = self.y + (self.padding / 2)

        self.W = self.get_width()
        self.H = self.get_height()

    def hover(self, **kwargs):
        pass

    def get_width(self):
        return self.font_render.get_width() + self.padding
    
    def get_height(self):
        return self.font_render.get_height() + self.padding
    #@staticmethod
    def draw_gradient(self, fc, sc):
        for y in range(self.H):
            r = int(fc[0] - (fc[0] - sc[0]) * y / self.H)
            g = int(fc[1] - (fc[1] - sc[1]) * y / self.H)
            b = int(fc[2] - (fc[2] - sc[2]) * y / self.H)
            pygame.draw.line(root, (r, g, b), (self.x, self.y + y), (self.W + self.x - 1, self.y + y))

    def render(self):
        if self.bg:
            pygame.draw.rect(root, self.bg, (self.x, self.y, self.W, self.H))
        elif self.gradient:
            self.draw_gradient(self.gradient[0], self.gradient[1])

        if self.border_size:
            pygame.draw.rect(root, self.border_color, (self.x, self.y, self.get_width(), self.get_height()), width=self.border_size)

        root.blit(self.font_render, (self.X, self.Y))

class Button:
    def __init__(self, **kwargs):
        # Propierties default.
        self.Text = self.Text()
    def config(self, **kwargs):
        pass
    def render(self, **kwargs):
        pass

class TextBox:
    def __init__(self, **kwargs):
        # Propierties default.
        self.Text = self.Text()
    def config(self, **kwargs):
        pass
    def render(self, **kwargs):
        pass

class MenuBar:
    def __init__(self, **kwargs):
        # Propierties default.
        self.Text = self.Text()
    def config(self, **kwargs):
        pass
    def render(self, **kwargs):
        pass
