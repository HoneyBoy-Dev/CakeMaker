import pygame
pygame.init()

root = None
layers = 1
cursor_layer = 0

def render(main):
    global cursor_layer
    if main:
        for item in main:
            main[item].render()

class Label:
    
    def __init__(self, **kwargs):
        # Propierties default.
        global layers, cursor_layer
        self.cake = None
        self.layer = 0
        self.layer += layers
        layers += 1
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
        self.border_radius = -1

        self.isCollision = False
        self.rightClick = False

        self.config(**kwargs)
        self.hover()
        self.active()
    
    def config(self, **kwargs):
        # Change propierties
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
        self.border_radius= kwargs.get('border_radius', self.border_radius)

        if self.limit_str:
            self.text = self.text[0:self.limit_str] + '...'

        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.font_render = self.font.render(self.text, self.anti_aliasing, self.color)
        self.hover(**kwargs)

    def hover(self, **kwargs):
        self.textHover = kwargs.get('text', self.text)
        self.font_sizeHover = kwargs.get('font_size', self.font_size)
        self.font_familyHover = kwargs.get('font_family', self.font_family)
        self.colorHover = kwargs.get('color', self.color)
        self.anti_aliasingHover = kwargs.get('anti_aliasing', self.anti_aliasing)
        self.limit_strHover =  kwargs.get('limit_str', self.limit_str)
        self.bgHover = kwargs.get('bg', self.bg)
        self.paddingHover = kwargs.get('padding', self.padding)
        self.border_sizeHover = kwargs.get('border_size', self.border_size)
        self.border_colorHover = kwargs.get('border_color', self.border_color)
        self.gradientHover = kwargs.get('gradient', self.gradient)
        self.border_radiusHover = kwargs.get('border_radius', self.border_radius)

        self.fontHover = pygame.font.SysFont(self.font_familyHover, self.font_sizeHover)
        self.font_renderHover = self.fontHover.render(self.textHover, self.anti_aliasingHover, self.colorHover)
        
    def active(self, **kwargs):
        self.isActive = False
        self.textActive = kwargs.get('text', self.text)
        self.font_sizeActive = kwargs.get('font_size', self.font_size)
        self.font_familyActive = kwargs.get('font_family', self.font_family)
        self.colorActive = kwargs.get('color', self.color)
        self.anti_aliasingActive = kwargs.get('anti_aliasing', self.anti_aliasing)
        self.limit_strActive =  kwargs.get('limit_str', self.limit_str)
        self.bgActive = kwargs.get('bg', self.bg)
        self.paddingActive = kwargs.get('padding', self.padding)
        self.border_sizeActive = kwargs.get('border_size', self.border_size)
        self.border_colorActive = kwargs.get('border_color', self.border_color)
        self.gradientActive = kwargs.get('gradient', self.gradient)
        self.border_radiusActive = kwargs.get('border_radius', self.border_radius)
        self.command = kwargs.get('command', None)
        self.fontActive = pygame.font.SysFont(self.font_familyActive, self.font_sizeActive)
        self.font_renderActive = self.fontActive.render(self.textActive, self.anti_aliasingActive, self.colorActive)

    def get_width(self):
        self.test = 0
        if self.isCollision:
            self.test= self.font_renderHover.get_width() + self.paddingHover
        else:
            self.test =  self.font_render.get_width() + self.padding
        return self.test
    
    def get_height(self):
        self.test = 0
        if self.isCollision:
            self.test = self.font_renderHover.get_height() + self.paddingHover
        else:
            self.test =  self.font_render.get_height() + self.padding
        return self.test

    def draw_gradient(self, fc, sc):
        for y in range(self.get_height()):
            r = int(fc[0] - (fc[0] - sc[0]) * y / self.get_height())
            g = int(fc[1] - (fc[1] - sc[1]) * y / self.get_height())
            b = int(fc[2] - (fc[2] - sc[2]) * y / self.get_height())
            pygame.draw.line(root, (r, g, b), (self.x, self.y + y), (self.get_width() + self.x - 1, self.y + y))

    def render(self):
        global cursor_layer
        self.hitbox = pygame.Rect(self.x, self.y, self.get_width(), self.get_height())
        self.isCollision =  self.hitbox.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if self.isCollision:
            cursor_layer = self.layer
            self.onMouseOver = True
            cursor_layer = 0

        if pygame.mouse.get_pressed()[0] and not self.rightClick:
            self.rightClick = True
            if self.onMouseOver:
                self.isActive = True
        elif not pygame.mouse.get_pressed()[0] and self.rightClick:
            self.rightClick = False

        if self.isActive and self.bgActive:
            pygame.draw.rect(root, self.bgActive, (self.x, self.y, self.get_width(), self.get_height()), border_radius=self.border_radiusActive)
        elif self.gradientActive and self.isActive:
            self.draw_gradient(self.gradientActive[0], self.gradientActive[1])
        elif self.bgHover and self.isCollision:
            pygame.draw.rect(root, self.bgHover, (self.x, self.y, self.get_width(), self.get_height()), border_radius=self.border_radiusHover)
        elif self.bg:
            pygame.draw.rect(root, self.bg, (self.x, self.y, self.get_width(), self.get_height()), border_radius=self.border_radius)
        elif self.gradientHover and self.isCollision:
            self.draw_gradient(self.gradientHover[0], self.gradientHover[1])
        elif self.gradient:
            self.draw_gradient(self.gradient[0], self.gradient[1])

        if self.border_sizeActive and self.isActive:
            pygame.draw.rect(root, self.border_colorActive, (self.x, self.y, self.get_width(), self.get_height()), width=self.border_sizeActive, border_radius=self.border_radiusActive)
        elif self.border_sizeHover and self.isCollision:
            pygame.draw.rect(root, self.border_colorHover, (self.x, self.y, self.get_width(), self.get_height()), width=self.border_sizeHover, border_radius=self.border_radiusHover)
        elif self.border_size:
            pygame.draw.rect(root, self.border_color, (self.x, self.y, self.get_width(), self.get_height()), width=self.border_size, border_radius=self.border_radius)

        if self.onMouseOver:
            self.X = self.x + (self.paddingHover / 2)
            self.Y = self.y + (self.paddingHover / 2)
        else:
            self.X = self.x + (self.padding / 2)
            self.Y = self.y + (self.padding / 2)

        if self.isActive:
            root.blit(self.font_renderActive, (self.X, self.Y))
        elif self.isCollision:
            root.blit(self.font_renderHover, (self.X, self.Y))
        else:
            root.blit(self.font_render, (self.X, self.Y))

        if self.isActive:
            self.isActive = False
            if self.command:
                self.command()

class Button:
    def __init__(self, **kwargs):
        # Propierties default.
        self.Button = Label(
            **kwargs,
          text='Button',
          border_size=2,
          padding=20,
          border_color= (63, 63, 63),
          gradient= [(215, 215, 215), (83, 93, 196)]
        )
        self.Button.hover(
            gradient= [(83, 93, 196), (215, 215, 215)]
        )
        self.Button.active(
            bg= (83, 93, 196)
        )
    def hover(self, **kwargs):
        self.Button.hover(**kwargs)
    def active(self, **kwargs):
        self.Button.active(**kwargs)
    def config(self, **kwargs):
        self.Button.config(**kwargs)
        pass
    def render(self, **kwargs):
        self.Button.render() 
        pass

class TextBox:
    def __init__(self, **kwargs):
        # Propierties default.
        self.Label = Label()
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
