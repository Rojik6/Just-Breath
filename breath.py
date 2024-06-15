import time
from graphics import Canvas

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
DELAY = 1/20
DELAY2 = 1/5
DELAY3 = 1/30
GROWTH_FACTOR = 4
CIRCLE_SIZE = 50


def grow(canvas, breath, color_choice, delay_choice):
    curr_coordinates = get_corner_coordinates(canvas, breath)
    canvas.delete(breath)
    return  canvas.create_oval(curr_coordinates[0] - GROWTH_FACTOR,
                            curr_coordinates[1] - GROWTH_FACTOR,
                            curr_coordinates[2] + GROWTH_FACTOR,
                            curr_coordinates[3] + GROWTH_FACTOR,
                            color = color_choice)

def shrink(canvas, breath, color_choice, delay_choice):
    curr_coordinates = get_corner_coordinates(canvas, breath)
    canvas.delete(breath)
    return  canvas.create_oval(curr_coordinates[0] + GROWTH_FACTOR,
                            curr_coordinates[1] + GROWTH_FACTOR,
                            curr_coordinates[2] - GROWTH_FACTOR,
                            curr_coordinates[3] - GROWTH_FACTOR,
                            color = color_choice)

def static(canvas, breath, color_choice, delay_choice):
    curr_coordinates = get_corner_coordinates(canvas, breath)
    canvas.delete(breath)
    return  canvas.create_oval(curr_coordinates[0],
                            curr_coordinates[1] + 0,
                            curr_coordinates[2] - 0,
                            curr_coordinates[3] - 0,
                            color = color_choice)

def get_corner_coordinates(canvas, canvas_obj):
    
    left_x, top_y = canvas.coords(canvas_obj)
    right_x = left_x + canvas.get_object_width(canvas_obj)
    bottom_y = top_y + canvas.get_object_height(canvas_obj)
    
    return left_x, top_y, right_x, bottom_y

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    print("Simply relax and breathe with the circle...")
    color_choice = input("Pick a color (black, blue, green, red, purple, yellow, orange): ")
    delay_choice = input("Choose speed: slow (to calm down), regular (to relax), or fast (to energize): ")
    if delay_choice == "slow":
        delay_choice =  DELAY2
    elif delay_choice == "regular":
        delay_choice = DELAY
    elif delay_choice == "fast":
        delay_choice = DELAY3
    else:
        delay_choice = DELAY
    breath = start(canvas, color_choice, delay_choice)
    while True:
        inhale(canvas, breath, color_choice, delay_choice)
        hold(canvas, breath, color_choice, delay_choice)
        exhale(canvas, breath, color_choice, delay_choice)
        hold(canvas, breath, color_choice, delay_choice)


def start(canvas, color_choice, delay_choice):
    breath = []
    
    breath.append(
        canvas.create_oval(CANVAS_WIDTH/2 - CIRCLE_SIZE / 2,
                            CANVAS_HEIGHT/2 - CIRCLE_SIZE / 2,
                            CANVAS_HEIGHT/2 + CIRCLE_SIZE / 2,
                            CANVAS_HEIGHT/2 + CIRCLE_SIZE / 2,
                            color = color_choice)
                            )
    
    return breath                 

def inhale(canvas, breath_list, color_choice, delay_choice):
    for i in range(50):
        for i in range(len(breath_list)):
            breath = breath_list[i]
            breath_list[i] = grow(canvas, breath, color_choice, delay_choice)
        
        time.sleep(delay_choice)


def exhale(canvas, breath_list, color_choice, delay_choice):
    for i in range(50):
        for i in range(len(breath_list)):
            breath = breath_list[i]
            breath_list[i] = shrink(canvas, breath, color_choice, delay_choice)
        
        time.sleep(delay_choice)

def hold(canvas, breath_list, color_choice, delay_choice):
    for i in range(4):
        for i in range(len(breath_list)):
            breath = breath_list[i]
            breath_list[i] = static(canvas, breath, color_choice, delay_choice)

        time.sleep(delay_choice)

if __name__ == '__main__':
    main()