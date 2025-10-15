<div align="center">
    <h1><img height="150px" src="./static/baxbench_icon.png" alt="BaxBench"><br>BaxBench</h1>

  <a href="https://www.python.org/">
<img alt="Build" src="https://img.shields.io/badge/Python-3.12-1f425f.svg?color=blue">
  </a>
  <a href="https://opensource.org/licenses/MIT">
<img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg">
  </a>

</div>

## [13.09.2025] Release v1.0.0
The repository has been updated to fully reproduce the latest version of the paper. If you are using BaxBench for your work, please consider rebasing to this latest version. The changes involve minor fixes in scenario tests and exploits, and migrating the environments to Debian Bullseye. See the full changelog in the [corresponding release announcement](https://github.com/logic-star-ai/baxbench/releases/tag/v1.0.0)

## 👋 Overview

BaxBench is a coding benchmark for evaluating the ability of LLMs on generating correct and secure code in realistic, security-critical settings.
Each coding task in BaxBench consists of a *scenario*, describing the API the backend application should implement, and a *framework*, fixing the implementation language and backend framework to use.
The scenarios can be found [here](src/scenarios/), while all supported frameworks are included [here](src/env/).

> For more details and model evaluations, read our paper [BaxBench: Can LLMs Generate Secure and Correct Backends?](https://arxiv.org/abs/2502.11844) or visit our [website](https://baxbench.com).

### Assets

- 📜 Paper: [BaxBench: Can LLMs Generate Secure and Correct Backends?](https://arxiv.org/abs/2502.11844)
- 🏆 Website & Leaderboard: [baxbench.com](https://baxbench.com)
- 🤗 Dataset: [datasets/LogicStar/BaxBench](https://huggingface.co/datasets/LogicStar/BaxBench)

## 🚀 Installation

**Prerequisites:**

> `docker`: Follow the instructions for installing Docker Desktop [here](https://docs.docker.com/desktop/) (Windows, MacOS, Linux) or for the Docker engine [here](https://docs.docker.com/engine/install/) (Linux). Make sure that Docker has root privileges on your machine.

### Option 1: Using Pixi (Recommended)

> `pixi`: Install pixi by following the instructions [here](https://pixi.sh/latest/#installation).

**Setting up the environment and running scripts**

After installing pixi, you can install the environment by running:
```bash
pixi install
```

To run any Python script in the project environment, use:
```bash
pixi run python <path_to_python_script> <args>
```

Or use the provided tasks:
```bash
pixi run generate  # Generate solutions
pixi run test      # Test generated solutions
pixi run evaluate  # Evaluate and print results
pixi run mypy      # Run mypy type checking
```

You can also import baxbench as a package:
```python
from baxbench.scenarios import all_scenarios
from baxbench.env import all_envs
```

### Option 2: Using Pipenv

> `python 3.12`: Install it from [here](https://www.python.org/downloads/).<br>
> `pipenv`: Install pipenv by following the instructions [here](https://pipenv.pypa.io/en/latest/).

**Setting up the environment and running scripts**

After ensuring that all prerequisites are installed, you can install the environment by running `pipenv install` from the root of the repository. Please ensure that this action does not change `Pipfile.lock`. To run any Python script in the project environment, run from the project root using the command:
```bash
pipenv run python <path_to_python_script> <args>
```

**Setting API keys**

To generate BaxBench task solutions, the current repository requires the user to set the following environment variables to API keys stored in environment variables in your `.bashrc` or the equivalent configuration file of your system:

```bash
export OPENAI_API_KEY="<your_API_key>"
export TOGETHER_API_KEY="<your_API_key>"
export ANTHROPIC_API_KEY="<your_API_key>"
export OPENROUTER_API_KEY="<your_API_key>"
```

> **Note:** You may set any API key you do not intend to use simply to an empty or invalid string.

## 🔗 Using BaxBench from Another Project

If you want to use BaxBench as a dependency in another pixi project, see the [guide on importing from other projects](./IMPORTING_FROM_OTHER_PROJECTS.md).

Quick example - add this to your project's `pyproject.toml`:

```toml
[tool.pixi.pypi-dependencies]
baxbench = { path = "/path/to/baxbench", editable = true }
```

Then import and use:

```python
from baxbench.scenarios import all_scenarios
from baxbench.env import all_envs
```

## 💫 Contributing

We welcome contributions from the community. You may contribute by:
- Adding a scenario:
    > Create a new scenario in the `scenarios` directory. Look at other scenarios as an example for what has to be there for completeness.<br>
    > Add the scenario to the `scenarios` list in `src/scenarios/__init__.py`.<br>
    > Open a pull request to integrate your scenario into the main branch. <br>
- Adding a new framework:
    > Create a new scenario in the `env` directory. Look at other environments as an example for what has to be there for completeness.<br>
    > Add the scenario to the `envs` list in `src/env/__init__.py`.<br>
    > Open a pull request to integrate your scenario into the main branch. <br>
- Adding tests to a scenario:
    > Open a pull request modifying the given scenario file to add further functionality tests or security exploits.
- Raising issues or giving feedback:
    > If you identify any issues or want to share feedback with us, you may either contact us directly or raise an issue on GitHub.
We are looking forward to working with the community and are extremely thankful for any contributions!

> **Note:** Before contributing code, please run `pixi run pre-commit install` (or `pipenv run pre-commit install` if using pipenv) in the root once to set up the pre-commit hooks.

## 👨🏻‍💻 Usage

#### Generating programs

To generate solutions to _all_ scenarios in the `scenarios` list, run the following command:

```bash
# Using pixi
pixi run python baxbench/main.py --models gpt-4o --mode generate --n_samples 10 --temperature 0.4

# Or using pipenv
pipenv run python baxbench/main.py --models gpt-4o --mode generate --n_samples 10 --temperature 0.4
```

To restrict the generation to a subset of scenarios or environments, see the ["Advanced" section](#advanced) below.

The programs and the generation logs will be saved in the directory `results`.

#### Testing generated programs

```bash
# Using pixi
pixi run python baxbench/main.py --models gpt-4o --mode test --n_samples 10 --temperature 0.4

# Or using pipenv
pipenv run python baxbench/main.py --models gpt-4o --mode test --n_samples 10 --temperature 0.4
```

If you have generated solutions externally, e.g., using our [Hugging Face dataset](https://huggingface.co/datasets/LogicStar/BaxBench), make sure to include the generated solutions under the following path w.r.t. the root of this repository:

`results/<model_name>/<scenario_id>/<env_id>/temp<t>-<spec_type>-<prompt_type>/sample<s>/code`

Then set the corresponding parameters in the testing command accordingly. See ["Advanced"](#advanced) below or the argument list in [main.py](src/main.py).

#### Evaluating and printing

```bash
# Using pixi
pixi run python baxbench/main.py --models gpt-4o --mode evaluate --n_samples 10 --temperature 0.4

# Or using pipenv
pipenv run python baxbench/main.py --models gpt-4o --mode evaluate --n_samples 10 --temperature 0.4
```

#### Advanced

Specific models/scenarios/frameworks/samples can be generated, tested, or evaluated by specifying the following arguments in the CLI:

```
--models
--scenarios
--envs
--only_samples
--safety_prompt
--spec_type
```

Each of these arguments takes values separated by spaces.

## ✍️ Citation
If you find our work helpful, please use the following citation.
```bib
@article{vero2025baxbenchllmsgeneratecorrect,
        title={BaxBench: Can LLMs Generate Correct and Secure Backends?}, 
        author={Mark Vero and Niels Mündler and Victor Chibotaru and Veselin Raychev and Maximilian Baader and Nikola Jovanović and Jingxuan He and Martin Vechev},
        year={2025},
        eprint={2502.11844},
        archivePrefix={arXiv},
}
```

## 📝 License
MIT. Check `LICENSE`.
