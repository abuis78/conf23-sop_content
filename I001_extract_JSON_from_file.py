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
    import re
    def check_and_format_json(data):
        if isinstance(data, str):  # If data is a string, we try to load it as JSON
            try:
                # Check if the string contains 'false' or 'true'
                if re.search(r"'false'|'true'", data, re.IGNORECASE):
                    # Replace 'false' and 'true' with "false" and "true"
                    data = re.sub(r"'false'", '"false"', data, flags=re.IGNORECASE)
                    data = re.sub(r"'true'", '"true"', data, flags=re.IGNORECASE)
                else:
                    data = data.replace("'", '"')  # Replace single quotes with double quotes
                
                data = json.loads(data)  # Try to parse string as JSON
                phantom.debug("The string is a valid JSON.")
            except json.JSONDecodeError:
                phantom.debug("The string is not a valid JSON.")
                pass
        elif isinstance(data, dict):  # If data is a dictionary, we dump it into a JSON string
            try:
                data = json.dumps(data)
                phantom.debug("The dictionary has been formatted into a valid JSON string:", data)
            except (TypeError, ValueError):
                phantom.debug("The dictionary could not be formatted into a valid JSON string.")
        else:
            phantom.debug("The data is neither a dictionary nor a JSON string.")
        phantom.debug(f"JSON Daten: {data}")
        return data
    
    
    my_list = []
    
    for item in playbook_input_vault_id_values[0]:
        success, message, vault_info = phantom.vault_info(vault_id=item)
        path = vault_info[0]["path"]
        
        with open(path, 'r') as file:
            data = json.load(file)
            entry = {
                "name": data['sop_json']['name'],
                "sop_json": check_and_format_json(data.get('sop_json')),
                "version": data.get('version'),
                "automation_phase": data.get('automation_phase'),
                "alert": data.get('alert'),
                "creator": data.get('creator')
            }
            
            my_list.append(entry)
        
            name = "SOP " + data['sop_json']['name']
            raw = {}
            cef = {}
            cef['sop_json'] = str(data.get('sop_json'))
            cef['name'] = str(data['sop_json']['name'])
            cef['version'] = str(data.get('version'))
            cef['creator'] = str(data.get('creator'))
            cef['automation_phase'] = str(data.get('automation_phase'))
            cef['alert'] = str(data.get('alert'))
            success, message, artifact_id = phantom.add_artifact(container=container, raw_data=raw, cef_data=cef, label='sop',name=name, severity='low',identifier=None)

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