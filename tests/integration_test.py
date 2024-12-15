import subprocess
import shutil
import tempfile
import os
import sys
from pathlib import Path


def run_command(command, cwd=None):
    """Runs a shell command and returns its output and error."""
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=cwd
    )
    stdout, stderr = process.communicate()
    return process.returncode, stdout.decode(), stderr.decode()


def test_integration_and_e2e():
    """Tests integration of tools in the template."""

    # Create temp dir for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Copy the template to the temp dir
        template_dir = Path(__file__).parent.parent
        shutil.copytree(template_dir, temp_dir, dirs_exist_ok=True)

        # Activate venv and install deps using uv
        print("creating venv")
        ret, out, err = run_command("python -m uv venv", cwd=temp_dir)
        assert (
            ret == 0
        ), f"uv venv command failed with error:\n{err}\nand output:\n{out}"
        print("installing dependencies")
        ret, out, err = run_command("python -m uv sync", cwd=temp_dir)
        assert (
            ret == 0
        ), f"uv sync command failed with error:\n{err}\nand output:\n{out}"
        print("installing pre-commit hooks")
        ret, out, err = run_command("pre-commit install", cwd=temp_dir)
        assert (
            ret == 0
        ), f"pre-commit install command failed with error:\n{err}\nand output:\n{out}"

        # Test linters and formatters using pre-commit
        print("running pre-commit")
        ret, out, err = run_command("pre-commit run --all-files", cwd=temp_dir)
        assert ret == 0, f"pre-commit run failed with error:\n{err}\nand output:\n{out}"

        # Test mypy
        print("running mypy")
        ret, out, err = run_command("mypy src/my_package", cwd=temp_dir)
        assert ret == 0, f"mypy failed with error:\n{err}\nand output:\n{out}"

        # Test pytest
        print("running pytest")
