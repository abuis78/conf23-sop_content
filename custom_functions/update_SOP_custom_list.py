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
        url_filter = '?_filter_name__icontains="' + str(prefix_filter) +'"&_filter_container="' + str(container_id) +'"'
        r_url = phantom.build_phantom_rest_url('artifact')
        
        url = r_url + url_filter
        r = phantom.requests.get(url,verify=False)
        v = r.json()
        # v_id = v.get('cef', {}).get('version')
        v_id = [item['cef']['version'] for item in data['data']]
        n = v.get('cef', {}).get('name')
        phantom.debug(f"v_id: {v_id}\n")
        if v_id is not None:
            r_url2 = phantom.build_phantom_rest_url('decided_list',list_name)
            r2 = phantom.requests.get(r_url2,verify=False)
            ln = r2.json()
            
            for i, sublist in enumerate(ln["content"]):
                if n in sublist[0]:
                    if int(v_id) <= int(sublist[1]):
                        phantom.debug(f"Nothing to Update for SOP: {n} this one is still up to date")
                    elif int(v_id) > int(sublist[1]):
                        phantom.debug(f"SOP Update")
                        phantom.debug(f"Element was found in row {i + 1} ")
                        row = i
                        r_url3 = phantom.build_phantom_rest_url('decided_list',list_name)
                        sublist[1] = str(v_id) 
                        l_e = sublist
                        data = { "update_rows": { row : sublist }}
                        phantom.debug(f"New Data: {data}")
                        r3 = phantom.requests.post(r_url3, json=data, verify=False).json()
                        phantom.debug(r3)
                    else:
                        phantom.debug("SOP ist not in list")
            
        elif v_id is  None:
            phantom.debug(f"-------")
            phantom.debug(f"It's not SOP Artifact {n}")
            
        
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
