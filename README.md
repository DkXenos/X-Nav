# X-Nav

- A terminal-based UI tool that allows for quick navigation into specific project directories
- Solves the friction of manually typing long cd (change directory) paths when switching between multiple projects
- Doesnt support windows for now i think

# shortcut
- to open using terminal:
- nano ~/.zshrc
- alias SHORTCUT_NAME='python3 /project_directory/xterm.py'
- control + O 
- enter
- control + X

- then you can type SHORTCUT_NAME in terminal to open the program

# xcode
- sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
- verify: xcode-select -p (it should print a directory to Developer folder)

- commands:
- open -a Xcode . (open current directory using xcode)
- open -a Xcode (open xcode with no directory)
- xed . (open xcode with current directory but shorter)
- after cd ke prokject you can just type xed . to open xcode on that directory
- or you can add alias ex: ("alias oxc='open -a Xcode' to open xcode with no directory selected")

# flow
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

