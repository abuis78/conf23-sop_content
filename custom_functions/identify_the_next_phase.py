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
    phantom.debug(json_data)
    
    target_order = None
    next_name = None
    for item in json_data['data'][0]:
        if item['name'] == current_phase_name:
            target_order = item['order']
            phantom.debug(target_order)
            break
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
