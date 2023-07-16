"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'update_sop_custom_list_1' block
    update_sop_custom_list_1(container=container)

    return

@phantom.playbook_block()
def update_sop_custom_list_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("update_sop_custom_list_1() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.id","artifact:*.id"])

    container_artifact_header_item_0 = [item[0] for item in container_artifact_data]

    parameters = []

    parameters.append({
        "artifact_id_list": container_artifact_header_item_0,
        "container_id": 33526,
        "prefix_filter": "SOP",
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

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return