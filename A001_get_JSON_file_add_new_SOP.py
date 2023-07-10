"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'playbook_i001_extract_json_from_file_3' block
    playbook_i001_extract_json_from_file_3(container=container)

    return

@phantom.playbook_block()
def format_sop_json(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_sop_json() called")

    template = """{{\"cef\":{{\n\"sop_json\": \"{0}\",\n\"version\": 2\n}}\n}}"""

    # parameter list for template variable replacement
    parameters = [
        "format_playbook_output:formatted_data"
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
        "name": format_sop_name,
        "tags": None,
        "label": None,
        "severity": None,
        "cef_field": None,
        "cef_value": None,
        "container": id_value,
        "input_json": format_sop_json,
        "cef_data_type": None,
        "run_automation": None,
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
def format_playbook_output(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_playbook_output() called")

    template = """{0}"""

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

    phantom.format(container=container, template=template, parameters=parameters, name="format_playbook_output")

    debug_3(container=container)

    return


@phantom.playbook_block()
def debug_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_3() called")

    format_playbook_output = phantom.get_format_data(name="format_playbook_output")

    parameters = []

    parameters.append({
        "input_1": format_playbook_output,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_3")

    return


@phantom.playbook_block()
def playbook_i001_extract_json_from_file_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i001_extract_json_from_file_3() called")

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
    playbook_run_id = phantom.playbook("conf23-sop_content/I001_extract_JSON_from_file", container=container, name="playbook_i001_extract_json_from_file_3", callback=playbook_i002_check_sop_version_2, inputs=inputs)

    return


@phantom.playbook_block()
def playbook_i002_check_sop_version_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i002_check_sop_version_2() called")

    playbook_i001_extract_json_from_file_3_output_name = phantom.collect2(container=container, datapath=["playbook_i001_extract_json_from_file_3:playbook_output:name"])
    playbook_i001_extract_json_from_file_3_output_version = phantom.collect2(container=container, datapath=["playbook_i001_extract_json_from_file_3:playbook_output:version"])

    playbook_i001_extract_json_from_file_3_output_name_values = [item[0] for item in playbook_i001_extract_json_from_file_3_output_name]
    playbook_i001_extract_json_from_file_3_output_version_values = [item[0] for item in playbook_i001_extract_json_from_file_3_output_version]

    inputs = {
        "sop_name": playbook_i001_extract_json_from_file_3_output_name_values,
        "sop_version": playbook_i001_extract_json_from_file_3_output_version_values,
        "liste_name": ["SOP"],
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "conf23-sop_content/I002_check_sop_version", returns the playbook_run_id
    playbook_run_id = phantom.playbook("conf23-sop_content/I002_check_sop_version", container=container, name="playbook_i002_check_sop_version_2", callback=add_comment_4, inputs=inputs)

    return


@phantom.playbook_block()
def add_comment_4(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_comment_4() called")

    playbook_i002_check_sop_version_2_output_sop_in_list_status = phantom.collect2(container=container, datapath=["playbook_i002_check_sop_version_2:playbook_output:sop_in_list_status"])

    playbook_i002_check_sop_version_2_output_sop_in_list_status_values = [item[0] for item in playbook_i002_check_sop_version_2_output_sop_in_list_status]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment=playbook_i002_check_sop_version_2_output_sop_in_list_status_values)

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