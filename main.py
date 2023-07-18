from turtle import Turtle, Screen

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
HALL_HEADER = 150
FONT_SIZE = 20

ROW = 5
COLUMN = 9

# SCREEN
main_screen = Screen()
main_screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.setworldcoordinates(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.title("kino")

# DRAWING SEATS
main_turtle = Turtle()
main_turtle.hideturtle()
main_turtle.speed(0)
main_turtle.penup()

# DRAWING CINEMA SCREEN


# TEXT
main_writer = Turtle()
main_writer.hideturtle()
main_writer.speed(0)
main_writer.penup()

cell_width = SCREEN_WIDTH / COLUMN
cell_height = (SCREEN_HEIGHT - HALL_HEADER) / ROW   # move all seats down to have space for info

seat_radius = (cell_height * 0.8) / 2               # cell become smaller that gives a space between seats

x = cell_width / 2
y = (cell_height / 2) - seat_radius

seats = {}

for r in range(ROW):
    for c in range(COLUMN):
        seats[(x, y)] = False                       # all seats are free 
        x += cell_width                             # move x to the next cell 
    x = cell_width / 2
    y += cell_height

# INFO TEXT
def write_free_seats():
    main_screen.tracer(False)
    main_writer.clear()                             # update info after new seat choosen
    main_writer.setposition(10, SCREEN_HEIGHT - (FONT_SIZE * 2))
    main_writer.pendown()
    free_seats = len(seats.values()) - sum(seats.values())
    main_writer.write(f"Free: {free_seats}", font=("TimesNewRoman", FONT_SIZE, "bold"))
    main_writer.penup()
    main_screen.tracer(True)

# DRAW CINEMA SCREEN


# DRAW SEAT
def draw_seat(x, y, color="steel blue"):
    main_turtle.setposition(x, y)
    main_turtle.pendown()
    main_turtle.begin_fill()
    main_turtle.circle(seat_radius)
    main_turtle.fillcolor(color)
    main_turtle.end_fill()
    main_turtle.penup()

# GET COORD OF SEAT
def get_seat(x, y):
    for _x, _y in seats:
        distance = ((x - _x)**2 + (y - (_y + seat_radius))**2)**0.5 #coord of place where drawing starts
        if distance <= seat_radius:
            return _x, _y
# def get_seat(x, y):
#     for seat in seats:
#         distance = ((x - seat[0])**2 + (y - (seat[1] + seat_radius))**2)**0.5
#         if distance <= seat_radius:
#             return seat

# BOOKING
def book_seat(x, y):
    seat_coord = get_seat(x, y)
    if seat_coord:                              # if seat is chosen
        seats[seat_coord] = True
        draw_seat(*seat_coord, color="tomato")  # * gives order\graduality
        write_free_seats()

# MAKES DRAWING MOMENTARY
main_screen.tracer(False)   
for seat in seats:
    draw_seat(*seat)
main_screen.tracer(True)

write_free_seats()

main_screen.onclick(book_seat)

main_screen.mainloop()