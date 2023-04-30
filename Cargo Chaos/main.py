import pygame
import sys
import os
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, SPAWN_DELAY, FPS, SPEED, INITIAL_SCORE
from sprites import Vehicle, Road
from game_utils import update_score, spawn_objects
from collisions import handle_collisions
from game_over import show_game_over_screen

def initialize_game():
  pygame.init()
  screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
  pygame.display.set_caption("Cargo Chaos")
  vehicle = Vehicle(WINDOW_WIDTH // 2 - 32, WINDOW_HEIGHT // 2 - 50)
  roads = [Road(0, 0)]
  all_sprites = pygame.sprite.LayeredUpdates()
  cargo_sprites = pygame.sprite.LayeredUpdates()
  delivery_sprites = pygame.sprite.LayeredUpdates()
  obstacle_sprites = pygame.sprite.LayeredUpdates()
  all_sprites.add(vehicle, layer=2)
  pygame.mixer.init()

  for road in roads:
    all_sprites.add(road, layer=0)
  return screen, vehicle, all_sprites, cargo_sprites, delivery_sprites, obstacle_sprites

def process_input(keys):
  x_speed = 0

  if keys[pygame.K_LEFT] or keys[pygame.K_a]:
    x_speed = -SPEED
  if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    x_speed = SPEED
  return x_speed

def main():
  screen, vehicle, all_sprites, cargo_sprites, delivery_sprites, obstacle_sprites = initialize_game()
  score = INITIAL_SCORE
  font = pygame.font.Font(None, 36)
  score_text = font.render(f"Score: {score}", True, (255, 255, 255))
  clock = pygame.time.Clock()
  spawn_timer = pygame.time.get_ticks()
  soundtrack_path = os.path.join("sound", "soundtrack.wav")
  pygame.mixer.music.load(soundtrack_path)
  pygame.mixer.music.set_volume(0.2)
  pygame.mixer.music.play(-1)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    keys = pygame.key.get_pressed()
    x_speed = process_input(keys)
    new_x = max(0, min(WINDOW_WIDTH - vehicle.rect.width, vehicle.rect.x + x_speed))
    vehicle.update(new_x, vehicle.rect.y)
    obstacle_collision, cargo_collision, delivery_collision = handle_collisions(vehicle, obstacle_sprites, cargo_sprites, delivery_sprites)

    if obstacle_collision:
      show_game_over_screen([score], screen, font, vehicle)
      spawn_timer, score = reset_game(vehicle, all_sprites, obstacle_sprites, cargo_sprites, delivery_sprites)
    if cargo_collision:
      vehicle.current_cargo = cargo_collision[0]
    if hasattr(vehicle, 'current_cargo'):
      vehicle.cargo_count += 1
      delattr(vehicle, 'current_cargo')

    score = update_score(vehicle, score, delivery_collision, font)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    move_and_remove_obstacles_and_cargos(obstacle_sprites, cargo_sprites, delivery_sprites, all_sprites)
    current_time = pygame.time.get_ticks()
    spawn_timer = spawn_objects(current_time, spawn_timer, SPAWN_DELAY, obstacle_sprites, cargo_sprites, delivery_sprites, all_sprites, vehicle)
    draw_game(screen, all_sprites, score_text)
    clock.tick(FPS)

def reset_game(vehicle, all_sprites, obstacle_sprites, cargo_sprites, delivery_sprites):
  spawn_timer = pygame.time.get_ticks()
  score = INITIAL_SCORE
  vehicle.rect.x = WINDOW_WIDTH // 2 - 32
  vehicle.rect.y = WINDOW_HEIGHT // 2 - 50
  obstacle_sprites.empty()
  all_sprites.empty()
  cargo_sprites.empty()
  delivery_sprites.empty()
  all_sprites.add(vehicle, layer=2)
  roads = [Road(0, 0)]

  for road in roads:
    all_sprites.add(road, layer=0)
  return spawn_timer, score

def move_and_remove_obstacles_and_cargos(obstacle_sprites, cargo_sprites, delivery_sprites, all_sprites):
  for sprite_group in (obstacle_sprites, cargo_sprites, delivery_sprites):
    for sprite in sprite_group:
      sprite.rect.y += SPEED
      if sprite.rect.y > WINDOW_HEIGHT:
        sprite_group.remove(sprite)
        all_sprites.remove(sprite)

def draw_game(screen, all_sprites, score_text):
  screen.fill((50, 50, 50))
  all_sprites.draw(screen)
  screen.blit(score_text, (10, 10))
  pygame.display.flip()

if __name__ == "__main__":
  main()