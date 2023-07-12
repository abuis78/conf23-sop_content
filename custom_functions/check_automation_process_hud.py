def check_automation_process_hud(status=None, container_id=None, phase_id=None, **kwargs):
    """
    Args:
        status
        container_id
        phase_id
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    url_filter = "?_filter_container_id=" + str(container_id) + "&_filter_phase=" + str(phase_id)
    task_url = phantom.build_phantom_rest_url('workbook_task')
    url = task_url + url_filter
    response = phantom.requests.get(url,verify=False)
    data = response.json()
    phantom.debug(data.get('count'))  
    done_tasks = data.get('count')
    
    
    url_filter = "?_filter_container_id=" + str(container_id) + "&_filter_phase=" + str(phase_id) + "&_filter_status="+ str(status)
    task_url = phantom.build_phantom_rest_url('workbook_task')
    url = task_url + url_filter
    response = phantom.requests.get(url,verify=False)
    data = response.json()
    phantom.debug(data.get('count'))
    all_tasks = data.get('count')
    
    message = "Current status of task automation"
    data = str(done_tasks) + "/" + str(all_tasks)
    if done_tasks == all_tasks:
        pin_style = "blue"
    else:
        pin_style = "red"
        
    phantom.pin(container=None, message=message,data=data, pin_type="card",pin_style=pin_style, truncate=True,name=None, trace=False)
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
