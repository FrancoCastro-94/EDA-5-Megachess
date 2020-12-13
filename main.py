import asyncio
import json
import websockets
from data import AUTH_TOKEN, pretty_board
from play import play_black, play_white


async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    print(message)
    await websocket.send(message)


async def start(token):
    url = "ws://megachess.herokuapp.com/service?authtoken={}".format(token)
    while True:
        print('connection to {}'.format(url))
        async with websockets.connect(url) as websocket:
            await play(websocket)


async def play(websocket):
    while True:
        try:
            response = await websocket.recv()
            print(f"< {response}")
            data = json.loads(response)

            if data['event'] == 'update_user_list':
                msg = {"username": "Franco", "message": "do you want to play?"}
                await send(websocket, 'challenge', msg)
                continue

            if data['event'] == 'gameover':
                print(f"< {response}")

            if data['event'] == 'ask_challenge':
                if data['data']['username'] == 'Franco':
                    await send(websocket, 'accept_challenge', {'board_id': data['data']['board_id']})
                    print(f"< {response}")

            if data['event'] == 'your_turn':
                pretty_board(data['data']['board'])      # show the game on console
                my_turn = list()
                if data['data']['actual_turn'] == 'white':
                    my_turn = play_white(data['data'])
                if data['data']['actual_turn'] == 'black':
                    my_turn = play_black(data['data'])

                msg = {
                       'board_id': data['data']['board_id'],
                       'turn_token': data['data']['turn_token'],
                       'from_row': my_turn[0],
                       'from_col': my_turn[1],
                       'to_row': my_turn[2],
                       'to_col': my_turn[3],
                       }

                await send(websocket, 'move', msg)

        except Exception as e:
            print('error {}'.format(str(e)))
            break  # force login again


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(start(AUTH_TOKEN))
    except Exception as e:
        print(e)
