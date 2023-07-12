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
    there_is_a_mapping_between_sop_and_allert(action=action, success=success, container=container, results=results, handle=handle)

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
    playbook_run_id = phantom.playbook("conf23-sop_content/I006_automated_processing_SOP", container=container, name="playbook_i006_automated_processing_sop_1", callback=playbook_i006_automated_processing_sop_1_callback, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_i006_automated_processing_sop_1_callback(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i006_automated_processing_sop_1_callback() called")

    
    # Downstream End block cannot be called directly, since execution will call on_finish automatically.
    # Using placeholder callback function so child playbook is run synchronously.


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