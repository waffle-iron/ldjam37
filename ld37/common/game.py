import pygame, sys
from pygame.locals import *
from ld37.common.constants import Colors
from ld37.common.startupactivities import *
from ld37.display.camera import Camera
from ld37.common.utils.libutils import update_image_rect

class Ldjam:
    def __init__(self, title):
        pygame.init()
        pygame.display.set_caption(title)
        self.window_d = (800, 600)
        self.screen = pygame.display.set_mode(self.window_d)

    def setup(self):
        self.clock = pygame.time.Clock()
        self.master_entity_list = create_starting_entities()
        self.camera = Camera(self.window_d[0], self.window_d[1], 1600, 1200)

    def play(self):
        pc = self.get_playable_entity()
        while not pc.done:
            # Set up tick
            pc = self.get_playable_entity()
            game_time = self.clock.tick(45)
            self.screen.fill(Colors.WHITE)

            # update
            for entity in self.master_entity_list:
                entity.update(game_time)
            self.camera.update(pc)

            # display
            for entity in [x for x in self.master_entity_list if x.is_displayable]:
                update_image_rect(entity.image, entity.rect)
                self.screen.blit(entity.image, self.camera.apply(entity))

            pygame.display.flip()
        pygame.quit()

    def get_playable_entity(self):
        return next(iter([x for x in self.master_entity_list if x.is_current_player_controllable]), None)
