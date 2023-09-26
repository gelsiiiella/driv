#Ito nalang gamitin mo - Oclinaria
import pygame
import sys
import heart_rate
from lib import FunctionLib
from lib import SoundLibrary
from lib import ImageLibrary
import writetotext

#Add achievement button


#Directory Management Variables
current_directory = FunctionLib.current_path()

pygame.init()

# Define colors
purple = (178, 164, 255)
peach = (255, 180, 180)
beige = (255, 222, 180)
yellow = (253, 247, 195)
sage = (121, 172, 120)
maroon = (154, 59, 59)
teal = (33, 156, 144)
blue = (48, 133, 195)
black = (0,0,0)

# Set up display
display_width = 900
display_height = 500

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Driving Simulation")
clock = pygame.time.Clock()

# Load intro background
intro_background = pygame.image.load(current_directory+"intro_bg.jpg")

# Load fonts
font = pygame.font.Font(None, 60)

# Button class
class Button:
    def __init__(self, text, x, y, width, height, inactive_color, active_color, action=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.action = action

    def draw(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            pygame.draw.rect(gameDisplay, self.active_color, (self.x, self.y, self.width, self.height))
            if click[0] == 1 and self.action is not None:
                self.action()
        else:
            pygame.draw.rect(gameDisplay, self.inactive_color, (self.x, self.y, self.width, self.height))

        text_surface = font.render(self.text, True, (0, 0, 0))
        gameDisplay.blit(text_surface, (self.x + 10, self.y + 10))

# Function to start the game setup process
def start_game_setup():
    global setup_step
    setup_step = 1  # Initialize the setup step to 1
    FunctionLib.writetosave("1\n2\n3\n4\n5")
    print(1+int(FunctionLib.readfromsave(3)))
    print("Game setup started.")

# Function to proceed to the next setup step
def next_setup_step():
    global setup_step
    setup_step += 1
    print(f"Setup Step {setup_step}")

# Function to start Continuous Play
def continuous_play():
    print("Continuous Play")

# Function to start Story Mode
def story_mode():
    print("Story Mode")

def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    gameDisplay.blit(text_surface, (x, y))
username = ""
input_box = pygame.Rect(300, 200, 200, 40)
active = False
text = ""

# Initialize setup step
setup_step = 0

# Create buttons
start_button = Button("Start", 350, 250, 200, 60, teal, blue, start_game_setup)
exit_button = Button("Exit", 350, 350, 200, 60, teal, blue, pygame.quit)
next_button = Button("Next", 350, 350, 200, 60, teal, blue, next_setup_step)
play_button = Button("Play", 350, 350, 200, 60, teal, blue, continuous_play)  # For selecting game mode

# Main menu loop
def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Display intro background
        gameDisplay.blit(intro_background, (0, 0))

        if setup_step == 0:
            # Display game title
            text = font.render("DRIVING SIMULATOR", True, (0, 0, 0))
            gameDisplay.blit(text, (250, 80))

            # Draw "Start" and "Exit" buttons
            start_button.draw()
            exit_button.draw()
        elif setup_step == 1:
            # Display username input here
            display_text("Enter Username:", black, 300, 200)
            #Username data could be sent to gameplay loop file for display purposes or for scoring system
            # Draw "Next" button
            next_button.draw()
        elif setup_step == 2:
            # Display character selection here
            display_text("Choose Your Character:", black, 250, 150)
            #Could be sent to gameplay loop file for scoring system
            # Draw "Next" button
            next_button.draw()
        elif setup_step == 3:
            # Display game mode selection here
            #Story and Play Mode
            #Story has 5 stages; Increasing difficulty; Increasing obstacles
            #Play mode is continuous; 

            display_text("Select Game Mode:", black, 300, 200)
            # Draw "Play" button
            play_button.draw()

        pygame.display.update()

intro_loop()

#Add a list containing Stage Unlocked, Play Mode Highscore, Username
#[username, 1, 0]
