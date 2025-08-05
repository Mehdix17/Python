# link : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def fast(step):
    for i in range(step):
        move()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
def turn():
    if right_is_clear():
        turn_right()
    else:
        turn_left()

    
while front_is_clear(): 
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear(): 
        move()
    else:
        turn_left()
                