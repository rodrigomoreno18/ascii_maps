import sys, os
import random
import pdb

def clamp(num, low, hi):
  return max(low, min(num, hi))

def gen_map(width, height):
  highest = height // 4
  lowest = highest * 3

  # 'cursor' que va escribiendo la superficie
  surf = random.randint(highest, lowest)
  
  # (y, x)
  mat = [[0 for _ in range(width)] for _ in range(height)]

  # pdb.set_trace()
  
  for x in range(width):
    char = random.choice((1, 1, 1, 2, 3)) # 1:_ 2:/ 3:\

    # Si se va a escribir un '\'
    # Bajar 1 nivel para que sea una bajada
    if char == 3:
      surf += 1

    if surf > lowest:
      surf = lowest
      char = 1 if char == 3 else char
    elif surf < highest:
      surf = highest
      char = 1 if char == 2 else char
    elif surf == highest and char == 2:
      char = 1

    mat[surf][x] = char

    if char == 1 and random.random() < 0.15:
      i = 0
      while i < random.randint(1, 4):
        mat[surf - i][x] = 100    # Tronco de arbol
        i += 1

      mat[surf - i][x] = 101      # Copa de arbol
      
    for y in range(surf + 1, height):
      mat[y][x] = random.choice((4,5,5,5,6))

    if char == 2:
      surf -= 1 
    
  return mat


def print_map(matrix, tiles, indexes=False):
  for y, row in enumerate(matrix):
    if indexes:
      print('y: ' + str(y).rjust(2, ' '), end=' | ')
    for x, col in enumerate(row):
      print(tiles[col], end='')

    print('')

if __name__ == '__main__':

  h, w = map(int, os.popen('stty size', 'r').read().split())
  
  tiles = {0:' ', 1:'_', 2:'/', 3:'\\',
           4:'@', 5:'#', 6:'%', 100:'|',
           101:'#'}

  end = False

  while not end:
    os.system('cls' if os.name == 'nt' else 'clear')

    mapita = gen_map(w, h - 5)

    print_map(mapita, tiles, indexes=False)

    if input('\nType anything to quit, enter to repeat: '):
      end = True
  






