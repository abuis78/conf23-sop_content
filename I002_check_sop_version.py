"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'check_if_reference_list_exists' block
    check_if_reference_list_exists(container=container)

    return

@phantom.playbook_block()
def check_if_reference_list_exists(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("check_if_reference_list_exists() called")

    playbook_input_liste_name = phantom.collect2(container=container, datapath=["playbook_input:liste_name"])

    playbook_input_liste_name_values = [item[0] for item in playbook_input_liste_name]

    check_if_reference_list_exists__list_status = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here.../rest/decided_list?_filter_name="SOP"
    phantom.debug(playbook_input_liste_name)
    decided_list_tag_url = phantom.build_phantom_rest_url('decided_list')
    filter_parameter = "?_filter_name=" + playbook_input_liste_name
    url = decided_list_tag_url + filter_parameter
    response = phantom.requests.get(url,verify=False)
    
    check_if_reference_list_exists__list_status = response.json()['count']

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="check_if_reference_list_exists:list_status", value=json.dumps(check_if_reference_list_exists__list_status))

    debug_2(container=container)

    return


@phantom.playbook_block()
def debug_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("debug_2() called")

    check_if_reference_list_exists__list_status = json.loads(_ if (_ := phantom.get_run_data(key="check_if_reference_list_exists:list_status")) != "" else "null")  # pylint: disable=used-before-assignment

    parameters = []

    parameters.append({
        "input_1": check_if_reference_list_exists__list_status,
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