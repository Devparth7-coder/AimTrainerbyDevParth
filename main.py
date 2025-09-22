import pygame
import sys
import random
import math
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

# Colors
BACKGROUND = (20, 20, 35)
TARGET_COLOR = (220, 60, 60)
TARGET_OUTLINE = (255, 200, 200)
TEXT_COLOR = (240, 240, 240)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER = (100, 160, 210)
BUTTON_TEXT = (240, 240, 240)

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2

class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.hovered = False
        
    def draw(self):
        color = BUTTON_HOVER if self.hovered else BUTTON_COLOR
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2, border_radius=10)
        
        font = pygame.font.SysFont('Arial', 24)
        text_surf = font.render(self.text, True, BUTTON_TEXT)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
        
    def check_hover(self, pos):
        self.hovered = self.rect.collidepoint(pos)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    return self.action
        return None

class Target:
    def __init__(self):
        self.radius = 30
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.color = TARGET_COLOR
        self.outline_color = TARGET_OUTLINE
        self.creation_time = time.time()
        self.lifetime = 2.0  # seconds
        
    def draw(self):
        # Draw target with concentric circles
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(screen, self.outline_color, (self.x, self.y), self.radius, 3)
        pygame.draw.circle(screen, self.outline_color, (self.x, self.y), self.radius * 0.6, 3)
        pygame.draw.circle(screen, self.outline_color, (self.x, self.y), self.radius * 0.3, 3)
        
    def is_clicked(self, pos):
        distance = math.sqrt((pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2)
        return distance <= self.radius
    
    def is_expired(self):
        return time.time() - self.creation_time > self.lifetime

class AimTrainer:
    def __init__(self):
        self.state = MENU
        self.score = 0
        self.targets = []
        self.misses = 0
        self.start_time = 0
        self.game_duration = 30  # seconds
        self.spawn_timer = 0
        self.spawn_delay = 1.0  # seconds
        self.difficulty_timer = 0
        self.difficulty_interval = 5  # seconds
        
        # Create buttons
        button_width, button_height = 200, 50
        center_x = WIDTH // 2 - button_width // 2
        
        self.start_button = Button(center_x, HEIGHT // 2, button_width, button_height, "Start Game", self.start_game)
        self.restart_button = Button(center_x, HEIGHT // 2 + 100, button_width, button_height, "Play Again", self.start_game)
        self.menu_button = Button(center_x, HEIGHT // 2 + 170, button_width, button_height, "Main Menu", self.show_menu)
        
    def start_game(self):
        self.state = PLAYING
        self.score = 0
        self.misses = 0
        self.targets = []
        self.start_time = time.time()
        self.spawn_timer = 0
        self.difficulty_timer = 0
        self.spawn_delay = 1.0
        
    def show_menu(self):
        self.state = MENU
        
    def spawn_target(self):
        self.targets.append(Target())
        
    def increase_difficulty(self):
        # Make targets smaller and spawn faster
        self.spawn_delay = max(0.3, self.spawn_delay * 0.85)
        for target in self.targets:
            target.radius = max(15, target.radius * 0.9)
            target.lifetime = max(1.0, target.lifetime * 0.9)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if self.state == MENU:
                action = self.start_button.handle_event(event)
                if action:
                    action()
                    
            elif self.state == PLAYING:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    target_hit = False
                    for target in self.targets[:]:
                        if target.is_clicked(event.pos):
                            self.targets.remove(target)
                            self.score += 1
                            target_hit = True
                            break
                    
                    if not target_hit:
                        self.misses += 1
                        
            elif self.state == GAME_OVER:
                action1 = self.restart_button.handle_event(event)
                action2 = self.menu_button.handle_event(event)
                if action1:
                    action1()
                if action2:
                    action2()
                    
    def update(self):
        if self.state == PLAYING:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            
            # Check if game is over
            if elapsed_time >= self.game_duration:
                self.state = GAME_OVER
                return
                
            # Spawn new targets
            if current_time - self.spawn_timer > self.spawn_delay:
                self.spawn_target()
                self.spawn_timer = current_time
                
            # Increase difficulty over time
            if current_time - self.difficulty_timer > self.difficulty_interval:
                self.increase_difficulty()
                self.difficulty_timer = current_time
                
            # Remove expired targets
            for target in self.targets[:]:
                if target.is_expired():
                    self.targets.remove(target)
                    self.misses += 1
                    
            # Update button hover states
            mouse_pos = pygame.mouse.get_pos()
            if self.state == MENU:
                self.start_button.check_hover(mouse_pos)
            elif self.state == GAME_OVER:
                self.restart_button.check_hover(mouse_pos)
                self.menu_button.check_hover(mouse_pos)
                
    def draw(self):
        screen.fill(BACKGROUND)
        
        if self.state == MENU:
            self.draw_menu()
        elif self.state == PLAYING:
            self.draw_game()
        elif self.state == GAME_OVER:
            self.draw_game_over()
            
        pygame.display.flip()
        
    def draw_menu(self):
        # Title
        title_font = pygame.font.SysFont('Arial', 64, bold=True)
        title_text = title_font.render("AIM TRAINER", True, TEXT_COLOR)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
        
        # Instructions
        instr_font = pygame.font.SysFont('Arial', 24)
        instructions = [
            "Click on targets as quickly as you can!",
            "Smaller targets appear as the game progresses.",
            f"Game duration: {self.game_duration} seconds"
        ]
        
        for i, line in enumerate(instructions):
            instr_text = instr_font.render(line, True, TEXT_COLOR)
            screen.blit(instr_text, (WIDTH // 2 - instr_text.get_width() // 2, HEIGHT // 3 + i * 30))
            
        # Start button
        self.start_button.draw()
        
    def draw_game(self):
        # Draw targets
        for target in self.targets:
            target.draw()
            
        # Draw UI elements
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, self.game_duration - elapsed_time)
        
        # Score and time
        font = pygame.font.SysFont('Arial', 28)
        score_text = font.render(f"Score: {self.score}", True, TEXT_COLOR)
        time_text = font.render(f"Time: {remaining_time:.1f}s", True, TEXT_COLOR)
        accuracy = self.score / (self.score + self.misses) * 100 if (self.score + self.misses) > 0 else 0
        accuracy_text = font.render(f"Accuracy: {accuracy:.1f}%", True, TEXT_COLOR)
        
        screen.blit(score_text, (20, 20))
        screen.blit(time_text, (WIDTH - time_text.get_width() - 20, 20))
        screen.blit(accuracy_text, (WIDTH // 2 - accuracy_text.get_width() // 2, 20))
        
    def draw_game_over(self):
        # Game over text
        font_large = pygame.font.SysFont('Arial', 48, bold=True)
        game_over_text = font_large.render("GAME OVER", True, TEXT_COLOR)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 4))
        
        # Stats
        font = pygame.font.SysFont('Arial', 32)
        score_text = font.render(f"Final Score: {self.score}", True, TEXT_COLOR)
        accuracy = self.score / (self.score + self.misses) * 100 if (self.score + self.misses) > 0 else 0
        accuracy_text = font.render(f"Accuracy: {accuracy:.1f}%", True, TEXT_COLOR)
        
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 3))
        screen.blit(accuracy_text, (WIDTH // 2 - accuracy_text.get_width() // 2, HEIGHT // 3 + 50))
        
        # Buttons
        self.restart_button.draw()
        self.menu_button.draw()
        
    def run(self):
        clock = pygame.time.Clock()
        
        while True:
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(60)

# Create and run the game
if __name__ == "__main__":
    game = AimTrainer()
    game.run()