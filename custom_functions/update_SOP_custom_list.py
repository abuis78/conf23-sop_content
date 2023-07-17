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
        phantom.debug(f"Art ID: {a}")
        url_filter = '?_filter_name__icontains="' + str(prefix_filter) +'"&_filter_container="' + str(container_id) +'"&_filter_id="' + str(a) + '"'
        r_url = phantom.build_phantom_rest_url('artifact')
        
        url = r_url + url_filter
        r = phantom.requests.get(url,verify=False)
        v = r.json()
        # phantom.debug(f"Daten: {v['data']}")
        for item in v['data']:
            n = item['cef']['name']
            v_id = item['cef']['version']
            ap = item['cef']['automation_phase']
            a = item['cef']['alert']
            
            if v_id is not None:
                r_url2 = phantom.build_phantom_rest_url('decided_list',list_name)
                r2 = phantom.requests.get(r_url2,verify=False)
                ln = r2.json()
                #phantom.debug(f"Custom-Liste: {ln}")
                phantom.debug(f"---START Check Liste----")
                for i, sublist in enumerate(ln["content"]):
                    #phantom.debug(f"sublist {sublist}")
                    f = False
                    if sublist[0] == n:
                        # phantom.debug(f"{n} ist in Subliste - in row {i}")
                        f = True
                        break
                        
                    if f:
                        phantom.debug(f"SOP {n} was found! - in row {i}")
                    else:
                        phantom.debug(f"SOP {n} was NOT found!")
                    """
                    if n in sublist[0]:
                        phantom.debug(f"The SOP {n} is in the list Available")
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
                    elif i == "":
                        phantom.debug("SOP ist not in list")
                        phantom.debug(f"missing SOP: {a}")
                        r_url4 = phantom.build_phantom_rest_url('decided_list',list_name)
                        phantom.debug(f"New Data: {n} {v_id} {ap} {a}")
                        sublist = [n,v_id,ap,a]
                        data = { "append_rows": [sublist] }
                        phantom.debug(f"New Data: {data}")
                        r4 = phantom.requests.post(r_url4, json=data, verify=False).json()
"""
            
            elif v_id is  None:
                phantom.debug(f"-------")
                phantom.debug(f"It's not SOP Artifact {n}")
    phantom.debug(f"---ENDE----")
        
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
