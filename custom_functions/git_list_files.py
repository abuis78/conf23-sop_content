def git_list_files(repo_path_local=None, repo_path_remote=None, filter_file_endswith=None, artifact_name_prefix=None, artifact_severity=None, **kwargs):
    """
    Args:
        repo_path_local
        repo_path_remote
        filter_file_endswith
        artifact_name_prefix
        artifact_severity
    
    Returns a JSON-serializable object that implements the configured data paths:
        file_list
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    import subprocess
    import os
    
    outputs = {}
    
    # Write your custom code here...
    phantom.debug(filter_file_endswith[0])
    filter_file_endswith = str(filter_file_endswith[0])

    def auflisten_git_verzeichnis(repo_path_local):
        os.chdir(repo_path_local)

        dateien = subprocess.check_output(["git", "ls-files"]).decode("utf8")
        phantom.debug("Files in the local Git repository:")
        phantom.debug(dateien)

    def check_git_diff(repo_path_remote):
        subprocess.run(["git", "remote", "set-url", "origin", repo_path_remote])
        subprocess.run(["git", "fetch"])
        
        subprocess.run(["git", "fetch"])
        
        result = subprocess.check_output(["git", "diff", "--name-only", "origin/main"]).decode("utf8")
        
        changed_files = []
        
        if result:
            phantom.debug("\nThere are differences between the local and remote repository:")
            changed_files = [datei for datei in result.split('\n')[:-1] if datei.endswith(filter_file_endswith)]
            if changed_files:
                phantom.debug("Modified "+filter_file_endswith+" files:")
                phantom.debug('\n'.join(changed_files))
                phantom.debug("\nUpdate the local repository...")
                subprocess.run(["git", "pull"])
            else:
                phantom.debug("No ."+filter_file_endswith+" files were changed.")
        else:
            phantom.debug("\nNo differences found. The local repository is up to date.")
            
        phantom.debug(changed_files)
        for item in changed_files:
            path_file = repo_path_local + item
            success, message, vault_id = phantom.vault_add(file_location=path_file,file_name=item)
            phantom.debug(vault_id)
            raw = {}
            cef = {}
            cef['vaultId'] = vault_id
            name = artifact_name_prefix + item
            success, message, artifact_id = phantom.add_artifact(container=None, raw_data=raw, cef_data=cef, label='sop',name=name, severity=artifact_severity,identifier=None,artifact_type='sop')
            phantom.debug('artifact added as id:'+str(artifact_id))
        outputs["file_list"]=changed_files
        return changed_files


    auflisten_git_verzeichnis(repo_path_local)
    check_git_diff(repo_path_remote)
    


        
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
