class ChessBoard:
    def __init__(self, size=5):
        self.size = size
        self.board = [[0] * size for _ in range(size)]
        self.moves_tried = 0

        # The ways a knight can move
        self.knight_moves = [
            (2, 1), (1, 2),    # Forward right
            (-1, 2), (-2, 1),  # Forward left
            (-2, -1), (-1, -2),  # Back left
            (1, -2), (2, -1)   # Back right
        ]

    def can_move_to(self, row, col):
        # Simple boundary and empty square check
        if row < 0 or col < 0 or row >= self.size or col >= self.size:
            return False
        return self.board[row][col] == 0

    def print_solution(self):
        # Print the board with proper spacing
        for row in self.board:
            print(' '.join(f'{move:2}' for move in row))
        print(f'\nTook {self.moves_tried} attempts to find this solution')

    def print_empty_board(self):
        # Print the board showing the movement space ('.' for empty squares)
        for row in self.board:
            print(' '.join(f'{cell:2}' if cell != 0 else ' 0' for cell in row))
        print()

    def solve(self):
        # Start from top-left corner
        self.board[0][0] = 1
        if self._find_tour(0, 0, move_number=2):
            return True
        return False

    def _find_tour(self, row, col, move_number):
        self.moves_tried += 1

        # Success! We filled the whole board
        if move_number > self.size * self.size:
            return True

        # Try each possible knight move
        for x_step, y_step in self.knight_moves:
            next_row = row + x_step
            next_col = col + y_step

            # If we can move there
            if self.can_move_to(next_row, next_col):
                # Try this move
                self.board[next_row][next_col] = move_number

                # If this leads to a solution, great!
                if self._find_tour(next_row, next_col, move_number + 1):
                    return True

                # If not, backtrack and try another move
                self.board[next_row][next_col] = 0

        return False


# Example usage
if __name__ == '__main__':
    # Create a 5x5 chess board
    game = ChessBoard(5)
    # Show the empty movement space (5x5 board)
    print("\n Empty board (knight's movement space):")
    game.print_empty_board()

    # Try to solve it
    print("Looking for a Knight's Tour solution...")
    if game.solve():
        print('\nFound a solution!')
        game.print_solution()
    else:
        print('\nNo solution exists for this board size')
