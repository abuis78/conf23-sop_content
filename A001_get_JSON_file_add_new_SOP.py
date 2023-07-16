"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'git_list_files_8' block
    git_list_files_8(container=container)

    return

@phantom.playbook_block()
def playbook_i001_extract_json_from_file_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i001_extract_json_from_file_3() called")

    filtered_artifact_0_data_filter_artifacts_for_sop_in_name = phantom.collect2(container=container, datapath=["filtered-data:filter_artifacts_for_sop_in_name:condition_1:artifact:*.cef.vaultId"], scope="all")

    filtered_artifact_0__cef_vaultid = [item[0] for item in filtered_artifact_0_data_filter_artifacts_for_sop_in_name]

    inputs = {
        "vault_id": filtered_artifact_0__cef_vaultid,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "conf23-sop_content/I001_extract_JSON_from_file", returns the playbook_run_id
    playbook_run_id = phantom.playbook("conf23-sop_content/I001_extract_JSON_from_file", container=container, name="playbook_i001_extract_json_from_file_3", inputs=inputs)

    return


@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["playbook_i002_check_sop_version_2:playbook_output:sop_in_list_status", "==", "update"]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        comment_existing_sop_is_being_updated(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 2
    found_match_2 = phantom.decision(
        container=container,
        conditions=[
            ["playbook_i002_check_sop_version_2:playbook_output:sop_in_list_status", "==", "newly_created"]
        ],
        delimiter=None)

    # call connected blocks if condition 2 matched
    if found_match_2:
        comment_the_new_sop_is_being_created(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'elif' condition 3
    found_match_3 = phantom.decision(
        container=container,
        conditions=[
            ["playbook_i002_check_sop_version_2:playbook_output:sop_in_list_status", "==", "nothing_to_do"]
        ],
        delimiter=None)

    # call connected blocks if condition 3 matched
    if found_match_3:
        comment_there_is_no_need_for_action(action=action, success=success, container=container, results=results, handle=handle)
        return

    return


@phantom.playbook_block()
def comment_existing_sop_is_being_updated(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("comment_existing_sop_is_being_updated() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="Existing SOP is being updated")

    update_sop(container=container)

    return


@phantom.playbook_block()
def comment_the_new_sop_is_being_created(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("comment_the_new_sop_is_being_created() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="The new SOP is being created")

    create_new_sop(container=container)

    return


@phantom.playbook_block()
def comment_there_is_no_need_for_action(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("comment_there_is_no_need_for_action() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="There is no need for action")

    return


@phantom.playbook_block()
def update_sop(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("update_sop() called")

    playbook_i001_extract_json_from_file_3_output_json_content = phantom.collect2(container=container, datapath=["playbook_i001_extract_json_from_file_3:playbook_output:json_content"])
    playbook_i001_extract_json_from_file_3_output_name = phantom.collect2(container=container, datapath=["playbook_i001_extract_json_from_file_3:playbook_output:name"])

    playbook_i001_extract_json_from_file_3_output_json_content_values = [item[0] for item in playbook_i001_extract_json_from_file_3_output_json_content]
    playbook_i001_extract_json_from_file_3_output_name_values = [item[0] for item in playbook_i001_extract_json_from_file_3_output_name]

    inputs = {
        "task": ["update"],
        "sop_json": playbook_i001_extract_json_from_file_3_output_json_content_values,
        "sop_name": playbook_i001_extract_json_from_file_3_output_name_values,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "conf23-sop_content/I003_create_SOP_as_Workbook", returns the playbook_run_id
    playbook_run_id = phantom.playbook("conf23-sop_content/I003_create_SOP_as_Workbook", container=container, name="update_sop", inputs=inputs)

    return


@phantom.playbook_block()
def create_new_sop(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("create_new_sop() called")

    playbook_i001_extract_json_from_file_3_output_json_content = phantom.collect2(container=container, datapath=["playbook_i001_extract_json_from_file_3:playbook_output:json_content"])
    playbook_i001_extract_json_from_file_3_output_name = phantom.collect2(container=container, datapath=["playbook_i001_extract_json_from_file_3:playbook_output:name"])

    playbook_i001_extract_json_from_file_3_output_json_content_values = [item[0] for item in playbook_i001_extract_json_from_file_3_output_json_content]
    playbook_i001_extract_json_from_file_3_output_name_values = [item[0] for item in playbook_i001_extract_json_from_file_3_output_name]

    inputs = {
        "task": ["create"],
        "sop_json": playbook_i001_extract_json_from_file_3_output_json_content_values,
        "sop_name": playbook_i001_extract_json_from_file_3_output_name_values,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "conf23-sop_content/I003_create_SOP_as_Workbook", returns the playbook_run_id
    playbook_run_id = phantom.playbook("conf23-sop_content/I003_create_SOP_as_Workbook", container=container, name="create_new_sop", inputs=inputs)

    return


@phantom.playbook_block()
def filter_artifacts_for_sop_in_name(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_artifacts_for_sop_in_name() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["SOP", "in", "artifact:*.name"]
        ],
        name="filter_artifacts_for_sop_in_name:condition_1",
        scope="all",
        case_sensitive=False,
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        playbook_i001_extract_json_from_file_3(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def playbook_i002_check_sop_version_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i002_check_sop_version_1() called")

    inputs = {
        "sop_name": [],
        "sop_version": [],
        "liste_name": [],
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "conf23-sop_content/I002_check_sop_version", returns the playbook_run_id
    playbook_run_id = phantom.playbook("conf23-sop_content/I002_check_sop_version", container=container, name="playbook_i002_check_sop_version_1", callback=decision_1, inputs=inputs)

    return


@phantom.playbook_block()
def git_list_files_8(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("git_list_files_8() called")

    parameters = []

    parameters.append({
        "repo_path_local": "/opt/soar/local_data/app_states/ff116964-86f7-4e29-8763-4462ce0d39a7/conf23/",
        "repo_path_remote": "https://github.com/abuis78/conf23.git",
        "filter_file_endswith": "json",
        "artifact_name_prefix": None,
        "artifact_severity": None,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="conf23-sop_content/git_list_files", parameters=parameters, name="git_list_files_8", callback=playbook_i001_extract_json_from_file_1)

    return


@phantom.playbook_block()
def playbook_i001_extract_json_from_file_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i001_extract_json_from_file_1() called")

    git_list_files_8__result = phantom.collect2(container=container, datapath=["git_list_files_8:custom_function_result.data.vault_id_list"])

    git_list_files_8_data_vault_id_list = [item[0] for item in git_list_files_8__result]

    inputs = {
        "vault_id": git_list_files_8_data_vault_id_list,
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