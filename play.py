import numpy
from random import randint
from turn import WhiteTurn, BlackTurn


def create_table(data_board):   # takes the board as a string and converts it to a 2x2 table
    list_board = list(data_board)
    to_array = numpy.array(list_board)
    to_table = to_array.reshape(16, 16)
    return to_table


def move_horse(horses):
    for h in horses:
        if h.move:
            return h.move


# to start moving a group of pawns then move the most advanced pawn
def move_pieces(pawns, horses, board, move_lef):

    if move_lef > 140:
        for p in pawns:
            if p.col < 8:    # group of pawns
                move = p.move(board)
                if move:
                    return move

    for p in reversed(pawns):   # take the most advanced pawn
        move = p.move(board)
        if move:
            return move

    move = move_horse(horses)    # if pawns move is not possible, this move a horse
    return move


def select_attack(attacks):
    for a in attacks:
        if a:
            return a


def forced_move():
    move = [randint(0, 15), randint(0, 15), randint(0, 15), randint(0, 15)]
    return move


def play_black(data):   # find for a possible attack, if there isn't then move a piece
    current_board = create_table(data['board'])
    turn = BlackTurn(current_board)
    attack = select_attack(turn.update_pieces())
    try:
        if attack:
            return [attack[1], attack[2], attack[3], attack[4]]
        move = move_pieces(turn.pawns, turn.horses, turn.board, data['move_left'])
        if move:
            return [move[0], move[1], move[2], move[3]]
        else:
            forced_move()

    except Exception as e:
        print(e)
        return forced_move()


def play_white(data):   # find for a possible attack, if there isn't then move a piece
    current_board = create_table(data['board'])
    turn = WhiteTurn(current_board)
    attack = select_attack(turn.update_pieces())
    try:
        if attack:
            return [attack[1], attack[2], attack[3], attack[4]]
        move = move_pieces(turn.pawns, turn.horses, turn.board, data['move_left'])
        if move:
            return [move[0], move[1], move[2], move[3]]
        else:
            forced_move()

    except Exception as e:
        print(e)
        return forced_move()
