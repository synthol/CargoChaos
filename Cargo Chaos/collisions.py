import pygame

def custom_collision(sprite1, sprite2):
  intersection_rect = sprite1.rect.clip(sprite2.rect)
  intersection_area = intersection_rect.width * intersection_rect.height
  return intersection_area > 800

def handle_collisions(vehicle, obstacle_sprites, cargo_sprites, delivery_sprites, boost_sprites):
  return (
    pygame.sprite.spritecollide(vehicle, obstacle_sprites, False, custom_collision),
    pygame.sprite.spritecollide(vehicle, cargo_sprites, True),
    pygame.sprite.spritecollide(vehicle, delivery_sprites, False),
    pygame.sprite.spritecollide(vehicle, boost_sprites, True),
  )