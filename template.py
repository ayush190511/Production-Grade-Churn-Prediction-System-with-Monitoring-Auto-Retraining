import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "churn_prediction"

# Ensure directories end with / to distinguish them from files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/data/", # Directory
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/features/",
    f"src/{project_name}/features/__init__.py",
    f"src/{project_name}/models/",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/monitoring/",
    f"src/{project_name}/monitoring/__init__.py",
    f"src/{project_name}/logger.py",
    "config/config.yaml", # Added a file inside config
    "tests/__init__.py",
    "requirements.txt",
    "setup.py",
    "notebooks/", # Directory
]

for filepath in list_of_files:
    filepath = Path(filepath)
    
    # 1. Handle Directories (Entries ending in / or with no extension)
    if str(filepath).endswith("/") or filepath.suffix == "":
        os.makedirs(filepath, exist_ok=True)
        logging.info(f"Creating directory: {filepath}")
        continue # Skip the file creation logic for directories

    # 2. Handle Files
    filedir = filepath.parent
    if filedir != Path("."):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Ensuring directory: {filedir} for file: {filepath.name}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath.name} already exists and is not empty.")