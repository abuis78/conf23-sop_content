def update_SOP_custom_list(artifact_id_list=None, container_id=None, prefix_filter=None, list_name=None, **kwargs):
    """
    Args:
        artifact_id_list
        container_id
        prefix_filter
        list_name
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    
    for a in artifact_id_list:
        url_filter = '/'+ str(a) + '?_filter_name__icontains="' + str(prefix_filter) +'"'
        r_url = phantom.build_phantom_rest_url('artifact')
        url = r_url + url_filter
        r = phantom.requests.get(url,verify=False)
        v = r.json()
        v_id = v.get('cef', {}).get('version')
        n = v.get('cef', {}).get('name')
        if v_id is not None:
            r_url2 = phantom.build_phantom_rest_url('decided_list',list_name)
            r2 = phantom.requests.get(r_url2,verify=False)
            ln = r2.json()
            
            for i, sublist in enumerate(ln["content"]):
                if n in sublist[0]:
                    if int(v_id) <= int(sublist[1]):
                        phantom.debug(f"Nothing to Update")
                    elif int(v_id) > int(sublist[1]):
                        phantom.debug(f"SOP Update")
                        phantom.debug(f"Element was found in row {i + 1} ")
                        r_url3 = phantom.build_phantom_rest_url('decided_list',list_name)
                        sublist[1] = str(v_id) 
                        data = { "content": sublist,"name": list_name}
                        phantom.debug(f"New Data: {data}")
                        r3 = phantom.requests.post(r_url3, json=data, verify=False).json()
                        phantom.debug(r3)
                    
        else:
            phantom.debug(f"-------Nicht da")
        
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
