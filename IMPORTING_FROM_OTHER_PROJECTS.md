# Using BaxBench from Another Pixi Project

This guide explains how to import and use BaxBench from another pixi project.

## Method 1: Install as a Local Editable Package (Recommended)

This is the best approach for development where you want changes in BaxBench to be immediately reflected in your other project.

### Step 1: Add BaxBench to your project's `pyproject.toml`

In your other pixi project's `pyproject.toml`, add:

```toml
[tool.pixi.pypi-dependencies]
baxbench = { path = "/worxpace/seclm_grpo/baxbench", editable = true }
```

Or use a relative path if your projects are in related directories:

```toml
[tool.pixi.pypi-dependencies]
baxbench = { path = "../baxbench", editable = true }
```

### Step 2: Install dependencies

```bash
cd /path/to/your/project
pixi install
```

### Step 3: Import and use

```python
# Import specific modules
from baxbench.scenarios import all_scenarios
from baxbench.env import all_envs
from baxbench.tasks import Task, TaskHandler

# Use them
print(f"Available scenarios: {len(all_scenarios)}")
print(f"Available environments: {len(all_envs)}")
```

## Method 2: Install from Git Repository

If BaxBench is hosted on GitHub/GitLab, you can install it directly:

```toml
[tool.pixi.pypi-dependencies]
baxbench = { git = "https://github.com/org/baxbench.git" }
```

With a specific branch or tag:

```toml
[tool.pixi.pypi-dependencies]
baxbench = { git = "https://github.com/org/baxbench.git", branch = "main" }
# or
baxbench = { git = "https://github.com/org/baxbench.git", tag = "v1.0.0" }
```

## Method 3: Manual PYTHONPATH Configuration

If you need quick access without installing, you can manually add the path:

### Option A: Using environment variables

In your project's `.env` file or shell:

```bash
export PYTHONPATH="/worxpace/seclm_grpo/baxbench:$PYTHONPATH"
```

### Option B: In Python code

```python
import sys
sys.path.insert(0, '/worxpace/seclm_grpo/baxbench')

# Now you can import
from baxbench.scenarios import all_scenarios
from baxbench.env import all_envs
```

### Option C: Using pixi tasks

Add a task to your project's `pyproject.toml`:

```toml
[tool.pixi.tasks]
run-with-baxbench = { cmd = "python your_script.py", env = { PYTHONPATH = "/worxpace/seclm_grpo/baxbench" } }
```

## Example: Complete Setup

Here's a complete example of a `pyproject.toml` for a project that uses BaxBench:

```toml
[project]
name = "my-baxbench-analysis"
version = "0.1.0"
description = "Analysis tools for BaxBench"
requires-python = ">=3.12"

dependencies = [
    "pandas",
    "numpy",
]

[tool.pixi.project]
channels = ["conda-forge"]
platforms = ["linux-64", "osx-64", "osx-arm64"]

[tool.pixi.dependencies]
python = "3.12.*"

[tool.pixi.pypi-dependencies]
my-baxbench-analysis = { path = ".", editable = true }
baxbench = { path = "../baxbench", editable = true }

[tool.pixi.tasks]
analyze = "python src/analyze.py"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

## Example Usage Script

Create a file `analyze_results.py`:

```python
#!/usr/bin/env python3
"""Example script that uses BaxBench from another project."""

from baxbench.scenarios import all_scenarios
from baxbench.env import all_envs
from baxbench.tasks import Task

def main():
    print(f"BaxBench has {len(all_scenarios)} scenarios")
    print(f"BaxBench has {len(all_envs)} environments")
    
    # List all scenario IDs
    print("\\nAvailable scenarios:")
    for scenario in all_scenarios:
        print(f"  - {scenario.id}: {scenario.description}")
    
    # List all environment IDs
    print("\\nAvailable environments:")
    for env in all_envs:
        print(f"  - {env.id}")

if __name__ == "__main__":
    main()
```

Run it:

```bash
pixi run python analyze_results.py
```

## Troubleshooting

### Import Error: "No module named 'baxbench'"

This happens if the package isn't installed correctly. Solutions:

1. **Ensure Python 3.12 is being used**: BaxBench requires Python 3.12+
   ```bash
   pixi run python --version  # Should show Python 3.12.x
   ```

2. **Reinstall the package**:
   ```bash
   pixi install --force
   ```

3. **Check if baxbench is installed**:
   ```bash
   pixi run pip list | grep baxbench
   ```

### Import Error: Module imports failing

Always import from the `baxbench` package namespace:

```python
# ✅ Correct
from baxbench.scenarios import all_scenarios
from baxbench.env import all_envs

# ❌ Wrong
from scenarios import all_scenarios  # Won't work
from src.scenarios import all_scenarios  # Old naming, won't work
```

### Path Issues

If using relative paths, make sure they're correct relative to your project root:

```bash
# Check if the path resolves correctly
ls -la ../baxbench/pyproject.toml
```

### Python Version Mismatch

BaxBench requires Python 3.12. Ensure your project also uses Python 3.12:

```toml
[tool.pixi.dependencies]
python = "3.12.*"
```

## Running BaxBench Tasks from Your Project

You can also run BaxBench's main functionality from your project:

```python
import subprocess
import sys

def run_baxbench(mode="evaluate", model="gpt-4o", n_samples=10):
    """Run BaxBench from another project."""
    baxbench_path = "/worxpace/seclm_grpo/baxbench"
    
    cmd = [
        sys.executable,
        f"{baxbench_path}/baxbench/main.py",
        "--models", model,
        "--mode", mode,
        "--n_samples", str(n_samples),
        "--temperature", "0.4"
    ]
    
    subprocess.run(cmd, cwd=baxbench_path)

# Usage
run_baxbench(mode="evaluate")
```

## Best Practices

1. **Pin to a specific version** if you need stability:
   ```toml
   baxbench = { git = "https://github.com/org/baxbench.git", tag = "v1.0.0" }
   ```

2. **Use editable installs** during development:
   ```toml
   baxbench = { path = "../baxbench", editable = true }
   ```

3. **Document the dependency** in your project's README:
   ```markdown
   ## Dependencies
   
   This project depends on BaxBench. Ensure it's cloned to `../baxbench` or adjust the path in `pyproject.toml`.
   ```

4. **Keep Python versions aligned**: Both projects should use the same Python version (3.12).

## Additional Resources

- [BaxBench README](./README.md)
- [Pixi Documentation](https://pixi.sh/latest/)
- [BaxBench Pixi Guide](./PIXI_GUIDE.md)

