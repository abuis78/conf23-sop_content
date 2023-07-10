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

    # check for 'else' condition 2
    add_comment_3(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def format_endpoint_delete_sop(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_endpoint_delete_sop() called")

    template = """/rest/workbook_template/{0}"""

    # parameter list for template variable replacement
    parameters = [
        "get_sop_id_for_update:action_result.data.*.parsed_response_body.data.0.id"
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

    phantom.act("delete data", parameters=parameters, name="delete_sop", assets=["soar_http"], callback=join_noop_2)

    return


@phantom.playbook_block()
def debug_delete(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_delete() called")

    format_json_for_create = phantom.get_format_data(name="format_json_for_create")

    parameters = []

    parameters.append({
        "input_1": format_json_for_create,
        "input_2": None,
        "input_3": None,
        "input_4": None,
        "input_5": None,
        "input_6": None,
        "input_7": None,
        "input_8": None,
        "input_9": None,
        "input_10": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_delete")

    return


@phantom.playbook_block()
def join_noop_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("join_noop_2() called")

    # if the joined function has already been called, do nothing
    if phantom.get_run_data(key="join_noop_2_called"):
        return

    # save the state that the joined function has now been called
    phantom.save_run_data(key="join_noop_2_called", value="noop_2")

    # call connected block "noop_2"
    noop_2(container=container, handle=handle)

    return


@phantom.playbook_block()
def noop_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("noop_2() called")

    parameters = [{}]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/noop", parameters=parameters, name="noop_2", callback=check_for_valid_json)

    return


@phantom.playbook_block()
def post_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("post_data_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_json_for_create = phantom.get_format_data(name="format_json_for_create")

    parameters = []

    parameters.append({
        "location": "/rest/workbook_template",
        "body": format_json_for_create,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("post data", parameters=parameters, name="post_data_1", assets=["soar_http"])

    return


@phantom.playbook_block()
def add_comment_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_comment_3() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="The SOP will be created")

    join_noop_2(container=container)

    return


@phantom.playbook_block()
def check_for_valid_json(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("check_for_valid_json() called")

    playbook_input_sop_json = phantom.collect2(container=container, datapath=["playbook_input:sop_json"])

    playbook_input_sop_json_values = [item[0] for item in playbook_input_sop_json]

    check_for_valid_json__sop_json = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(playbook_input_sop_json_values)
    try:
        json_data = json.loads(playbook_input_sop_json_values)
        phantom.debug("The string is a valid JSON.")
        
        formatted_json = json.dumps(json_data, indent=2)
        phantom.debug(formatted_json)
        
    except ValueError as e:
        phantom.debug("The string is not a valid JSON.")
    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="check_for_valid_json:sop_json", value=json.dumps(check_for_valid_json__sop_json))

    debug_delete(container=container)

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