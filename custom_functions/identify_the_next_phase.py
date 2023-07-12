def identify_the_next_phase(current_phase_name=None, container_id=None, **kwargs):
    """
    identify the next phase and set it as current
    
    Args:
        current_phase_name
        container_id
    
    Returns a JSON-serializable object that implements the configured data paths:
        next_phase_name
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    url_filter = "?_filter_container_id="+ str(container_id)
    w_url = phantom.build_phantom_rest_url('workbook_phase')
    url = w_url + url_filter
    response = phantom.requests.get(url,verify=False)
    json_data = response.json()["data"]
    
    target_order = None
    next_order = None
    next_name = None
    
    for item in json_data:
        phantom.debug(item['name'])
        if item['name'] == current_phase_name:
            target_order = item['order']
            break
            
    if target_order is not None:
        for item in json_data:
            if item['order'] > target_order:
                next_order = item['order']
                next_name = item['name']
                break
    
    phantom.debug(f"Die 'order' Nummer des 'Generatedd SOP Tasks' ist: {target_order}")
    phantom.debug(f"Die nächste 'order' Nummer ist: {next_order} und der zugehörige 'name' ist: {next_name}")
    phantom.set_phase(container=container_id, phase=next_name, trace=False)
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
