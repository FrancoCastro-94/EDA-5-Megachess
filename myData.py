import numpy as np

token = '0d26fca5-bf53-4fd4-9ec5-c575fe16e76f'
# FrancoDos = '8b3573bf-6850-40f3-87f1-13c346819f7b'

board = 'rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR'

def getBoard():
    toList = list(board)
    toArray = np.array(toList)
    ToBoard = toArray.reshape(16, 16)
    return ToBoard

def getToken():
    return token
