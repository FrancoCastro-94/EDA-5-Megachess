from play import create_table

# 'b' is a default table to test
b = 'rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                ' \
    '                                                                                                ' \
    'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR'

AUTH_TOKEN = '0d26fca5-bf53-4fd4-9ec5-c575fe16e76f'

PRETTY_PIECES = {
    'p': '♟',
    'P': '♙',
    'r': '♜',
    'R': '♖',
    'k': '♚',
    'K': '♔',
    'h': '♞',
    'H': '♘',
    'b': '♝',
    'B': '♗',
    'q': '♛',
    'Q': '♕',
    ' ': ' ',
}


def board():
    return create_table(b)


def pretty_board(_string_board):
    _pretty_board = create_table(_string_board)
    for row in range(16):
        for col in range(16):
            piece = _pretty_board[row][col]
            _pretty_board[row][col] = PRETTY_PIECES[piece]

    print(_pretty_board)
