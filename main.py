import pygame
import sys
import random

pygame.init()
pygame.display.set_caption("Roger window")
try:
    icon = pygame.image.load("test.jpg")
    pygame.display.set_icon(icon)
except Exception as e:
    print(f"Error loading icon: {e}")


clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 600))

font = pygame.font.SysFont("Arial", 24)

square_x = 600
square_y = 400


coin_x = random.randint(10,1150)
coin_y = random.randint(10,550)
score = 0
high_score = 0

enemy_square_x = random.choice([100, 1000])
enemy_square_y = random.choice([100, 500])
enemy_speed = 2 + (1 * score)
enemy_dir_x = random.choice([-1, 1])
enemy_dir_y = random.choice([-1, 1])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if score > high_score:
        high_score = score

    enemy_speed = 2 + (1 * score)
    enemy_square_x += enemy_speed * enemy_dir_x
    enemy_square_y += enemy_speed * enemy_dir_y
    if enemy_square_x <= 10 or enemy_square_x >= 1140:
        enemy_dir_x *= -1
    if enemy_square_y <= 10 or enemy_square_y >= 540:
        enemy_dir_y *= -1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and square_x > 10:
        square_x -= 5
    if keys[pygame.K_RIGHT] and square_x < 1140:
        square_x += 5
    if keys[pygame.K_UP] and square_y > 10:
        square_y -= 5
    if keys[pygame.K_DOWN] and square_y < 540:
        square_y += 5

    player_rect = pygame.Rect(square_x, square_y, 50, 50)
    coin_rect = pygame.Rect(coin_x, coin_y, 50, 50)
    enemy_rect = pygame.Rect(enemy_square_x, enemy_square_y, 50, 50)
    
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_x = random.randint(10,1140)
        coin_y = random.randint(10,540)
    
    if player_rect.colliderect(enemy_rect):
        score = 0

    screen.fill((30,30,30))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 40))

    pygame.draw.rect(screen, (0, 255, 0), player_rect)
    pygame.draw.ellipse(screen, (255, 255, 0), coin_rect)
    pygame.draw.rect(screen, (255, 0, 0), enemy_rect)

    pygame.draw.rect(screen, (255, 122, 255), (0, 0, 1200, 600), 10)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()