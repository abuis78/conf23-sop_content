def git_list_files(repo_path_local=None, repo_path_remote=None, filter_file_endswith=None, artifact_name_prefix=None, artifact_severity=None, **kwargs):
    """
    Args:
        repo_path_local
        repo_path_remote
        filter_file_endswith
        artifact_name_prefix
        artifact_severity
    
    Returns a JSON-serializable object that implements the configured data paths:
        vault_id_list
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import subprocess
    import os
    
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

    def auflisten_git_verzeichnis(repo_path_local):
        # Wechseln Sie zum lokalen Repository-Verzeichnis
        os.chdir(repo_path_local)

        # Liste alle Dateien, die vom lokalen Git-Repository verfolgt werden
        dateien = subprocess.check_output(["git", "ls-files"]).decode("utf8")
        phantom.debug("Dateien im lokalen Git-Repository:")
        phantom.debug(dateien)

    def check_git_diff(repo_path_remote):
        # Holt die neuesten Informationen vom remote repository
        subprocess.run(["git", "remote", "set-url", "origin", repo_path_remote])
        subprocess.run(["git", "fetch"])
        
        # Holt die neuesten Informationen vom remote repository
        subprocess.run(["git", "fetch"])
        
        # Überprüft den Unterschied zwischen dem lokalen und dem remote repository
        result = subprocess.check_output(["git", "diff", "--name-only", "origin/main"]).decode("utf8")

        if result:
            phantom.debug("\nEs gibt Unterschiede zwischen dem lokalen und dem remote Repository:")
            phantom.debug(result)
            phantom.debug("\nAktualisiere das lokale Repository...")
            subprocess.run(["git", "pull"])
        else:
            phantom.debug("\nKeine Unterschiede gefunden. Das lokale Repository ist aktuell.")



    #auflisten_git_verzeichnis(repo_path_local)
    #check_git_diff(repo_path_remote) 
    list_json_files(repo_path_local)
    
        
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
