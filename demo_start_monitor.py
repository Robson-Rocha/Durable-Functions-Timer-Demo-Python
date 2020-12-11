import aiohttp
import asyncio
from datetime import datetime


async def get_json(url: str) -> dict:
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            return await response.json()

async def start_process() -> dict:
    return await get_json('http://localhost:7071/api/starter_function')

async def monitor_process(process: dict) -> None:
    while True:
        await asyncio.sleep(1)
        status = await get_json(process['statusQueryGetUri'])
        instance_id = status['instanceId']
        output = status['output']
        runtimeStatus = status['runtimeStatus']
        time = datetime.now().strftime("%H:%M:%S")
        if runtimeStatus == 'Pending':
            print(f'[{time} - {instance_id}] Process is starting...')
        elif runtimeStatus == 'Running':
            print(f'[{time} - {instance_id}] Process is running...')
        elif runtimeStatus == 'Completed':
            print(f'[{time} - {instance_id}] Process has COMPLETED with result "{output}"')
            break
        elif runtimeStatus == 'Failed':
            print(f'[{time} - {instance_id}] Process has FAILED with result "{output}"')
            break
        else:
            print(f'[{time} - {instance_id}] Process status is "{runtimeStatus}"...')

async def main() -> None:
    process = await start_process()
    print(f'''Instance ID: {process['id']}''')
    await monitor_process(process)

if __name__ == "__main__":
    try:
        #asyncio.run(main())
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        print('User stopped monitoring')
    except aiohttp.client_exceptions.ClientConnectorError:
        print('Unable to connect')
