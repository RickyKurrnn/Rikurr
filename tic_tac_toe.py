# Manually defining the TwoPlayersGame class since it cannot be imported from easyAI
class TwoPlayersGame:
    def _init_(self, players):
        self.players = players
        self.nplayer = 1  # Set the first player to start

    def play(self):
        """Main game loop"""
        while not self.is_over():
            self.show()
            move = self.current_player.ask_move(self)  # Use current_player to get the next move
            self.make_move(move)
            self.switch_player()  # Use the switch_player method to change turns
        self.show()
        if self.loss_condition():
            print(f"Player {self.nopponent} wins!")
        else:
            print("It's a draw.")

    @property
    def current_player(self):
        """Return the player whose turn it is"""
        return self.players[self.nplayer - 1]

    @property
    def nopponent(self):
        """Get the opponent player"""
        return 3 - self.nplayer

    def switch_player(self):
        """Switch the current player"""
        self.nplayer = 3 - self.nplayer

# Importing other components from easyAI
from easyAI import AI_Player, Negamax
from easyAI.Player import Human_Player

# Extending the game logic for Tic Tac Toe
class GameController(TwoPlayersGame):
    def _init_(self, players):
        super()._init_(players)
        self.board = [0] * 9  # Initialize the board

    # Define possible moves
    def possible_moves(self):
        return [a + 1 for a, b in enumerate(self.board) if b == 0]

    # Make a move
    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

    # Does the opponent have three in a line?
    def loss_condition(self):
        possible_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]
        return any([all([(self.board[i - 1] == self.nopponent) for i in combination]) for combination in possible_combinations])

    # Check if the game is over
    def is_over(self):
        return (self.possible_moves() == []) or self.loss_condition()

    # Show current position
    def show(self):
        print('\n' + '\n'.join([' '.join([['.', 'O', 'X'][self.board[3 * j + i]]
                                         for i in range(3)]) for j in range(3)]))

    # Compute the score
    def scoring(self):
        return -100 if self.loss_condition() else 0

    # Implement the copy method to allow AI to simulate moves
    def copy(self):
        """Create a copy of the current game state"""
        copied_game = GameController(self.players)
        copied_game.board = self.board[:]
        copied_game.nplayer = self.nplayer
        return copied_game

if __name__ =1
== "_main_":
    # Define the algorithm
    algorithm = Negamax(7)

    # Start the game
    GameController([Human_Player(), AI_Player(algorithm)]).play()