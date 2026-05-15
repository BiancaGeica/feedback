# Feedback Generator

## Purpose

This project is designed to generate realistic, anonymized feedback datasets in JSON format.

The primary goal is to provide reliable, non-sensitive data for testing the main project's data processing and analysis scripts. It features complete Moodle schema compliance (25 questions) and context-aware text generation based on dynamic student profiles.

## Content

- `main.py`
    - This script loads course metadata from Pickle files and uses predefined logic to create simulated student feedback in the `feedback_contents` directory.

- `templates.py`
    - Contains the logic and templates for generating realistic, context-aware text feedback based on the student's generated grade and profile.

- `test_generator.py`
    - Unit testing script (the checker) that validates the output schema length (ensuring 25 questions) and verifies logical consistency between the assigned grades and the generated text.

- `convert_script.py`
    - Utility script for converting data, typically between Pickle and JSON formats.

- `config.conf`
    - Configuration file containing settings for running the script.

- `pickles/`
    - Directory that will be created, containing the necessary input Pickle files:
    - `feedbacks.p` - Contains the list of existing feedbacks from IDs and their configurations.
    - `courses.p` - Contains metadata about courses: ID, name, category ID.
    - `categories.p` - Contains metadata about course categories.
    - `courses4categories.p` - Contains metadata about relationship between courses and categories.

- `jsons/`
    - Directory containing the JSON versions of the metadata files (e.g., `categories.json`, `courses.json`) and `profesori.json`, which provides mock teacher names for dynamic extraction.

- `feedback_contents/`
    - This is the directory that will be created automatically after running the python script.
    - It contains the resulting feedback JSON files.
    - e.g. `1000.json`.

## Requirements for Running the Script

- Python Version: 3.x

- The script requires the existence of the following Pickle files: `feedbacks.p`, `courses.p`, `categories.p`, `courses4categories.p`

## Virtual Environment Setup

- It is recommended to use a virtual environment (venv) to isolate project dependencies.

- Creating venv steps:
    - create venv: `python3 -m venv venv`
    - activate venv:
        - Linux/macOS: `source venv/bin/activate`
        - Windows: `venv\Scripts\activate`
    - The script uses `json`, `os`, `pickle`, `random`, and `unittest`. These are standard built-in Python libraries, so no additional `pip install` commands are required for them to run.

- When you finished working with the project, deactivate the environment: `deactivate` or `exit`

## Running the Script

- `python3 convert_script.py` : this will generate the pickle files based on the JSONs necessary to run the main script.

- `python3 main.py` : this version will take the interval for the number of students that is set in the script `config.conf`.

- `python3 main.py --min-students <val_min> --max-students <val_max>` : the interval for the number of students will be set as [val_min, val_max].
- those 2 values can be whatever positive number you want with the condition that val_min <= val_max.

## Testing the Script

- `python3 -m unittest test_generator.py -v` : runs the test suite (the checker) to ensure the generated data respects the 25-question schema and maintains logical text consistency based on student profiles.