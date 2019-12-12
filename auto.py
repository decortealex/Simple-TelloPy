import pygame
from time import sleep
from app.TEST import Drone

drone = Drone()


drone.video()

drone.takeoff()
drone.forward(0.5)
drone.sleep(5)
drone.land()