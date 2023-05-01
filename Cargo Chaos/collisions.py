import pygame

def custom_collision(sprite1, sprite2):
  intersection_rect = sprite1.rect.clip(sprite2.rect)
  intersection_area = intersection_rect.width * intersection_rect.height
  return intersection_area > 800

def handle_collisions(vehicle, obstacle_sprites, cargo_sprites, delivery_sprites):
  obstacle_collision = pygame.sprite.spritecollide(vehicle, obstacle_sprites, False, custom_collision)
  cargo_collision = pygame.sprite.spritecollide(vehicle, cargo_sprites, True)
  delivery_collision = pygame.sprite.spritecollide(vehicle, delivery_sprites, False)
  return obstacle_collision, cargo_collision, delivery_collision