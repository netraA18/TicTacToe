# import pygame

# pygame.init()

# screen_width, screen_height = 400, 400

# screen = pygame.display.set_mode((screen_width, screen_height))
# screen.fill((255, 255, 255))
# while True:
#     line_color = (255,0,0)
#     pygame.draw.line(screen,line_color, (60,80), (130,100))
    
#     pygame.display.update()
    
ask_operator = str(input("X or O: "))
operator = ask_operator



grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]



def display_grid():
    print()
    for r in grid:
        print(r)   
    print()


display_grid()

x_check = ['X', 'X', 'X']
o_check = ['O', 'O', 'O']


def check_rows():
    for r in grid:
        if r == x_check or r == o_check:
            return True
    return False

def check_diaganols():
    if grid[0][0] == grid[1][1] == grid[2][2] == "X" or grid[0][0] == grid[1][1] == grid[2][2] == "O":
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == "X" or grid[0][2] == grid[1][1] == grid[2][0] == "O":
        return True
    return False


def check_columns():
    for i in range(0,3):
        if grid[0][i] == grid[1][i] == grid[2][i] == "X" or grid[0][i] == grid[1][i] == grid[2][i] == "O":
            return True
    return False

def check_win():
    if check_rows() or check_diaganols() or check_columns():
        print("You Won!")
        return True
    return False

def check_draw():
    for row in grid:
        if ' ' in row:
            return False
    return True


while True:
    row_numb = str(input("Which row? "))
    col_numb = str(input("Which column? "))
    if int(row_numb) >= 1 and int(row_numb) <= 3 and int(col_numb) >= 1 and int(col_numb) <= 3:
        grid[int(row_numb) - 1][int(col_numb) - 1] = operator
        display_grid()
        if check_win():
            break
        elif check_draw():
            print("Draw")
            break
        if operator == "X":
            new_operator = "O"
        else:
            new_operator = "X"
        operator = new_operator
    else:
        print("The row and column number must be between 1 and 3")
