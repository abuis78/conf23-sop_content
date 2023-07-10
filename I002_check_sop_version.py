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

    phantom.custom_function(custom_function="community/noop", parameters=parameters, name="noop_5", callback=finde_sop_in_list)

    return


@phantom.playbook_block()
def finde_sop_in_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("finde_sop_in_list() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    playbook_input_liste_name = phantom.collect2(container=container, datapath=["playbook_input:liste_name"])
    playbook_input_sop_name = phantom.collect2(container=container, datapath=["playbook_input:sop_name"])

    parameters = []

    # build parameters list for 'finde_sop_in_list' call
    for playbook_input_liste_name_item in playbook_input_liste_name:
        for playbook_input_sop_name_item in playbook_input_sop_name:
            if playbook_input_liste_name_item[0] is not None and playbook_input_sop_name_item[0] is not None:
                parameters.append({
                    "exact_match": True,
                    "list": playbook_input_liste_name_item[0],
                    "column_index": 0,
                    "values": playbook_input_sop_name_item[0],
                })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("find listitem", parameters=parameters, name="finde_sop_in_list", assets=["phantom"], callback=finde_sop_in_list_callback)

    return


@phantom.playbook_block()
def finde_sop_in_list_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("finde_sop_in_list_callback() called")

    
    mutch_debug(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)
    decision_if_match_found(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=filtered_artifacts, filtered_results=filtered_results)


    return


@phantom.playbook_block()
def mutch_debug(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("mutch_debug() called")

    finde_sop_in_list_result_data = phantom.collect2(container=container, datapath=["finde_sop_in_list:action_result.summary.found_matches","finde_sop_in_list:action_result.data.0.1","finde_sop_in_list:action_result.parameter.context.artifact_id"], action_results=results)

    finde_sop_in_list_summary_found_matches = [item[0] for item in finde_sop_in_list_result_data]
    finde_sop_in_list_result_item_1 = [item[1] for item in finde_sop_in_list_result_data]

    parameters = []

    parameters.append({
        "input_1": finde_sop_in_list_summary_found_matches,
        "input_2": finde_sop_in_list_result_item_1,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="mutch_debug")

    return


@phantom.playbook_block()
def decision_if_match_found(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_if_match_found() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["finde_sop_in_list:action_result.summary.found_matches", "==", 1]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        add_comment_7(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 2
    found_match_2 = phantom.decision(
        container=container,
        conditions=[
            ["finde_sop_in_list:action_result.summary.found_matches", "==", 0]
        ],
        delimiter=None)

    # call connected blocks if condition 2 matched
    if found_match_2:
        add_comment_8(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def add_comment_7(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_comment_7() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="SOP found in list")

    filter_found_sop(container=container)

    return


@phantom.playbook_block()
def add_comment_8(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_comment_8() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="SOP not found in list")

    format_list_json_append_sop(container=container)

    return


@phantom.playbook_block()
def add_listitem_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_listitem_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    playbook_input_liste_name = phantom.collect2(container=container, datapath=["playbook_input:liste_name"])
    format_list_json_append_sop = phantom.get_format_data(name="format_list_json_append_sop")

    parameters = []

    # build parameters list for 'add_listitem_1' call
    for playbook_input_liste_name_item in playbook_input_liste_name:
        if playbook_input_liste_name_item[0] is not None and format_list_json_append_sop is not None:
            parameters.append({
                "list": playbook_input_liste_name_item[0],
                "new_row": format_list_json_append_sop,
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("add listitem", parameters=parameters, name="add_listitem_1", assets=["phantom"])

    return


@phantom.playbook_block()
def format_list_json_append_sop(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_list_json_append_sop() called")

    template = """[\"{0}\", \"{1}\"]"""

    # parameter list for template variable replacement
    parameters = [
        "playbook_input:sop_name",
        "playbook_input:sop_version"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_list_json_append_sop")

    add_listitem_1(container=container)

    return


@phantom.playbook_block()
def decision_version_check(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_version_check() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["playbook_input:sop_version", ">", "filtered-data:filter_found_sop:condition_1:finde_sop_in_list:action_result.data.0.1"]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        add_comment_10(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 2
    found_match_2 = phantom.decision(
        container=container,
        conditions=[
            ["playbook_input:sop_version", "<=", "filtered-data:filter_found_sop:condition_1:finde_sop_in_list:action_result.data.0.1"]
        ],
        delimiter=None)

    # call connected blocks if condition 2 matched
    if found_match_2:
        add_comment_11(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def filter_found_sop(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_found_sop() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["finde_sop_in_list:action_result.data.0.0", "==", "playbook_input:sop_name"]
        ],
        name="filter_found_sop:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        debug_9(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)
        decision_version_check(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def debug_9(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_9() called")

    filtered_result_0_data_filter_found_sop = phantom.collect2(container=container, datapath=["filtered-data:filter_found_sop:condition_1:finde_sop_in_list:action_result.data.0.0","filtered-data:filter_found_sop:condition_1:finde_sop_in_list:action_result.data.0.1"])

    filtered_result_0_data_0_0 = [item[0] for item in filtered_result_0_data_filter_found_sop]
    filtered_result_0_data_0_1 = [item[1] for item in filtered_result_0_data_filter_found_sop]

    parameters = []

    parameters.append({
        "input_1": filtered_result_0_data_0_0,
        "input_2": filtered_result_0_data_0_1,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_9")

    return


@phantom.playbook_block()
def add_comment_10(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_comment_10() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="There is a new version")

    update_version_no_in_list(container=container)

    return


@phantom.playbook_block()
def add_comment_11(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_comment_11() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="The version is the same or older than the existing one")

    return


@phantom.playbook_block()
def update_version_no_in_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("update_version_no_in_list() called")

    playbook_input_sop_version = phantom.collect2(container=container, datapath=["playbook_input:sop_version"])
    playbook_input_liste_name = phantom.collect2(container=container, datapath=["playbook_input:liste_name"])
    playbook_input_sop_name = phantom.collect2(container=container, datapath=["playbook_input:sop_name"])

    playbook_input_sop_version_values = [item[0] for item in playbook_input_sop_version]
    playbook_input_liste_name_values = [item[0] for item in playbook_input_liste_name]
    playbook_input_sop_name_values = [item[0] for item in playbook_input_sop_name]

    input_parameter_0 = 1

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    sop_version = playbook_input_sop_version[0][0]
    sop_name = playbook_input_sop_name[0][0]
    liste_name = playbook_input_liste_name[0][0]
    decided_list_tag_url = phantom.build_phantom_rest_url('decided_list',liste_name)
    data = { "update_rows": { "0": [sop_name, sop_version]}}
    response = phantom.requests.post(decided_list_tag_url,json=data,verify=False)
    ################################################################################
    ## Custom Code End
    ################################################################################

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