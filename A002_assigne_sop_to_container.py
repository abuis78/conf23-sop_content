"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_i010_identify_the_use_caes_1' block
    playbook_i010_identify_the_use_caes_1(container=container)

    return

@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["check_if_alert_has_a_mapping_to_an_sop:custom_function:match", "==", 0]
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
    phantom.add_tags(container=container, tags="a_progress")

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

    check_if_alert_has_a_mapping_to_an_sop__sop = json.loads(_ if (_ := phantom.get_run_data(key="check_if_alert_has_a_mapping_to_an_sop:sop")) != "" else "null")  # pylint: disable=used-before-assignment

    inputs = {
        "sop": check_if_alert_has_a_mapping_to_an_sop__sop,
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

    check_if_alert_has_a_mapping_to_an_sop__automation_phase = json.loads(_ if (_ := phantom.get_run_data(key="check_if_alert_has_a_mapping_to_an_sop:automation_phase")) != "" else "null")  # pylint: disable=used-before-assignment

    inputs = {
        "automation_phase": check_if_alert_has_a_mapping_to_an_sop__automation_phase,
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
    phantom.set_label(container=container, label="conf_cases")
    phantom.set_severity(container=container, severity="high")
    phantom.set_sensitivity(container=container, sensitivity="amber")

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
            "phase_id": playbook_i007_sop_automation_dispatcher_1_output_phase_id_item[0],
            "container_id": id_value,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="conf23-sop_content/check_automation_process_hud", parameters=parameters, name="check_automation_process_hud_6", callback=decision_3)

    return


@phantom.playbook_block()
def decision_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_3() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["check_automation_process_hud_6:custom_function_result.data.success_quote", "==", 1]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        add_tag_to_container_a_done(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    add_tag_to_container_a_progress(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def add_tag_to_container_a_done(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_tag_to_container_a_done() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.add_tags(container=container, tags="a_done")
    phantom.set_label(container=container, label="conf_cases")
    phantom.set_sensitivity(container=container, sensitivity="green")
    phantom.set_severity(container=container, severity="medium")

    container = phantom.get_container(container.get('id', None))

    set_next_phase_as_current_phase(container=container)

    return


@phantom.playbook_block()
def set_next_phase_as_current_phase(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("set_next_phase_as_current_phase() called")

    id_value = container.get("id", None)
    check_if_alert_has_a_mapping_to_an_sop__automation_phase = json.loads(_ if (_ := phantom.get_run_data(key="check_if_alert_has_a_mapping_to_an_sop:automation_phase")) != "" else "null")  # pylint: disable=used-before-assignment

    parameters = []

    parameters.append({
        "container_id": id_value,
        "current_phase_name": check_if_alert_has_a_mapping_to_an_sop__automation_phase,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="conf23-sop_content/identify_the_next_phase", parameters=parameters, name="set_next_phase_as_current_phase")

    return


@phantom.playbook_block()
def playbook_i010_identify_the_use_caes_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i010_identify_the_use_caes_1() called")

    inputs = {}

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "conf23-sop_content/I010_Identify_the_use_caes", returns the playbook_run_id
    playbook_run_id = phantom.playbook("conf23-sop_content/I010_Identify_the_use_caes", container=container, name="playbook_i010_identify_the_use_caes_1", callback=check_if_alert_has_a_mapping_to_an_sop, inputs=inputs)

    return


@phantom.playbook_block()
def check_if_alert_has_a_mapping_to_an_sop(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("check_if_alert_has_a_mapping_to_an_sop() called")

    playbook_i010_identify_the_use_caes_1_output_use_case_id = phantom.collect2(container=container, datapath=["playbook_i010_identify_the_use_caes_1:playbook_output:use_case_id"])

    playbook_i010_identify_the_use_caes_1_output_use_case_id_values = [item[0] for item in playbook_i010_identify_the_use_caes_1_output_use_case_id]

    input_parameter_0 = "SOP"

    check_if_alert_has_a_mapping_to_an_sop__match = None
    check_if_alert_has_a_mapping_to_an_sop__sop = None
    check_if_alert_has_a_mapping_to_an_sop__automation_phase = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    success, message, execs = phantom.get_list(list_name=input_parameter_0, values=playbook_i010_identify_the_use_caes_1_output_use_case_id_values[0], column_index=3, trace=False)
    
    
    if execs['matches']:
        check_if_alert_has_a_mapping_to_an_sop__match = 1
    else:
        check_if_alert_has_a_mapping_to_an_sop__match = 0
    
    phantom.debug('match: {}'.format( check_if_alert_has_a_mapping_to_an_sop__match))
    
    check_if_alert_has_a_mapping_to_an_sop__sop = execs['matches'][0]['value'][0]
    check_if_alert_has_a_mapping_to_an_sop__automation_phase = execs['matches'][0]['value'][2]

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="check_if_alert_has_a_mapping_to_an_sop:match", value=json.dumps(check_if_alert_has_a_mapping_to_an_sop__match))
    phantom.save_run_data(key="check_if_alert_has_a_mapping_to_an_sop:sop", value=json.dumps(check_if_alert_has_a_mapping_to_an_sop__sop))
    phantom.save_run_data(key="check_if_alert_has_a_mapping_to_an_sop:automation_phase", value=json.dumps(check_if_alert_has_a_mapping_to_an_sop__automation_phase))

    decision_1(container=container)

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