import pygame, random, time

pygame.init()

window_size = 700
screen = pygame.display.set_mode((window_size, window_size))

center = int(window_size/2)

pygame.display.set_caption("Window")

red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 175, 0)
black = (0, 0, 0)
white = (255, 255, 255)

font = pygame.font.SysFont("Times New Roman", 40)
small_font = pygame.font.SysFont("Times New Roman", 30)
smaller_font = pygame.font.SysFont("Times New Roman", 20)
big_font = pygame.font.SysFont("Arial", 70)

def init_round_text(n) :
    text = font.render("Round "+str(n), True, white)
    return text, text.get_width()

round_number = 1
round_text, round_text_width = init_round_text(round_number)
space_text = font.render("Press Space Key to Continue", True, white)
space_text_width = space_text.get_width()

round_screen = True
first_round = False
guess = False

correct = False
incorrect = False

end_report = False


guess_text1 = small_font.render("Was the colored dot shorter or longer than the rest?", True, white)

guess_text2 = small_font.render("Press 'S'", True, white)

guess_text3 = small_font.render("Press 'L'", True, white)

guess_text4 = big_font.render("?", True, red)

guess_text5 = small_font.render("for shorter", True, white)

guess_text6 = small_font.render("for longer", True, white)

increment = 75


correct_text = big_font.render("CORRECT!", True, green)
incorrect_text = big_font.render("INCORRECT", True, red)

index = [[green, -1], [green, 1], [red, -1], [red, 1], [green, -1], [green, 1], [red, -1], [red, 1]]
colors_and_times = []

for times in range(2) :
    selection = list(range(8))
    while selection != [] :
        choic = random.choice(selection)
        colors_and_times.append(index[choic])
        selection.remove(choic)

index = [[green, 1], [green, 1], [red, 1], [red, 1], [green, 1], [green, 1], [red, 1], [red, 1]]

selection = list(range(8))
while selection != [] :
    choic = random.choice(selection)
    colors_and_times.append(index[choic])
    selection.remove(choic)

#print(colors_and_times, len(colors_))

for cat_i, cat in enumerate(colors_and_times) :
    print(cat_i, cat)
#quit()

current_cat = colors_and_times[round_number-1]


results_text = font.render("RESULTS", True, white)
results_text_width = results_text.get_width()

list_texts = [smaller_font.render(str(x+1), True, white) for x in range(24)]

round_text2 = smaller_font.render("ROUND", True, white)
dot_color_text = smaller_font.render("Dot Color", True, white)
dot_color_x = round_text2.get_width()+65
los_text = smaller_font.render("Longer or Shorter", True, white)
los_x = dot_color_x+dot_color_text.get_width()+65
guess_text = smaller_font.render("Guess", True, white)
guess_x = los_x+los_text.get_width()+65
correct_question_text = smaller_font.render("Correct?", True, white)
correct_x = guess_x+guess_text.get_width()+65

g_or_r = dot_color_x+int((dot_color_text.get_width()/2))-8
l_or_s1 = los_x+int((los_text.get_width()/2))-6
l_or_s2 = guess_x+int((guess_text.get_width()/2))-6
y_or_n = correct_x+int((correct_question_text.get_width()/2))-8

r_text = smaller_font.render("R", True, red)
g_text = smaller_font.render("G", True, green)
l_text = smaller_font.render("L", True, white)
s_text = smaller_font.render("S", True, white)
y_text = smaller_font.render("Y", True, white)
n_text = smaller_font.render("N", True, white)

while True :
    while round_screen :
        screen.fill(black)
        screen.blit(round_text, (int((window_size-round_text_width)/2), 0))
        screen.blit(space_text, (int((window_size-space_text_width)/2), 300))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    round_screen = False
                    first_round = True

                    rando = 0.5 #random.randint(300, 500)

                    """
                    dot_fps = int((rando/1000)*fps)
                    dot_times = 0
                    on = False
                    limit = 4

                    white_on = True

                    count = 0
                    #print("WHITE DOT MILLISECONDS: ", rando, dot_fps)
                    #print()
                    """
        pygame.display.update()
    if first_round :
        for lim in range(4) :
            screen.fill(black)
            pygame.draw.circle(screen, white, (center, center), 40)
            pygame.display.update()
            time.sleep(rando)

            screen.fill(black)
            pygame.display.update()
            time.sleep(rando)

        screen.fill(black)
        colored_color = current_cat[0]
        colored_plus_or_minus = rando+((current_cat[1]*increment)/1000)
        print(colored_plus_or_minus)
        pygame.draw.circle(screen, colored_color, (center, center), 40)
        pygame.display.update()
        time.sleep(colored_plus_or_minus)
        screen.fill(black)
        pygame.display.update()
        time.sleep(colored_plus_or_minus)
        first_round = False
        guess = True

    """
    while first_round :
        screen.fill(black)
        
        count += 1
        if count == dot_fps :
            if on :
                on = False
                if dot_times == limit and white_on :
                    colored_plus_or_minus = rando+((current_cat[1]*increment)/1000)
                    
                    dot_fps = int((colored_plus_or_minus/1000)*fps)

                    #print("COLORED DOT MILLISECONDS: ", colored_plus_or_minus, dot_fps)
                    dot_times = 0
                    on = False
                    white_on = False
                    colored_color = current_cat[0]
                    limit = 1
                    
                    
            else :
                on = True
                dot_times += 1
                if dot_times == limit+1 and not white_on :
                    guess = True
                    first_round = False
            count = 0
        clock.tick(fps)
        if first_round :
            if on :
                if white_on :
                    pygame.draw.circle(screen, white, (center, center), 40)
                else :
                    pygame.draw.circle(screen, colored_color, (center, center), 40)
        pygame.display.update()
    """

    
    while guess :
        screen.fill(black)
        screen.blit(guess_text1, (int((window_size-guess_text1.get_width())/2), 20))
        screen.blit(guess_text2, (int((center-guess_text2.get_width())/2), 300))
        screen.blit(guess_text5, (int((center-guess_text5.get_width())/2), 330))
        screen.blit(guess_text3, (int((center+(center-guess_text3.get_width())/2)), 300))
        screen.blit(guess_text6, (int((center+(center-guess_text6.get_width())/2)), 330))
        screen.blit(guess_text4, (int((window_size-guess_text4.get_width())/2), 280))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_s :
                    colors_and_times[round_number-1].append(-1)
                    if colored_plus_or_minus < rando :
                        #Correct answer
                        correct = True
                        guess = False
                        colors_and_times[round_number-1].append(1)
                    else :
                        #Incorrect answer
                        incorrect = True
                        guess = False
                        colors_and_times[round_number-1].append(-1)
                if event.key == pygame.K_l :
                    colors_and_times[round_number-1].append(1)
                    if colored_plus_or_minus > rando :
                        #Correct answer
                        correct = True
                        guess = False
                        colors_and_times[round_number-1].append(1)
                    else :
                        #Incorrect answer
                        incorrect = True
                        guess = False
                        colors_and_times[round_number-1].append(-1)
        pygame.display.update()
        
    while correct :
        screen.fill(black)
        screen.blit(correct_text, (int((window_size-correct_text.get_width())/2), int((window_size-correct_text.get_height())/2)))
        screen.blit(space_text, (int((window_size-space_text_width)/2), 500))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    correct = False
                    round_screen = True
                    round_number += 1
                    round_text, round_text_width = init_round_text(round_number)
                    if round_number != 25 :
                        current_cat = colors_and_times[round_number-1]
                    if round_number == 9 :
                        increment -= 25
                    elif round_number == 17 :
                        increment -= 15
                    elif round_number == 25 :
                        correct = False
                        end_report = True
                    
        pygame.display.update()

    while incorrect :
        screen.fill(black)
        screen.blit(incorrect_text, (int((window_size-incorrect_text.get_width())/2), int((window_size-incorrect_text.get_height())/2)))
        screen.blit(space_text, (int((window_size-space_text_width)/2), 500))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    incorrect = False
                    round_screen = True
                    round_number += 1
                    round_text, round_text_width = init_round_text(round_number)
                    if round_number != 25 :
                        current_cat = colors_and_times[round_number-1]
                    if round_number == 9 :
                        increment -= 25
                    elif round_number == 17 :
                        increment -= 15
                    elif round_number == 25 :
                        incorrect = False
                        end_report = True
        pygame.display.update()
    while end_report :
        screen.fill(black)
        screen.blit(results_text, (int((window_size-results_text_width)/2), 0))
        y_val = 100
        for lt_i, lt in enumerate(list_texts) :
            screen.blit(lt, (20, y_val))
            if colors_and_times[lt_i][0] == (255, 0, 0) :
                screen.blit(r_text, (g_or_r, y_val))
            else :
                screen.blit(g_text, (g_or_r, y_val))
            if colors_and_times[lt_i][1] == 1 :
                screen.blit(l_text, (l_or_s1, y_val))
            else :
                screen.blit(s_text, (l_or_s1, y_val))
            if colors_and_times[lt_i][2] == 1 :
                screen.blit(l_text, (l_or_s2, y_val))
            else :
                screen.blit(s_text, (l_or_s2, y_val))
            if colors_and_times[lt_i][3] == 1 :
                screen.blit(y_text, (y_or_n, y_val))
            else :
                screen.blit(n_text, (y_or_n, y_val))
            pygame.draw.line(screen, white, (0, y_val+23), (window_size, y_val+23))
            y_val += 23
            if lt_i in [7, 15, 23] :
                y_val += 22
        screen.blit(round_text2, (20, 60))
        screen.blit(dot_color_text, (dot_color_x, 60))
        screen.blit(los_text, (los_x, 60))
        screen.blit(guess_text, (guess_x, 60))
        screen.blit(correct_question_text, (correct_x, 60)) 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    pass
        pygame.display.update()
        
    
