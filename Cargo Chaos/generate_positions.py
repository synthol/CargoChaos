import random
from constants import WINDOW_WIDTH, WINDOW_HEIGHT

def generate_random_position(ahead_distance, obstacle_sprites, cargo_sprites, delivery_sprites, vehicle, min_distance=100):
  while True:
    x, y = random.randint(0, WINDOW_WIDTH - 32), random.randint(0, WINDOW_HEIGHT - 32)
    too_close = False

    for sprite_group in (obstacle_sprites, cargo_sprites, delivery_sprites):
      for sprite in sprite_group:
        dist = ((sprite.rect.x - x)**2 + (sprite.rect.y - y)**2)**0.5
        if dist < min_distance:
          too_close = True
          break
      if too_close:
        break

    if not too_close and y < vehicle.rect.y - ahead_distance and (
      abs(x - vehicle.rect.x) >= min_distance or abs(y - vehicle.rect.y) >= min_distance
    ):
      return x, y