from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    for i in range(N_CIRCLES) :
       draw_random_circles(canvas) 


def draw_random_circles(canvas):
    x1 = random.randint(0, CANVAS_HEIGHT- CIRCLE_SIZE)
    y1 = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
    x2 = x1 + CIRCLE_SIZE
    y2 = y1 + CIRCLE_SIZE
    canvas.create_oval(x1,y1,x2,y2,random_color())

def random_color():
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()
