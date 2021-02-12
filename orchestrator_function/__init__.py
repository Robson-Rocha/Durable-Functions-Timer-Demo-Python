import datetime
import logging

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext) -> str:
    yield context.call_activity(
        'create_long_running_process_activity_function', context.instance_id)

    while True:
        fire_at = (context.current_utc_datetime 
                   + datetime.timedelta(seconds=5))
        yield context.create_timer(fire_at)
        long_running_process_finished = yield context.call_activity(
            'check_if_long_running_process_finished_activity_function',
            context.instance_id)
        if long_running_process_finished:
            break

    result = yield context.call_activity(
        'get_long_running_process_result_activity_function', 
        context.instance_id)
    
    logging.info('Long process finished with result %s', result)
    return result

main = df.Orchestrator.create(orchestrator_function)