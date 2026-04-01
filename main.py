# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
pygame.display.set_caption("Roger's First Game Development")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

font = pygame.font.SysFont("Arial", 32)

square_x = 600
square_y = 300
player_color = (0, 255, 0)
player_movement = 5
boost_timer = 0

score = 0
highscore = 0

coin_x = random.randint(10, 1220)
coin_y = random.randint(10, 660)
coin_color = (255, 255, 0)

# Enemy - Starts with basic speed, as my score climbs, enemy speed increases
# if i touch Enemy, my score will reset to 0, Enemy speed reset
# Goal would be try to beat my own highscore
enemy_square_x = random.randint(10, 1220)
enemy_square_y = random.randint(10, 660)
enemy_color = (255, 0, 0)
enemy_speed = 2 + (1 * score)
enemy_direction_x = random.choice([-1, 1])
enemy_direction_y = random.choice([-1, 1])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    enemy_speed = 2 + (1 * score)
    enemy_square_x += enemy_speed * enemy_direction_x
    enemy_square_y += enemy_speed * enemy_direction_y
    if enemy_square_x <= 10 or enemy_square_x >= 1220:
        enemy_direction_x *= -1
    if enemy_square_y <= 10 or enemy_square_y >= 660:
        enemy_direction_y *= -1

    # RENDER YOUR GAME HERE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and square_x > 10:
        square_x -= player_movement
    if keys[pygame.K_RIGHT] and square_x < 1220:
        square_x += player_movement
    if keys[pygame.K_UP] and square_y > 10:
        square_y -= player_movement
    if keys[pygame.K_DOWN] and square_y < 660:
        square_y += player_movement

    if keys[pygame.K_SPACE] and boost_timer <= 0:
        player_color = (255, 255, 255)
        boost_timer = 2

    if boost_timer > 0:
        player_movement = 20
        boost_timer -= 1
    else:
        player_color = (0, 255, 0)
        player_movement = 5

    score_text = font.render(f"Score: {score}", True, (255, 255, 255)) 
    highscore_text = font.render(f"Highscore: {highscore}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))   
    screen.blit(highscore_text, (10, 42))

    player_rectangle = pygame.Rect(square_x, square_y, 50, 50)
    coin_ellipse = pygame.Rect(coin_x, coin_y, 50, 50)
    enemy_rectangle = pygame.Rect(enemy_square_x, enemy_square_y, 50, 50)

    if score > highscore:
        highscore = score

    if player_rectangle.colliderect(coin_ellipse):
        score += 1
        coin_x = random.randint(10, 1220)
        coin_y = random.randint(10, 660)
    
    if player_rectangle.colliderect(enemy_rectangle):
        score = 0
    
    pygame.draw.ellipse(screen, coin_color, coin_ellipse)
    pygame.draw.rect(screen, player_color, player_rectangle)
    pygame.draw.rect(screen, enemy_color, enemy_rectangle)
    pygame.draw.rect(screen, (255, 120, 255), (0, 0, 1280, 720), 10)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()