import random
from constants import WINDOW_WIDTH, WINDOW_HEIGHT

def generate_random_position(ahead_distance, obstacle_sprites, cargo_sprites, delivery_sprites, vehicle, min_distance=100, spawn_height_ratio=0.3):
  while True:
    x, y = random.randint(0, WINDOW_WIDTH - 32), random.randint(0, int(WINDOW_HEIGHT * spawn_height_ratio) - 32)
    too_close = any(
      ((sprite.rect.x - x)**2 + (sprite.rect.y - y)**2)**0.5 < min_distance
      for sprite_group in (obstacle_sprites, cargo_sprites, delivery_sprites)
      for sprite in sprite_group
    )
    if not too_close and y < vehicle.rect.y - ahead_distance and (abs(x - vehicle.rect.x) >= min_distance or abs(y - vehicle.rect.y) >= min_distance): return x, y