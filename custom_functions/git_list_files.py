def git_list_files(local_repo_path=None, online_repo_path=None, filter_file_endswith=None, **kwargs):
    """
    Args:
        local_repo_path
        online_repo_path
        filter_file_endswith
    
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

    def get_local_git_json_files(local_repo_path):
        # Git-Befehl ausführen, um alle Dateien im Repository zu erhalten
        cmd = ["git", "ls-tree", "--name-only", "-r", "HEAD"]
        output = subprocess.check_output(cmd, cwd=local_repo_path).decode().strip()

        # Die Ausgabe in eine Liste von Dateinamen aufteilen
        file_list = output.split("\n")

        # Filtere Dateien mit der Erweiterung ".json"
        json_files = [file for file in file_list if file.endswith(".json")]

        return json_files

    def is_local_file_older(file_path, local_repo_path):
        # Git-Befehl ausführen, um den letzten Commit-Zeitstempel für die Datei zu erhalten
        cmd = ["git", "log", "-1", "--format=%ct", "--", file_path]
        output = subprocess.check_output(cmd, cwd=local_repo_path).decode().strip()

        if output:
            local_timestamp = int(output)
            return local_timestamp
        else:
            return None

    def is_remote_file_newer(file_path, online_repo_path):
        # Git-Befehl ausführen, um den letzten Commit-Zeitstempel für die Datei zu erhalten
        cmd = ["git", "ls-remote", "--exit-code", "--quiet", "--refs", online_repo_path, "HEAD"]
        try:
            subprocess.check_output(cmd)
            return True  # Remote-Repository und Branch existieren
        except subprocess.CalledProcessError:
            return False  # Remote-Repository oder Branch existieren nicht

    def replace_with_remote_file(file_path, online_repo_path):
        # Git-Befehl ausführen, um die Datei mit der Version aus dem Remote-Repository zu ersetzen
        cmd = ["git", "checkout", "origin/HEAD", "--", file_path]
        subprocess.run(cmd, cwd=online_repo_path)


    # Lokale JSON-Dateien erhalten
    local_json_files = get_local_git_json_files(local_repo_path)

    # Überprüfe jede lokale Datei
    for file in local_json_files:
        local_file_path = os.path.join(local_repo_path, file)

        # Überprüfe, ob die lokale Datei älter ist als die Online-Version
        if is_local_file_older(local_file_path, local_repo_path):
            if is_remote_file_newer(file, online_repo_path):
                # Die Online-Version ist neuer, ersetze die lokale Datei
                replace_with_remote_file(file, online_repo_path)
                phantom.debug(f"Die lokale Datei '{file}' wurde mit der neueren Online-Version aktualisiert.")
            else:
                phantom.debug(f"Die lokale Datei '{file}' ist bereits auf dem neuesten Stand.")

        else:
            phantom.debug(f"Die lokale Datei '{file}' hat keine Versionsinformationen.")

    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
