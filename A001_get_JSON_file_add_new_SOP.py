"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'format_3' block
    format_3(container=container)

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
def format_sop_json(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_sop_json() called")

    template = """{{\"cef\":{{\n\"sop_json\": \"{0}\",\n\"version\": 2\n}}\n}}"""

    # parameter list for template variable replacement
    parameters = [
        "format_3:formatted_data"
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
def format_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_3() called")

    template = """{\n  \"name\": \"1234_test_search\",\n  \"description\": \"This is an example SOP for a test correlation search\",\n  \"phases\": [\n    {\n      \"id\": \"Generated SOP Tasks\",\n      \"name\": \"Generated SOP Tasks\",\n      \"tasks\": [\n{\n\t\t\t\"name\": \"F01-Check file hash\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"F02-Check file name/path\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"P01-Check InitiatingProcessParentFileName of the InitiatingProcessFileName\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"N16-Check for internal traffic\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"U01-Get username\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"U02-Check if the user is local admin\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"U04-Check for login activities on other hosts\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"U05-Check login types\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"H01-How many users are logging in on the host\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"H02-Host IP\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"H04-Check for added autorun entries\"\n\t\t}\n      ]\n    },\n    {\n      \"id\": \"Additional_Info\",\n      \"name\": \"Additional Info\",\n      \"tasks\": [\n        {\n\t\t\t\"name\": \"Notes / Remarks\",\n            \"description\": \"\"\n\t\t}\n      ]\n    },\n    {\n      \"id\": \"Recommendations\",\n      \"name\": \"Recommendations\",\n      \"tasks\": [\n        {\n\t\t\t\"name\": \"Notes / Remarks\",\n            \"description\": \"\"\n\t\t}\n      ]\n    }\n  ],\n  \"is_default\": false,\n  \"is_note_required\": true\n}"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_3")

    format_sop_name(container=container)

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