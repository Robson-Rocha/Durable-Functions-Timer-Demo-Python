from shared_code.key_value_store import KeyValueStore


async def main(instanceid: str) -> bool:
    kvs = KeyValueStore(instanceid)
    await kvs.set_value('Long_Running_Process_Finished', 'False')
    return 'Process started'
