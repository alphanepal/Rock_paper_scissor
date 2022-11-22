import random
def is_winnner(player,opponent):
    if(player=='r' and opponent=='s') or(player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True

def play():
    user=input(" What is your choice?'r' for rock,'p' for paper,'s' for scissors")
    computer = random.choice(['r','p','s'])

    if user==computer:
        return 'It is a tie'

    if is_winnner(user,computer):
        return 'You won!'
    return 'You lost'


print(play()) 