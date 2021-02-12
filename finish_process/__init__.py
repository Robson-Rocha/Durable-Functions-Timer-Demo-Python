import azure.functions as func

from shared_code.key_value_store import KeyValueStore


async def main(req: func.HttpRequest) -> func.HttpResponse:
    instanceid = req.params.get('instanceid')
    result = req.params.get('result')

    kvs = KeyValueStore(instanceid)
    await kvs.set_value('Long_Running_Process_Result', result)
    await kvs.set_value('Long_Running_Process_Finished', 'True')

    return func.HttpResponse(
            f"{instanceid} process and 'Long_Running_Process_Result' key set to '{result}'",
            status_code=200
    )
