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
    from git import Repo
    
    outputs = {}
    
    # Write your custom code here...



    # Pfad zum lokalen Repository
    local_repo_path = repo_path_local

    # Pfad zum entfernten Repository
    remote_repo_path = repo_path_remote

    # Erstellen Sie ein Repo-Objekt für das lokale Repo
    local_repo = Repo(local_repo_path)

    # Überprüfen Sie, ob das lokale Repo sauber ist (keine Änderungen)
    if local_repo.is_dirty(untracked_files=True):
        phantom.debug('Das lokale Repository hat nicht verfolgte Dateien oder Änderungen.')

    # Fetchen Sie alle Änderungen vom Remote-Repo
    fetch_info = local_repo.remotes.origin.fetch()

    # Erstellen Sie eine Liste für aktuellere Dateien
    newer_files = []

    # Gehen Sie durch alle Commits von HEAD bis zum neuesten Fetch
    for commit in local_repo.iter_commits('HEAD..origin/master'):
        # Gehen Sie durch jede geänderte Datei in jedem Commit
        for file in commit.stats.files:
            newer_files.append(file)

    # Drucken Sie die aktuelleren Dateien
    for file in newer_files:
        phantom.debug(file)

        
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
