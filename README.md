# Modern Python Project Template

This repository provides a modern Python project template, designed for efficient development with `uv`, `ruff`, `mypy`, `pytest`, and Git hooks powered by `pre-commit`. It aims to provide a solid foundation for new Python projects, promoting code quality, consistency, and reduced errors. This template is designed to be used with Linuxbrew for consistent package management across platforms.

## Features

*   **`uv` for Dependency Management:** Fast and efficient dependency resolution and virtual environment management.
*   **`ruff` for Linting and Formatting:** Enforces consistent code style, catches errors early, and provides auto-fixing capabilities.
*   **`mypy` for Type Checking:** Adds static typing to your Python code, preventing type-related errors.
*   **`pytest` for Testing:** Provides a robust and flexible testing framework.
*   **`pre-commit` for Git Hooks:** Automates code quality checks before every commit.
*   **`pyproject.toml` for Configuration:** Centralized project configuration using the official `pyproject.toml` standard.
*   **Clean Project Structure:** A well-defined structure with separate `src` and `tests` directories.
*   **Cross-Platform Compatibility:** Designed for use with Linuxbrew to provide a consistent development environment across Windows (via WSL), macOS, and Linux.

## Getting Started

Follow these steps to set up this project template for development:

### 1. Platform Specific Initialization

Before cloning the repository, make sure you have Linuxbrew installed (or Homebrew on macOS).

### Windows/WSL Setup

1.  **Install WSL:** Follow the official Microsoft instructions to install WSL and choose a Linux distribution (e.g., Ubuntu).

2.  **Open a *Direct* WSL Terminal:**
    *   **Do NOT use `wsl` from a Windows terminal (like PowerShell or Command Prompt).**
    *   **In VS Code:** Open a *new* integrated terminal by clicking the "+" button on the terminals tab, and select your WSL distribution (e.g., "Ubuntu", "Debian") from the dropdown menu.
    *   **From Start Menu:** Alternatively, launch your WSL distribution's terminal directly from the Windows Start Menu (e.g., "Ubuntu", "Debian").

    **All subsequent steps in this section must be executed within this *direct* WSL terminal.**

3.  **Install Base Dependencies (Within WSL):**
    ```bash
    sudo apt update && sudo apt install -y build-essential curl file git
    ```
4.  **Install Linuxbrew:**
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
5.  **Add Linuxbrew to `PATH`:**
    Add the following lines to your `~/.bashrc` or `~/.zshrc` (depending on your shell):
    ```bash
    export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
    export MANPATH="/home/linuxbrew/.linuxbrew/share/man:$MANPATH"
    export INFOPATH="/home/linuxbrew/.linuxbrew/share/info:$INFOPATH"
    ```
    Then run `source ~/.bashrc` or `source ~/.zshrc`.
6.  **Install Python via Linuxbrew:** `brew install python`

#### macOS

1.  **Install Homebrew:** If you don't have it already, install Homebrew by running the following command in the terminal:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
2.  **Install Python via Homebrew:** `brew install python`

#### Linux

1.  **Install Linuxbrew:** Follow the instructions on the Linuxbrew homepage: [https://brew.sh/](https://brew.sh/)
2.  **Install Python via Linuxbrew:** `brew install python`

### 2. Project Setup

Once Linuxbrew (or Homebrew on macOS) and Python are installed, you can continue with the following steps:

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <project_name>
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    uv venv
    ```
    This command creates a virtual environment, if one does not exist already.

3.  **Install Dependencies:**
    ```bash
     uv sync
    ```
    This command installs all dependencies from your lock file (`uv.lock`), including development dependencies.

4.  **Install Git Hooks:**
    ```bash
    pre-commit install
    ```
    This command installs the pre-commit hooks that ensure formatting and linting happen automatically before each commit.

5. **Create a lock file**:
    ```bash
    uv lock
    ```
    This command creates a lock file which locks all dependencies in the project to a known version.

## Development

*   **Code in `src`:** Start adding your Python code inside the `src/my_package` directory.
*  **Create tests:** Create your tests in the `tests` directory, and import your code using the name of the package, in this case `my_package`.
*   **Run tests:** Use `pytest` in the root folder to run tests.
  ```bash
  pytest
  ```

## Automatic Linting and Formatting

*   `ruff` automatically fixes formatting and linting errors when you save changes.

## Type Checking

*   `mypy` is run as part of the pre-commit hooks and will catch any type issues.

## Configuration

### Core Configuration

The project's core configuration is located in the `pyproject.toml` file.

*   **Project Metadata:**
    *   Basic project information like name, version, description, authors, etc.
    *   Python version specified in `requires-python`
*   **Dependencies:**
    *   Project's dependencies listed in the `[project.dependencies` array.
    *   Development dependencies listed in the `[project.optional-dependencies.dev]` array, or you can add additional groups.

#### `[tool.uv]`

*   `default-groups = ["dev"]`: Sets dev dependencies to be installed by default.

#### `[tool.ruff]`

*   `line-length = 100`: Sets the maximum line length.
*   `select`: List of rules enabled from `ruff` and different linters.
*   `ignore`: List of rules ignored.
*   `fix = true`: Automatically fix linting errors.
*   `per-file-ignores`: Configure specific files or patterns for ignoring certain rules.
*    `quote-style = "single"`: Sets style to use single quotes.

#### `[tool.mypy]`

*   `mypy_path = "src"`: The location of your packages for mypy type checking.
*   `python_version = "3.10"`: The Python version being used.
*   `strict = true`: Enables strict type checking options.
*   `plugins = ["pytest_mypy_plugins"]`: Makes pytest plugin available for mypy.

### Git Hooks Configuration (`.pre-commit-config.yaml`)

This file configures `pre-commit`, a tool that runs checks before each commit. It includes:

*   **General-Purpose Hooks (`pre-commit-hooks`):** Trailing whitespace removal, end-of-file newline enforcement, YAML validation, etc.
*   **`ruff` Hook (`astral-sh/ruff-pre-commit`):** Automatically fixes `Ruff` errors (`ruff --fix`).
*   **`black` Hook (`psf/black`):** Automatically reformats your code with the black formatter
*   **`mypy` Hook (`pre-commit/mirrors-mypy`):** Checks code for type errors with `mypy`

### VS Code Configuration (`.vscode/settings.json`)

This file configures the VS Code editor.

*   **Type Checking:** `python.analysis.typeCheckingMode`: Enables Python's type checker.
*   **Linting:** `python.linting.ruffEnabled`: Enables `ruff` as the linter.
*   **Formatting:** `python.formatting.provider`: Disables default formatter, since pre-commit is being used.
*   **Ruff Settings:** Settings for Ruff language server (e.g., `importStrategy`, `organizeImports`, `fixAll`, `showSyntaxErrors`).
*   `ruff.configurationPreference`: prioritize file based configs.

## Common and Useful Configurations (Not in Base Config)

Here are some additional configurations that are often useful and are commonly used or at least helpful if applicable.

### 1. Custom Ruff Rules and Ignores

*   **`[tool.ruff.lint.per-file-ignores]`:** Use this section to ignore rules for specific files. For example:

    ```toml
    [tool.ruff.lint.per-file-ignores]
    "tests/*" = ["S101", "ANN"]  # Allow asserts and skip annotations in tests.
    "src/my_package/legacy.py" = ["B001", "B002"] # Ignore specific bugbear rules for legacy code
    ```

*   **`extend-select` and `extend-ignore`:** Add additional rules or ignore rules for the project.

    ```toml
    [tool.ruff.lint
    extend-select = ["PT"] # adds rules from flake8-pytest
    extend-ignore = ["ANN101", "ANN401"] # extends the ignore rules
    ```

*   **Rule Specific Options:** Certain rules can be further configured, like for example isort options.

    ```toml
    [tool.ruff.lint.isort]
    force-wrap-aliases = true
    ```

### 2. Custom Mypy Options

*   **`ignore_missing_imports`:** If you are having issues with dependencies and type checking. Set to `true`.

    ```toml
    [tool.mypy]
    ignore_missing_imports = true
    ```

*   **`disallow_untyped_defs`:** If you want to require type annotations in function definitions, use `disallow_untyped_defs = true`.

    ```toml
    [tool.mypy]
    disallow_untyped_defs = true
    ```

*  **`disallow_any_explicit`**: If you want to disallow explicit use of `Any` types in the code.

   ```toml
   [tool.mypy]
    disallow_any_explicit = true
   ```

*   **`warn_unreachable`:** If you want to enable warning for unreachable code

    ```toml
    [tool.mypy]
    warn_unreachable = true
    ```

    See [Mypy configuration docs](https://mypy.readthedocs.io/en/stable/config_file.html) for a complete listing of available settings.

### 3. `uv` Configuration

*   **`constraint-dependencies`:** If you want to pin a transitive dependency to a specific version use `constraint-dependencies`.

    ```toml
    [tool.uv]
        constraint-dependencies = ["cryptography<42.0.0"]
    ```

*   **`override-dependencies`:** Forces a dependency to use a specific version

    ```toml
    [tool.uv]
        override-dependencies = ["cryptography==42.0.0"]
    ```

*   **`index`:** You can specify additional package indexes to get dependencies from

    ```toml
    [[tool.uv.index]]
     name = "pytorch"
     url = "https://download.pytorch.org/whl/cu121"
     explicit = true

     [tool.uv.sources]
     torch = { index = "pytorch" }
    ```

### 4. Test Configuration

*   `pytest.ini`: Create a `pytest.ini` in your root folder to configure options for `pytest`.

    ```ini
    [pytest]
    testpaths = tests
    addopts =
        --cov=src/my_package
        --cov-report term-missing
        -vv
    ```

    This will make sure that pytest runs against all tests in the tests folder

    It will also add coverage info for `src/my_package`

    It will also run in verbose mode

### 5. `pre-commit` Config

You can add additional hooks from other repositories.

You can configure existing hooks as needed. For example if you want to exclude files from ruff you can use:

```yaml
-   id: ruff
    args: ["--fix", "--exclude", "path/to/exclude"]
```

## Contributing

If you would like to add features to this template, or suggest improvements, feel free to create a pull request.