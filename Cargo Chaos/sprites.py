import pygame
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, IMG_PATHS

class SpriteTemplate(pygame.sprite.Sprite):
  def __init__(self, x, y, img_key, scale=None):
    super().__init__()
    self.image = pygame.image.load(IMG_PATHS[img_key]).convert_alpha()
    if scale: self.image = pygame.transform.scale(self.image, scale)
    self.rect = self.image.get_rect()
    self.rect.x, self.rect.y = x, y

class Vehicle(SpriteTemplate):
  def __init__(self, x, y):
    super().__init__(x, y, "vehicle", (100, 100))
    self.cargo_count, self.max_cargo_count = 0, 3 

  def update(self, x, y):
    self.rect.x, self.rect.y = x, y
    if self.rect.clamp(pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)).size != self.rect.size: self.rect.x, self.rect.y = self.rect.clamp(pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)).topleft

class Obstacle(SpriteTemplate):
  def __init__(self, x, y):
    super().__init__(x, y, "obstacle", (32, 32))

class Road(SpriteTemplate):
  def __init__(self, x, y):
    super().__init__(x, y, "road", (WINDOW_WIDTH, WINDOW_HEIGHT))

class Cargo(SpriteTemplate):
  def __init__(self, x, y):
    super().__init__(x, y, "cargo", (32, 32))

class Delivery(SpriteTemplate):
  def __init__(self, x, y):
    super().__init__(x, y, "delivery")

class Boost(SpriteTemplate):
  def __init__(self, x, y):
    super().__init__(x, y, "boost", (32, 32))