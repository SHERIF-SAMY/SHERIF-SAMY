# import library
# create a screen 
#hide the mouse 
#create a new window 
# allow window recieve input keyword
#delay time 
#set the head for snake where 
# set the snake 
#set food 
# shape the food 
#direction to right (snake)
# while true 
#next key
# if next key = -1 key = key
#snake[0] = new head
# when the snake die and quit
#new head
# how snake move 
#if food == snake none 
# set new food
#food = new food if new food =! snake else none 
#end
#_________________________________________________________________________
import random
import curses
# create screen
screen = curses.initscr()
# hide the mouse
curses.curs_set(0)
# get whidth and height of screen
screen_height, screen_width = screen.getmaxyx()
# create new window
window = curses.newwin(screen_height, screen_width, 0, 0)
# take input from keybord
window.keypad(1)
#to make delay [ speed of snake ]
window.timeout(180)
# the frist position of head snake
snk_x = screen_width // 4
snk_y = screen_height // 2
# building the bode of snake
snake = [
  [snk_y, snk_x],
  [snk_y - 1, snk_x],
  [snk_y - 2, snk_x]
        ]
# the frist position of food
food = [screen_height // 2, screen_width // 2]
# the shape of food [ dimond ]
window.addch(food[0], food[1], curses.ACS_DIAMOND)
# the frist diminyion [ to right ]
key = curses.KEY_RIGHT
# its the loop make game runing
while True:
# create the next dimention
  next_key = window.getch()
  if next_key == -1:
    key = key
  else:
    key = next_key
# to know if the snake did or no
  #if snake did end the game
  if (snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width]
      or snake[0] in snake[1:]):
    curses.endwin()
    quit()
# to make keybord control of the snake 
  new_head = [snake[0][0], snake[0][1]]
  if key == curses.KEY_UP:
    new_head[0] -= 1
  if key == curses.KEY_DOWN:
    new_head[0] += 1
  if key == curses.KEY_RIGHT:
    new_head[1] += 1
  if key == curses.KEY_LEFT:
    new_head[1] -= 1

  snake.insert(0, new_head)
# if snake and food in the same position hide the food
  if snake[0] == food:
    food = None
# make random position of food
    while food is None:
      new_food = [
        random.randint(1, screen_height - 1),
        random.randint(1, screen_width - 1),
      ]
      food = new_food if new_food not in snake else None
      window.addch(food[0], food[1], curses.ACS_DIAMOND)
  else:
    tail = snake.pop()
    window.addch(tail[0], tail[1], " ")

  window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

