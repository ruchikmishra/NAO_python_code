import pygame
import sys
import sys
from naoqi import ALProxy
import time
import almath
import csv
import pandas as pd


data1 = pd.read_csv('C:/Users/rouge/Generate_BART_GPT2/generated_file.csv')
tts = ALProxy("ALTextToSpeech","192.168.1.132", 9559)
tts.setParameter("speed",85)
tts.say("Hello, My name is TAILS. Welcome to LARRI.")
tts.say("I will be your host today")
tts.say("I will give you a situation and ask questions based on that.")


tts.say("Are you ready?")



# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1200
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("User Interface")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

def myfunc(x):
    return x

# Define button class
class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self, screen, outline=None):
        # Draw button
        pygame.draw.rect(screen, self.color, self.rect, 0)

        # Draw button text
        font = pygame.font.SysFont(None, 20)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        # Check if button is clicked
        if self.rect.collidepoint(pos):
            return True
        return False

# Create buttons
button1 = Button(400, 200, 100, 50, "YES", GRAY)
button2 = Button(600, 200, 100, 50, "NO", GRAY)
button3 = Button(800, 200, 100, 50, "NO RESPONSE", GRAY)

var = myfunc(0)








def create_event(lines_of_text):
# Main loop
##    val=0
    while True:
        # Handle events
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
##                continue
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if button1.is_clicked(pos):
##                        print("Button 1 clicked!")
                        val = myfunc(1)
                        return val
                        
                        
                    elif button2.is_clicked(pos):
##                        print("Button 2 clicked!")
                        val = myfunc(2)
                        return val
                    elif button3.is_clicked(pos):
##                        print("Button 3 clicked!")
                        val = myfunc(3)
                        return val
##            pygame.quit()
        # Clear the screen
        screen.fill(WHITE)

        # Draw buttons
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        font = pygame.font.SysFont(None, 24)
        line_height = font.get_linesize()
        # Draw a line of text
        for i, line in enumerate(lines_of_text):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (screen_width // 2 - text_surface.get_width() // 2, 30 + 1.5*i * line_height))

        # Update the display
        pygame.display.flip()
##        return val

count = 0
i=1
while(i):
    
    n=0
    nr=0
    c=0
    data1 = pd.read_csv('C:/Users/rouge/Generate_BART_GPT2/generated_file.csv')
    contx = data1.values[count][0]
    ques = data1.values[count][1]
    ansa = data1.values[count][2]
    ansb = data1.values[count][3]
    ansc = data1.values[count][4]
    correct_or_not = ["Is it correct now?"]
    contiue_txt = ["Do you want to continue this session? If yes. press Y/y, if not, press N/n: "]
    
    store_val = create_event(contiue_txt)
    ### For asking to continue the sessions ............................
    if store_val == 1 and c==0:
        print(type(store_val))
        print(store_val)
        
    #...... For asking if this content is appropriate for children with ASD.
        text_all = ["Please choose if this is an apropriate example for children with ASD: ",contx,ques+ "? ", "A. "+ansa , "B. "+ansb, "C. "+ansc]
        store_val2 = create_event(text_all)
        if store_val2==int(1):
            tts.say(contx)
            time.sleep(0.4)
            tts.say(ques)
            time.sleep(0.2)
            ans_var = ["Did the child answer correctly?"]
            store_val3 = create_event(ans_var)
            ####.... If the child anwered correctly the first time ..........
            if store_val3==int(1):
                tts.say("Great job! Let's try another example")
                c=1
                count+=1
                
            ### If the child answered incorrectly..............
            elif store_val3==int(2) and n==0:
                tts.say("Let's try again! I will repeat the example and also give you some options to choose from")
                tts.say(contx)
                
                time.sleep(0.4)
                tts.say(ques)
                tts.say("Option A")
                tts.say(ansa)
                time.sleep(0.4)
                tts.say("Option B")
                tts.say(ansb)
                time.sleep(0.4)
                tts.say("Option C")
                tts.say(ansc)
                time.sleep(0.4)
                
                #### If child answered correctly the second time..................
                store_val4 = create_event(correct_or_not)
                if store_val4 == int(1):
                    n=1
                    tts.say("Great Job! Let's continue with more examples")
                    count+=1
                    
                elif store_val4 == int(2):
##                    print("lets try again")
                    n=1
                    tts.say("That is incorrect. But no problem, we have more exciting examples")
                    count+=1

                elif store_val4 == int(3):
##                    print("lets try again")
                    n=1
                    tts.say("No problem, we have more exciting examples")
                    count+=1

            elif store_val3==int(3) and nr==0:
                tts.say("Let me repeat again and also give some options to choose from")
                tts.say(contx)
                time.sleep(0.4)
                tts.say(ques)
                tts.say("Option A")
                tts.say(ansa)
                time.sleep(0.4)
                tts.say("Option B")
                tts.say(ansb)
                time.sleep(0.4)
                tts.say("Option C")
                tts.say(ansc)
                time.sleep(0.4)
                store_val5 = create_event(correct_or_not)
                if store_val5 == int(1):
                    nr=1
                    tts.say("Great Job! Let's continue with more examples")
                    count+=1
                elif store_val5 == int(2):
                    nr=1
                    tts.say("That is incorrect. But no problem, we have more exciting examples")
                    count+=1
                elif store_val5 == int(3):
                    nr=1
                    tts.say("No problem, we have more exciting examples")
                    count+=1
          
        else:
            count+=1
            print("change the example")
    elif store_val==int(2):
        i=0
    elif store_val==int(3):
        i=0




















    
