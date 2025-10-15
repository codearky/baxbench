# BaxBench + Pixi Quick Reference

## Installation

```bash
# Install pixi
curl -fsSL https://pixi.sh/install.sh | bash

# Install BaxBench dependencies
cd /path/to/baxbench
pixi install
```

## Running Scripts

```bash
# Run any Python script
pixi run python baxbench/main.py --help

# Run with arguments
pixi run python baxbench/main.py \
  --models gpt-4o \
  --mode generate \
  --n_samples 10 \
  --temperature 0.4
```

## Predefined Tasks

```bash
# List all available tasks
pixi task list

# Run specific tasks (need to add full arguments)
pixi run python baxbench/main.py --models gpt-4o --mode generate --n_samples 10 --temperature 0.4
pixi run python baxbench/main.py --models gpt-4o --mode test --n_samples 10 --temperature 0.4
pixi run python baxbench/main.py --models gpt-4o --mode evaluate --n_samples 10 --temperature 0.4

# Run type checking
pixi run mypy

# Install pre-commit hooks
pixi run pre-commit install
```

## Shell Access

```bash
# Start a shell with the pixi environment
pixi shell

# Inside the shell, run commands directly
python baxbench/main.py --help
python --version
exit
```

## Using from Another Project

### In your other project's `pyproject.toml`:

```toml
[tool.pixi.pypi-dependencies]
baxbench = { path = "../baxbench", editable = true }
```

### In your Python code:

```python
from baxbench.scenarios import all_scenarios
from baxbench.env import all_envs

print(f"Found {len(all_scenarios)} scenarios")
```

## Environment Management

```bash
# Show environment info
pixi info

# Update dependencies
pixi update

# Clean and reinstall
rm -rf .pixi
pixi install

# Show installed packages
pixi run pip list
```

## Common Workflows

### Generate Solutions

```bash
pixi run python baxbench/main.py \
  --models gpt-4o \
  --mode generate \
  --n_samples 10 \
  --temperature 0.4
```

### Test Solutions

```bash
pixi run python baxbench/main.py \
  --models gpt-4o \
  --mode test \
  --n_samples 10 \
  --temperature 0.4
```

### Evaluate Results

```bash
pixi run python baxbench/main.py \
  --models gpt-4o \
  --mode evaluate \
  --n_samples 10 \
  --temperature 0.4
```

### Run Type Checking

```bash
pixi run mypy
# or
pixi run bash scripts/run_mypy.sh
```

### Set Up Pre-commit Hooks

```bash
pixi run pre-commit install
pixi run pre-commit run --all-files
```

## Troubleshooting

### Check Python Version

```bash
pixi run python --version
# Should show: Python 3.12.x
```

### Verify Dependencies

```bash
pixi run python -c "import requests, openai, docker, tabulate; print('OK')"
```

### Check Package Installation

```bash
pixi run pip list | grep baxbench
```

### Clean Install

```bash
rm -rf .pixi pixi.lock
pixi install
```

### View Environment Location

```bash
pixi info
# Look for "Environments:" section
```

## File Locations

- **Configuration**: `pyproject.toml`
- **Lock file**: `pixi.lock` (auto-generated, commit to git)
- **Environment**: `.pixi/` (don't commit, in .gitignore)
- **Source code**: `baxbench/`
- **Results**: `results/` (created when running)

## Environment Variables

Set these before running generation:

```bash
export OPENAI_API_KEY="your_key_here"
export TOGETHER_API_KEY="your_key_here"
export ANTHROPIC_API_KEY="your_key_here"
export OPENROUTER_API_KEY="your_key_here"
```

Or add to `~/.bashrc` or `~/.zshrc` for persistence.

## Documentation

- [Full Pixi Guide](./PIXI_GUIDE.md)
- [Importing from Other Projects](./IMPORTING_FROM_OTHER_PROJECTS.md)
- [Main README](./README.md)
- [Pixi Official Docs](https://pixi.sh/latest/)

