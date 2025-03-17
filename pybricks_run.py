
import sys
import asyncio
import contextlib

from pybricksdev.ble import find_device
from pybricksdev.connections.pybricks import PybricksHubBLE

# this script must be in the current working directory and will be sent to the hub
MY_PROGRAM = sys.argv[1]

async def main():
    async with contextlib.AsyncExitStack() as stack:
        dev = await find_device()
        hub = PybricksHubBLE(dev)
        await hub.connect()
        stack.push_async_callback(hub.disconnect)
        stack.push_async_callback(hub.stop_user_program)
        await hub.run(MY_PROGRAM, print_output=True, wait=True)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Goodbye!")

