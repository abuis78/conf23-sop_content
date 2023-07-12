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

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phase = playbook_input_automation_phase_values[0]
    success, message = phantom.set_phase(container=id_value,phase=phase)
    success, message, phase_id, phase_name = phantom.get_phase()
    phantom.debug(phase_id)
    
    url_filter = "?_filter_container_id=" + str(id_value) + "&_filter_phase=" + str(phase_id)
    rest_url = phantom.build_phantom_rest_url('workbook_task')
    url = rest_url + url_filter
    
    response = phantom.requests.get(url,verify=False,)
    
    data = response.json()
    phantom.debug(data["data"])
    
    for task in data["data"]:
        phantom.debug(task["name"])
        # get the ID of the Playbook
        #url_filter = '?_filter_name="'+ task['data']['name'] + '"'
        #url_playbook = phantom.build_phantom_rest_url('playbook')
        #url = url_playbook + url_filter
        #response = phantom.requests.get(url,verify=False)
        #playbook_id = response.json()['data'][0]['id']
        #phantom.debug(playbook_id)
        
        # trigger the Playbook
        #url_run_playbook = phantom.build_phantom_rest_url('playbook_run')
       # data = {'container_id': id_value, 'playbook_id': playbook_id, 'scope': 'new', 'run': 'true'}
       # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
       # response3 = phantom.requests.post(url_run_playbook, data=json.dumps(data), headers=headers, verify=False)
        #phantom.debug("phantom returned status code {} with message {}".format(response3.status_code, response3.text))
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