import time

rule = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def get_game():
  with open('input.txt', 'r') as f:
    lines = f.read().split('\n\n')
  board = []
  for line in lines[0].split('\n'):
    board.append(list(line))
  directions = [d for d in lines[1] if d != '\n']

  return board, directions

def get_start_point(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == '@':
        return i, j

def is_valid_move(x, y, direction, board):
  if 0 <= x < len(board) and 0 <= y < len(board[0]):
    if board[x][y] == '.':
      return True
    elif board[x][y] == 'O':
      while board[x][y] != '#':
        x, y = x + rule[direction][0], y + rule[direction][1]
        return is_valid_move(x, y, direction, board)
  return False

def move_box(x, y, direction, board):
  dx, dy = rule[direction]
  nx, ny = x + dx, y + dy

  if board[nx][ny] == '#':
    return x - dx, y - dy

  if board[nx][ny] == 'O':
    nx, ny = move_box(nx, ny, direction, board)

  board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
  return x, y

def calculate_score(board):
  score = 0
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 'O':
        score += 100 * i + j
  return score

def print_board(board):
  for row in board:
    print(''.join(row))
  print()

board, order = get_game()
x, y = get_start_point(board)
print(f"start_point: {x}, {y}")
print_board(board)
for move in order:
  nx, ny = x + rule[move][0], y + rule[move][1]
  print(move)
  if is_valid_move(nx, ny, move, board):
    if board[nx][ny] == '.':
      board[nx][ny] = '@'
      board[x][y] = '.'
      x, y = nx, ny
    elif board[nx][ny] == 'O':
      nx, ny = move_box(nx, ny, move, board)
      board[x][y] = '.'
      board[nx][ny] = '@'
      x, y = nx, ny
  print_board(board)
  time.sleep(1)


print(f"final score: {calculate_score(board)}")
