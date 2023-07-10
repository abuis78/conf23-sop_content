"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_i001_extract_json_from_file_1' block
    playbook_i001_extract_json_from_file_1(container=container)

    return

@phantom.playbook_block()
def playbook_i001_extract_json_from_file_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i001_extract_json_from_file_1() called")

    container_artifact_data = phantom.collect2(container=container, datapath=["artifact:*.cef.vaultId"])

    container_artifact_cef_item_0 = [item[0] for item in container_artifact_data]

    inputs = {
        "vault_id": container_artifact_cef_item_0,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "conf23-sop_content/I001_extract_JSON_from_file", returns the playbook_run_id
    playbook_run_id = phantom.playbook("conf23-sop_content/I001_extract_JSON_from_file", container=container, name="playbook_i001_extract_json_from_file_1", inputs=inputs)

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