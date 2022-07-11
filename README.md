<div>
    <h1>
        Github action with pre-commit for python
    </h1>
    <p>This repository was created from some blogs and documents, which I will leave below.</p>
    <br>
    <h3>Github action <code>.github/workflows/pre-commit-check.yml</code></h3>
    <pre><code>
name: pre-commit
on:
  pull_request:
  push:
    branches: [main]
jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v3
    - name: Install pre-commit
      run: |
        pip install pre-commit
    - name: Install requirements
      run: |
        pip install -r requirements.txt
    - uses: pre-commit/action@v3.0.0
    </code></pre>
    <h3>Pre-commit file: <code>.pre-commit-config.yaml</code></h3>
    <pre><code>
fail_fast: false
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
        - id: debug-statements #Check for debugger imports and breakpoint() calls in python files
        - id: check-ast #Simply check whether files parse as valid python
        - id: fix-byte-order-marker #removes UTF-8 byte order marker
        - id: check-json
        - id: detect-aws-credentials # detect-aws-credentials is not in repo
        - id: detect-private-key # detect-private-key is not in repo
        - id: check-yaml
        - id: check-added-large-files
        - id: check-shebang-scripts-are-executable
        - id: check-case-conflict #Check for files with names that would conflict on    case-insensitive filesystem like MacOS HFS+ or Windows FAT
        - id: end-of-file-fixer #Makes sure files end in a newline and only a newline
        - id: trailing-whitespace
        - id: mixed-line-ending
  - repo: local
    hooks:
        - id: black # black is a pre-commit hook that runs to check for format issues
          name: black
          entry: black
          language: system
          types: [python]
  - repo: https://github.com/asottile/blacken-docs
    rev: v1.12.1
    hooks:
    -   id: blacken-docs #blacken-docs is a pre-commit hook that runs to check for issues ithe docs
        additional_dependencies: [black]
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
        - id: isort #isort is a pre-commit hook that runs to check for issues in imports and docstrings
          args: ["--profile", "black", "--filter-files"]
  - repo: local
    hooks:
        - id: pylint # pylint is a pre-commit hook that runs as a linter to check for style
          name: pylint
          entry: pylint
          language: system
          types: [python]
          exclude: ^venv/ ^.git/ ^.vscode/ ^.DS_Store
  - repo: local
    hooks:
        - id: mypy # mypy is a pre-commit hook that runs as a linter to check for type errors
          name: mypy
          entry: mypy
          language: system
          types: [python]
          exclude: ^venv/ ^.git/ ^.vscode/ ^.DS_Store
  - repo: https://github.com/asottile/pyupgrade
    rev: v2.37.0
    hooks:
        - id: pyupgrade #pyupgrade is a pre-commit hook that runs to check for issues in th  codebase
          args: [--py36-plus]
    </code></pre>
    <br>
    The documentation that I used to create this repository is:
    <p><a href="https://pre-commit.com/#install">https://pre-commit.com/#install</a></p>
    <p><a href="https://pre-commit.com/#usage">https://pre-commit.com/#usage</a></p>
    <p><a href="https://composed.blog/python/pre-commit">https://composed.blog/python/pre-commit</a></p>
    <p><a
            href="https://towardsdatascience.com/pre-commit-hooks-you-must-know-ff247f5feb7e">https://towardsdatascience.com/pre-commit-hooks-you-must-know-ff247f5feb7e</a>
    </p>
    <p><a
            href="https://verdantfox.com/blog/view/how-to-use-git-pre-commit-hooks-the-hard-way-and-the-easy-way">https://verdantfox.com/blog/view/how-to-use-git-pre-commit-hooks-the-hard-way-and-the-easy-way</a>
    </p>
    <p>Some hooks examples:</p>
    <p><a href="https://github.com/pre-commit/pre-commit-hooks">https://github.com/pre-commit/pre-commit-hooks</a></p>
</div>
