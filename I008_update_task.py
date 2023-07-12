"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'task_note_title' block
    task_note_title(container=container)

    return

@phantom.playbook_block()
def workbook_task_update_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("workbook_task_update_1() called")

    id_value = container.get("id", None)
    playbook_input_current_task = phantom.collect2(container=container, datapath=["playbook_input:current_task"])
    task_note_title = phantom.get_format_data(name="task_note_title")
    task_note_content = phantom.get_format_data(name="task_note_content")

    parameters = []

    # build parameters list for 'workbook_task_update_1' call
    for playbook_input_current_task_item in playbook_input_current_task:
        parameters.append({
            "task_name": playbook_input_current_task_item[0],
            "note_title": task_note_title,
            "note_content": task_note_content,
            "status": "complete",
            "owner": "current",
            "container": id_value,
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="conf23-sop_content/workbook_task_update", parameters=parameters, name="workbook_task_update_1")

    return


@phantom.playbook_block()
def task_note_title(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("task_note_title() called")

    template = """Automatic processing of the task"""

    # parameter list for template variable replacement
    parameters = []

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="task_note_title")

    task_note_content(container=container)

    return


@phantom.playbook_block()
def task_note_content(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("task_note_content() called")

    template = """This task was processed automatically. The result of the automatic processing looks as follows:\n\n{0}\n"""

    # parameter list for template variable replacement
    parameters = [
        "playbook_input:automation_results"
    ]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.format(container=container, template=template, parameters=parameters, name="task_note_content")

    workbook_task_update_1(container=container)

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