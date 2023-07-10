"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'check_if_reference_list_exists' block
    check_if_reference_list_exists(container=container)

    return

@phantom.playbook_block()
def check_if_reference_list_exists(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("check_if_reference_list_exists() called")

    playbook_input_liste_name = phantom.collect2(container=container, datapath=["playbook_input:liste_name"])

    playbook_input_liste_name_values = [item[0] for item in playbook_input_liste_name]

    check_if_reference_list_exists__list_status = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here.../rest/decided_list?_filter_name="SOP"
    phantom.debug(playbook_input_liste_name[0][0])
    liste_name = playbook_input_liste_name[0][0]
    decided_list_tag_url = phantom.build_phantom_rest_url('decided_list')
    filter_parameter = '?_filter_name="' + liste_name + '"'
    url = decided_list_tag_url + filter_parameter
    phantom.debug(url)
    response = phantom.requests.get(url,verify=False)
    
    phantom.debug(response.json()['count'])
    check_if_reference_list_exists__list_status = response.json()['count']

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="check_if_reference_list_exists:list_status", value=json.dumps(check_if_reference_list_exists__list_status))

    decision_1(container=container)

    return


@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["check_if_reference_list_exists:custom_function:list_status", "==", 1]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        add_comment_3(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    add_comment_4(action=action, success=success, container=container, results=results, handle=handle)

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

    phantom.comment(container=container, comment="reference list exists")

    join_noop_5(container=container)

    return


@phantom.playbook_block()
def add_comment_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_comment_4() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="add missing reference list")

    format_payload(container=container)

    return


@phantom.playbook_block()
def format_payload(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_payload() called")

    template = """{\"content\":[[\"name\",\"version\"]],\"name\":\"SOP\"}"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_payload")

    post_data_1(container=container)

    return


@phantom.playbook_block()
def post_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("post_data_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    format_payload = phantom.get_format_data(name="format_payload")

    parameters = []

    parameters.append({
        "location": "/rest/decided_list",
        "body": format_payload,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("post data", parameters=parameters, name="post_data_1", assets=["soar_http"], callback=join_noop_5)

    return


@phantom.playbook_block()
def join_noop_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("join_noop_5() called")

    # if the joined function has already been called, do nothing
    if phantom.get_run_data(key="join_noop_5_called"):
        return

    # save the state that the joined function has now been called
    phantom.save_run_data(key="join_noop_5_called", value="noop_5")

    # call connected block "noop_5"
    noop_5(container=container, handle=handle)

    return


@phantom.playbook_block()
def noop_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("noop_5() called")

    parameters = [{}]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/noop", parameters=parameters, name="noop_5", callback=find_listitem_1)

    return


@phantom.playbook_block()
def find_listitem_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("find_listitem_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    playbook_input_liste_name = phantom.collect2(container=container, datapath=["playbook_input:liste_name"])

    parameters = []

    # build parameters list for 'find_listitem_1' call
    for playbook_input_liste_name_item in playbook_input_liste_name:
        if playbook_input_liste_name_item[0] is not None:
            parameters.append({
                "exact_match": True,
                "list": playbook_input_liste_name_item[0],
                "column_index": 0,
                "values": playbook_input_liste_name_item[0],
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("find listitem", parameters=parameters, name="find_listitem_1", assets=["phantom"], callback=debug_6)

    return


@phantom.playbook_block()
def debug_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_6() called")

    find_listitem_1_result_data = phantom.collect2(container=container, datapath=["find_listitem_1:action_result.message","find_listitem_1:action_result.parameter.context.artifact_id"], action_results=results)

    find_listitem_1_result_message = [item[0] for item in find_listitem_1_result_data]

    parameters = []

    parameters.append({
        "input_1": find_listitem_1_result_message,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_6")

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return