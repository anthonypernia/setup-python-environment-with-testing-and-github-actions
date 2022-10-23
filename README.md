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
    <li>The first example is when some test fails, in one case the Hook solves the problem and you only need to add the files that were modified, in the other case, you need to solve the code issue</li>
    <img src="https://raw.githubusercontent.com/anthonypernia/pre-commit-setup-for-python-with-github-action/develop/assets/pre-commit-fail.png"></img>
    <li>The second example is when the code passes all tests and is ready to be uploaded to the remote repository.</li>
    <img src="https://raw.githubusercontent.com/anthonypernia/pre-commit-setup-for-python-with-github-action/develop/assets/pre-commit-ok.png"></img>
    </ul>
    <br>
    <p>The files that we are using:</p>
        <h3>Pre-commit file: <code>.pre-commit-config.yaml</code> <a href="https://github.com/anthonypernia/pre-commit-setup-for-python-with-github-action/blob/main/.pre-commit-config.yaml">Link</a></h3>
        <p>You can see the file <a href="https://github.com/anthonypernia/pre-commit-setup-for-python-with-github-action/blob/main/.pre-commit-config.yaml">Here</a></p>
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
    - name: Coverage
      run: |
        coverage run -m pytest
        coverage report -m
        coverage xml
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v2
      with:
        token: ${{ secrets.CODECOV_TOKEN }}
        files: ./coverage.xml
        flags: unittests
        name: codecov-umbrella
        fail_ci_if_error: true
    </code></pre>
    <br>
    <h3>Also, in folder "actions-to-use" are other templates to use, for example:</h3>
    <p><a href="https://github.com/anthonypernia/pre-commit-setup-for-python-with-github-action/tree/main/action-to-use">Link to actions-to-use folder</a></p>
    <ul>
    <li><p><a href="https://github.com/anthonypernia/pre-commit-setup-for-python-with-github-action/blob/main/action-to-use/pre-commit-and-merge.yml">pre-commit-and-merge.yml</a>, if you want to approve all the PRs that pass the pre-commit hooks</p></li>
    <li><p><a href="https://github.com/anthonypernia/pre-commit-setup-for-python-with-github-action/blob/main/action-to-use/pre-commit-on-pr.yml">pre-commit-on-pr.yml</a>, if you want to run pre-commit hooks only on PR to Main branch</p></li>
    <li><p><a href="https://github.com/anthonypernia/pre-commit-setup-for-python-with-github-action/blob/main/action-to-use/pre-commit-on-push-and-pr.yml">pre-commit-on-push-and-pr.yml</a>, if you want to run pre-commit hooks on PR to Main branch and Push to Develop branch</p></li>
    <li><p><a href="https://github.com/anthonypernia/pre-commit-setup-for-python-with-github-action/blob/main/action-to-use/pre-commit-and-pytest.yml">pre-commit-and-pytest.yml.yml</a>, if you want to run pre-commit hooks on PR to Main branch and Push to Develop branch, but also run Pytest</p></li>
    <li><p><a href="https://github.com/anthonypernia/pre-commit-setup-for-python-with-github-action/blob/main/action-to-use/pre-commit-pytest-coverage-codecov.yml">pre-commit-pytest-coverage-codecov.yml</a>, if you want to run pre-commit hooks on PR to Main branch,Push to Develop branch, and analyze the coverage using the pytest and coverage libraries usin <a href="https://app.codecov.io/gh">Codecov</a></p></li>
    </ul>
    <h3>Best Option: pre-commit-pytest-coverage-codecov</h3>
    <p>The one that I consider the best is the last one, since it checks the coverage, does the tests with pytest, and executes the pre-commit so that you can see the coverage graphs in the PR</p>
    <p>You need to create an account in <a href="https://app.codecov.io/gh">Codecov</a>, give it permission to scan repositories, get the codecov token , and store in secrets as CODECOV_TOKEN</p>
    <p>The process flow would be, for example, in PR you can see if the pre-commit was executed without errors</p>
    <img src="https://raw.githubusercontent.com/anthonypernia/pre-commit-setup-for-python-with-github-action/develop/assets/pre-commit-fail-github.png"></img>
    <p>When the problem is solved, when pushing again the tests will be updated. After that, the tests will be executed, then you can see the coverage result, and coverage graphs</p>
    <img src="https://raw.githubusercontent.com/anthonypernia/pre-commit-setup-for-python-with-github-action/develop/assets/bad-pr.png"></img>
    <img src="https://raw.githubusercontent.com/anthonypernia/pre-commit-setup-for-python-with-github-action/develop/assets/coverage-bad.png"></img>
    <p>After solving all the errors, you can see all the tests that were approved</p>
    <img src="https://raw.githubusercontent.com/anthonypernia/pre-commit-setup-for-python-with-github-action/develop/assets/pr-ok.png"></img>
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
    <p>Information about Pytest:</p>
    <p><a href="https://docs.pytest.org/en/6.2.x/customize.html">https://docs.pytest.org/en/6.2.x/customize.html</a></p>
    <p>Codecov Documentation:</p>
    <p><a href="https://docs.codecov.com/docs">https://docs.codecov.com/docs</a></p>
</div>
