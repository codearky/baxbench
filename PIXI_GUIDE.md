# Pixi Installation and Usage Guide for BaxBench

This guide provides detailed instructions for using [Pixi](https://pixi.sh) with BaxBench.

## Why Pixi?

Pixi is a modern, cross-platform package manager that provides:
- Fast dependency resolution and installation
- Reproducible environments across platforms
- Built-in task management
- No need to manually install Python - pixi handles it for you
- Support for both conda and PyPI packages

## Installation

### 1. Install Pixi

Follow the instructions at [https://pixi.sh/latest/#installation](https://pixi.sh/latest/#installation).

Quick install commands:

**Linux & macOS:**
```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

**Windows (PowerShell):**
```powershell
iwr -useb https://pixi.sh/install.ps1 | iex
```

### 2. Install BaxBench Dependencies

From the BaxBench repository root:

```bash
pixi install
```

This will:
- Install Python 3.12
- Install all required dependencies (requests, openai, docker, etc.)
- Set up the development environment

## Usage

### Running Scripts

To run any Python script in the project environment:

```bash
pixi run python <path_to_script> <args>
```

Example:
```bash
pixi run python baxbench/main.py --models gpt-4o --mode generate --n_samples 10 --temperature 0.4
```

### Using Predefined Tasks

Pixi provides convenient shortcuts for common operations:

#### Generate Solutions
```bash
pixi run generate
```
Note: You'll need to add additional arguments like `--models`, `--n_samples`, etc.

Full example:
```bash
pixi run python baxbench/main.py --models gpt-4o --mode generate --n_samples 10 --temperature 0.4
```

#### Test Solutions
```bash
pixi run python baxbench/main.py --models gpt-4o --mode test --n_samples 10 --temperature 0.4
```

#### Evaluate Results
```bash
pixi run python baxbench/main.py --models gpt-4o --mode evaluate --n_samples 10 --temperature 0.4
```

#### Run Type Checking (MyPy)
```bash
pixi run mypy
```

#### Set Up Pre-commit Hooks
```bash
pixi run pre-commit install
```

### List Available Tasks

To see all available tasks:
```bash
pixi task list
```

### Shell Access

To start a shell with the pixi environment activated:
```bash
pixi shell
```

In this shell, you can run Python and other commands directly without the `pixi run` prefix:
```bash
python baxbench/main.py --help
```

Exit the shell with `exit` or Ctrl+D.

## Environment Variables

Remember to set your API keys in your environment before running generation tasks:

```bash
export OPENAI_API_KEY="<your_API_key>"
export TOGETHER_API_KEY="<your_API_key>"
export ANTHROPIC_API_KEY="<your_API_key>"
export OPENROUTER_API_KEY="<your_API_key>"
```

These should be set in your shell or in your `~/.bashrc` (or equivalent) file.

## Troubleshooting

### Clean and Reinstall

If you encounter issues, you can clean and reinstall:

```bash
# Remove the pixi environment
rm -rf .pixi

# Reinstall
pixi install
```

### Check Python Version

To verify Python 3.12 is installed:
```bash
pixi run python --version
```

### Verify Dependencies

To check if dependencies are installed correctly:
```bash
pixi run python -c "import requests, openai, docker, tabulate; print('All dependencies OK')"
```

### Test Package Imports

To verify the baxbench package can be imported:
```bash
pixi run python -c "from baxbench.scenarios import all_scenarios; print(f'{len(all_scenarios)} scenarios available')"
```

## Comparing Pixi with Pipenv

| Feature | Pixi | Pipenv |
|---------|------|--------|
| Python Installation | Automatic | Manual |
| Dependency Resolution | Fast | Slower |
| Cross-platform | Excellent | Good |
| Task Management | Built-in | Via scripts |
| Lock File | `pixi.lock` | `Pipfile.lock` |
| Run Command | `pixi run` | `pipenv run` |

Both tools are supported in BaxBench, so you can choose the one that works best for your workflow.

## Additional Resources

- [Pixi Documentation](https://pixi.sh/latest/)
- [Pixi GitHub Repository](https://github.com/prefix-dev/pixi)
- [BaxBench README](README.md)

