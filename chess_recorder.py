import time
from typing import List


class Move:
    def __init__(self, notation: str, player: str):
        self.notation = notation
        self.player = player  # 'White' or 'Black'

    def __str__(self):
        return f"{self.player}: {self.notation}"


class MoveHistory:
    def __init__(self):
        self.moves: List[Move] = []

    def add_move(self, move: Move):
        self.moves.append(move)

    def list_moves(self):
        for i, move in enumerate(self.moves, start=1):
            print(f"{i:02d}. {move}")

    def save_to_file(self, filename: str):
        with open(filename, 'w') as f:
            for move in self.moves:
                f.write(f"{move.player}: {move.notation}\n")
        print(f"Game saved to {filename}")

    def load_from_file(self, filename: str):
        self.moves.clear()
        try:
            with open(filename, 'r') as f:
                for line in f:
                    player, notation = line.strip().split(": ")
                    self.moves.append(Move(notation, player))
            print(f"Game loaded from {filename}")
        except FileNotFoundError:
            print("File not found.")

    def replay(self, delay=1):
        print("Replaying game...\n")
        for move in self.moves:
            print(move)
            time.sleep(delay)
        print("\nReplay finished.")


class ChessGame:
    def __init__(self):
        self.history = MoveHistory()
        self.current_turn = 'White'

    def input_move(self):
        notation = input(f"{self.current_turn}'s move (e.g., e4, Nf3, O-O): ").strip()
        if self.validate_notation(notation):
            self.history.add_move(Move(notation, self.current_turn))
            self.toggle_turn()
        else:
            print("Invalid notation. Please try again.")

    def toggle_turn(self):
        self.current_turn = 'Black' if self.current_turn == 'White' else 'White'

    def validate_notation(self, notation: str) -> bool:
        return bool(notation) and len(notation) <= 6

    def show_menu(self):
        print("\n=== Chess Notation Recorder ===")
        print("1. Input Move")
        print("2. Show Move History")
        print("3. Replay Game")
        print("4. Save Game")
        print("5. Load Game")
        print("6. Exit")

    def run(self):
        while True:
            self.show_menu()
            option = input("Select an option: ").strip()

            if option == '1':
                self.input_move()
            elif option == '2':
                self.history.list_moves()
            elif option == '3':
                self.history.replay()
            elif option == '4':
                filename = input("Enter filename to save: ").strip()
                self.history.save_to_file(filename)
            elif option == '5':
                filename = input("Enter filename to load: ").strip()
                self.history.load_from_file(filename)
            elif option == '6':
                print("Exiting...")
                break
            else:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    game = ChessGame()
    game.run()
