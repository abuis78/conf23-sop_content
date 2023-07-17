"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'get_latest_version_of_files_from_git' block
    get_latest_version_of_files_from_git(container=container)

    return

@phantom.playbook_block()
def get_latest_version_of_files_from_git(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_latest_version_of_files_from_git() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("git pull", parameters=parameters, name="get_latest_version_of_files_from_git", assets=["git 1"], callback=git_list_files_12)

    return


@phantom.playbook_block()
def git_list_files_12(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("git_list_files_12() called")

    get_latest_version_of_files_from_git_result_data = phantom.collect2(container=container, datapath=["get_latest_version_of_files_from_git:action_result.data.*.response","get_latest_version_of_files_from_git:action_result.parameter.context.artifact_id"], action_results=results)

    parameters = []

    # build parameters list for 'git_list_files_12' call
    for get_latest_version_of_files_from_git_result_item in get_latest_version_of_files_from_git_result_data:
        parameters.append({
            "pull_response": get_latest_version_of_files_from_git_result_item[0],
            "repo_path_local": "/opt/soar/local_data/app_states/ff116964-86f7-4e29-8763-4462ce0d39a7/conf23/",
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="conf23-sop_content/git_list_files", parameters=parameters, name="git_list_files_12", callback=debug_2)

    return


@phantom.playbook_block()
def playbook_i001_extract_json_from_file_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("playbook_i001_extract_json_from_file_2() called")

    git_list_files_12__result = phantom.collect2(container=container, datapath=["git_list_files_12:custom_function_result.data.vault_id_list"])

    git_list_files_12_data_vault_id_list = [item[0] for item in git_list_files_12__result]

    inputs = {
        "vault_id": git_list_files_12_data_vault_id_list,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    # call playbook "conf23-sop_content/I001_extract_JSON_from_file", returns the playbook_run_id
    playbook_run_id = phantom.playbook("conf23-sop_content/I001_extract_JSON_from_file", container=container, name="playbook_i001_extract_json_from_file_2", callback=filter_for_sop_artifatcs, inputs=inputs)

    return


@phantom.playbook_block()
def update_sop_custom_list_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("update_sop_custom_list_1() called")

    id_value = container.get("id", None)
    filtered_artifact_0_data_filter_for_sop_artifatcs = phantom.collect2(container=container, datapath=["filtered-data:filter_for_sop_artifatcs:condition_1:artifact:*.id","filtered-data:filter_for_sop_artifatcs:condition_1:artifact:*.id"], scope="all")

    filtered_artifact_0__id = [item[0] for item in filtered_artifact_0_data_filter_for_sop_artifatcs]

    parameters = []

    parameters.append({
        "artifact_id_list": filtered_artifact_0__id,
        "container_id": id_value,
        "prefix_filter": "SOP",
        "list_name": "SOP",
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
def filter_for_sop_artifatcs(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("filter_for_sop_artifatcs() called")

    # collect filtered artifact ids and results for 'if' condition 1
    matched_artifacts_1, matched_results_1 = phantom.condition(
        container=container,
        conditions=[
            ["SOP", "in", "artifact:*.name"]
        ],
        name="filter_for_sop_artifatcs:condition_1",
        scope="all",
        delimiter=None)

    # call connected blocks if filtered artifacts or results
    if matched_artifacts_1 or matched_results_1:
        check_sop_list(action=action, success=success, container=container, results=results, handle=handle, filtered_artifacts=matched_artifacts_1, filtered_results=matched_results_1)

    return


@phantom.playbook_block()
def check_sop_list(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("check_sop_list() called")

    input_parameter_0 = "SOP"

    check_sop_list__list_name = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    decided_list_tag_url = phantom.build_phantom_rest_url('decided_list')
    filter_parameter = '?_filter_name="' + input_parameter_0 + '"'
    url = decided_list_tag_url + filter_parameter
    response = phantom.requests.get(url,verify=False)
    # phantom.debug(response.json()['count'])
    l_r = response.json()['count']
    if l_r == 0:
        phantom.debug(f"Create new List {input_parameter_0}")
        url = phantom.build_phantom_rest_url('decided_list')
        data = {"content":[["name","version","automation_phase","alert"]],"name":"SOP"}
        response_data = phantom.requests.post(url, json=data, verify=False).json()
    
    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="check_sop_list:list_name", value=json.dumps(check_sop_list__list_name))

    update_sop_custom_list_1(container=container)

    return


@phantom.playbook_block()
def debug_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_2() called")

    git_list_files_12__result = phantom.collect2(container=container, datapath=["git_list_files_12:custom_function_result.data.vault_id_list"])

    git_list_files_12_data_vault_id_list = [item[0] for item in git_list_files_12__result]

    parameters = []

    parameters.append({
        "input_1": git_list_files_12_data_vault_id_list,
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