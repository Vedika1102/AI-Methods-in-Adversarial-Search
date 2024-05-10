#!/usr/local/bin/python3
#
# 
# 
# raichu.py : Play the game of Raichu
#
# Names and userIDs - Vedika Shinde (vshinde), Gayatri Gattani (ggattani), & Rishikesh Kakde (rkakde)

import sys
from copy import deepcopy

# Function to convert board to string
def board_to_string(board, N):
    return "\n".join(board[i:i + N] for i in range(0, len(board), N))

# Function to check if a player has won
def whether_win_ornot(board):
    # Initialize sets for the two players
    white_player = set()
    black_player = set()
    # Define symbols for pieces
    wh, bl = ['w', 'W', '@'], ['b', 'B', '$']

    row_index = 0
    while row_index < len(board):
        col_index = 0
        while col_index < len(board[row_index]):
            each_col = board[row_index][col_index]
            # Adding pieces to the respective sets
            if each_col in bl:
                black_player.add(each_col)
            elif each_col in wh:
                white_player.add(each_col)
            col_index += 1
        row_index += 1

    # Check if a player has won
    if len(black_player) == 0 or len(white_player) == 0:
        return True
    return False

# Function to check if the move is within the board's boundaries
def check_for_location(location, N):
    if (0 <= location[0] < N):
        if (0 <= location[1] < N):
            return True
        else:
            return False
    else:
        return False

# Function to transform Pichu or Pikachu into Raichu
def transform_to_raichu(board_copy, N, move, player):
    if player[0] == 'w':
        location = (N - 1, '@')
    else:
        location = (0, '$')
    if move[0] == location[0]:
        board_copy[move[0]][move[1]] = location[1]
    else:
        pass

# Function to get all possible moves of Pichu
def get_possible_pichu_moves(board, N, player, location):
    b_lst = list()
    if player[0] == 'w':
        diag_l_one, diag_l_two = (location[0] + 1, location[1] - 1), (location[0] + 2, location[1] - 2)
        diag_r_one, diag_r_two = (location[0] + 1, location[1] + 1), (location[0] + 2, location[1] + 2)
        next_move = (diag_r_one, diag_l_one, diag_r_two, diag_l_two)
    else:
        diag_l_one, diag_l_two = (location[0] - 1, location[1] - 1), (location[0] - 2, location[1] - 2)
        diag_r_one, diag_r_two = (location[0] - 1, location[1] + 1), (location[0] - 2, location[1] + 2)
        next_move = (diag_r_one, diag_l_one, diag_r_two, diag_l_two)

    for i in range(0, 4):
        mov = next_move[i]
        row, col = mov
        if i >= 2:
            if player[0] == 'b':
                delete = 'w'
            else:
                delete = 'b'
            if check_for_location(mov, N) and board[row][col] == '.' and board[next_move[i - 2][0]][next_move[i - 2][1]] == delete:
                copy_board = deepcopy(board)
                copy_board[row][col] = board[location[0]][location[1]]
                copy_board[location[0]][location[1]] = '.'
                copy_board[next_move[i - 2][0]][next_move[i - 2][1]] = '.'
                transform_to_raichu(copy_board, N, mov, player)
                b_lst.append(copy_board)
            elif i < 2:
                if check_for_location(mov, N) and board[row][col] == '.':
                    copy_board = deepcopy(board)
                    copy_board[row][col] = board[location[0]][location[1]]
                    copy_board[location[0]][location[1]] = '.'
                    transform_to_raichu(copy_board, N, mov, player)
                    b_lst.append(copy_board)
            else:
                pass

    return b_lst


# function get all possible moves of pikachu
def get_possible_pikachu_moves(board, N, player, loc):
  b_lst = list()
  left_1, left_2, left_3 = (loc[0], loc[1] - 1), (loc[0], loc[1] - 2), (loc[0], loc[1] - 3)
  right_1, right_2, right_3 = (loc[0], loc[1] + 1),  (loc[0], loc[1] + 2), (loc[0], loc[1] + 3)
  next_move_1, next_move_2, next_move_3= (right_1, left_1), (right_2, left_2), (right_3, left_3)
  if player[1] == 'W':
      up_1, up_2, up_3 = (loc[0] + 1, loc[1]), (loc[0] + 2, loc[1]),  (loc[0] + 3, loc[1])
      next_move = (*next_move_1, up_1, *next_move_2, up_2, *next_move_3, up_3)
  else:
      up_1, up_2, up_3 = (loc[0] - 1, loc[1]), (loc[0] - 2, loc[1]), (loc[0] - 3, loc[1])
      next_move = (*next_move_1, up_1, *next_move_2, up_2, *next_move_3, up_3)
  for i in range(0,9):
      move = next_move[i]
      cur_row, cur_col = move
      if i <3:
          if check_for_location(move, N) and board[cur_row][cur_col] == '.':
            copy_board = deepcopy(board)
            copy_board[cur_row][cur_col] = board[loc[0]][loc[1]]
            copy_board[loc[0]][loc[1]] = '.'
            transform_to_raichu(copy_board, N, move, player)
            b_lst.append(copy_board)
      if i >=3 and i <6:
              move = next_move[i]
              cur_row, cur_col = move
              if check_for_location(move, N) and board[cur_row][cur_col] == '.' and board[next_move[i-3][0]][next_move[i-3][1]] == '.':
                  copy_board = deepcopy(board)
                  copy_board[cur_row][cur_col] = board[loc[0]][loc[1]]
                  copy_board[loc[0]][loc[1]]= '.'
                  transform_to_raichu(copy_board, N, move, player)
                  b_lst.append(copy_board)
      if i >=3 and i <6:
           if player[1]=='W':
              delete='bB'
           else:
              delete='wW'
              move = next_move[i]
              row, col = move
              if check_for_location(move, N) and board[row][col] == '.' and board[next_move[i-3][0]][next_move[i-3][1]] in delete:
                  copy_board = deepcopy(board)
                  copy_board[row][col] = board[loc[0]][loc[1]]
                  copy_board[loc[0]][loc[1]]='.'
                  copy_board[next_move[i-3][0]][next_move[i-3][1]] = '.'
                  transform_to_raichu(copy_board, N, move, player)
                  b_lst.append(copy_board)
      if i >=6 and i <9:
              move = next_move[i]
              row, col = move
              if check_for_location(move, N) and board[row][col] == '.':
                  cond = False
                  if board[next_move[i-6][0]][next_move[i-6][1]] in delete and board[next_move[i-3][0]][next_move[i-3][1]] == '.':
                      cond = True
                  if board[next_move[i-6][0]][next_move[i-6][1]] == '.' and board[next_move[i-3][0]][next_move[i-3][1]] in delete:
                      cond = True
                  if cond:
                      copy_board = deepcopy(board)
                      copy_board[row][col]  = board[loc[0]][loc[1]]
                      copy_board[loc[0]][loc[1]] = '.'
                      copy_board[next_move[i-3][0]][next_move[i-3][1]] =  '.'
                      copy_board[next_move[i-6][0]][next_move[i-6][1]] = '.'
                      transform_to_raichu(copy_board, N, move, player)
                      b_lst.append(copy_board)
  return b_lst


# function get all possible moves of raichu
def get_possible_raichu_moves(board, N, player, loc):
  if player[2] == '@':
      delete = 'bB$'
  else:
       delete = 'wW@'
  b_lst = list()
  left, up, down, right  = (0, -1), (1, 0), (-1, 0), (0, 1)
  diag_r_up, diag_l_up, diag_r_down, diag_l_down = (1, 1), (1, -1), (-1, 1), (-1, -1)
  next_move = (up, down, right, left, diag_r_up, diag_l_up, diag_r_down, diag_l_down)
  for i in range(8):
      visited = 0
      cor = (0, 0)
      inc = 1
      while inc < N:
          row = loc[0] + next_move[i][0]*inc
          col =  loc[1] + next_move[i][1]*inc
          if check_for_location((row,col), N) and board[row][col] in delete and visited < 1:
              r1 = row + next_move[i][0]
              c1 = col + next_move[i][1]
              if check_for_location((r1,c1), N) and board[r1][c1] == '.':
                  copy_board = deepcopy(board)
                  copy_board[row][col] = '.'
                  copy_board[r1][c1] =  copy_board[loc[0]][loc[1]]
                  copy_board[loc[0]][loc[1]] = '.'
                  b_lst.append(copy_board)
                  inc += 1
                  visited += 1
                  cor = (row,col)
              else:
                  break
          elif check_for_location((row,col), N) and board[row][col] == '.' and visited < 2:
              copy_board = deepcopy(board)
              copy_board[loc[0]][loc[1]] = '.'
              copy_board[row][col] = copy_board[loc[0]][loc[1]]
              if visited == 1:
                  copy_board[cor[0]][cor[1]] = '.'
              b_lst.append(copy_board)
          else:
              break
          inc += 1
  return b_lst

# function gives all successor states
def successor_states(board, N, player):
    successor_list = list()
    each_row = 0
    while each_row < N:
        for each_col in range(N):
            if board[each_row][each_col] == player[0]:
                output_moves= get_possible_pichu_moves(board, N, player, (each_row,each_col))
                if output_moves:
                    successor_list = successor_list + output_moves
                else:
                    pass
            elif board[each_row][each_col] == player[1]:
                successor_list = successor_list + get_possible_pikachu_moves(board, N, player, (each_row,each_col))
            elif board[each_row][each_col] == player[2]:
                successor_list = successor_list + get_possible_raichu_moves(board, N, player, (each_row,each_col))
            else:
                pass
        each_row += 1
    return successor_list

# function assess states in the board
def access_states(board, wh_check):
    if wh_check:
        object_set = 'wW@'
    else:
        object_set = 'bB$'
    frequency = dict()
    row_idx = 0
    while row_idx < len(board):
        col_idx = 0
        while col_idx < len(board[row_idx]):
            if board[row_idx][col_idx] not in frequency:
                frequency[board[row_idx][col_idx]] = 1
            else:
                frequency[board[row_idx][col_idx]] += 1
            col_idx += 1
        row_idx += 1
    res_score = 0
    for each_piece, c in frequency.items():
        if each_piece == 'b' or each_piece == 'w':
            if each_piece not in object_set:
                res_score -= c
            else:
                res_score += c
        elif each_piece == 'B' or each_piece == 'W':
            if each_piece not in object_set:
                res_score -= c * 5
            else:
                res_score += c * 5
        elif each_piece == '@' or each_piece == '$':
            if each_piece in object_set:
                res_score += c * 10
            else:
                res_score -= c * 10
        else:
            pass
    return res_score


# max function defined for alpha beta and updates value of alpha
def maximum_function(board, alpha, beta, depth, N, player):
    if whether_win_ornot(board):
        return access_states(board, player[0])
    elif depth == 3:
        return access_states(board, player[0])
    else:
        for each_state in successor_states(board, N, player[0]):
            alph = max(alpha, minimum_function(each_state, alpha, beta, depth+1, N, player))
            if alph < beta:
                pass
            else:
                break

        return alph

# min function defined for alpha beta and updates value of beta
def minimum_function(board, alpha, beta, depth, N, player):
    if whether_win_ornot(board) :
        return access_states(board, player[1])
    elif depth == 3:
       return access_states(board, player[1])
    else:
        each_jump = player[1]
        for each_state in successor_states(board, N, each_jump):
            beta = min(beta, maximum_function(each_state, alpha, beta, depth+1, N, player))
            if alpha < beta:
                pass
            else:
                break
        return beta

def find_best_move(board, N, player, timelimit):

    board_copy = list()
    beta, alpha = float("inf"), float("-inf")

    for i in range(0, len(board), N):
        x = list(board[i:i + N])
        board_copy.append(x)

    board_to_traverse = board_copy

    if player == 'b':
        player = ['b', 'B', '$']
    elif player == 'w':
         player = ['w', 'W', '@']
    else:
        pass

    x = ['w', 'W', '@']
    y = ['b', 'B', '$']
    player_moves = [x, y]
    max_value = alpha
    best_move = None
    for each_state in successor_states(board_to_traverse, N, player):
        res = maximum_function(each_state, alpha, beta, 0, N, player_moves)
        if max_value >= res:
            pass
        else:
            temp_str = ''
            for each_row in each_state:
                for each_col in each_row:
                    temp_str += each_col
            max_value, best_move = res, temp_str

    final_best_move = [best_move]
    return final_best_move



if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")

    (_, N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    for new_board in find_best_move(board, N, player, timelimit):
        print(new_board)



