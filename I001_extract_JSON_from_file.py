"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'get_file_information_extract_content' block
    get_file_information_extract_content(container=container)

    return

@phantom.playbook_block()
def get_file_information_extract_content(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("get_file_information_extract_content() called")

    playbook_input_vault_id = phantom.collect2(container=container, datapath=["playbook_input:vault_id"])

    playbook_input_vault_id_values = [item[0] for item in playbook_input_vault_id]

    get_file_information_extract_content__json_content = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    for item in playbook_input_vault_id:
        vault_id = playbook_input_vault_id[0]
        success, message, vault_info = phantom.vault_info(vault_id=vault_id[0])
        path = vault_info[0]["path"]
        
        with open(path) as file:
            data = json.load(file)
            get_file_information_extract_content__json_content = str(data)
        

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="get_file_information_extract_content:json_content", value=json.dumps(get_file_information_extract_content__json_content))

    debug_1(container=container)

    return


@phantom.playbook_block()
def debug_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_1() called")

    get_file_information_extract_content__json_content = json.loads(_ if (_ := phantom.get_run_data(key="get_file_information_extract_content:json_content")) != "" else "null")  # pylint: disable=used-before-assignment

    parameters = []

    parameters.append({
        "input_1": get_file_information_extract_content__json_content,
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

    phantom.custom_function(custom_function="community/debug", parameters=parameters, name="debug_1")

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    get_file_information_extract_content__json_content = json.loads(_ if (_ := phantom.get_run_data(key="get_file_information_extract_content:json_content")) != "" else "null")  # pylint: disable=used-before-assignment

    output = {
        "json_content": get_file_information_extract_content__json_content,
    }

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_playbook_output_data(output=output)

    return