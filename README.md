<div>
    <h1>
        Github action with pre-commit for python
    </h1>
    <p>This repository was created from some blogs and documents, which I will leave below.</p>
    <br>
    <h3>How to use:</h3>
    <Put>Clone the repo <code>https://github.com/anthonypernia/pre-commit-python-action-example.git</code> or just download the files and put the files in your repo</p>
    <p>Install the libraries, which are in requirements.txt <code>pip install -r requirements.txt </code></p>
    <p>To execute <code>pre-commit</code> use the following command:</p>
    <pre><code>pre-commit run --all-files</code></pre>
    <p>And then, the library starts checking the code with all the hooks that we are using in the <code>pre-commit-config</code> file</p>
    <p>you could receive three messages in the pipeline:</p>
    <ul>
    <li>Passed - When everything is fine, and I pass the test </li>
    <li>Failed - When the test failed</li>
    <li>Skipped - When a test is skipped or does not apply to the file</li>
    </ul>
    <p>The good news is that most hooks do the necessary modifications to improve the code automatically so you just had to add the file again with <code>git add FILE_TO_ADD.py</code> and run again <code>pre-commit run --all-files</code></p>
    <h4>Here are two running examples</h4>
    <ul>
    <li>The first example is when some test fails, in this case the Hook solves the problem and you only need to add the files that were modified </li>
    <img src="https://raw.githubusercontent.com/anthonypernia/pre-commit-python-action-example/main/assets/example2.png"></img>
    <li>The second example is when the code passes all tests and is ready to be uploaded to the remote repository.</li>
    <img src="https://raw.githubusercontent.com/anthonypernia/pre-commit-python-action-example/main/assets/example1.png"></img>
    </ul>
    <br>
    <p>The files that we are using:</p>
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
    <h3>The Github action to execute pre-commit as a workflow part is: <code>.github/workflows/pre-commit-check.yml</code></h3>
    <pre><code>
name: pre-commit
on:
  pull_request:
    branches: [main]
  push:
    branches: [develop]
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
    <br>
    Also, in the folder "./actions-to-use" there are two examples:
    <ul>
    <li>accept-all.yml, if we want to approve all the PRs that pass the pre-commit</li>
    <li>check-on-pr-and-push.ym and check-on-pr.yml if we want to run pre-commit on PR</li>
    </ul>
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
