import asyncio
import json
from random import randint
import sys
import websockets


# Franco = '0d26fca5-bf53-4fd4-9ec5-c575fe16e76f'      <-- me
auth_token = '8b3573bf-6850-40f3-87f1-13c346819f7b'  # <-- opponent


async def send(websocket, action, data):
    message = json.dumps(
        {
            'action': action,
            'data': data,
        }
    )
    print(message)
    await websocket.send(message)

"""
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
"""

async def start(auth_token):
    uri = "ws://megachess.herokuapp.com/service?authtoken={}".format(auth_token)
    while True:
        print('connection to {}'.format(uri))
        async with websockets.connect(uri) as websocket:
            await play(websocket)


async def play(websocket):
    while True:
        try:
            response = await websocket.recv()
            print(f"< {response}")
            data = json.loads(response)

            if data['event'] == 'update_user_list':
                # await ask(websocket, 'Franco')
                continue
            if data['event'] == 'gameover':
                print('el juego ha finalizado')

            if data['event'] == 'ask_challenge':

                if data['data']['username'] == 'Franco':
                    print(f"< {response}")
                    await send(websocket, 'accept_challenge', {'board_id': data['data']['board_id']} )  # recordar las comas

            if data['event'] == 'your_turn':
                await send(websocket, 'move',
                           {
                               'board_id': data['data']['board_id'],
                               'turn_token': data['data']['turn_token'],
                               'from_row': randint(0, 15),
                               'from_col': randint(0, 15),
                               'to_row': randint(0, 15),
                               'to_col': randint(0, 15),
                           },
                           )

        except Exception as e:
            print('error {}'.format(str(e)))
            break  # force login again


if __name__ == '__main__':
   # if len(sys.argv) >= 2:
       # auth_token = sys.argv[1]
        asyncio.get_event_loop().run_until_complete(start(auth_token))
  #  else:
  #      print('please provide your auth_token')
