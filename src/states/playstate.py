from random import randint
import pygame
from pygame.color import THECOLORS
from src.functions import Write, make_block, make_pattern, random_color, transition
from src.states.base import Base

class Play(Base):

    def __init__(self) -> None:
        super().__init__()

        # if the game is started
        self.just_started = True

        # current level
        self.level = 1

        # score
        self.score = 0

        # current pattern
        self.current_pattern = make_pattern(randint(1, 5), 40)
        self.moving_blocks = []
        self.current_block_color = random_color()

        for pattern in self.current_pattern:
            block = make_block(pattern, self.current_block_color)
            self.moving_blocks.append(block)

        
        # all blocks
        self.all_blocks = []

    def render(self) -> None:
        
        if self.just_started :
            Write("Level 1", self.levelDisplayer_rect.width // 2, self.levelDisplayer_rect.height // 2, (255, 255, 255), 48,  self.levelDisplayer)
            self.screen.blit(self.levelDisplayer, self.levelDisplayer_rect)

        else:
            for pattern in self.current_pattern:
                print(pattern)
                pygame.draw.rect(self.screen, pattern['color'], (pattern['x'], pattern['y'], pattern['width'], pattern['height']), 5)


    def update(self, params) -> None:

        # game started animation
        if self.just_started:
            try:
                self.levelDisplayer_rect.y = next(self.cordy)
            except StopIteration:
                if self.levelDisplayer_rect.y == self.screen_height // 2- 50:
                    pygame.time.delay(1000)
                    self.cordy = transition(self.levelDisplayer_rect.y, self.screen_height + 50, 30)
                else:
                    self.just_started = False

        self.render() 

    def enter(self, **param) -> None:
        self.screen = param['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = param['gstatemachine']

        self.levelDisplayer =  pygame.Surface([self.screen_width, 100])
        self.levelDisplayer.fill(THECOLORS['skyblue'])
        self.levelDisplayer_rect  =  self.levelDisplayer.get_rect()
        self.levelDisplayer_rect.x = 0
        self.levelDisplayer_rect.y = -100
        
        self.cordy = transition(-100, self.screen_height // 2- 50, 30)