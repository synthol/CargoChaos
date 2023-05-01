import sys
import os

def resource_path(relative_path):
  if hasattr(sys, "_MEIPASS"):
    return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath("."), relative_path)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
SPEED = 5
INITIAL_SCORE = 0
VEHICLE_IMG = resource_path(os.path.join("assets", "img", "vehicle.png"))
OBSTACLE_IMG = resource_path(os.path.join("assets", "img", "obstacle.png"))
ROAD_IMG = resource_path(os.path.join("assets", "img", "road.png"))
CARGO_IMG = resource_path(os.path.join("assets", "img", "cargo.png"))
DELIVERY_IMG = resource_path(os.path.join("assets", "img", "delivery.png"))