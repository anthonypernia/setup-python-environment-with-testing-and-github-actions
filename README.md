<div>
    <h1>
        Setup Python environment with pre-commit, pytest and github actions
    </h1>
    <p>This repository was created from some blogs and documents, which I will leave below.</p>
    <p>Works in python and PySpark.</p>
    <br>
    <h3>How to use:</h3>
    <p>You can clone the repo <a target="_blank" href="https://github.com/anthonypernia/pre-commit-python-action-example.git">https://github.com/anthonypernia/pre-commit-python-action-example.git</a> or just download the files that you need and use in your repo.</p>
    <p>Install the necessary libraries:</p>
    <ul>
      <li>pre-commit</li>
      <li>mypy</li>
      <li>black</li>
      <li>pytest</li>
      <li>isort</li>
      <li>pylint</li>
      <li>coverage</li>
    </ul>
    <p>Or just install the requirements.txt that is in this repo using: <code>pip install -r requirements.txt </code></p>
    <h2>Pre-commit</h2>
    <p>Pre-commit is a tool that we use to identify issues in our code, such as type errors, syntax errors, functions without documentation, etc  </p>
    <p>To learn more about Pre-commit you can check the <a target="_blank" href="https://pre-commit.com/#intro">Documentation</a> </p>
    <p>To execute <code>pre-commit</code> use the following command:</p>
    <pre><code>pre-commit run --all-files</code></pre>
    <p>And then, the library starts checking the code with all the hooks that we are using in the <code>pre-commit-config</code> file. The first time it will take about 2 minutes </p>
    <p>You could receive three messages in the pipeline:</p>
    <ul>
    <li>Passed - When everything is fine, and I pass the test </li>
    <li>Failed - When the test failed</li>
    <li>Skipped - When a test is skipped or does not apply to the file</li>
    </ul>
    <p>The good news is that most hooks do the necessary modifications to improve the code automatically so you just had to add the file again with <code>git add FILE_TO_ADD.py</code> and run again <code>pre-commit run --all-files</code></p>
    <h3>Here are two running examples</h3>
    <ul>
    <li>The first example is when some test fails, in one case the Hook solves the problem and you only need to add the files that were modified, in the other case, you need to solve the code issue</li>
    <img src="https://raw.githubusercontent.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/main/assets/pre-commit-fail.png"></img>
    <li>The second example is when the code passes all tests and is ready to be uploaded to the remote repository.</li>
    <img src="https://raw.githubusercontent.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/main/assets/pre-commit-ok.png"></img>
    </ul>
    <p>However, the main function of pre-commit is to be called automatically before the commit. You can do it with:  <pre><code>pre-commit install</code></pre></p>
    <p>You will receive a message like this: <pre><code>pre-commit installed at .git/hooks/pre-commit</code></pre></p></p>
    <p>Then, every time you do a commit, the pre-commit will be executed</p>
    <img src="https://raw.githubusercontent.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/main/assets/commit-example.png"></img>
    <p>In case it passes all the tests, the commit will be executed, otherwise it will not</p>
    <p>You can copy my pre-commit configuration:</p>
    <p>Pre-commit file: <code>.pre-commit-config.yaml</code> <a target="_blank" href="https://github.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/blob/main/.pre-commit-config.yaml">Link</a></p>
    <h2>Github Action using Pre-Commit, PyTest and Coverage</h2>
    <p>Github actions is the way that we have to apply CICD or run customized workflows</p>
    <p>You can take a look at the <a target="_blank" href="https://docs.github.com/en/actions">Documentation</a></p>
    <p>The funniest thing is that pre-commit can be added to a workflow as an automated task, we can add unit testing, check the coverage, etc. All this task can be executed after push our code or create a pull request.</p>
    <h4>There are some examples with customized workflows:</h4>
    <ul>
    <li><p><a target="_blank" href="https://github.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/blob/main/action-to-use/pre-commit-and-merge.yml">pre-commit-and-merge.yml</a>, This workflow will merge all the push that pass the pre-commit tests, from the develop branch, into the master branch</p></li>
    <li><p><a target="_blank" href="https://github.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/blob/main/action-to-use/pre-commit-on-pr.yml">pre-commit-on-pr.yml</a>, This workflow will execute pre-commit on all pull requests to main branch and will show the result in the PR</p></li>
    <li><p><a target="_blank" href="https://github.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/blob/main/action-to-use/pre-commit-on-push-and-pr.yml">pre-commit-on-push-and-pr.yml</a>, Same as before , but in this case it will execute test on PR to main branch and all push to develop
    </p></li>
    <li><p><a target="_blank" href="https://github.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/blob/main/action-to-use/pre-commit-and-pytest.yml">pre-commit-and-pytest.yml.yml</a>, In this case, in addition to running the pre-commit tests, this workflow will run the pytest suite.</p></li>
    <li><p><a target="_blank" href="https://github.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/blob/main/action-to-use/pre-commit-pytest-coverage-codecov.yml">pre-commit-pytest-coverage-codecov.yml</a>, This workflow is the most complete. it will execute the following actions:
    <ul>
    <li>run pre-commit test</li>
    <li>run pytest suite</li>
    <li>check the coverage and upload to Codecov</li>
    <li>it will fail if coverage is not ok</li>
    </ul>
    You can find more info in <a target="_blank" href="https://app.codecov.io/gh">Codecov</a></p></li>
    </ul>
    <h3>Best Option: pre-commit-pytest-coverage-codecov</h3>
    <p>The one that I consider the best is the last one because it checks the coverage, execute the pytest suite, and executes the pre-commit so that  at the end you can see the coverage graphs in the PR</p>
    <p>You need to create an account in <a target="_blank" href="https://app.codecov.io/gh">Codecov</a>, give it permission to scan repositories, get the codecov token , and store in secrets as CODECOV_TOKEN</p>
    <p>If you want to configure coverage to approve, you need to create a file called <code>codecov.yml</code></p>
    <p>You can check the file that I use <a target="_blank" href="https://github.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/blob/main/codecov.yml" >Here</a></p>
    <p>Here is an example of a PR using that workflow, in that case, we have some errors in pre-commit and we need to solve it</p>
    <img src="https://raw.githubusercontent.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/main/assets/pre-commit-fail-github.png"></img>
    <p>When the problem is solved, when you push your code again, the tests will be updated, in that case, we need to update the test to complete the coverage</p>
    <img src="https://raw.githubusercontent.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/main/assets/bad-pr.png"></img>
    <img src="https://raw.githubusercontent.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/main/assets/coverage-bad.png"></img>
    <p>After solving all the errors, you can see all the tests that were approved</p>
    <img src="https://raw.githubusercontent.com/anthonypernia/setup-python-environment-with-testing-and-github-actions/main/assets/pr-ok.png"></img>
    <br>
    The documentation that I used to create this repository is:
    <p><a target="_blank" href="https://pre-commit.com/#install">https://pre-commit.com/#install</a></p>
    <p><a target="_blank" href="https://pre-commit.com/#usage">https://pre-commit.com/#usage</a></p>
    <p><a target="_blank" href="https://composed.blog/python/pre-commit">https://composed.blog/python/pre-commit</a></p>
    <p><a
            target="_blank" href="https://towardsdatascience.com/pre-commit-hooks-you-must-know-ff247f5feb7e">https://towardsdatascience.com/pre-commit-hooks-you-must-know-ff247f5feb7e</a>
    </p>
    <p><a
            target="_blank" href="https://verdantfox.com/blog/view/how-to-use-git-pre-commit-hooks-the-hard-way-and-the-easy-way">https://verdantfox.com/blog/view/how-to-use-git-pre-commit-hooks-the-hard-way-and-the-easy-way</a>
    </p>
    <p>Some hooks examples:</p>
    <p><a target="_blank" href="https://github.com/pre-commit/pre-commit-hooks">https://github.com/pre-commit/pre-commit-hooks</a></p>
    <p>Information about Pytest:</p>
    <p><a target="_blank" href="https://docs.pytest.org/en/6.2.x/customize.html">https://docs.pytest.org/en/6.2.x/customize.html</a></p>
    <p>Codecov Documentation:</p>
    <p><a target="_blank" href="https://docs.codecov.com/docs">https://docs.codecov.com/docs</a></p>
</div>
