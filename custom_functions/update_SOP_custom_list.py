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
    import re
    
    outputs = {}
    
    # Write your custom code here...


    def check_and_format_json(data):
        if isinstance(data, str):  # If data is a string, we try to load it as JSON
            try:
                json.loads(data)  # Try to parse string as JSON to check if it is valid
                phantom.debug("The string is a valid JSON.")
            
                # Check if the string contains 'false' or 'true'
                if re.search(r"'false'|'true'", data, re.IGNORECASE):
                    # Replace 'false' and 'true' with "false" and "true"
                    data = re.sub(r"'false'", '"false"', data, flags=re.IGNORECASE)
                    data = re.sub(r"'true'", '"true"', data, flags=re.IGNORECASE)
                else:
                    data = data.replace("'", '"')  # Replace single quotes with double quotes

                # Check if modified string is still valid JSON
                try:
                    json.loads(data)
                except json.JSONDecodeError:
                    phantom.debug("The modified string is not a valid JSON.")
                    return None
            
            except json.JSONDecodeError:
                phantom.debug("The string is not a valid JSON.")
                return None
        elif isinstance(data, dict):  # If data is a dictionary, we dump it into a JSON string
            try:
                data = json.dumps(data,ensure_ascii=False, default=str)
                phantom.debug("The dictionary has been formatted into a valid JSON string:", data)
            except (TypeError, ValueError):
                phantom.debug("The dictionary could not be formatted into a valid JSON string.")
                return None
        else:
            phantom.debug("The data is neither a dictionary nor a JSON string.")
            return None
    
        phantom.debug(f"JSON Daten: {data}")
        return data


    def create_update_workbook(task,name,json,a):
        phantom.debug(f"IDD {a}")
        filter_url = '?_filter_id="' + str(a) + '"'
        url = phantom.build_phantom_rest_url('artifact')
        url = url + filter_url
        phantom.debug(f"URL {url}")
        r = phantom.requests.get(url, verify=False)
        data = r.json()
        if len(data['data']) > 0:
            sop_json = data['data'][0]['cef']['sop_json']
        else:
            phantom.debug("Die Liste 'data' ist leer.")

        phantom.debug(f"request r {data}")
        
    
                          
    #check if List
    
    for a in artifact_id_list:
        phantom.debug(f"Art ID: {a}")
        url_filter = '?_filter_name__icontains="' + str(prefix_filter) +'"&_filter_container="' + str(container_id) +'"&_filter_id="' + str(a) + '"'
        r_url = phantom.build_phantom_rest_url('artifact')
        
        url = r_url + url_filter
        r = phantom.requests.get(url,verify=False)
        v = r.json()
        # phantom.debug(f"Daten: {v['data']}")
        row = 0
        for item in v['data']:
            n = item['cef']['name']
            v_id = item['cef']['version']
            ap = item['cef']['automation_phase']
            a = item['cef']['alert']
            json_data = item['cef']['sop_json']
            
            if v_id is not None:
                
                r_url2 = phantom.build_phantom_rest_url('decided_list',list_name)
                r2 = phantom.requests.get(r_url2,verify=False)
                ln = r2.json()
                #phantom.debug(f"Custom-Liste: {ln}")
                phantom.debug(f"---START Check Liste----")
                f = False
                for i, sublist in enumerate(ln["content"]):
                    if n == sublist[0]:
                        f = True
                        if int(v_id) <= int(sublist[1]):
                            # SOP is in the SOP Custom List
                            phantom.debug(f"Nothing to Update for SOP: {n} this one is still up to date")
                        elif int(v_id) > int(sublist[1]):
                            # SOP needes to be update due to the new version no
                            phantom.debug(f"SOP Update")
                            phantom.debug(f"Element was found in row {i + 1} ")
                            row = i
                            r_url3 = phantom.build_phantom_rest_url('decided_list',list_name)
                            sublist[1] = str(v_id) 
                            l_e = sublist
                            data = { "update_rows": { row : sublist }}
                            phantom.debug(f"New Data: {data}")
                            r3 = phantom.requests.post(r_url3, json=data, verify=False).json()
                            create_update_workbook("u",n, json_data,a)
                        break
                if not f:
                    # SOP is not jet in the Custom List create a new entry
                    phantom.debug(f"Create new entry for {n}")
                    r_url4 = phantom.build_phantom_rest_url('decided_list',list_name)
                    phantom.debug(f"New Data: {n} {v_id} {ap} {a}")
                    sublist = [n,v_id,ap,a]
                    data = { "append_rows": [sublist] }
                    phantom.debug(f"New Data: {data}")
                    r4 = phantom.requests.post(r_url4, json=data, verify=False).json()
                    create_update_workbook("c",n, json_data,a)
                        
    phantom.debug(f"---ENDE----")
        
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
