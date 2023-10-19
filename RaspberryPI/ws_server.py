import asyncio
import ssl
import websockets
from datetime import datetime
import RPi.GPIO as GPIO

#GPIO PINS
inputA_pin = 11;
inputB_pin = 13

# GPIO Configs
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inputA_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(inputB_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


async def button_server(websocket, path):
    while True:
        await asyncio.sleep(1)
        
        # In your actual code, replace this with your button press logic
        button_pressed = 0

        inputA_value = GPIO.input(inputA_pin)
        inputB_value = GPIO.input(inputB_pin)
       
        if inputA_value == 1:
            message = "ButtonA"
            await websocket.send(message)
        elif inputB_value == 1:
            message = "ButtonB"
            await websocket.send(message)

        # await asyncio.sleep(0.05)  # Adjust the sleep interval as needed


print("Starting websocket server on ws://localhost:8765")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('certs2/server.crt', 'certs2/server.key')


# start_server = websockets.serve(button_server, "localhost", 8765, ssl=ssl_context)
start_server = websockets.serve(button_server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

