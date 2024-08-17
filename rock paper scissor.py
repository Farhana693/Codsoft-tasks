from tkinter import *
import tkinter.font as font
import random

root = Tk()
root.title("Rock Paper Scissors Game-Farhana")
app_font = font.Font(size=12)
root.config(bg='#F9F9F9')
root.geometry('600x300')

player_score = 0
computer_score = 0
options = [('Rock', 0), ('Paper', 1), ('Scissors', 2)]

Label(root, text='Rock Paper Scissors', font=font.Font(size=24, weight='bold'), bg='#F9F9F9').pack(pady=10)

main_frame = Frame(root, bg='#F9F9F9')
main_frame.pack(pady=10)

def player_choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text=f'You Selected: {player_input[0]}')
    computer_choice_label.config(text=f'Computer Selected: {computer_input[0]}')

    if player_input == computer_input:
        winner_label.config(text="It's a Tie!", fg='orange')
    elif (player_input[1] - computer_input[1]) % 3 == 1:
        player_score += 1
        winner_label.config(text="You Win!!!", fg='green')
    else:
        computer_score += 1
        winner_label.config(text="Computer Wins!!!", fg='red')

    update_scores()

def get_computer_choice():
    return random.choice(options)

def update_scores():
    player_score_label.config(text=f'Your Score: {player_score}')
    computer_score_label.config(text=f'Computer Score: {computer_score}')

Button(main_frame, text='Rock', width=12, height=2, bg='#FFB6C1', font=app_font, command=lambda: player_choice(options[0])).grid(row=0, column=0, padx=10, pady=10)
Button(main_frame, text='Paper', width=12, height=2, bg='#FFD700', font=app_font, command=lambda: player_choice(options[1])).grid(row=0, column=1, padx=10, pady=10)
Button(main_frame, text='Scissors', width=12, height=2, bg='#ADD8E6', font=app_font, command=lambda: player_choice(options[2])).grid(row=0, column=2, padx=10, pady=10)

player_choice_label = Label(root, text='You Selected: ---', font=app_font, bg='#F9F9F9')
player_choice_label.pack(pady=5)

computer_choice_label = Label(root, text='Computer Selected: ---', font=app_font, bg='#F9F9F9')
computer_choice_label.pack(pady=5)

winner_label = Label(root, text="Let's Play!", font=font.Font(size=16, weight='bold'), bg='#F9F9F9')
winner_label.pack(pady=10)

score_frame = Frame(root, bg='#F9F9F9')
score_frame.pack(pady=10)

player_score_label = Label(score_frame, text='Your Score: 0', font=app_font, bg='#F9F9F9')
player_score_label.grid(row=0, column=0, padx=20)

computer_score_label = Label(score_frame, text='Computer Score: 0', font=app_font, bg='#F9F9F9')
computer_score_label.grid(row=0, column=1, padx=20)

root.mainloop()

