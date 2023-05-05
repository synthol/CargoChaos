import pygame
import sys
import os
from constants import resource_path, WINDOW_WIDTH, WINDOW_HEIGHT, FPS, SPEED, INITIAL_SCORE
from sprites import Vehicle, Road
from game_utils import update_score, adjusted_spawn_delay, spawn_objects
from collisions import handle_collisions
from game_over import show_game_over_screen

def initialize_game():
  pygame.init()
  screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
  pygame.display.set_caption("Cargo Chaos")
  vehicle = Vehicle(WINDOW_WIDTH // 2 - 32, WINDOW_HEIGHT - 250)
  roads = [Road(0, 0)]
  all_sprites, cargo_sprites, delivery_sprites, obstacle_sprites, boost_sprites = pygame.sprite.LayeredUpdates(), pygame.sprite.LayeredUpdates(), pygame.sprite.LayeredUpdates(), pygame.sprite.LayeredUpdates(), pygame.sprite.LayeredUpdates()
  all_sprites.add(vehicle, layer=2)
  pygame.mixer.init()
  for road in roads: all_sprites.add(road, layer=0)
  return screen, vehicle, all_sprites, cargo_sprites, delivery_sprites, obstacle_sprites, boost_sprites

def render_cargo_text(font, vehicle):
  return font.render(f"Cargo: {vehicle.cargo_count}/{vehicle.max_cargo_count}", True, (240, 65, 65) if vehicle.cargo_count == vehicle.max_cargo_count else (255, 255, 255))

def process_input(keys):
  return -SPEED if keys[pygame.K_LEFT] or keys[pygame.K_a] else SPEED if keys[pygame.K_RIGHT] or keys[pygame.K_d] else 0

def main():
  screen, vehicle, all_sprites, cargo_sprites, delivery_sprites, obstacle_sprites, boost_sprites = initialize_game()
  score, font, clock = INITIAL_SCORE, pygame.font.Font(None, 36), pygame.time.Clock()
  score_text = font.render(f"Score: {score}", True, (255, 255, 255))
  boost_timer = None
  boost_spawn_counter = 0
  spawn_timer, soundtrack_path = pygame.time.get_ticks(), resource_path(os.path.join("assets", "sound", "soundtrack.wav"))
  pygame.mixer.music.load(soundtrack_path)
  pygame.mixer.music.set_volume(0.2)
  pygame.mixer.music.play(-1)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    x_speed = process_input(pygame.key.get_pressed())
    current_time = pygame.time.get_ticks()
    obstacle_collision, cargo_collision, delivery_collision, boost_collision = handle_collisions(vehicle, obstacle_sprites, cargo_sprites, delivery_sprites, boost_sprites)
    if boost_collision and boost_timer is None: boost_timer = current_time + 5000
    if boost_timer is not None and current_time >= boost_timer: boost_timer = None
    h_speed = x_speed if boost_timer is None else x_speed * 2
    vehicle.update(max(0, min(WINDOW_WIDTH - vehicle.rect.width, vehicle.rect.x + h_speed)), vehicle.rect.y)

    if obstacle_collision:
      show_game_over_screen([score], screen, font, vehicle)
      boost_timer = [boost_timer]
      spawn_timer, score = reset_game(vehicle, all_sprites, obstacle_sprites, cargo_sprites, delivery_sprites, boost_sprites, boost_timer)
      boost_timer = boost_timer[0]
      
    if cargo_collision and vehicle.cargo_count < vehicle.max_cargo_count: vehicle.current_cargo = cargo_collision[0]

    if hasattr(vehicle, 'current_cargo'):
      vehicle.cargo_count += 1
      delattr(vehicle, 'current_cargo')

    score = update_score(vehicle, score, delivery_collision)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    cargo_text = render_cargo_text(font, vehicle)
    move_and_remove_obstacles_and_cargos(obstacle_sprites, cargo_sprites, delivery_sprites, boost_sprites, all_sprites)
    spawn_timer = spawn_objects(pygame.time.get_ticks(), spawn_timer, adjusted_spawn_delay(score), obstacle_sprites, cargo_sprites, delivery_sprites, boost_sprites, all_sprites, vehicle)
    draw_game(screen, all_sprites, score_text, cargo_text)
    boost_spawn_counter += 1
    clock.tick(FPS)

def reset_game(vehicle, all_sprites, obstacle_sprites, cargo_sprites, delivery_sprites, boost_sprites, boost_timer):
  spawn_timer, score = pygame.time.get_ticks(), INITIAL_SCORE
  vehicle.rect.x, vehicle.rect.y = WINDOW_WIDTH // 2 - 32, WINDOW_HEIGHT - 250
  obstacle_sprites.empty(), all_sprites.empty(), cargo_sprites.empty(), delivery_sprites.empty(), boost_sprites.empty()
  all_sprites.add(vehicle, layer=2)
  roads = [Road(0, 0)]
  for road in roads: all_sprites.add(road, layer=0)
  boost_timer[0] = None
  return spawn_timer, score

def move_and_remove_obstacles_and_cargos(obstacle_sprites, cargo_sprites, delivery_sprites, boost_sprites, all_sprites):
  for sprite_group in (obstacle_sprites, cargo_sprites, delivery_sprites, boost_sprites):
    for sprite in sprite_group:
      sprite.rect.y += SPEED
      if sprite.rect.y > WINDOW_HEIGHT: sprite_group.remove(sprite), all_sprites.remove(sprite)

def draw_game(screen, all_sprites, score_text, cargo_text):
  screen.fill((50, 50, 50)), all_sprites.draw(screen)
  screen.blit(score_text, (10, 10)), screen.blit(cargo_text, (10, 40))
  pygame.display.flip()

if __name__ == "__main__": main()