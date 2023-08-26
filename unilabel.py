import pygame.font

class UniversalLabel:
    def __init__(self, game, msg, width, height, bg_color, text_color, font, size, pos, x, y):
        """Initialize the label's attributes."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Dimensions and properties
        self.width, self.height = width, height
        self.bg_color = bg_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(font, size)

        #  Making the label (had to go thru hell to figure how to make this part universal :D)
        if x == 0 and y == 0:
            # This scenario occurs if the user specified a pos and not x and y coordinates.
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            rect = self.rect # This is for getattr() to do its job
            screen_rect = self.screen_rect # This is for getattr() to do its job
            rect2 = getattr(screen_rect, pos) # This is the equivalent of "self.screen_rect.pos"
            setattr(rect, pos, rect2) # Finally, equalize the two rects (this is just self.rect.pos = self.screen_rect.pos)
        else:
            # This happens if the user wants to use exact coordinates.
            self.rect = pygame.Rect(x, y, self.width, self.height)

        # render
        self.rendermsg(msg)

    def rendermsg(self, msg):
        """Render the label in the requested part of the screen."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw the label to the screen."""
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)