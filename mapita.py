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
  mapita = gen_map(90, 20)
  
  tiles = [' ', '_', '/', '\\', '@', '#', '%']
  print_map(mapita, tiles, indexes=True)
