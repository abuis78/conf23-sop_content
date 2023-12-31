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

    phantom.comment(container=container, comment="reference list NOT exists")

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
        "body": format_payload,
        "location": "/rest/decided_list",
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

    phantom.custom_function(custom_function="community/noop", parameters=parameters, name="noop_5", callback=filter_sop_artifacts)

    return


@phantom.playbook_block()
def finde_sop_in_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("finde_sop_in_list() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    playbook_input_liste_name = phantom.collect2(container=container, datapath=["playbook_input:liste_name"])
    filtered_artifact_0_data_filter_sop_artifacts = phantom.collect2(container=container, datapath=["filtered-data:filter_sop_artifacts:condition_1:artifact:*.cef.name","filtered-data:filter_sop_artifacts:condition_1:artifact:*.id"])

    parameters = []

    # build parameters list for 'finde_sop_in_list' call
    for playbook_input_liste_name_item in playbook_input_liste_name:
        for filtered_artifact_0_item_filter_sop_artifacts in filtered_artifact_0_data_filter_sop_artifacts:
            if playbook_input_liste_name_item[0] is not None and filtered_artifact_0_item_filter_sop_artifacts[0] is not None:
                parameters.append({
                    "list": playbook_input_liste_name_item[0],
                    "values": filtered_artifact_0_item_filter_sop_artifacts[0],
                    "exact_match": True,
                    "column_index": 0,
                    "context": {'artifact_id': filtered_artifact_0_item_filter_sop_artifacts[1]},
                })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("find listitem", parameters=parameters, name="finde_sop_in_list", assets=["phantom"], callback=decision_if_match_found)

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

    phantom.act("add listitem", parameters=parameters, name="add_listitem_1", assets=["phantom"], callback=format_sop_version_check_new_1)

    return


@phantom.playbook_block()
def format_list_json_append_sop(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_list_json_append_sop() called")

    template = """[\"{0}\", \"{1}\"]"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:filter_sop_artifacts:condition_1:artifact:*.cef.name",
        "filtered-data:filter_sop_artifacts:condition_1:artifact:*.cef.version"
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
            ["filtered-data:filter_sop_artifacts:condition_1:artifact:*.cef.version", ">", "filtered-data:filter_found_sop:condition_1:finde_sop_in_list:action_result.data.0.1"]
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
            ["filtered-data:filter_sop_artifacts:condition_1:artifact:*.cef.version", "<=", "filtered-data:filter_found_sop:condition_1:finde_sop_in_list:action_result.data.0.1"]
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
            ["finde_sop_in_list:action_result.data.0.0", "==", "filtered-data:filter_sop_artifacts:condition_1:artifact:*.name"]
        ],
        name="filter_found_sop:condition_1",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        decision_version_check(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

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

    format_sop_version_check_current(container=container)

    return


@phantom.playbook_block()
def update_version_no_in_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("update_version_no_in_list() called")

    playbook_input_sop_version = phantom.collect2(container=container, datapath=["playbook_input:sop_version"])
    playbook_input_liste_name = phantom.collect2(container=container, datapath=["playbook_input:liste_name"])
    playbook_input_sop_name = phantom.collect2(container=container, datapath=["playbook_input:sop_name"])
    finde_sop_in_list_result_data = phantom.collect2(container=container, datapath=["finde_sop_in_list:action_result.summary.locations.0.0"], action_results=results)

    playbook_input_sop_version_values = [item[0] for item in playbook_input_sop_version]
    playbook_input_liste_name_values = [item[0] for item in playbook_input_liste_name]
    playbook_input_sop_name_values = [item[0] for item in playbook_input_sop_name]
    finde_sop_in_list_summary_locations_0_0 = [item[0] for item in finde_sop_in_list_result_data]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    sop_version = playbook_input_sop_version[0][0]
    sop_name = playbook_input_sop_name[0][0]
    liste_name = playbook_input_liste_name[0][0]
    list_position = finde_sop_in_list_summary_locations_0_0[0]
    
    phantom.debug(sop_version)
    phantom.debug(sop_name)
    phantom.debug(liste_name)
    phantom.debug(list_position)
    
    
    decided_list_tag_url = phantom.build_phantom_rest_url('decided_list',liste_name)
    data = { "update_rows": { list_position: [sop_name, sop_version]}}
    phantom.debug(data)
    response = phantom.requests.post(decided_list_tag_url,json=data,verify=False)
    phantom.debug("phantom returned status code {} with message {}".format(response.status_code, response.text))
    ################################################################################
    ## Custom Code End
    ################################################################################

    format_comment_update(container=container)

    return


@phantom.playbook_block()
def add_comment_13(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_comment_13() called")

    format_comment_update = phantom.get_format_data(name="format_comment_update")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment=format_comment_update)

    format_sop_version_check_updated(container=container)

    return


@phantom.playbook_block()
def format_comment_update(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_comment_update() called")

    template = """SOP Version no. was set to: {0}\n"""

    # parameter list for template variable replacement
    parameters = [
        "filtered-data:filter_sop_artifacts:condition_1:artifact:*.cef.version"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_comment_update")

    add_comment_13(container=container)

    return


@phantom.playbook_block()
def format_sop_version_check_updated(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_sop_version_check_updated() called")

    template = """update"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_sop_version_check_updated")

    join_noop_15(container=container)

    return


@phantom.playbook_block()
def format_sop_version_check_current(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_sop_version_check_current() called")

    template = """nothing_to_do"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_sop_version_check_current")

    join_noop_15(container=container)

    return


@phantom.playbook_block()
def format_sop_version_check_new_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_sop_version_check_new_1() called")

    template = """newly_created"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_sop_version_check_new_1")

    join_noop_15(container=container)

    return


@phantom.playbook_block()
def join_noop_15(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("join_noop_15() called")

    # if the joined function has already been called, do nothing
    if phantom.get_run_data(key="join_noop_15_called"):
        return

    # save the state that the joined function has now been called
    phantom.save_run_data(key="join_noop_15_called", value="noop_15")

    # call connected block "noop_15"
    noop_15(container=container, handle=handle)

    return


@phantom.playbook_block()
def noop_15(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("noop_15() called")

    parameters = [{}]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/noop", parameters=parameters, name="noop_15", callback=set_type_of_update_in_the_list)

    return


@phantom.playbook_block()
def set_type_of_update_in_the_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("set_type_of_update_in_the_list() called")

    format_sop_version_check_updated = phantom.get_format_data(name="format_sop_version_check_updated")
    format_sop_version_check_current = phantom.get_format_data(name="format_sop_version_check_current")
    format_sop_version_check_new_1 = phantom.get_format_data(name="format_sop_version_check_new_1")

    set_type_of_update_in_the_list__status_type = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug("Update {}".format(format_sop_version_check_updated))
    phantom.debug("Current {}".format(format_sop_version_check_current))
    phantom.debug("New {}".format(format_sop_version_check_new_1))
    
    if format_sop_version_check_updated is not "":
        set_type_of_update_in_the_list__status_type = format_sop_version_check_updated
    elif format_sop_version_check_current is not "":
        set_type_of_update_in_the_list__status_type = format_sop_version_check_current
    elif format_sop_version_check_new_1 is not "":
        set_type_of_update_in_the_list__status_type = format_sop_version_check_new_1
        
    phantom.debug("Ausgabe {}".format(set_type_of_update_in_the_list__status_type))

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="set_type_of_update_in_the_list:status_type", value=json.dumps(set_type_of_update_in_the_list__status_type))

    return

@phantom.playbook_block()
def filter_sop_artifacts(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_sop_artifacts() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["SOP", "in", "artifact:*.name"]
        ],
        name="filter_sop_artifacts:condition_1",
        scope="all",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        update_sop_custom_list_1(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def update_sop_custom_list_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("update_sop_custom_list_1() called")

    id_value = container.get("id", None)
    filtered_artifact_0_data_filter_sop_artifacts = phantom.collect2(container=container, datapath=["filtered-data:filter_sop_artifacts:condition_1:artifact:*.id","filtered-data:filter_sop_artifacts:condition_1:artifact:*.id"])

    filtered_artifact_0__id = [item[0] for item in filtered_artifact_0_data_filter_sop_artifacts]

    parameters = []

    parameters.append({
        "artifact_id_list": filtered_artifact_0__id,
        "container_id": id_value,
        "prefix_filter": "SOP",
        "list_name": "SOP",
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="conf23-sop_content/update_SOP_custom_list", parameters=parameters, name="update_sop_custom_list_1")

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    set_type_of_update_in_the_list__status_type = json.loads(_ if (_ := phantom.get_run_data(key="set_type_of_update_in_the_list:status_type")) != "" else "null")  # pylint: disable=used-before-assignment

    output = {
        "sop_in_list_status": set_type_of_update_in_the_list__status_type,
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