# python-for-fun

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)

An simple testing project that tested in vscode.

<br>

## Pre-requisites
- python 3.11+
- pylint 2.4.4+
- pydantic 1.9.0+
- pytest 6.2.5+
- pytest-cov 3.0.0+
- pytest-vscodedebug 0.1.0+
- coverage 6.3.2+
- mypy 0.931+
- pre-commit 2.17.0+

## pyenv
```sh
sudo apt install -y gcc make build-essential libssl-dev libffi-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev liblzma-dev

curl https://pyenv.run | bash
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

pyenv install 3.11.9
pyenv versions
```

## pipenv
```sh
pyenv local 3.11.9
pip install --user pipenv
pipenv --version
# ppipenv, version 2022.5.2

export PIPENV_CUSTOM_VENV_NAME=.venv
export PIPENV_VENV_IN_PROJECT=1
pipenv install --dev --python 3.11.9

export APP_ENV=Development
pipenv run tests
```


## virtualenv
```sh
# create venv (for the 1st time)
python3 -m venv .venv

# activate venv
source .venv/bin/activate
#or source .venv/Scripts/activate

# inside the venv
# (.venv)
# TODO: your stuff

# deactivate from venv
deactivate

# delete venv if would like to cleanup
# rm -r .venv
```

## Hello World!
```sh
# inside the venv
# (.venv)

python --version

# System Requirements and Installation
pip install -r requirements.txt
pip install -e .

# Start to run program with Development configuration
APP_ENV=Development python app_package/main.py
# Example result:
# Salary Report (Empty)
# ===
# (1) Top Managers:
#     Jeff
#
# (2) Divisions:
#
#     Employees of: Jeff
#         ∟Dave
#     Salary above: 100000
#
#         Employees of: Dave
#             ∟Andy
#             ∟Dan
#             ∟Jason
#             ∟Rick
#             ∟Suzanne
#         Salary above: 380000
# ===
# Total Salary: 480000
```

## Code Quality
---

### Type check
```sh
# inside the venv
# (.venv)

# install mypy (for the 1st time)
pip install mypy

# check app_package/**/*.py
mypy app_package/

# check tests/**/*.py
mypy tests/
```

### pytest
```sh
# inside the venv
# (.venv)

# install pytest (for the 1st time)
# pip uninstall pytest
pip install 'pytest<8.0.0'
pip install pytest-cov
pytest --version
# pytest 6.2.5

# System Requirements and Installation
pip install -r requirements.txt
pip install -e .

# Start to run test with `Development` configuration
export APP_ENV=Development
pytest tests/

# Code coverage with report
coverage report -m

# deactivate from venv
deactivate

# delete venv if needed
# rm -r .venv
```
Output:
```
====================================== test session starts =======================================
platform linux -- Python 3.11.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
benchmark: 3.4.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: {workspaceFolder}, configfile: pytest.ini
plugins: benchmark-3.4.1, cov-3.0.0, vscodedebug-0.1.0
collected 10 items

tests/test_config.py::test_postive PASSED                                                  [ 10%]
tests/test_config.py::test_negative PASSED                                                 [ 20%]
tests/test_exam.py::test_vowel_postive PASSED                                              [ 30%]
tests/test_exam.py::test_vowel_corner PASSED                                               [ 40%]
tests/test_exam.py::test_palindrome_postive SKIPPED (just testing skip)                    [ 50%]
tests/test_exam.py::test_palindrome_negative SKIPPED (just testing skip)                   [ 60%]
tests/test_exam.py::test_palindrome_corner PASSED                                          [ 70%]
tests/test_salary_report.py::test_postive_byfile PASSED                                    [ 80%]
tests/test_salary_report.py::test_postive_bylist PASSED                                    [ 90%]
tests/test_salary_report_benchmark.py::test_perf SKIPPED (just testing skip)               [100%]

==================================== short test summary info =====================================
SKIPPED [1] tests/test_exam.py:34: just testing skip
SKIPPED [1] tests/test_exam.py:46: just testing skip
SKIPPED [1] tests/test_salary_report_benchmark.py:6: just testing skip
================================== 7 passed, 3 skipped in 9.69s ==================================
```

Available unit tests. See:
- [test_config.py](./tests/test_config.py) - detect runtime env from environment variable
- [test_salary_report.py](./tests/test_salary_report.py) - calculate salary and generate a report
- [test_exam.py](./tests/test_exam.py) - code challenges

### Pylint
```py
# inside the venv
# (.venv)

# install pylint (for the 1st time)
pip install pylint

pylint --version
#pylint 2.12.2
#astroid 2.9.3
#Python 3.11.9 (default, Nov 26 2021, 20:14:08)
#[GCC 9.3.0]

pylint -j 4 *.py
#--------------------------------------------------------------------
#Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## Debug in VS Code
### Pre-requisites
- pytest 6.2.5+
- pytest-cov 3.0.0+
- pytest-vscodedebug 0.1.0+
- [Python Test Explorer for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter)

### Configuration .vscode/launch.json
```
{
  "configurations": [
    {
      "name": "Python: Remote Attach",
      "type": "python",
      "request": "attach",
      "connect": {
        "host": "localhost",
        "port": 10001,
      },
      "pathMappings": [
        {
          "localRoot": "${workspaceFolder}",
          "remoteRoot": "."
        }
      ]
    }
  ]
}
```

### Launch vscodedebug
```sh
# inside the venv
# (.venv)

# install pytest-vscodedebug (for the 1st time)
pip install pytest-vscodedebug

export APP_ENV=Development
py.test --vscodedebug tests/test_exam.py
```
Output:
```
====================================== test session starts =======================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
benchmark: 3.4.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: {workspaceFolder}, configfile: pytest.ini
plugins: benchmark-3.4.1, cov-3.0.0, vscodedebug-0.1.0
collected 5 items
⏳ VS Code debugger can now be attached on port 10001
```
Then start `Debug from TEST EXPLORER`
```
...
⚙️ VS Code debugger attached
...
```

## pre-commit
### Pre-requisites
- pre-commit 2.17.0+
- config file `.pre-commit-config.yaml`

### Manually run
```sh
# inside the venv
# (.venv)

# install pre-commit (for the 1st time)
pip install pre-commit

pre-commit --version
#pre-commit 2.19.0

pre-commit install
#pre-commit installed at .git/hooks/pre-commit

pre-commit run --all-files
```
Output
```
[INFO] Initializing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Initializing environment for https://github.com/psf/black.
[INFO] Installing environment for https://github.com/pre-commit/pre-commit-hooks.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
[INFO] Installing environment for https://github.com/psf/black.
[INFO] Once installed this environment will be reused.
[INFO] This may take a few minutes...
Check Yaml...........................................(no files to check)Skipped
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Passed
```

### Auto run while git committing
```
git commit -m "test: pre-commit"
Check Yaml...............................................................Passed
Fix End of Files.........................................................Passed
Trim Trailing Whitespace.................................................Passed
[main 031ec02] test: pre-commit
 10 files changed, 70 insertions(+), 29 deletions(-)
 create mode 100644 .pre-commit-config.yaml
 ```

## References
- [pip_install](https://pip.pypa.io/en/stable/getting-started/)
- [venv_install](https://docs.python.org/3/library/venv.html)
- [mypy_install](https://mypy.readthedocs.io/en/stable/getting_started.html)
- [pytest-vscodedebug](https://pypi.org/project/pytest-vscodedebug/)
- [pytest-Basic patterns and examples](https://docs.pytest.org/en/latest/example/simple.html)
- [Python testing in Visual Studio Code](https://code.visualstudio.com/docs/python/testing)

<br>
<br>

---

**Enjoy this python_for_fun project!**

---
