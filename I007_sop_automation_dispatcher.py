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
    phase_id, phase_name = phantom.get_phase()
    phantom.debug(phase_id)
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