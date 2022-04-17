import pygame
import random
import math
import sys
import os

# STRUCTURE CLASSES
class Maze:
    def __init__(self):
        self.start_coord = (tiles_x, tiles_y)
        self.matrix = []

    def gen_blank_matrix(self):
        self.matrix = []
        for rows in range(tiles_y):
            row = []
            for columns in range((tiles_x * 2) + 1):
                row.append(2)
            self.matrix.append(row)
            row = []
            for columns in range(tiles_x):
                row.append(2)
                row.append(0)
            row.append(2)
            self.matrix.append(row)
        row = []  # creates final row
        for columns in range((tiles_x * 2) + 1):
            row.append(2)
        self.matrix.append(row)

    def check_up(self, x, y, symbol, obstacle="yes"):
        if obstacle == "n/a":
            if ((y * 2) - 1) - 2 >= 0:
                if self.matrix[((y * 2) - 1) - 2][((x * 2) - 1)] == symbol:
                    return True
                else:
                    return False
            else:
                return False
        if obstacle == "yes":
            if ((y * 2) - 1) - 2 >= 0:
                if self.matrix[((y * 2) - 1) - 2][((x * 2) - 1)] == symbol and \
                        self.matrix[((y * 2) - 1) - 1][((x * 2) - 1)] != symbol:
                    return True
                else:
                    return False
            else:
                return False
        if obstacle == "no":
            if ((y * 2) - 1) - 2 >= 0:
                if self.matrix[((y * 2) - 1) - 2][((x * 2) - 1)] == self.matrix[((y * 2) - 1) - 1][((x * 2) - 1)] == symbol:
                    return True
                else:
                    return False
            else:
                return False

    def check_down(self, x, y, symbol, obstacle="yes"):
        if obstacle == "n/a":
            if (((y * 2) - 1) + 2) <= (tiles_y * 2):
                if self.matrix[((y * 2) - 1) + 2][((x * 2) - 1)] == symbol:
                    return True
                else:
                    return False
            else:
                return False
        if obstacle == "yes":
            if (((y * 2) - 1) + 2) <= (tiles_y * 2):
                if self.matrix[((y * 2) - 1) + 2][((x * 2) - 1)] == symbol and \
                        self.matrix[((y * 2) - 1) + 1][((x * 2) - 1)] != symbol:
                    return True
                else:
                    return False
            else:
                return False
        if obstacle == "no":
            if (((y * 2) - 1) + 2) <= (tiles_y * 2):
                if self.matrix[((y * 2) - 1) + 2][((x * 2) - 1)] == self.matrix[((y * 2) - 1) + 1][((x * 2) - 1)] == symbol:
                    return True
                else:
                    return False
            else:
                return False

    def check_left(self, x, y, symbol, obstacle="yes"):
        if obstacle == "n/a":
            if ((x * 2) - 1) - 2 >= 0:
                if self.matrix[((y * 2) - 1)][((x * 2) - 1) - 2] == symbol:
                    return True
                else:
                    return False
            else:
                return False
        if obstacle == "yes":
            if ((x * 2) - 1) - 2 >= 0:
                if self.matrix[((y * 2) - 1)][((x * 2) - 1) - 2] == symbol and \
                        self.matrix[((y * 2) - 1)][((x * 2) - 1) - 1] != symbol:
                    return True
                else:
                    return False
            else:
                return False
        if obstacle == "no":
            if ((x * 2) - 1) - 2 >= 0:
                if self.matrix[((y * 2) - 1)][((x * 2) - 1) - 2] == self.matrix[((y * 2) - 1)][((x * 2) - 1) - 1] == symbol:
                    return True
                else:
                    return False
            else:
                return False

    def check_right(self, x, y, symbol, obstacle="yes"):
        if obstacle == "n/a":
            if ((x * 2) - 1) + 2 <= (tiles_x * 2):
                if self.matrix[((y * 2) - 1)][((x * 2) - 1) + 2] == symbol:
                    return True
                else:
                    return False
            else:
                return False
        if obstacle == "yes":
            if ((x * 2) - 1) + 2 <= (tiles_x * 2):
                if self.matrix[((y * 2) - 1)][((x * 2) - 1) + 2] == symbol and \
                        self.matrix[((y * 2) - 1)][((x * 2) - 1) + 1] != symbol:
                    return True
                else:
                    return False
            else:
                return False
        if obstacle == "no":
            if ((x * 2) - 1) + 2 <= (tiles_x * 2):
                if self.matrix[((y * 2) - 1)][((x * 2) - 1) + 2] == self.matrix[((y * 2) - 1)][((x * 2) - 1) + 1] == symbol:
                    return True
                else:
                    return False
            else:
                return False

    def possible_dirs(self, x, y, symbol, obstacle="yes"):
        dirs = []
        if self.check_right(x, y, symbol, obstacle):
            dirs.append("right")
        if self.check_down(x, y, symbol, obstacle):
            dirs.append("down")
        if self.check_up(x, y, symbol, obstacle):
            dirs.append("up")
        if self.check_left(x, y, symbol, obstacle):
            dirs.append("left")
        return dirs

    def fill(self, x, y, symbol=1, direction="none"):
        self.matrix[((y * 2) - 1)][((x * 2) - 1)] = symbol  # coordinates switched (y,x) is used when calling for value and is starting from index 1
        if direction == "up":
            self.matrix[((y * 2) - 1) + 1][((x * 2) - 1)] = symbol  # has to go the opposite way to break wall
        if direction == "down":
            self.matrix[((y * 2) - 1) - 1][((x * 2) - 1)] = symbol
        if direction == "left":
            self.matrix[((y * 2) - 1)][((x * 2) - 1) + 1] = symbol
        if direction == "right":
            self.matrix[((y * 2) - 1)][((x * 2) - 1) - 1] = symbol

    def gen_rooms(self):
        pass
    
    def gen_rand_maze(self, start_x, start_y):
        stack = []
        forward = True
        done = False
        self.matrix[1][0] = 1
        self.matrix[(tiles_y * 2) - 1][tiles_x * 2] = 1
        x = start_x
        y = start_y
        self.fill(x, y, )
        stack.append([x, y])
        while not done:
            while forward:
                if len(self.possible_dirs(x, y, 0)) == 0:
                    if len(self.possible_dirs(x, y, 1)) > 0 and random.randint(1, 100) <= tile_size <= 50:
                        rand_dir = random.choice(self.possible_dirs(x, y, 1))
                        if rand_dir == "up":
                            y -= 1
                            self.fill(x, y, 1, "up")
                            y += 1
                        if rand_dir == "down":
                            y += 1
                            self.fill(x, y, 1, "down")
                            y -= 1
                        if rand_dir == "left":
                            x -= 1
                            self.fill(x, y, 1, "left")
                            x += 1
                        if rand_dir == "right":
                            x += 1
                            self.fill(x, y, 1, "right")
                            y -= 1
                    forward = False
                else:
                    rand_dir = random.choice(self.possible_dirs(x, y, 0))
                    if rand_dir == "up":
                        y -= 1
                        self.fill(x, y, 1, "up")
                        stack.append([x, y])
                    if rand_dir == "down":
                        y += 1
                        self.fill(x, y, 1, "down")
                        stack.append([x, y])
                    if rand_dir == "left":
                        x -= 1
                        self.fill(x, y, 1, "left")
                        stack.append([x, y])
                    if rand_dir == "right":
                        x += 1
                        self.fill(x, y, 1, "right")
                        stack.append([x, y])
            last_pos = stack[-1]
            x = last_pos[0]
            y = last_pos[1]
            # direction = last_pos[2]
            if len(self.possible_dirs(x, y, 0)) == 0:
                stack.pop(-1)
            else:
                # stack.append([x, y, direction])
                forward = True
            if len(stack) == 0:
                done = True

        
        # create an exit 

    def extend_maze(self, size):
        row = 0
        for rows in range(tiles_y):
            index = 1
            for columns in range(tiles_x):
                for i in range(size - 1):
                    self.matrix[row].insert(index, self.matrix[row][index])
                index += size + 1
            row += 1
            index = 1
            for columns in range(tiles_x):
                for i in range(size - 1):
                    self.matrix[row].insert(index, self.matrix[row][index])
                index += size + 1
            copy = self.matrix[row].copy()
            for i in range(size - 1):
                self.matrix.insert(row, copy)
            row += size

        # creates final row
        index = 1
        for columns in range(tiles_x):
            for i in range(size - 1):
                self.matrix[row].insert(index, self.matrix[-1][index])
            index += size + 1

    def load(self):
        on_screen.empty()
        other_sprites.empty()
        obstacles.empty()

        xpos = 0
        ypos = 0
        x = 0
        y = 0
        for rows in self.matrix:
            for tile in rows:
                tiles[x][y].abs_pos_x = xpos
                tiles[x][y].abs_pos_y = ypos
                tiles[x][y].rect.topleft = (xpos, ypos)
                other_sprites.add(tiles[x][y])
                # if tile in symbol_dict.keys():   # checks if the symbol is in my dictionary

                if tile == 1:  # path
                    tiles[x][
                        y].is_obstacle = False  # don't actually need this line because by default the cell is not obstacle
                    '''picture_path = images_dict['path_images'][random.randint(0, len(images_dict['path_images']) - 1)]
                    tiles[x][y].image = pygame.image.load(picture_path)'''
                    image = images_dict[path_key][random.randint(0, len(images_dict[path_key]) - 1)]
                    tiles[x][y].image = image

                    '''cell = Cell(x, y, symbol_dict[tile][random.randint(1, len(symbol_dict[tile])) - 1], False)
                    all_sprites.add(cell)'''
                elif tile == 2:  # wall
                    tiles[x][y].is_obstacle = True
                    obstacles.add(tiles[x][y])
                    '''picture_path = images_dict['wall_images'][random.randint(0, len(images_dict['wall_images']) - 1)]
                    tiles[x][y].image = pygame.image.load(picture_path)'''
                    image = images_dict[wall_key][random.randint(0, len(images_dict[wall_key]) - 1)]
                    tiles[x][y].image = image
                    '''cell = Cell(x, y, symbol_dict[tile][random.randint(1, len(symbol_dict[tile])) - 1])
                    all_sprites.add(cell)
                    # obstacles.add(cell)'''
                    pass

                x += 1
                xpos += tile_size
            ypos += tile_size
            y += 1
            xpos = 0
            x = 0

    def init_level(self):

        # Maze.matrix = []
        self.gen_blank_matrix()
        self.gen_rand_maze(self.start_coord[0], self.start_coord[1])
        self.extend_maze(extend_size)
        self.load()


# SPRITE CLASSES
class Cell(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([tiles_x, tiles_y])  # default/temporary surface
        self.rect = self.image.get_rect()
        self.abs_pos_x = 0  # default/temporary pos
        self.abs_pos_y = 0
        self.is_obstacle = False  # default/temporary state
        self.rel_pos_x = 0  # default/temporary pos
        self.rel_pos_y = 0

    def update(self, function='update'):
        if function == 'update':
            pass
        if function == 'go_to_rel':
            if hero.abs_pos_x <= screen_width:
                rel_x = int(self.abs_pos_x - rel_dict['left'])
            elif hero.abs_pos_x >= total_width - screen_width:
                rel_x = int(screen_width - (rel_dict['right'] - self.abs_pos_x))
            else:
                rel_x = int(self.abs_pos_x - rel_dict['left'])  # both work I think
            if hero.abs_pos_y <= screen_height:
                rel_y = int(self.abs_pos_y - rel_dict['top'])
            elif hero.abs_pos_y >= total_height - screen_height:
                rel_y = int(screen_height - (rel_dict['bottom'] - self.abs_pos_y))
            else:
                rel_y = int(self.abs_pos_y - rel_dict['top'])  # both work I think
            if -tile_size <= rel_x <= screen_width and -tile_size <= rel_y <= screen_height:
                self.rect.x = rel_x
                self.rect.y = rel_y
                on_screen.add(self)
            else:
                on_screen.remove(self)
            pass
        if function == 'go_to_abs':
            self.rect.x = self.abs_pos_x
            self.rect.y = self.abs_pos_y
            pass

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Player(pygame.sprite.Sprite):
    def __init__(self, frames_key):
        super().__init__()
        #frames
        self.frame_ind = 0
        self.up_frames = images_dict[frames_key]['up']
        self.down_frames = images_dict[frames_key]['down']
        self.left_frames = images_dict[frames_key]['left']
        self.right_frames = images_dict[frames_key]['right']
        self.idle_frames = images_dict[frames_key]['idle']
        self.facing('idle')
        self.frames = self.idle_frames
        self.image = self.frames[self.frame_ind]
        self.rect = self.image.get_rect()

        #position
        self.abs_pos_x = int(1.5 * tile_size)
        self.abs_pos_y = int(1.5 * tile_size)  # default pos at the top left open tile
        self.rel_pos_x = 0  # ((((1 + extend_size) * tiles_x) + 1) * tile_size)/2  # default/temporary
        self.rel_pos_y = 0  # ((((1 + extend_size) * tiles_y) + 1) * tile_size)/2  # this calculation uses center not topleft
        self.rect.topleft = (self.abs_pos_x, self.abs_pos_y)
        player_group.add(self)
        self.counter = 0
        self.pos_x = math.floor(self.abs_pos_x / tile_size)
        self.pos_y = math.floor(self.abs_pos_y / tile_size)
        self.update_rel_borders()

        #other
        self.credit = 0
        self.grade = "A"

    def facing(self, facing):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.idle = False
        if facing == 'right':
            self.right = True
        if facing == 'left':
            self.left = True
        if facing == 'up':
            self.up = True
        if facing == 'down':
            self.down = True
        if facing == 'idle':
            self.idle = True

    def move(self, abs_change_x, abs_change_y):
        # self.update_pos()
        candidates = []
        if not abs_change_x == 0:
            pos1_y = math.floor((self.abs_pos_y + abs_change_y) / tile_size)
            pos2_y = math.ceil((self.abs_pos_y + abs_change_y) / tile_size)
            if abs_change_x < 0:
                pos1_x = math.floor((self.abs_pos_x + abs_change_x) / tile_size)
                pos2_x = pos1_x

                candidates.append((pos1_x, pos1_y))
                candidates.append((pos2_x, pos2_y))
            elif abs_change_x > 0:
                pos1_x = math.ceil((self.abs_pos_x + abs_change_x) / tile_size)
                pos2_x = pos1_x

                candidates.append((pos1_x, pos1_y))
                candidates.append((pos2_x, pos2_y))
        if not abs_change_y == 0:
            pos1_x = math.floor((self.abs_pos_x + abs_change_x) / tile_size)
            pos2_x = math.ceil((self.abs_pos_x + abs_change_x) / tile_size)
            if abs_change_y < 0:

                pos1_y = math.floor((self.abs_pos_y + abs_change_y) / tile_size)
                pos2_y = pos1_y

                candidates.append((pos1_x, pos1_y))
                candidates.append((pos2_x, pos2_y))
            elif abs_change_y > 0:
                pos1_y = math.ceil((self.abs_pos_y + abs_change_y) / tile_size)
                pos2_y = pos1_y

                candidates.append((pos1_x, pos1_y))
                candidates.append((pos2_x, pos2_y))

        if not is_obstacle(candidates):
            self.abs_pos_x += abs_change_x
            self.abs_pos_y += abs_change_y

        else:
            if abs_change_x <= col_tol:
                pass
            else:
                self.move((abs(abs_change_x) - 1) * int(abs(abs_change_x) / abs_change_x),
                          abs_change_y)
            if abs_change_y <= col_tol:
                pass
            else:
                self.move(abs_change_x,
                          (abs(abs_change_y) - 1) * int(abs(abs_change_y) / abs_change_y))

    def action(self):
        global mouse_x, mouse_y
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # global keys, mouse_x, mouse_y
        # keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.frames = self.up_frames
            self.facing('up')
            self.move(0, (-1 * player_vel))  # subtract y to move up

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.frames = self.down_frames
            self.facing('down')
            self.move(0, player_vel)

        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.frames = self.left_frames
            self.facing('left')
            self.move((-1 * player_vel), 0)

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.frames = self.right_frames
            self.facing('right')
            self.move(player_vel, 0)

        else:
            self.frames = self.idle_frames

    def animation(self):
        self.counter += 1
        if (self.counter % (fps * player_ani_speed)) == 0:
            self.frame_ind = ((self.frame_ind + 1) % len(self.frames))
            self.image = self.frames[self.frame_ind]

    def update_rel_borders(self):
        rel_dict['top'] = max(self.rect.centery - screen_height / 2, 0)
        rel_dict['bottom'] = min(self.rect.centery + screen_height / 2, total_height)
        rel_dict['left'] = max(self.rect.centerx - screen_width / 2, 0)
        rel_dict['right'] = min(self.rect.centerx + screen_width / 2, total_width)
        self.pos_x = math.floor(self.rect.centerx / tile_size)
        self.pos_y = math.floor(self.rect.centery / tile_size)

    def update(self, function='update'):
        if function == 'update':
            self.action()
            self.update_rel_borders()

        if function == 'animation':
            self.animation()

        if function == 'go_to_rel':

            if hero.abs_pos_x <= screen_width:
                self.rel_pos_x = int(self.abs_pos_x - rel_dict['left'])
            elif hero.abs_pos_x >= total_width - screen_width:
                self.rel_pos_x = int(screen_width - (rel_dict['right'] - self.abs_pos_x))
            else:
                self.rel_pos_x = screen_width / 2  # int(self.abs_pos_x - rel_dict['left'])  # both work I think
            if hero.abs_pos_y <= screen_height:
                self.rel_pos_y = int(self.abs_pos_y - rel_dict['top'])
            elif hero.abs_pos_y >= total_height - screen_height:
                self.rel_pos_y = int(screen_height - (rel_dict['bottom'] - self.abs_pos_y))
            else:
                self.rel_pos_y = screen_height / 2  # int(self.abs_pos_y - rel_dict['top'])  # both work I think

            self.rect.x = self.rel_pos_x
            self.rect.y = self.rel_pos_y

            pass
        if function == 'go_to_abs':
            self.rect.x = self.abs_pos_x
            self.rect.y = self.abs_pos_y
            pass

class GameState:
    def __init__(self):
        self.state = 'init'
        self.level = -1
        self.lvl = []

    def init_game(self):
        # initial stuff put here
        self.level = -1
        self.lvl = []
        self.state = 'new_level'

    def new_level(self):
        maze = Maze()
        self.lvl.append(maze)
        maze.init_level()
        self.level += 1
        self.state = 'main_loop'

    def main_loop(self):
        global keys, hero

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # drawing/updating
        # calculation stage
        player_group.update('go_to_abs')
        other_sprites.update('go_to_abs')
        player_group.update()

        # screen relative visual stage
        screen.fill(bg)
        player_group.update('go_to_rel')
        other_sprites.update('go_to_rel')
        player_group.update('animation')  # must be after go to rel

        on_screen.draw(screen)

        font = pygame.font.Font('freesansbold.ttf', 25)
        grade = font.render(f'Grade: {hero.grade}', True, (0,0,0), (255,255,255))
        grade_rec = grade.get_rect()
        x, y = screen.get_size()
        grade_rec.center = (x-75, 25)
        for i in range(hero.credit):
            pencil_image = pygame.image.load('images/pencil.png')
            screen.bliz(pencil_image, (x-(i*25), 25))
        screen.blit(grade, grade_rec)

        player_group.draw(screen)  # needs to come after the tiles to be in front
        pygame.display.flip()

    def load_level(self, level_num):
        self.lvl[level_num].load()

    def state_manager(self):
        if self.state == 'init':
            self.init_game()
        if self.state == 'new_level':
            self.new_level()
        if self.state == 'main_loop':
            self.main_loop()


def instantiate_cells():
    x = 0
    y = 0
    x_tiles = ((1 + extend_size) * tiles_x) + 1
    y_tiles = ((1 + extend_size) * tiles_y) + 1
    for a in range(x_tiles):
        row = []
        for b in range(y_tiles):  # switched dimensions for the flipped tiles list
            cell = Cell()
            row.append(
                cell)  # uses (x, y) system so the "matrix" is flipped on the y=-x line DON'T calculate tiles with this because it is flipped orientation
            # all_sprites.add(cell) no need to add it here since I'm going to empty the group when I initialize the game
            x += tile_size
        tiles.append(row)
        y += tile_size
        x = 0


def is_obstacle(candidates):
    for pos in candidates:
        try: 
            if tiles[pos[0]][pos[1]].is_obstacle:
                return True
        except:
            if game_state.level + 1 < len(game_state.lvl):
                game_state.level += 1
                game_state.load_level(game_state.level)
            else:
                game_state.state = 'new_level'
            hero.abs_pos_x = int(1.5 * tile_size)
            hero.abs_pos_y = int(1.5 * tile_size)

    return False

# loads images from within the same folder as the .py or optionally in an adjacent folder
# Specify the key (type string) for the image on the dictionary
# string is a format type string that replaces the string with ascending numbers up to "last_index"
def format_images_dict(dictionary, key, string, last_index, folder_name=None, lower_key=None):
    images = []
    if folder_name is not None:
        for i in range(last_index + 1):
            images.append(os.path.join(folder_name, string.format(i)))
    else:
        for i in range(last_index + 1):
            images.append(string.format(i))

    images = list(map(lambda x: pygame.transform.scale(pygame.image.load(x), (48, 48)), images))
    images = {i: images[i] for i in range(0, len(images))}

    if lower_key is None:
        dictionary[key] = images
    else:
        # format_images_dict(images, lower_key, string, last_index)
        if key in dictionary:
            dictionary[key][lower_key] = images
        else:
            dictionary[key] = {}
            dictionary[key][lower_key] = images



# general setup
pygame.init()
clock = pygame.time.Clock()

# game setup
tile_size = 48
tiles_x = 15  # int(544/tile_size)  # 110
tiles_y = 10  # int(320/tile_size)  # 70
extend_size = 5

fps = 30
player_vel = 12
player_ani_speed = 0.3  # secs per frame
col_tol = 4

path_key = 'path_images'
wall_key = 'wall_images'
hero_key = 'hero_frames'
enemy_key = 'enemy_frames'
images_dict = {}
# symbol_dict = {}
format_images_dict(images_dict, path_key, 'floor_{}.png', 3, "images/5(all frames)/floor")  # path
format_images_dict(images_dict, wall_key, 'catacombs_{}.png', 11, "images/5(all frames)/wall")  # wall

# animation_dict = {}
# animation frames
format_images_dict(images_dict, hero_key, 'D{}.png', 10, 'images/down', "down")
format_images_dict(images_dict, hero_key, 'U{}.png', 10, 'images/up', 'up')
format_images_dict(images_dict, hero_key, 'L{}.png', 10, 'images/left', 'left')
format_images_dict(images_dict, hero_key, 'R{}.png', 10, 'images/right', 'right')
format_images_dict(images_dict, hero_key, 'I{}.png', 2, 'images/idle', 'idle')
game_state = GameState()

# screen setup
screen_width = int(tiles_x * 2)  * tile_size  # int(((tiles_x * 2) + 1) * tile_size)  # must be after tiles setup
screen_height = int(tiles_y * 2) * tile_size  # int(((tiles_y * 2) + 1) * tile_size)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Generator")
bg = (0, 0, 0)
total_width = ((((1 + extend_size) * tiles_x) + 1) * tile_size)
total_height = ((((1 + extend_size) * tiles_y) + 1) * tile_size)

rel_dict = {}

# sprite setup
on_screen = pygame.sprite.Group()
other_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
player_group = pygame.sprite.GroupSingle()

hero = Player(hero_key)  # make sure is after player group & frames setup & before instantiate cells

tiles = []  # Zero indexed
instantiate_cells()  # make sure it's after I create all_sprites group and variable for extend size
while True:
    game_state.state_manager()
    clock.tick(fps)
