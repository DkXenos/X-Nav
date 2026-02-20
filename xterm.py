import os
import shlex
import subprocess

try:
    from pick import pick
except ImportError:
    pick = None

MAD_DIR = os.environ.get("MAD_DIR", os.path.expanduser("~/Documents/MAD"))

def get_subfolders(base_dir: str) -> list[str]:
    return sorted(
        folder
        for folder in os.listdir(base_dir)
        if not folder.startswith(".") and os.path.isdir(os.path.join(base_dir, folder))
    )


def open_terminal_tab(target_path: str) -> None:
    safe_path = shlex.quote(target_path)
    command = f"cd {safe_path}; clear"
    script = f'''
tell application "Terminal"
    activate
    if (count of windows) is 0 then
        do script "{command}"
    else
        do script "{command}" in front window
    end if
end tell
'''.strip()
    subprocess.run(["osascript", "-e", script], check=True)


def main():
    try:
        if pick is None:
            print("Missing dependency: install with 'python3 -m pip install pick'")
            return

        if not os.path.isdir(MAD_DIR):
            print(f"Directory does not exist: {MAD_DIR}")
            return

        
        workspaces = get_subfolders(MAD_DIR)
        if not workspaces:
            print("No workspace folders found.")
            return

        workspace, _ = pick(workspaces, "Select a workspace:", indicator=">", default_index=0)
        workspace_path = os.path.join(MAD_DIR, workspace)

        
        projects = get_subfolders(workspace_path)
        if not projects:
            print(f"No projects found in {workspace}.")
            return

        project, _ = pick(projects, f"Select a project in {workspace}:", indicator=">", default_index=0)
        target_path = os.path.join(workspace_path, project)

        open_terminal_tab(target_path)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()