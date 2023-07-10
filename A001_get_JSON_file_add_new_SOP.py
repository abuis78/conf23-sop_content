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
    playbook_run_id = phantom.playbook("conf23-sop_content/I001_extract_JSON_from_file", container=container, name="playbook_i001_extract_json_from_file_1", callback=debug_2, inputs=inputs)

    return


@phantom.playbook_block()
def format_sop_json(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_sop_json() called")

    template = """{{\"cef\":{{\n\"sop_json\": {0},\n\"version\": 2\n}}\n}}"""

    # parameter list for template variable replacement
    parameters = [
        "playbook_i001_extract_json_from_file_1:playbook_output:json_content"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_sop_json")

    create_new_sop_artifact(container=container)

    return


@phantom.playbook_block()
def create_new_sop_artifact(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("create_new_sop_artifact() called")

    id_value = container.get("id", None)
    format_sop_name = phantom.get_format_data(name="format_sop_name")
    format_sop_json = phantom.get_format_data(name="format_sop_json")

    parameters = []

    parameters.append({
        "container": id_value,
        "name": format_sop_name,
        "label": None,
        "severity": None,
        "cef_field": None,
        "cef_value": None,
        "cef_data_type": None,
        "tags": None,
        "run_automation": None,
        "input_json": format_sop_json,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/artifact_create", parameters=parameters, name="create_new_sop_artifact")

    return


@phantom.playbook_block()
def format_sop_name(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_sop_name() called")

    template = """NEW SOP"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_sop_name")

    format_sop_json(container=container)

    return


@phantom.playbook_block()
def debug_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_2() called")

    playbook_i001_extract_json_from_file_1_output_json_content = phantom.collect2(container=container, datapath=["playbook_i001_extract_json_from_file_1:playbook_output:json_content.0"])

    playbook_i001_extract_json_from_file_1_output_json_content_0 = [item[0] for item in playbook_i001_extract_json_from_file_1_output_json_content]

    parameters = []

    parameters.append({
        "input_1": playbook_i001_extract_json_from_file_1_output_json_content_0,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_2")

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