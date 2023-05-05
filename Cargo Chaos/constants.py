import sys
import os

WINDOW_WIDTH, WINDOW_HEIGHT, FPS, SPEED, INITIAL_SCORE = 800, 600, 60, 5, 0
temp_resource_path = lambda p: os.path.join(getattr(sys, '_MEIPASS', os.path.abspath('.')), p)
IMG_PATHS = {k: temp_resource_path(os.path.join("assets", "img", f"{k}.png")) for k in ["vehicle", "obstacle", "road", "cargo", "delivery", "boost"]}

def resource_path(relative_path):
  base_path = getattr(sys, '_MEIPASS', os.path.abspath('.'))
  return os.path.join(base_path, relative_path)