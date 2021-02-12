import logging

import azure.functions as func

from shared_code.key_value_store import KeyValueStore


async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    instanceid = req.params.get('instanceid')

    kvs = KeyValueStore(instanceid)
    await kvs.set_value('Long_Running_Process_Finished', 'True')

    return func.HttpResponse(
            f"{instanceid} process 'Long_Running_Process_Finished' key set to 'True'",
            status_code=200
    )
