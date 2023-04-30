import pygame
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, VEHICLE_IMG, OBSTACLE_IMG, ROAD_IMG, CARGO_IMG, DELIVERY_IMG

class Vehicle(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load(VEHICLE_IMG).convert_alpha()
    self.image = pygame.transform.scale(self.image, (64, 100))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.cargo_count = 0

  def update(self, x, y):
    old_x = self.rect.x
    old_y = self.rect.y
    self.rect.x = x
    self.rect.y = y

    if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH or self.rect.top < 0 or self.rect.bottom > WINDOW_HEIGHT:
      self.rect.x = old_x
      self.rect.y = old_y

class Obstacle(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load(OBSTACLE_IMG).convert_alpha()
    self.image = pygame.transform.scale(self.image, (32, 32))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Road(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load(ROAD_IMG).convert_alpha()
    self.image = pygame.transform.scale(self.image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Cargo(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load(CARGO_IMG).convert_alpha()
    self.image = pygame.transform.scale(self.image, (32, 32))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Delivery(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load(DELIVERY_IMG).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y