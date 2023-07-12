"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'git_list_files_1' block
    git_list_files_1(container=container)

    return

@phantom.playbook_block()
def git_list_files_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("git_list_files_1() called")

    playbook_input_repo_path_local = phantom.collect2(container=container, datapath=["playbook_input:repo_path_local"])
    playbook_input_repo_path_remote = phantom.collect2(container=container, datapath=["playbook_input:repo_path_remote"])
    playbook_input_filter_file_endswith = phantom.collect2(container=container, datapath=["playbook_input:filter_file_endswith"])

    playbook_input_filter_file_endswith_values = [item[0] for item in playbook_input_filter_file_endswith]

    parameters = []

    # build parameters list for 'git_list_files_1' call
    for playbook_input_repo_path_local_item in playbook_input_repo_path_local:
        for playbook_input_repo_path_remote_item in playbook_input_repo_path_remote:
            parameters.append({
                "repo_path_local": playbook_input_repo_path_local_item[0],
                "repo_path_remote": playbook_input_repo_path_remote_item[0],
                "filter_file_endswith": playbook_input_filter_file_endswith_values,
            })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="conf23-sop_content/git_list_files", parameters=parameters, name="git_list_files_1", callback=add_files_to_container)

    return


@phantom.playbook_block()
def format_list_of_files(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("format_list_of_files() called")

    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "git_list_files_1:custom_function_result.data.file_list"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="format_list_of_files")

    debug_2(container=container)

    return


@phantom.playbook_block()
def debug_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_2() called")

    format_list_of_files = phantom.get_format_data(name="format_list_of_files")

    parameters = []

    parameters.append({
        "input_1": format_list_of_files,
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
def add_files_to_container(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_files_to_container() called")

    git_list_files_1__result = phantom.collect2(container=container, datapath=["git_list_files_1:custom_function_result.data.file_list"])

    git_list_files_1_data_file_list = [item[0] for item in git_list_files_1__result]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(git_list_files_1_data_file_list[0])

    ################################################################################
    ## Custom Code End
    ################################################################################

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