import sys, os
import random
import pdb

def clamp(num, low, hi):
  return max(low, min(num, hi))

def gen_map(width, height):
  lowest = height // 4
  highest = lowest * 3

  # 'cursor' que va escribiendo la superficie
  surf = random.randint(lowest, highest)
  
  # (y, x)
  mat = [[0 for _ in range(width)] for _ in range(height)]

  # pdb.set_trace()
  
  for x in range(width):
    char = random.choice((1, 2, 3)) # 1:_ 2:/ 3:\

    if char == 3:
      if x and mat[surf - 1][x - 1] == 2:
        surf -= 1
      else:
        surf -= 2   

    mat[surf][x] = char

    if char == 2:
      surf += 1

    if surf < lowest:
      surf = lowest
      char = 1
    elif surf > highest:
      surf = highest
      char = 1

    
  return mat


def print_map(matrix):
  for y, row in enumerate(matrix):
    for x, col in enumerate(row):
      print('_' if col == 1 else '/' if col == 2 else '\\' if col == 3 else ' ', end='')

    print('')

if __name__ == '__main__':
  mapita = gen_map(90, 20)

  print_map(mapita)
