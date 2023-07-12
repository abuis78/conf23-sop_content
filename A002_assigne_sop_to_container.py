"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'search_for_sop_mapping' block
    search_for_sop_mapping(container=container)

    return

@phantom.playbook_block()
def search_for_sop_mapping(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("search_for_sop_mapping() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    name_value = container.get("name", None)

    parameters = []

    if name_value is not None:
        parameters.append({
            "exact_match": True,
            "list": "SOP",
            "column_index": 2,
            "values": name_value,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("find listitem", parameters=parameters, name="search_for_sop_mapping", assets=["phantom"], callback=decision_1)

    return


@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["search_for_sop_mapping:action_result.summary.found_matches", "==", 0]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        there_is_no_sop_mapping_to_this_allert(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    check_current_stage_of_process(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def there_is_no_sop_mapping_to_this_allert(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("there_is_no_sop_mapping_to_this_allert() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="There is no SOP mapping to this Allert")

    return


@phantom.playbook_block()
def there_is_a_mapping_between_sop_and_allert(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("there_is_a_mapping_between_sop_and_allert() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="There is a mapping between SOP and allert")

    playbook_i006_automated_processing_sop_1(container=container)

    return


@phantom.playbook_block()
def playbook_i006_automated_processing_sop_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i006_automated_processing_sop_1() called")

    search_for_sop_mapping_result_data = phantom.collect2(container=container, datapath=["search_for_sop_mapping:action_result.data.0.0"], action_results=results)

    search_for_sop_mapping_result_item_0 = [item[0] for item in search_for_sop_mapping_result_data]

    inputs = {
        "sop": search_for_sop_mapping_result_item_0,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "conf23-sop_content/I006_automated_processing_SOP", returns the playbook_run_id
    playbook_run_id = phantom.playbook("conf23-sop_content/I006_automated_processing_SOP", container=container, name="playbook_i006_automated_processing_sop_1", callback=playbook_i007_sop_automation_dispatcher_1, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_i007_sop_automation_dispatcher_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i007_sop_automation_dispatcher_1() called")

    search_for_sop_mapping_result_data = phantom.collect2(container=container, datapath=["search_for_sop_mapping:action_result.data.0.3"], action_results=results)

    search_for_sop_mapping_result_item_0 = [item[0] for item in search_for_sop_mapping_result_data]

    inputs = {
        "automation_phase": search_for_sop_mapping_result_item_0,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "conf23-sop_content/I007_sop_automation_dispatcher", returns the playbook_run_id
    playbook_run_id = phantom.playbook("conf23-sop_content/I007_sop_automation_dispatcher", container=container, name="playbook_i007_sop_automation_dispatcher_1", callback=check_automation_process_hud_6, inputs=inputs)

    return


@phantom.playbook_block()
def check_current_stage_of_process(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("check_current_stage_of_process() called")

    tags_value = container.get("tags", None)

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["a_progress", "in", tags_value]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        return

    # check for 'else' condition 2
    there_is_a_mapping_between_sop_and_allert(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def add_tag_to_container_a_progress(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_tag_to_container_a_progress() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_tags(container=container, tags="a_progress")

    container = phantom.get_container(container.get('id', None))

    return


@phantom.playbook_block()
def check_automation_process_hud_6(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("check_automation_process_hud_6() called")

    id_value = container.get("id", None)
    playbook_i007_sop_automation_dispatcher_1_output_phase_id = phantom.collect2(container=container, datapath=["playbook_i007_sop_automation_dispatcher_1:playbook_output:phase_id"])

    parameters = []

    # build parameters list for 'check_automation_process_hud_6' call
    for playbook_i007_sop_automation_dispatcher_1_output_phase_id_item in playbook_i007_sop_automation_dispatcher_1_output_phase_id:
        parameters.append({
            "status": 1,
            "container_id": id_value,
            "phase_id": playbook_i007_sop_automation_dispatcher_1_output_phase_id_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="conf23-sop_content/check_automation_process_hud", parameters=parameters, name="check_automation_process_hud_6", callback=add_tag_to_container_a_progress)

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