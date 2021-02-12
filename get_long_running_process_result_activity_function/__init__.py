from shared_code.key_value_store import KeyValueStore


async def main(instanceid: str) -> bool:
    kvs = KeyValueStore(instanceid)
    value = await kvs.get_value('Long_Running_Process_Finished')
    return value
