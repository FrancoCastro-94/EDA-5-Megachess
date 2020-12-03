import asyncio
import json
import websockets
from service import play_black, play_white

AUTH_TOKEN = '0d26fca5-bf53-4fd4-9ec5-c575fe16e76f'


async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    print(message)
    await websocket.send(message)


async def start(auth_token):
    url = "ws://megachess.herokuapp.com/service?authtoken={}".format(auth_token)
    while True:
        print('connection to {}'.format(url))
        async with websockets.connect(url) as websocket:
            await play(websocket)


async def play(websocket):
    global _in_game
    while True:
        try:
            response = await websocket.recv()
            print(f"< {response}")
            data = json.loads(response)

            if data['event'] == 'update_user_list':
                newData = {"username": "Franco", "message": "do you want to play?"}
                await send(websocket, 'challenge', newData)

            if data['event'] == 'gameover':
                continue

            if data['event'] == 'ask_challenge':
                if data['data']['username'] == 'Franco':
                    await send(websocket, 'accept_challenge', {'board_id': data['data']['board_id']})
                    print(f"< {response}")

            if data['event'] == 'your_turn':  # and id_game == data['data']['board_id']
                if data['data']['actual_turn'] == 'white':
                    my_turn = play_white(data['data'])
                if data['data']['actual_turn'] == 'black':
                    my_turn = play_black(data['data'])
                await send(websocket, 'move',
                           {
                               'board_id': data['data']['board_id'],
                               'turn_token': data['data']['turn_token'],
                               'from_row': my_turn[0],
                               'from_col': my_turn[1],
                               'to_row': my_turn[2],
                               'to_col': my_turn[3],
                           },
                           )

        except Exception as e:
            print('error {}'.format(str(e)))
            break  # force login again


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(start(AUTH_TOKEN))
    except:
        print('Algo ocurrio, corra de nuevo el programa')
