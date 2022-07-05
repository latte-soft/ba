import os, shutil

# "Constant" values for validation etc..
directories = [
    "./build"
]

# "Constant" values for validation etc..
build_instructions = [
    { # README.md
        "type": "path",
        "current_path": "README.md",
        "new_path": "build/README.md"
    },
    { # CHANGELOG.txt
        "type": "path",
        "current_path": "CHANGELOG.txt",
        "new_path": "build/CHANGELOG.txt"
    },
    { # VERSION.txt
        "type": "path",
        "current_path": "VERSION.txt",
        "new_path": "build/VERSION.txt"
    },
    { # Basic Admin Essentials 2.0.rbxm
        "type": "command",
        "command": "rojo build \"default.project.json\" -o \"build/Basic Admin Essentials 2.0.rbxm\"",
        "new_path": "build/Basic Admin Essentials 2.0.rbxm"
    },
    { # Basic Admin Essentials 2.0.rbxmx
        "type": "command",
        "command": "rojo build \"default.project.json\" -o \"build/Basic Admin Essentials 2.0.rbxmx\"",
        "new_path": "build/Basic Admin Essentials 2.0.rbxmx"
    }
]

cmds_needed = [
    "rojo"
]

# Multi-use functions and variables for fast call
os_path = os.path

isdir = os_path.isdir
isfile = os_path.isfile
abspath = os_path.abspath
mkdir = os.mkdir
rmdir = os.rmdir

shutil_which = shutil.which
shutil_rmtree = shutil.rmtree

def safe_rmtree(path):
    try:
        shutil_rmtree(path)
    except Exception as err:
        print(f"\nError removing dir \"{path}\": {err}")
        quit()

    return None

def safe_readfile(path):
    try:
        opened_file = open(path, "r")
        opened_file_contents = opened_file.read()
        opened_file.close()

        return opened_file_contents
    except Exception as err:
        print(f"\nError reading file \"{path}\": {err}")
        quit()

    return None

def safe_writefile(path, contents):
    try:
        opened_file = open(path, "w")
        opened_file.write(contents)
        opened_file.close()
    except Exception as err:
        print(f"\nError writing file \"{path}\": {err}")
        quit()

    return None

# Check needed commands (`cmds_needed`)
print("Checking needed commands..")

for cmd in cmds_needed:
    if shutil_which(cmd):
        print(f"- Command \"{cmd}\" found!")
        continue

    print(f"- Needed command \"{cmd}\" not found, qutting process..")
    quit()

# Scan through needed build path(s) in-case rmdir is needed
print("\nScanning previous build directories..")

for directory in directories:
    if isdir(directory):
        print(f"- Existing \"{directory}\" directory found, removing..")
        safe_rmtree(directory)

    mkdir(directory)

# Start build operations
print("\nStarting build operations..")

for build_instruction in build_instructions:
    build_inst_type = build_instruction["type"]

    if build_inst_type == "path":
        current_path = build_instruction["current_path"]
        new_path = build_instruction["new_path"]

        print(f"- Creating file \"{new_path}\"..")
        safe_writefile(new_path, safe_readfile(current_path))

    elif build_inst_type == "command":
        build_command = build_instruction["command"]

        print(f"\n- Executing command: {build_command}\n")
        os.system(build_command)

# Finally; check files and directories
print("\nChecking created build files..")

for directory in directories:
    if isdir(directory):
        print(f"- Found directory \"{abspath(directory)}\"!")

for build_instruction in build_instructions:
    new_path = build_instruction["new_path"]

    if isfile(new_path):
        print(f"- Found file \"{abspath(new_path)}\"!")