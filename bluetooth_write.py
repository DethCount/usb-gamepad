import time
import concurrent
import asyncio
import bleak

async def main():
    loop = asyncio.new_event_loop()

    client = bleak.BleakClient('D8:A9:8B:7E:1E:D2')
    is_connected = await client.connect()
    print(is_connected)
    response = await client.write_gatt_char('0000ffe1-0000-1000-8000-00805f9b34fb', b'MOVE X 0.000000')

    print(response)

if __name__ == "__main__":
    asyncio.run(main())
