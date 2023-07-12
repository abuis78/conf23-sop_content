"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'set_automation_phase' block
    set_automation_phase(container=container)

    return

@phantom.playbook_block()
def add_comment_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("add_comment_1() called")

    playbook_input_automation_phase = phantom.collect2(container=container, datapath=["playbook_input:automation_phase"])

    playbook_input_automation_phase_values = [item[0] for item in playbook_input_automation_phase]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment=playbook_input_automation_phase_values)

    return


@phantom.playbook_block()
def set_automation_phase(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("set_automation_phase() called")

    id_value = container.get("id", None)
    playbook_input_automation_phase = phantom.collect2(container=container, datapath=["playbook_input:automation_phase"])

    playbook_input_automation_phase_values = [item[0] for item in playbook_input_automation_phase]

    set_automation_phase__phase_id = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    import time
    
    phase = playbook_input_automation_phase_values[0]
    success, message = phantom.set_phase(container=id_value,phase=phase)
    success, message, phase_id, phase_name = phantom.get_phase()
    phantom.debug(phase_id)
    set_automation_phase__phase_id = phase_id
    
    url_filter = "?_filter_container_id=" + str(id_value) + "&_filter_phase=" + str(phase_id)
    rest_url = phantom.build_phantom_rest_url('workbook_task')
    url = rest_url + url_filter
    
    response = phantom.requests.get(url,verify=False,)
    
    data = response.json()
    data = json.loads(data)
    data = data["data"]
    
    phantom.debug(data)
    item_chunks = [data[i:i+5] for i in range(0, len(data), 5)]
    phantom.debug(item_chunks)
    
    for i, chunk in enumerate(item_chunks):
        phantom.debug(chunk["name"])
        current_task = chunk["name"]
        # get the ID of the Playbook
        url_filter = '?_filter_name="'+ current_task + '"'
        url_playbook = phantom.build_phantom_rest_url('playbook')
        url = url_playbook + url_filter
        response = phantom.requests.get(url,verify=False)
        data = response.json()
        if data["count"] == 0:
            phantom.debug("no playbook found")
        else:
            phantom.debug(data["data"][0]["id"])
            playbook_id = data["data"][0]["id"]
        
        
            # trigger the Playbook
            url_run_playbook = phantom.build_phantom_rest_url('playbook_run')
            inputs = { "current_task": current_task}
            data = {'container_id': id_value, 'playbook_id': playbook_id, 'scope': 'new', 'run': 'true','inputs': inputs}
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            response3 = phantom.requests.post(url_run_playbook, data=json.dumps(data), headers=headers, verify=False)
            phantom.debug("phantom returned status code {} with message {}".format(response3.status_code, response3.text))
            
        if i != len(item_chunks) - 1:
            time.sleep(1)
            
    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="set_automation_phase:phase_id", value=json.dumps(set_automation_phase__phase_id))

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    set_automation_phase__phase_id = json.loads(_ if (_ := phantom.get_run_data(key="set_automation_phase:phase_id")) != "" else "null")  # pylint: disable=used-before-assignment

    output = {
        "phase_id": set_automation_phase__phase_id,
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