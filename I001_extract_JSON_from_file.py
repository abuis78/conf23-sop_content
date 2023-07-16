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

    get_file_information_extract_content__data_list = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(playbook_input_vault_id)
    phantom.debug(playbook_input_vault_id_values)
    my_list = []
    
    for item in playbook_input_vault_id_values:
        vault_id = playbook_input_vault_id_values[0]
        success, message, vault_info = phantom.vault_info(vault_id=vault_id[0])
        path = vault_info[0]["path"]
        
        with open(path, 'r') as file:
            data = json.load(file)
            entry = {
                "name": data['sop_json']['name'],
                "sop_json": data.get('sop_json'),
                "version": data.get('version'),
                "creator": data.get('creator')
            }
            
            my_list.append(entry)
        
            name = "SOP " + data['sop_json']['name']
            raw = {}
            cef = {}
            cef['sop_json'] = str(data.get('sop_json'))
            success, message, artifact_id = phantom.add_artifact(container=container, raw_data=raw, cef_data=cef, label='netflow',name='test_event', severity='low',identifier=None,artifact_type='network')

            phantom.debug('artifact added as id:'+str(artifact_id))
    
            
    phantom.debug(my_list)
    get_file_information_extract_content__data_list = my_list
    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="get_file_information_extract_content:data_list", value=json.dumps(get_file_information_extract_content__data_list))

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    get_file_information_extract_content__data_list = json.loads(_ if (_ := phantom.get_run_data(key="get_file_information_extract_content:data_list")) != "" else "null")  # pylint: disable=used-before-assignment

    output = {
        "data_list": get_file_information_extract_content__data_list,
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