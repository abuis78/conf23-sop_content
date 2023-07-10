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
        phantom.debug("vault_info: {}".format(vault_info))
        path = vault_info[0]["path"]
        name = vault_info[0]["name"]
        phantom.debug("path: {}".format(path))
        phantom.debug("name: {}".format(name))
        file_path_name = '/'.join([path, name])
        phantom.debug(file_path_name)
        
        with open(file_path_name) as file:
            data = json.load(file)
        
        phantom.debug("data: {}".format(data))

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="get_file_information_extract_content:json_content", value=json.dumps(get_file_information_extract_content__json_content))

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