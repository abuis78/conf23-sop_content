def update_SOP_custom_list(artifact_id_list=None, container_id=None, prefix_filter=None, **kwargs):
    """
    Args:
        artifact_id_list
        container_id
        prefix_filter
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    phantom.debug(f"a liste {artifact_id_list}")
    for a in artifact_id_list:
        url_filter = '/'+ str(a) + '?_filter_name__icontains="' + str(prefix_filter) +'"'
        r_url = phantom.build_phantom_rest_url('artifact')
        r = phantom.requests.get(r_url,verify=False)
        d = r.json()["data"]
        v = d[0]["version"]
        phantom.debug(f"Version {a} {v}")
        
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
