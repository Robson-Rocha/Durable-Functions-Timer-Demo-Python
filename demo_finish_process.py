import asyncio

from shared_code.key_value_store import KeyValueStore


async def main(instance_id: str, result: str) -> None:
    kvs = KeyValueStore(instance_id, 'https://keyvalue.immanuel.co/api/KeyVal')
    await kvs.set_value('Long_Running_Process_Finished', 'True')
    await kvs.set_value('Long_Running_Process_Result', result)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--instance_id", type=str, default=5, 
                        required=True)
    parser.add_argument("-r", "--result", type=str, default=10, 
                        required=True)
    ns = parser.parse_args()
    asyncio.get_event_loop().run_until_complete(main(**ns.__dict__))
