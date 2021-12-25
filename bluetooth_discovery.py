from asyncio import run
from bleak import BleakScanner, BleakClient

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)
        client = BleakClient(d.address)

        is_connected = False
        try:
            is_connected = await client.connect()
        except Exception:
            pass

        if is_connected:
            services = await client.get_services()
            for s in services:
                print(s)
                characs = s.characteristics
                print(len(characs))
                for c in characs:
                    print('Charac:', c)

            await client.disconnect()

if __name__ == "__main__":
    run(main())

