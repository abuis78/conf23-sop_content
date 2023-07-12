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