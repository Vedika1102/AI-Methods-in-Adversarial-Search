
# AI Methods in Adversarial Search 


# Raichu: An Adversarial Search and Uncertainty Reasoning AI

## Overview

This project implements an AI for the game "Raichu," a complex board game played on an n x n grid. The game features three types of pieces (Pichus, Pikachus, and Raichus) in two colors (black and white), each with unique movement rules. The AI utilizes adversarial search techniques to determine the best move for a given board state under time constraints. Raichu is a strategic board game where players move pieces with varying abilities across the board with the aim of capturing the opponent's pieces or reaching the opposite end to transform into a more powerful piece, Raichu. The game ends when one player jumps all the opponent's pieces.

## Game Rules
* Pichus move one square forward diagonally or jump over an opponent's piece two squares forward diagonally, capturing it.
* Pikachus move one or two squares in horizontal or vertical directions, or jump over and capture opponent's pieces within two or three squares.
* Raichus are promoted from Pichus or Pikachus when reaching the opposite side of the board and can move any number of squares in all directions, including jumps over and capturing opponent's pieces.

  
## Methodology/Approach

The Raichu program is divided into several functions, each designed to handle specific tasks required for the game's AI to function:
- `board_to_string(board, N)`: Converts the board into a string format for display.
- `whether_win_or_not(board)`: Determines if a win condition is met by checking if any player has run out of pieces.
- `transform_to_raichu(board_copy, N, move, player)`: Transforms a Pichu or Pikachu to Raichu if they reach the opposite side of the board.
- `get_possible_pichu_moves(board, N, player, location)`: Generates all legal moves for Pichu pieces, considering their movement constraints.
- `get_possible_pikachu_moves(board, N, player, loc)`: Similar to Pichu, this function generates legal moves for Pikachu pieces.
- `get_possible_raichu_moves(board, N, player, loc)`: Generates all legal moves for the most powerful piece, Raichu, which has the most complex movement.
- `successor_states(board, N, player)`: Combines the move generation functions to create a list of all possible successor states for a given board configuration.
- `access_states(board, wh_check)`: Evaluates the board state to give it a heuristic score based on the current distribution of pieces.
- `maximum_function(board, alpha, beta, depth, N, player)`: Implements the maximizer for the Minimax algorithm with Alpha-Beta pruning.
- `minimum_function(board, alpha, beta, depth, N, player)`: Implements the minimizer for the Minimax algorithm with Alpha-Beta pruning.
- `find_best_move(board, N, player, timelimit)`: Does the search by calling the maximum and minimum functions to find the best move within the given time limit.

## Challenges Encountered


The development of the Raichu game AI presented several substantial challenges, the most prominent of which revolved around the successor function and the distinct movement rules for the three types of pieces: Pichu, Pikachu, and Raichu.
Crafting the `successor_states` function required a deep understanding of the game's rules and to ensure that all possible moves were accounted for. The complexity of the game's mechanics made this a particularly difficult task. The differentiation in movement patterns and the promotion of Pichu to Pikachu and then to Raichu, each with its own unique rules, required careful consideration and meticulous testing to guarantee correctness.
Since the test cases were not provided, we had to come up with our own test case which was a difficult challenge on its own.
Debugging was also a significant hurdle due to the variety of possible board states and the strategic depth of Raichu.
