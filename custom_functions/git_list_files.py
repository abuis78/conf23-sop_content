def git_list_files(repo_path_local=None, pull_response=None, **kwargs):
    """
    Args:
        repo_path_local
        pull_response
    
    Returns a JSON-serializable object that implements the configured data paths:
        vault_id_list
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import subprocess
    import os
    import re
    from git import Repo
    
    outputs = {}
    
    # Write your custom code here...
    def list_json_files(repo_path_local):
        json_files = []
        vault_id_list = []
        phantom.debug(repo_path_local)
        for root, dirs, files in os.walk(repo_path_local):
            for file in files:
                if file.endswith('.json'):
                    json_files.append(os.path.join(root, file))
                    file = os.path.join(root, file)
                    parts = file.split('/')
                    name = parts[-1]  
                    success, message, vault_id = phantom.vault_add(container=None, file_location=file, file_name=name, metadata=None, trace=False)
                    vault_id_list.append(vault_id)
                else:
                    phantom.debug("Fuck off")
        phantom.debug("JSON file liste: {}".format(json_files))
        phantom.debug("Vault ID file liste: {}".format(vault_id_list))
        outputs["vault_id_list"] = vault_id_list
        return vault_id_list

    json_files = re.findall(r'\b\w+\.json\b', pull_response)
    
    phantom.debug(json_files)
    
    #list_json_files(repo_path_local)
    
        
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
