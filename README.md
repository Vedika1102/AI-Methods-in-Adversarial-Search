# vsshinde-ggattani-rkakde-a2
# Report for Assignment 2: AI Methods in Adversarial Search and Naive Bayes Classification

## Problem Descriptions

### Part 1: Raichu

Raichu is a strategic board game where players move pieces with varying abilities across the board with the aim of capturing the opponent's pieces or reaching the opposite end to transform into a more powerful piece, Raichu. The game ends when one player jumps all the opponent's pieces.

### Part 2: Truth be Told

The task was to classify text objects into two categories using the Naive Bayes classifier. The challenge involved processing the text, calculating the likelihood of each class based on the training data, and classifying new unseen data accurately.

## Methodology/Approach

### Part 1: Raichu

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

### Part 2: Truth be Told

The text classification program employs Naive Bayes to classify text objects. Its main functions are:
- `load_file(filename)`: Loads the text file and separates it into labels and objects for processing.
- `classifier(train_data, test_data)`: The core function where the Naive Bayes classifier is implemented. It processes training data to calculate class priors and word likelihoods, then applies these to classify test objects.
The code uses regular expressions to clean and split the input text into words. It uses dictionaries to keep track of word counts and class occurrences, which are then used to calculate probabilities needed for the Naive Bayes classification.

## Challenges Encountered

### Part 1: Raichu

The development of the Raichu game AI presented several substantial challenges, the most prominent of which revolved around the successor function and the distinct movement rules for the three types of pieces: Pichu, Pikachu, and Raichu.
Crafting the `successor_states` function required a deep understanding of the game's rules and to ensure that all possible moves were accounted for. The complexity of the game's mechanics made this a particularly difficult task. The differentiation in movement patterns and the promotion of Pichu to Pikachu and then to Raichu, each with its own unique rules, required careful consideration and meticulous testing to guarantee correctness.
Since the test cases were not provided, we had to come up with our own test case which was a difficult challenge on its own.
Debugging was also a significant hurdle due to the variety of possible board states and the strategic depth of Raichu.
 
### Part 2: Truth be Told

In contrast, Part 2 of the assignment was more straightforward. The implementation of the Naive Bayes classifier came with its own set of challenges but was less complex compared to the adversarial search in Part 1. The main issue encountered was ensuring that the text processing handled various edge cases, such as punctuation and case sensitivity, which could affect the accuracy of the classification.
