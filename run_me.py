
### Python Script: `run_me.py`

import os
import subprocess

# Define the project directory
project_dir = os.path.join(os.path.expanduser("~"), "Desktop", "code_projects", "kc303va1")

# Define the example file path
example_file = os.path.join(project_dir, "example.kc303va1")

# Run the interpreter with the example file
try:
    subprocess.run(["python", "interpreter.py", example_file], cwd=project_dir, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running the interpreter: {e}")
    exit(1)

print("Interpreter ran successfully!")
