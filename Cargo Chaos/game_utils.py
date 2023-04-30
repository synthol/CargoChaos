from sprites import Obstacle, Cargo, Delivery
from generate_positions import generate_random_position

def update_score(vehicle, score, delivery_collision, font):
  if hasattr(vehicle, 'cargo_count'):
    if delivery_collision:
      score += vehicle.cargo_count
      vehicle.cargo_count = 0
  return score

def spawn_objects(current_time, spawn_timer, SPAWN_DELAY, obstacle_sprites, cargo_sprites, delivery_sprites, all_sprites, vehicle):
  if current_time - spawn_timer >= SPAWN_DELAY:
    if len(obstacle_sprites) < 6:
      new_obstacle = Obstacle(*generate_random_position(100, obstacle_sprites, cargo_sprites, delivery_sprites, vehicle))
      obstacle_sprites.add(new_obstacle)
      all_sprites.add(new_obstacle, layer=1)
    if len(cargo_sprites) < 3:
      new_cargo = Cargo(*generate_random_position(100, obstacle_sprites, cargo_sprites, delivery_sprites, vehicle))
      cargo_sprites.add(new_cargo)
      all_sprites.add(new_cargo, layer=1)
    if len(delivery_sprites) < 1:
      new_location = Delivery(*generate_random_position(200, obstacle_sprites, cargo_sprites, delivery_sprites, vehicle))
      delivery_sprites.add(new_location)
      all_sprites.add(new_location, layer=1)
  return spawn_timer