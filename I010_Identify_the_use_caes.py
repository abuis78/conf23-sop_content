"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'identify_the_use_cases_by_the_alert_name' block
    identify_the_use_cases_by_the_alert_name(container=container)

    return

@phantom.playbook_block()
def identify_the_use_cases_by_the_alert_name(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("identify_the_use_cases_by_the_alert_name() called")

    name_value = container.get("name", None)

    identify_the_use_cases_by_the_alert_name__use_case_id = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    import re
    match = re.match(r'(\d+)_', name_value)
    if match:
        number = match.group(1)
        phantom.debug(number)
        identify_the_use_cases_by_the_alert_name__use_case_id = number
    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key="identify_the_use_cases_by_the_alert_name:use_case_id", value=json.dumps(identify_the_use_cases_by_the_alert_name__use_case_id))

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    identify_the_use_cases_by_the_alert_name__use_case_id = json.loads(_ if (_ := phantom.get_run_data(key="identify_the_use_cases_by_the_alert_name:use_case_id")) != "" else "null")  # pylint: disable=used-before-assignment

    output = {
        "use_case_name": identify_the_use_cases_by_the_alert_name__use_case_id,
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