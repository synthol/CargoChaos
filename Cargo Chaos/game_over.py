import pygame
import sys
import os
from constants import resource_path, WINDOW_WIDTH, WINDOW_HEIGHT, INITIAL_SCORE

def draw_game_over_screen(screen, game_over_text, score_text, restart_button, exit_button, restart_text, exit_text, mouse_pos):
  screen.fill((50, 50, 50))
  screen.blit(game_over_text, (WINDOW_WIDTH // 2 - 70, WINDOW_HEIGHT // 2 - 50))
  screen.blit(score_text, (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 20))

  if restart_button.collidepoint(mouse_pos):
    pygame.draw.rect(screen, (130, 130, 130), restart_button)
  else:
    pygame.draw.rect(screen, (100, 100, 100), restart_button)
  if exit_button.collidepoint(mouse_pos):
    pygame.draw.rect(screen, (130, 130, 130), exit_button)
  else:
    pygame.draw.rect(screen, (100, 100, 100), exit_button)

  screen.blit(restart_text, (restart_button.x + restart_button.width // 2 - restart_text.get_width() // 2, restart_button.y + restart_button.height // 2 - restart_text.get_height() // 2))
  screen.blit(exit_text, (exit_button.x + exit_button.width // 2 - exit_text.get_width() // 2, exit_button.y + exit_button.height // 2 - exit_text.get_height() // 2))
  pygame.display.flip()

def handle_game_over_events():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      return pygame.mouse.get_pos()
  return None

def show_game_over_screen(score_ref, screen, font, vehicle):
  game_over = True
  game_over_text = font.render("Game Over!", True, (255, 255, 255))
  score_text = font.render(f"Score: {score_ref[0]}", True, (255, 255, 255))
  restart_button = pygame.Rect(WINDOW_WIDTH // 2 - 110, WINDOW_HEIGHT // 2 + 30, 100, 30)
  exit_button = pygame.Rect(WINDOW_WIDTH // 2 + 10, WINDOW_HEIGHT // 2 + 30, 100, 30)
  restart_text = font.render("Restart", True, (255, 255, 255))
  exit_text = font.render("Exit", True, (255, 255, 255))

  while game_over:
    mouse_pos = pygame.mouse.get_pos()
    draw_game_over_screen(screen, game_over_text, score_text, restart_button, exit_button, restart_text, exit_text, mouse_pos)
    mouse_pos = handle_game_over_events()
    pygame.mixer.music.set_volume(0.0)
    if mouse_pos is not None:
      if restart_button.collidepoint(mouse_pos):
        score_ref[0] = INITIAL_SCORE
        vehicle.cargo_count = 0
        score_text = font.render(f"Score: {score_ref[0]}", True, (255, 255, 255))
        soundtrack_path = resource_path(os.path.join("assets", "sound", "soundtrack.wav"))
        pygame.mixer.music.load(soundtrack_path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        return
      elif exit_button.collidepoint(mouse_pos):
        pygame.quit()
        sys.exit()