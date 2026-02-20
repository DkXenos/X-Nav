# X-Nav

- A terminal-based UI tool that allows for quick navigation into specific project directories
- Solves the friction of manually typing long cd (change directory) paths when switching between multiple projects

# shortcut
- to open using terminal:
- nano ~/.zshrc
- alias SHORTCUT_NAME='python3 /project_directory/xterm.py'
- control + O 
- enter
- control + X

- then you can type SHORTCUT_NAME in terminal to open the program

# setup
- create a .env and fill out your directory:
- PROJECT_DIR = "file/file/file/parent_folder"

- parent_folder:
- >child_folder_1
- >child_folder_2
- >child_folder_3
- >child_folder_4
- >child_folder_5

- child_folder_1:
- >ProjectApp_1
- >ProjectApp_2
- >ProjectApp_3
- >ProjectApp_4
- >ProjectApp_5

- select with up or down arrow then enter.
- then terminal is directed to that directory

