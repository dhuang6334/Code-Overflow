import pygame
import random
import math
import sys
import os


# STRUCTURE CLASSES
class Maze:
    # matrix = []

    def __init__(self):
        # self.matrix_coord = [0, 0]

        self.start_coord = (tiles_x, tiles_y)
        self.matrix = []

    '''def __init__(sprite):
        sprite.x = 0
        sprite.y = 0
        sprite.dir = ""
    '''  # I don't know how or if this works

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
        # self.rect.topleft = [abs_pos_x, abs_pos_y]
        self.abs_pos_x = 0  # default/temporary pos
        self.abs_pos_y = 0
        # self.rect.topleft = (self.abs_pos_x, self.abs_pos_y)
        # self.vel = player_vel
        self.is_obstacle = False  # default/temporary state
        self.rel_pos_x = 0  # default/temporary pos
        self.rel_pos_y = 0

    def move(self):
        pass

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
            '''rel_x = screen_width - (rel_dict['right'] - self.rect.x)
            rel_y = screen_height - (rel_dict['bottom'] - self.rect.y)'''
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
        self.frame_ind = 0
        self.frames = images_dict[frames_key]
        self.image = self.frames[self.frame_ind]
        self.rect = self.image.get_rect()
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

        '''if abs_change_x == abs_change_y == 0:
            new_corner1_pos_x = self.pos_x
            new_corner1_pos_y = self.pos_y
            new_corner2_pos_x = self.pos_x
            new_corner2_pos_y = self.pos_y'''
        '''tile_change_x = new_pos_x - self.pos_x
        tile_change_y = new_pos_y - self.pos_y'''
        '''if abs_change_x < 0:
            new_pos_x = math.floor((self.abs_pos_x + abs_change_x) / tile_size)
            new_pos_y = math.floor((self.abs_pos_y + abs_change_y) / tile_size)
        else:


        if abs_change_y < 0:
            new_pos_x = math.ceil((self.abs_pos_x + abs_change_x) / tile_size)
            new_pos_y = math.ceil((self.abs_pos_y + abs_change_y) / tile_size)
        else:
            new_pos_x = self.pos_x
            new_pos_y = self.pos_y'''

        if not is_obstacle(candidates):
            '''self.pos_x += tile_change_x
            self.pos_y += tile_change_y'''

            self.abs_pos_x += abs_change_x
            self.abs_pos_y += abs_change_y
            '''self.pos_x = math.floor(self.rect.centerx / tile_size)
            self.pos_y = math.floor(self.rect.centery / tile_size)'''

        else:
            '''if pygame.sprite.spritecollideany(self, obstacles):
                # print(True)
                # add a bounce back animation?
                pass
            else:'''
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
            '''if pygame.sprite.spritecollideany(self, obstacles):  #  abs_change_x == abs_change_y <= 8
                # add a bounce back animation?
                pass
            else:
                if not abs_change_x == abs_change_y <= 8:
                    self.move((abs(abs_change_x) - 1) * (abs(abs_change_x)/abs_change_x),
                              (abs(abs_change_y) - 1) * (abs(abs_change_y)/abs_change_y))'''

        # def shoot(self, speed, angle):

        pass

    def action(self):
        global mouse_x, mouse_y
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # global keys, mouse_x, mouse_y
        # keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(0, (-1 * player_vel))  # subtract y to move up

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(0, player_vel)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.move((-1 * player_vel), 0)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.move(player_vel, 0)
        

       
        '''for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                angle = math.atan((mouse_y - self.rel_pos_y)/(mouse_x - self.rel_pos_x))
                if mouse_x - self.rel_pos_x < 0:
                    angle += math.pi  # 180 degs

                Projectile(self.rel_pos_x, self.rel_pos_y, angle)
                print('shoot')
                pass  # mouse_x, mouse_y'''

        other_sprites.update()  # doesn't do anything rn

    def facing(self, direction):
        global mouse_x, mouse_y
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if direction == 'left':
            if self.rect.centerx > mouse_x:
                return True
            else:
                return False
        elif direction == 'right':
            if self.rect.centerx < mouse_x:
                return True
            else:
                return False
        elif direction == 'up':
            if self.rect.centery > mouse_y:
                return True
            else:
                return False
        elif direction == 'down':
            if self.rect.centery < mouse_y:
                return True
            else:
                return False

    def update_frame(self):
        global mouse_x, mouse_y
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.image = pygame.transform.flip(self.frames[self.frame_ind], self.facing('right'), False)

    def animation(self):
        self.counter += 1
        if (self.counter % (fps * player_ani_speed)) == 0:
            self.frame_ind = ((self.frame_ind + 1) % len(self.frames))
            self.update_frame()
            self.counter = 0

    '''def update_pos(self):
        self.pos_x = math.floor(self.abs_pos_x / tile_size)
        self.pos_y = math.floor(self.abs_pos_y / tile_size)'''

    def update_rel_borders(self):
        rel_dict['top'] = max(self.rect.centery - screen_height / 2, 0)
        rel_dict['bottom'] = min(self.rect.centery + screen_height / 2, total_height)
        rel_dict['left'] = max(self.rect.centerx - screen_width / 2, 0)
        rel_dict['right'] = min(self.rect.centerx + screen_width / 2, total_width)
        self.pos_x = math.floor(self.rect.centerx / tile_size)
        self.pos_y = math.floor(self.rect.centery / tile_size)

    def update(self, function='update'):
        # global keys
        # print(self.pos_x, self.pos_y)
        if function == 'update':
            self.action()
            self.update_rel_borders()

            '''print(self.abs_pos_x, self.abs_pos_y)
            print(self.rect.x, self.rect.y)'''  # for debugging purposes to see if location is a screen relative visual trick

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
            '''rel_x = int(max(self.rect.x - rel_dict['left'],
                            screen_width - (rel_dict['right'] - self.rect.x)))  # both work I think

            rel_y = int(max(self.rect.y - rel_dict['top'],
                            screen_height - (rel_dict['bottom'] - self.rect.y)))  # both work I think'''

            self.rect.x = self.rel_pos_x
            self.rect.y = self.rel_pos_y

            pass
        if function == 'go_to_abs':
            self.rect.x = self.abs_pos_x
            self.rect.y = self.abs_pos_y
            pass


'''
    def update(self, *args):
        self.move()
        if -1 * tile_size < self.rect.x < screen_width + tile_size and \
                -1 * tile_size < self.rect.y < screen_height + tile_size:
            on_screen.add(self)
        else:
            on_screen.remove(self)'''


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
        global keys, KEYDOWN, mouse_x, mouse_y
        
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pass
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pass
            if event.type == pygame.KEYDOWN:
                KEYDOWN = True
            else:
                KEYDOWN = False
        """
        if keys[pygame.K_SPACE]:  # restart game
            self.state = 'init'
        if keys[pygame.K_RSHIFT]:  # next level
            if self.level + 1 < len(self.lvl):
                self.level += 1
                self.load_level(self.level)
            else:
                self.state = 'new_level'
        if keys[pygame.K_LSHIFT]:  # previous level load
            if self.level - 1 >= 0:
                self.level -= 1
                self.load_level(self.level)
        if keys[pygame.K_r]:  # refresh level
            self.load_level(self.level)"""

        # drawing/updating
        # calculation stage
        player_group.update('go_to_abs')
        other_sprites.update('go_to_abs')
        projectiles.update('go_to_abs')
        player_group.update()

        # screen relative visual stage
        screen.fill(bg)
        player_group.update('go_to_rel')
        other_sprites.update('go_to_rel')
        projectiles.update('go_to_rel')
        player_group.update('animation')  # must be after go to rel
        on_screen.draw(screen)
        player_group.draw(screen)  # needs to come after the tiles to be in front
        projectiles.update()
        #projectiles.draw(screen)
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

    images = list(map(lambda x: pygame.image.load(x), images))
    images = {i: images[i] for i in range(0, len(images))}

    if lower_key is None:
        dictionary[key] = images
    else:
        # format_images_dict(images, lower_key, string, last_index)
        dictionary[key][lower_key] = images
    '''if not dictionary[key]: # if there isn't this key add it
        dictionary[key] = images
    else:'''


'''def format_list(list_name, string, total):
    for i in range(total + 1):
        list_name.append(string.format(i))'''  # format_list not rly needed

# general setup
pygame.init()
clock = pygame.time.Clock()

# game setup
tile_size = 32
tiles_x = 17  # int(544/tile_size)  # 110
tiles_y = 10  # int(320/tile_size)  # 70
extend_size = 3

fps = 60
player_vel = 12
player_ani_speed = 0.2  # secs per frame
col_tol = 4

path_key = 'path_images'
wall_key = 'wall_images'
hero_key = 'hero_frames'
enemy_key = 'enemy_frames'
images_dict = {}
# symbol_dict = {}
format_images_dict(images_dict, path_key, 'rect_gray_{}_old.png', 3)  # path
format_images_dict(images_dict, wall_key, 'catacombs_{}.png', 11)  # wall

# animation_dict = {}
# animation frames
format_images_dict(images_dict, hero_key, 'hooded_figure_{}.png', 1)
format_images_dict(images_dict, hero_key, 'shieldMage_redKnight_{}.png', 1, '5(all frames)')
#format_images_dict(images_dict, 'hero_frames', 'hooded_figure_{}.png', 1, 'up') # can create keys if they are non-existent
#format_images_dict(images_dict['hero_frames'], 'down', 'hooded_figure_{}.png', 1)  # only works if 'hero_frames' key is a thingformat_images_dict(images_dict, enemy_key, 'hooded_figure_{}.png', 1, '5(all frames)', '')
print(images_dict)
game_state = GameState()

global keys, mouse_x, mouse_y, KEYDOWN
# keys = {}
# screen setup
screen_width = int(((tiles_x * 2) + 1) * 32)  # int(((tiles_x * 2) + 1) * tile_size)  # must be after tiles setup
screen_height = int(((tiles_y * 2) + 1) * 32)  # int(((tiles_y * 2) + 1) * tile_size)
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
projectiles = pygame.sprite.Group()
player_group = pygame.sprite.GroupSingle()

hero = Player(hero_key)  # make sure is after player group & frames setup & before instantiate cells

tiles = []  # Zero indexed
instantiate_cells()  # make sure it's after I create all_sprites group and variable for extend size
#print(images_dict)
while True:
    game_state.state_manager()
    clock.tick(fps)
