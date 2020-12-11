from shared_code.key_value_store import KeyValueStore


async def main(instanceid: str) -> bool:
    kvs = KeyValueStore(instanceid)
    return await kvs.get_value('Long_Running_Process_Result')
