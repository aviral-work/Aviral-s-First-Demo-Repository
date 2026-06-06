import random
def rps(rock,paper,scissors):
    # rules
    score=0
    chance=chanc
    if (chance=="rock" and r==rock) or (chance=="scissors" and r==scissors) or (chance=="paper" and r==paper) :
        score==score
    if (chance=="rock" and r==scissors) or (chance=="scissors" and r==paper or (chance=="paper" and r==rock)):
        score=score+1
    if (chance=="scissors" and r==rock) or (chance=="paper" and r==scissors) or (chance=="paper" and r==rock):
        score=score-1
        return score
chanc=input('Enter rock, paper or scissors= ')
list=['rock','paper','scissors']
r=list.random


