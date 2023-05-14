import os
import turtle
import random
from levels import level_1, level_2, blank_maze, level_3, level_4
from sprites import sprite_images
import socket
import threading

serverAddressPort = ("127.0.0.1", 1000)
bufferSize = 32768

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
UDPClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
UDPClientSocket.bind(serverAddressPort)



wn = turtle.Screen()
wn.bgcolor('#1c2f2f')
wn.title('Maze Game')
wn.setup(width=700, height=700)
wn.tracer(0)
grid_block_size = 24

# set up sprites from the images folder
os.chdir("images")
for sprite in sprite_images:
    wn.register_shape(sprite)
os.chdir("../..")



# classes
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color('#362020')
        self.shape("jungle.gif")
        self.penup()
        self.speed(0)
        self.name = 'Wall'


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.name = 'Player'
        self.shape("player-right.gif")
        self.gold = 0
        self.counter = 1

    def move_up(self):
        #check if there are paths on left or right
        new_x_cor = self.xcor()
        new_y_cor = self.ycor() + 24
        paths = check_path_available(new_x_cor, new_y_cor, walls)
        print(paths)
        check_walls = check_object_collision(new_x_cor, new_y_cor, walls)
        self.counter = stuff_collision(treasures, doors, enemies, grid_block_size, self.counter)
        while paths < 3 and check_walls:
            new_x_cor = self.xcor()
            new_y_cor = self.ycor() + 24
            paths = check_path_available(new_x_cor, new_y_cor, walls)
            print(paths)
            check_walls = check_object_collision(new_x_cor, new_y_cor, walls)
            self.counter = stuff_collision(treasures, doors, enemies, grid_block_size, self.counter)
            if check_walls:
                self.setposition(new_x_cor, new_y_cor)
                self.shape("player-left.gif")

        if paths == 3 and check_walls:
            self.setposition(new_x_cor, new_y_cor)
            self.shape("player-left.gif")

        if paths == 4 and check_walls:
            self.setposition(new_x_cor, new_y_cor)
            self.shape("player-left.gif")



    def move_down(self):
        new_x_cor = self.xcor()
        new_y_cor = self.ycor() - 24
        paths = check_path_available(new_x_cor, new_y_cor, walls)
        check_walls = check_object_collision(new_x_cor, new_y_cor, walls)
        self.counter = stuff_collision(treasures, doors, enemies, grid_block_size, self.counter)
        while paths < 3 and check_walls:
            new_x_cor = self.xcor()
            new_y_cor = self.ycor() - 24
            paths = check_path_available(new_x_cor, new_y_cor, walls)
            check_walls = check_object_collision(new_x_cor, new_y_cor, walls)
            self.counter = stuff_collision(treasures, doors, enemies, grid_block_size, self.counter)
            if check_walls:
                self.setposition(self.xcor(), self.ycor() - 24)
                self.shape("player-right.gif")
        if paths == 3 and check_walls:
            self.setposition(new_x_cor, new_y_cor)
            self.shape("player-right.gif")

        if paths == 4 and check_walls:
            self.setposition(new_x_cor, new_y_cor)
            self.shape("player-right.gif")

    def move_left(self):
        print("left direct")
        new_x_cor = self.xcor() - 24
        new_y_cor = self.ycor()
        paths = check_path_available(new_x_cor, new_y_cor, walls)
        check_walls = check_object_collision(new_x_cor, new_y_cor, walls)
        self.counter = stuff_collision(treasures,doors,enemies,grid_block_size,self.counter)

        while paths < 3 and check_walls:
            new_x_cor = self.xcor() - 24
            new_y_cor = self.ycor()
            paths = check_path_available(new_x_cor, new_y_cor, walls)
            check_walls = check_object_collision(new_x_cor, new_y_cor, walls)
            self.counter = stuff_collision(treasures, doors, enemies, grid_block_size, self.counter)

            if check_walls:
                self.setposition(new_x_cor, new_y_cor)
                self.shape("player-left.gif")
        if paths == 3 and check_walls:
            self.setposition(new_x_cor, new_y_cor)
            self.shape("player-left.gif")

        if paths == 4 and check_walls:
            self.setposition(new_x_cor, new_y_cor)
            self.shape("player-left.gif")
    def move_right(self):

        new_x_cor = self.xcor() + 24
        new_y_cor = self.ycor()
        paths = check_path_available(new_x_cor, new_y_cor, walls)
        check_walls = check_object_collision(new_x_cor, new_y_cor, walls)
        self.counter = stuff_collision(treasures, doors, enemies, grid_block_size, self.counter)
        while paths < 3 and check_walls:
            new_x_cor = self.xcor() + 24
            new_y_cor = self.ycor()
            paths = check_path_available(new_x_cor, new_y_cor, walls)
            check_walls = check_object_collision(new_x_cor, new_y_cor, walls)
            self.counter = stuff_collision(treasures, doors, enemies, grid_block_size, self.counter)
            if check_walls:
                self.setposition(new_x_cor, new_y_cor)
                self.shape("player-right.gif")
        if paths == 3 and check_walls:
            self.setposition(new_x_cor, new_y_cor)
            self.shape("player-right.gif")

        if paths == 4 and check_walls:
            self.setposition(new_x_cor, new_y_cor)
            self.shape("player-right.gif")


    def hide(self):
        hide_sprite(self)


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.name = 'Treasure'
        self.shape('gold.gif')
        self.color('#D4AF37')
        self.gold = 100
        self.goto(x, y)

    def hide(self):
        hide_sprite(self)


class Door(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.name = 'Door'
        self.shape('scaled_door.gif')
        self.color('#D4AF37')
        self.goto(x, y)

    def hide(self):
        hide_sprite(self)


class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.gold = 50
        self.name = 'Enemy'
        self.shape('enemy-right.gif')
        self.setposition(x, y)
        self.direction = set_direction()

    def change_direction(self):
        if self.direction == 'up':
            dx = 0
            dy = 24
        elif self.direction == 'down':
            dx = 0
            dy = -24
        elif self.direction == 'left':
            dx = -24
            dy = 0
            self.shape('enemy-left.gif')
        elif self.direction == 'right':
            dx = 24
            dy = 0
            self.shape('enemy-right.gif')

        # check if player is near
        if self.distance(player) < (difficulty * 100):
            if player.xcor() < self.xcor():
                self.direction = 'left'

            elif player.xcor() > self.xcor():
                self.direction = 'right'

            elif player.ycor() < self.ycor():
                self.direction = 'down'

            elif player.ycor() > self.ycor():
                self.direction = 'up'

        # move enemy
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        # check for collisions
        check = check_object_collision(move_to_x, move_to_y, walls)
        if check:
            self.setposition(move_to_x, move_to_y)
        else:
            # choose a different direction
            self.direction = set_direction()

        # reposition enemies after a certain time has passed
        wn.ontimer(self.change_direction, t=random.randint(100, 300))

    def hide(self):
        hide_sprite(self)


# game status
levelsList = {}
walls = []
treasures = []
enemies = []
doors = []
difficulty = 1

# levels
levelsList[0] = blank_maze
levelsList[1] = level_1
levelsList[2] = level_2
levelsList[3] = level_3
levelsList[4] = level_4



# functions
def setup_maze(level):
    # Clear previous maze
    pen.clear()
    walls.clear()
    for treasure in treasures:
        treasure.hide()
    treasures.clear()
    for door in doors:
        door.hide()
    doors.clear()
    for enemy in enemies:
        enemy.hide()
    enemies.clear()

    # Clear previous treasures


    # Clear previous enemies


    # for number the given number of rows
    for y in range(len(level)):
        # for number of 'X's in a given row
        for x in range(len(level[y])):
            character = level[y][x]
            # position blocks
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # mark squares in the position of 'X's in the rows
            if character == 'X':
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == 'P':
                player.setposition(screen_x, screen_y)

            if character == 'T':
                treasures.append(Treasure(screen_x, screen_y))

            if character == 'D':
                doors.append(Door(screen_x, screen_y))

            # if character == 'E':
            #     enemies.append(Enemy(screen_x, screen_y))





def collision_check(sprite1, sprite2, block_size, counter):
    global difficulty
    if sprite2.distance(sprite1) < block_size:
        if sprite2.name == 'Treasure':
            sprite1.gold += sprite2.gold
            sprite2.hide()
            # difficulty += 1
            treasures.remove(sprite2)
            print("Player has {} gold".format(player.gold))
        if sprite2.name == 'Enemy':
            sprite1.hide()
            print("Player with {} gold was killed by a hunting skeleton! GAME OVER!".format(player.gold))

        if sprite2.name == 'Door':
            print("door")
            counter += 1
            player.counter = counter
            setup_maze(levelsList[counter])
    return counter


def start_enemies_moving(t):
    for enemy in enemies:
        wn.ontimer(enemy.change_direction, t=t)


def set_direction():
    return random.choice(['up', 'down', 'left', 'right'])


def hide_sprite(sprite):
    sprite.setposition(2000, 2000)
    sprite.hideturtle()


def check_object_collision(next_x, next_y, object_list):
    if (next_x, next_y) not in object_list:
        return True
    else:
        return False



#check for the number of available paths
def check_path_available(next_x, next_y, object_list):
    nr = 0
    if (next_x + 24, next_y) not in object_list:
        nr += 1
    if (next_x - 24, next_y) not in object_list:
        nr += 1
    if (next_x, next_y + 24) not in object_list:
        nr += 1
    if (next_x, next_y - 24) not in object_list:
        nr += 1
    return nr

#headset connection stuff
def listenUDP():
    global command
    while True:
        bytesAddressPair = UDPClientSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]
        # print(type(message))
        # print(message)
        # print(type(controlCommands[0]))
        for cm in controlCommands:
            if str.encode(cm) in message:
                print(str.encode(cm))
                command = cm
                print("The given command is: " + command)


# class instances
pen = Pen()
player = Player()

# keyboard bindings
controlCommands = ["FORWARD","LEFT", "STOP", "RIGHT", "BACK"]
command = ""



# keyboard bindings
wn.listen()
wn.onkeypress(player.move_up, "Up")
wn.onkeypress(player.move_down, "Down")
wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")

threadUDP = threading.Thread(target=listenUDP)
threadUDP.start()

# append levels to levels list
counter = 1
collided = False
setup_maze(levelsList[counter])
# set enemies moving after given timer
start_enemies_moving(250)
# main loop
def stuff_collision(treasures, doors, enemies, grid_block_size, counter):
    for treasure in treasures:
        counter = collision_check(player, treasure, grid_block_size, counter)
    # check player and door collision
    for door in doors:
        counter = collision_check(player, door, grid_block_size, counter)
    # check player and enemy collision
    for enemy in enemies:
        counter = collision_check(player, enemy, grid_block_size, counter)
    # update screen
    wn.update()
    command = ""
    return counter

while True:
    if command == "FORWARD":
        player.move_up()
    elif command == "LEFT":
        player.move_left()
    elif command == "RIGHT":
        player.move_right()
    elif command == "BACK":
        player.move_down()
    stuff_collision(treasures, doors, enemies, grid_block_size, counter)

