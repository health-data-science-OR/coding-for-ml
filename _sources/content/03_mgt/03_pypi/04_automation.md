# Automation

The manual upload steps I've outlined in the [PyPI section](./03_pypi.md) are somewhat historical.  We know that most modern projects make use of version control in the cloud such as GitLab or GitHub.  These tools include ways to automatically publish updates to PyPI.  

## GitHub Actions

One option to automate publication of updates to a PyPI package is a GitHub action. An action can be described as a job or a workflow that runs when certain events are triggered. For example, when code is pushed to a remote repository or when a new release is created.  To be clear 
actions aren't part of the package - they are instead a tools for continuous integration of code. They help the package managers do repetitive tasks needed for maintenance and publishing efficiently and consistently.

Actions are specified in YAML (Yet Another Markup Language). And are actually quite straightforward to read.  GitHub has a large number of templates available you can use and adapt.

You can read more about GitHub actions [here](https://docs.github.com/en/actions)

## Automating package publication to PyPI

The YAML below is an action that is used to automate the updating of a package on PyPI. It is triggered when a new **release** of the code is made on the main branch.

```yaml
name: Upload Python Package

on:
  release:
    types: [published]

permissions:
  contents: read

jobs:
  deploy:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install hatch
    - name: Build package
      run: hatch build
    - name: Publish package
      uses: pypa/gh-action-pypi-publish@27b31702a0e7fc50959f5ad993c78deac1bdfc29
      with:
        user: __token__
        password: ${{ secrets.PYPI_TOKEN }}
```

To set this up you will need to supply GitHub with the API token for your package.  Its stored securely in GitHub in what is called a **Secret**.  In the YAML above you see the final line uses `${{ secrets.PYPI_TOKEN }}`. This means I have named my secret that stores the API project token as `PYPI_TOKEN`. It is essential to create and use a package specific API token for PyPI (or TestPyPI). Do not use an account wide token.  

This action runs on a new release of the code.  A release is version of the package that follows the {major}.{minor}.{patch} (e.g. v1.1.2) naming convention we introduced when first learning how to [structure a local python package](./01_local.md). For simplicity I recommend ensuring release numbering matching the package version you have in `__init__.py`. For any package on GitHub you can see the current version on the landing page. For example, for a package I am developing called `sim-tools` you can see the current version highlighted in the screenshot below.  

![release](../../../images/release.png)

To create a new release is simple. Click on the **Releases** link highlighted above followed by **Draft new release**.  You can read more about releases [here](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
 
## Where are actions stored?

When we have added added an action to GitHub our repo looks slightly different.  We now have a new directory called `.github` that contains the YAML file describing the action. 

```
analysis-package
├── .github
│   ├── workflows
│   |   ├── publish_package.yml
├── analysis_package
│   ├── __init__.py
│   ├── model.py
│   ├── data
│   |   ├── model_data.csv
├── tests
│   ├── test_model.py
├── LICENSE
├── environment.yml
├── README.md
└── pyproject.toml
```

