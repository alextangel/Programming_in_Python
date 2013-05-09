# template for "Stopwatch: The Game"
import simplegui
import math

# define global variables
interval = 100
milisec = 0
check = False
attemp = 0
second = 0
minute = 0
hit = 0
a = 0
b = 0
c = 0
d = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global second
    global minute
    global milisec
    global a
    global b
    global c
    global d
    
    d = milisec%10
    if milisec == 10:
        second+=1
        c = second%10
        b = (math.floor(second/10))%6
        milisec = 0
        if second == 60:
            minute+=1
            a = minute%10
            second = 0
            
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

#format the score
def score():
    return str(hit) + "/" + str(attemp)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global attemp
    global milisec
    global check
    check = True

def stop():
    global attemp
    global hit
    global check
    global d
    check = False
    attemp +=1
    if d == 0:
        hit +=1

def reset():
    global attemp, hit, second, minute, milisec
    global a,b,c,d
    
    milisec = 0
    attemp = 0
    second = 0
    minute = 0
    hit = 0
    a = 0
    b = 0
    c = 0
    d = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global second
    global minute
    global milisec
    global a
    global b
    global c
    global d
    if check == True:
        milisec+=1
        
# define draw handler
def draw(canvas):
    canvas.draw_text(format(milisec),[90, 120], 50, "White")
    canvas.draw_text(score(),[240, 30], 32, "Red")
# create frame
frame = simplegui.create_frame("Text drawing", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)
frame.add_button("Start", start, 75)
frame.add_button("Stop", stop, 75)
frame.add_button("Reset", reset, 75)

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric