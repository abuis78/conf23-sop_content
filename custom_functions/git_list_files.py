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

    file_liste = re.findall(r'\b\w+\.json\b', pull_response)
    
    phantom.debug("file_liste: {}".format(file_liste))
    vault_id_list = []
    if file_liste:
        for file_name in file_liste:
            for root, directories, file in os.walk(repo_path_local):
                if file_name in file:
                    voller_pfad = os.path.join(root, file_name)
                    success, message, vault_id = phantom.vault_add(container=None, file_location=voller_pfad, file_name=file_name, metadata=None, trace=False)
                    vault_id_list.append(vault_id)
    else:
        phantom.debug("file_liste is emty")       
    
    outputs["vault_id_list"] = vault_id_list
    
        
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
