
async def ask(websocket, username):
    data = {"username": username, "message": "do you want to play?"}
    await send(websocket, 'challenge', data)


async def accept(websocket, board_id):
    data = {"board_id": board_id}
    await send(websocket, 'challenge', data)




async def move(websocket, data):
    data = {
        'board_id': data['data']['board_id'],
        'turn_token': data['data']['turn_token'],
        'from_row': randint(0, 15),
        'from_col': randint(0, 15),
        'to_row': randint(0, 15),
        'to_col': randint(0, 15),
    }
    await send(websocket, 'move', data)

def update_board_dos(data_board):
    list_board = list(data_board)
    toArray = np.array(list_board)
    ToBoard = toArray.reshape(16, 16)
    return ToBoard

def update_board(data_board):
    to_list = list(data_board)
    board = list()
    for i in range(0, 256, 16):
        board.append(to_list[i:i + 16])
    return board


