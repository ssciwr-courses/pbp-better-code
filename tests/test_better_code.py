import pytest
import subprocess
from pathlib import Path


@pytest.fixture(scope="module")
def input_file_path():
    # Get the repository directory
    current_dir = Path(__file__).resolve().parents[1]
    input_file_path = current_dir / "chapter5"
    return input_file_path


@pytest.fixture(scope="module")
def python_modules(input_file_path):
    # get the python files
    input_files = list(input_file_path.glob("*.py"))
    return input_files


def test_import(python_modules):
    total_failure = 0
    for module in python_modules:
        command = f"python -m py_compile {module}"
        failure = 0
        try:
            subprocess.check_output(command, shell=True)
        except subprocess.CalledProcessError as e:
            failure = e.returncode
        if failure != 0:
            print(f"Error: Could not import {module}")
        total_failure += failure
    assert total_failure == 0


def test_notebook(input_file_path):
    # try to run the notebook
    notebook_path = input_file_path / "better_code.ipynb"
    command = f"jupyter nbconvert --to notebook --execute {notebook_path} --output {notebook_path}"
    failure = 0
    try:
        subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        failure = e.returncode
    if failure != 0:
        print(f"Error: Could not run Jupyter on {notebook_path}")
    assert failure == 0
