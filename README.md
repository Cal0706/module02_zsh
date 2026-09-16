# ISM3232 - Module 2: zsh Navigation and File Operations

## Commands Practiced

| Command | What it does |
| pwd | Prints the current working directory |
| ls | Lists visible files and folders |
| ls -la | Lists all files including hidden ones |
| cd | Moves up one directory |
| cp | Copies a file |
| cd .. | Moves up one directory |
| touch | Creates a new empty file |
| echo | Prints text or writes text into a file |
| cat | Displays the full contents of a file |
| head -1 | Displays the first line of a file |
| mv | Moves a file |
| rm | Removes a file forever |

## AI Use Statement
I did not use AI for this lab.


## Week 3: Virtual Environments and .zshrc

### Virtual Environment Commands

| python3 -m venv .venv | Creates a Python virtual environment |
| source .venv/bin/activate | Activates the virtual environment |
| pip install pytest ruff | Installs both into file |
| deactivate | Exits the virtual environment |
| which python3 | Shows which Python installation is in use |
| source ~/.zshrc | Reloads the zsh configuration file |

### Aliases

| ll | Runs ls -la to show a detailed file list |
| c | Clears the terminal |
| py | Runs python3 |
| gs | Runs git status |
| ga | Runs git add . |
| gcmsg | Creates a Git commit with a message |
| gp | Runs git push |
| gl | Shows the Git log in one-line format |
|tree2 | Shows the directory tree two levels deep |

### Shell Functions

| mkcd | Creates a new directory and immediately enters it | 