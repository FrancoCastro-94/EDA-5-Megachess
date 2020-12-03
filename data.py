from service import update_board

b = 'rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                            ' \
    '                                                                                    ' \
    'PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR'

AUTH_TOKEN = '0d26fca5-bf53-4fd4-9ec5-c575fe16e76f'

id_game = ''


def board():
    return update_board(b)
