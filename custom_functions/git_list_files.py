def git_list_files(repo_path_local=None, repo_path_remote=None, filter_file_endswith=None, **kwargs):
    """
    Args:
        repo_path_local
        repo_path_remote
        filter_file_endswith
    
    Returns a JSON-serializable object that implements the configured data paths:
        file_list
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    from git import Repo
    import os

    outputs = {}
    
    # Write your custom code here...

    # Konfigurieren Sie diese Parameter entsprechend
    github_repo_url = repo_path_remote  # Ihr Repository-URL
    local_repo_dir = repo_path_local # Lokales Repo-Verzeichnis

    # Erstellen Sie ein Repo-Objekt, das auf das lokale Repo verweist
    if not os.path.exists(local_repo_dir):
        os.makedirs(local_repo_dir)
        repo = Repo.clone_from(github_repo_url, local_repo_dir)
    else:
        repo = Repo(local_repo_dir)

    # Ziehen Sie die neuesten Änderungen vom Remote-Repo
    origin = repo.remote()
    origin.pull()

    # Überprüfen Sie alle Dateien in den Repositorys und aktualisieren Sie sie lokal, falls nötig
    for item in repo.tree():
        if item.path.endswith('.git'):  # ignorieren Sie .git Dateien
            continue

        file_path = os.path.join(local_repo_dir, item.path)
        if not os.path.exists(file_path) or os.path.getmtime(file_path) < item.commit.committed_date:
            print(f"Datei {item.path} wird aktualisiert ...")
            with open(file_path, 'wb') as file:
                file.write(item.data_stream.read())
            os.utime(file_path, times=(item.commit.committed_date, item.commit.committed_date))

        
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
