import pygame
from game import launch_local
from client import launch_client

pygame.init() 



def main():
    """
    main method of the program.
    """
    while True:
        winner_screen(start_menu())


if __name__ == "__main__":
    main()