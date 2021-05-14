import chess

from chess import Board, Move, STARTING_FEN


piece_values = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000,
}


board = chess.Board("N7/p4pk1/1PP5/2Pn4/1R2b1r1/5pp1/3p4/5Kb1 w - - 0 1")

print(board)

print("Hello World")
