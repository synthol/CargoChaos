import pygame
import random
from sprites import Obstacle, Cargo, Delivery, Boost
from generate_positions import generate_random_position

def update_score(vehicle, score, delivery_collision):
  if hasattr(vehicle, 'cargo_count') and delivery_collision:
    score += vehicle.cargo_count
    vehicle.cargo_count = 0
  return score

def adjusted_spawn_delay(score):
  return max(1000 - score * 10, 100)

def spawn_objects(current_time, spawn_timer, adjusted_spawn_delay, obstacle_sprites, cargo_sprites, delivery_sprites, boost_sprites, all_sprites, vehicle):
  if current_time - spawn_timer < adjusted_spawn_delay: return spawn_timer
  spawn_timer = pygame.time.get_ticks()

  def spawn(sprites, sprite_class, min_spawn_interval, max_spawn_interval):
    if random.randint(min_spawn_interval, max_spawn_interval) != min_spawn_interval: return
    sprite = sprite_class(*generate_random_position(100, obstacle_sprites, cargo_sprites, delivery_sprites, vehicle, spawn_height_ratio=0.3))
    sprites.add(sprite)
    all_sprites.add(sprite, layer=1)

  if len(obstacle_sprites) < 6: spawn(obstacle_sprites, Obstacle, 1, 1)
  if len(cargo_sprites) < 3: spawn(cargo_sprites, Cargo, 1, 1)
  if len(delivery_sprites) < 1: spawn(delivery_sprites, Delivery, 1, 1)
  if len(boost_sprites) < 1 and current_time % 1000 < 10: spawn(boost_sprites, Boost, 1, 1)
  return spawn_timer