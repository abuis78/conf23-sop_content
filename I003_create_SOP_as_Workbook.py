"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'decision_task_type' block
    decision_task_type(container=container)

    return

@phantom.playbook_block()
def format_endpoint_find_sop(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_endpoint_find_sop() called")

    template = """/rest/workbook_template?_filter_name=\"{0}\""""

    # parameter list for template variable replacement
    parameters = [
        "playbook_input:sop_name"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_endpoint_find_sop")

    get_sop_id_for_update(container=container)

    return


@phantom.playbook_block()
def get_sop_id_for_update(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_sop_id_for_update() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_endpoint_find_sop = phantom.get_format_data(name="format_endpoint_find_sop")

    parameters = []

    if format_endpoint_find_sop is not None:
        parameters.append({
            "location": format_endpoint_find_sop,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("get data", parameters=parameters, name="get_sop_id_for_update", assets=["soar_http"], callback=format_endpoint_delete_sop)

    return


@phantom.playbook_block()
def decision_task_type(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_task_type() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["playbook_input:task", "==", "update"]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        format_endpoint_find_sop(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def format_endpoint_delete_sop(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_endpoint_delete_sop() called")

    template = """/rest/workbook_template/{0}"""

    # parameter list for template variable replacement
    parameters = [
        "get_sop_id_for_update:action_result.data.*.response_body.*.id"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_endpoint_delete_sop")

    delete_sop(container=container)

    return


@phantom.playbook_block()
def delete_sop(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("delete_sop() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_endpoint_delete_sop = phantom.get_format_data(name="format_endpoint_delete_sop")

    parameters = []

    if format_endpoint_delete_sop is not None:
        parameters.append({
            "location": format_endpoint_delete_sop,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("delete data", parameters=parameters, name="delete_sop", assets=["soar_http"])

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    output = {
        "sop_id": [],
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_playbook_output_data(output=output)

    return