import random
import os
import pygame
from player import Player
from ball import Ball
from enemy import Enemy

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
PLAYER_HEIGHT = 10
PLAYER_WIDTH = 100
PLAYER_X = SCREEN_WIDTH // 2
PLAYER_Y = SCREEN_HEIGHT - PLAYER_HEIGHT

BALL_DIM = 10

E_HEIGHT = 20
E_WIDTH = 50
E_ROWS = 6

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
    def __init__(self):
        self.player = Player(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, RED)
        self.ball = Ball(PLAYER_X, PLAYER_Y - 20, BALL_DIM, BALL_DIM, WHITE)
        self.enemies = [] 
        for y in range(4, 4 + E_ROWS):
            for x in range(SCREEN_WIDTH // E_WIDTH):
                tmp = Enemy(x*E_WIDTH, y*E_HEIGHT, E_WIDTH, E_HEIGHT, (y%250 + 50, x%250 + 50, (y*x)%250 + 50))
                self.enemies.append(tmp)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.ball_move_x = 3
        self.ball_move_y = 3
        self.move_right = False
        self.move_left = False
        self.running = True

    def get_random_color(self):
        return (random.randrange(10,256),
                random.randrange(10,256),
                random.randrange(10,256))

    def draw_player(self):
        pygame.draw.rect(self.screen, self.player.color, self.player.rect)

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.ball.color, self.ball.rect)
    def draw_enemies(self):
        for e in self.enemies:
            pygame.draw.rect(self.screen, e.color, e.rect)

    def move_r(self):
        self.player.move(3)

    def move_l(self):
        self.player.move(-3)

    def move_ai(self):
        if self.ball.x > self.player.x + PLAYER_WIDTH // 2:
            self.move_r()
        else:
            self.move_l()
    def move_ball(self):
        self.ball.move(self.ball_move_x, self.ball_move_y)

    def test_collision(self):
        for e in self.enemies:
            if self.ball.rect.colliderect(e.rect):
                self.ball_move_y *= -1
                self.enemies.remove(e)

        if self.player.rect.colliderect(self.ball.rect):
            #if self.ball.x < self.player.x + PLAYER_WIDTH//2 and self.ball_move_x > 1:
                #self.ball_move_x *= -1
            #if self.ball.x > self.player.x + PLAYER_WIDTH//2 and self.ball_move_x < 0:
                #self.ball_move_x *= -1
            self.ball_move_y *= -1
        if self.ball.x <= 0:
            self.ball_move_x *= -1
        if self.ball.x >= SCREEN_WIDTH-BALL_DIM:
            self.ball_move_x *= -1
        if self.ball.y <= 0:
            self.ball_move_y *= -1
        if self.ball.y > SCREEN_HEIGHT:
            self.running = False

    def play(self):
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        # Set up the display
        pygame.display.set_caption("FLAPPY-BIRD")

        clock = pygame.time.Clock()

        while self.running:
    
            if self.move_left:
                if self.player.x > 0:
                    self.move_l()
            elif self.move_right:
                if self.player.x < SCREEN_WIDTH-PLAYER_WIDTH:
                    self.move_r()

            self.screen.fill(BLACK)
            self.draw_player()
            self.draw_ball()
            self.draw_enemies()
            self.move_ball()
            self.test_collision()
            self.move_ai()
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.running = False
                    if e.key == pygame.K_LEFT:
                        self.move_left = True
                        self.move_right = False
                    if e.key == pygame.K_RIGHT:
                        self.move_right = True
                        self.move_left = False
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_LEFT:
                        self.move_right = False
                        self.move_left = False
                    if e.key == pygame.K_RIGHT:
                        self.move_right = False
                        self.move_left = False
if __name__ == "__main__":
    g = Game()
    g.play()
