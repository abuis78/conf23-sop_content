"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'assigne_sop' block
    assigne_sop(container=container)

    return

@phantom.playbook_block()
def assigne_sop(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("assigne_sop() called")

    playbook_input_sop = phantom.collect2(container=container, datapath=["playbook_input:sop"])

    playbook_input_sop_values = [item[0] for item in playbook_input_sop]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    phantom.debug(playbook_input_sop_values)
    success, message = phantom.promote(template=playbook_input_sop_values)

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