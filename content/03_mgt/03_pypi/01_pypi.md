# Installable Python packages

If you want to deploy a python package professionally, sustainably, and easily to colleagues, clients or just everyone in general then a great way to do it is using a combination of GitHub, and/or the Python Package Index (PyPI) and `pip`.  In this chapter we will learn how to setup a python package so that it is ready to be installed from GitHub or PyPI and also how to use `hatch`. 

## What is pip?

A package management system for installing **local packages, packages from GitHub and python packages from the Python package index**.  Example usage:

`$ pip install numpy`

or

`$ pip install numpy==1.18.0`

I recommend exploring what packages are available on [PyPI](https://pypi.org/).  The chances are when you get stuck in data science project there will be a package on pypi to help you.  For example, if you need to solve some really complex multi-objective optimisation problems you could pip install [DEAP](https://pypi.org/project/deap/).  Obviously you need to have an up-to-date version of `pip` before you can install anything.  If you are using an Anaconda distribution or conda environment (for example, `hds_code` provided with this book) you should already have `pip` installed. If you are stuck there are some instructions [here](https://packaging.python.org/tutorials/installing-packages/)

```{admonition} Pronouncing PyPI
:class: tip, dropdown
For a long time I prounounced PyPI as "Pie Pie", but its correct prounciation is "Pie Pea Eye". This makes more sense as "Pie Pie" should be reserved for the high performance implementation of Python in [PyPy](https://pypy.org/).
```

## Why create and deploy an installable package for your own projects?

In summary, it is useful if you want to use a package in multiple projects without asking the user to manage the source code or dependencies themselves. This can, of course, be managed in various ways, but I've found that people I work with have had an easier time when the software is managed by `pip`.  For example, we haven't manually managed the source for `pandas`, `matplotlib` or `numpy` in this book.  That's far too complicated. Package managers in general including `pip`  make packages accessible to others.  That's a great thing for **open science** and health data science.

So the obvious use case for `pip` in health data science is if you want others to be able to easily install and use your software/project in their own work.  I use it a lot for educational software for students.  I like the idea that students can use course learning software after they leave a University and access updated versions of it if they want to refresh their skills.  In recent years I've also been using the package structure to make computer simulation models from my research open and reusable by others.

>  At a minimum I recommend making your package open via a cloud based version control system such as GitHub. If it is structured correctly it can be installed by `pip`.  


## The difference between packages and projects

Let's assume you are working on a data science project that aims to predict a patient's risk of a certain type of cancer given data collected in a series of GP consultations.  You have the data and now need to set up Python software environment on your computer to do the analysis and modelling. This is relatively simple - you already have Python version 3.10 installed and you decide you also need `numpy`, `pandas` and `keras`.  You `pip install` these packages and end up with versions 1.26, 2.2.2 and 2.15 respectively.   You can think of this software environment as a **reproducible software environment** for your project. This is the general process you follow for every data science project you will conduct. You'll choose a Python version (maybe the latest, maybe just the version you normally use) and install **compatible** packages. Its important because it means that if you wanted to repeat the analysis you could do so using the same version of Python and packages.

When you are developing a package you need to think differently.  Put yourself in the position of someone trying to support others conduct data science projects in Python. Firstly, you will need to be clear about what versions of Python your package will support. For example, you might want users of Python 3.8, 3.9, 3.10 and 3.11 to all be able to install and use the package. Note that the more versions of python you want to support the less likely it is you can make use of new features introduced in the updates so think carefully before you try to support all of version Python 3 as prior to version 3.6 they were very different. Secondly, you will need to declare what software dependencies your package requires (e.g. `numpy`, `pandas`, `keras`). For dependencies you need to select the minimum version that will run your code.  Over time these dependencies will release their own new versions and, for example, `numpy`  may deprecate old functions/constants that you rely on (especially on a major release e.g. `numpy>=2.0`). In these instances you could either modify your package and release your own new version or specify a maximum version of the `numpy` that is compatible (e.g. `numpy<2.0`)

```{admonition} What versions of Python should I support!?
:class: tip, dropdown
For my own packages (as of 2024) I no longer support Python prior to version 3.8. And I plan to drop support for 3.8 in the next few years. Before you use this as a hard and fast rule make sure you talk to your potential users. For example, if they have a Python 3.7 environment and that's unlikely to change you will want to support it.
```

The difference is illustrated in the Figure below. Here **your-package v1.0.0** is your analysis package. There are three projects using your package with different (supported) version of Python and dependencies. There is also a project that is currently using Python 3.6 that is not compatible with your package.

```{image} ../../imgs/package_versus_project.png
:alt: package_vs_project
:class: bg-primary mb-1
:width: 800px
:align: center
```

## Setting up a git repo

I don't want to be too prescriptive here.  It really is up to you and your collaborators how you organise your own code.  There are many suggestions online as well. The structure I am going to introduce here is a simple one I use in my own projects.  You will see variations of it online.  Here's the template repo.  We will then take a look at the elements individually.   You can view the template repository and the code it contains on [GitHub](https://github.com/health-data-science-OR/pypi-template)

```
pypi_template
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

### `environment.yml`

One thing I have learnt from the Open Source community is it is useful to include a virtual conda environment for yourself and developers who contribute to the library.  That is what is in `environment.yml`. For example the `pypi_package` template includes the following:

```yaml
name: pypi_package_dev
channels:
  - conda-forge
dependencies:
  - black
  - flake8
  - hatch
  - jupyterlab=4.2.4
  - jupyterlab-spellchecker=0.8.4
  - matplotlib=3.9.1
  - nbqa
  - numpy=2.0.1
  - pandas=2.2.2
  - pip=24.0
  - python=3.11
  - pytest=8.3.2
```

It is entirely up to you what you include in the development environment, but I find it useful to include

* An notebook type IDE like `jupyterlab` for creating notebooks that contain examples of the package in use.
* The latest update of linting tools such as `black`, `flake8` and `nbqa` 
* A build tool such as `hatch` (we will see how this works shortly)
* Testing tools such as `pytest` (we will see how hatch can be used as well).

### `pyproject.toml`

```{admonition} Where has setup.py gone?
:class: information, dropdown
In prior versions of this book I included material that built an installable python package using `setuptools` + `build` and the script `setup.py` (plus several other files!).  That approach still works and is employed by many major data science packages. However, I have found that a `hatch` + `pyproject.toml` is a cleaner and simpler solution overall.  You can still access my `setuptools` materials in the archived [version 2.0.2 of the book.](https://zenodo.org/records/10016866)
```

This is the important file for `pip` and controls the installation of your package.  TOML standards for [Tom's Obvious Minimal Language](https://toml.io/en/). In simple terms `pyproject.toml` is readable way to write down the configuration of of your package. It includes information about what software is used to build the package and all the package "meta-data" e.g. name, version, description. I've included a reusable template in the repo that can be used to edit.  Let's take a look at the full file and break it down.

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "analysis_package"
dynamic = ["version"]
description = "A short, but useful description of your package"
readme = "README.md"
license = "MIT"
requires-python = ">=3.8"
authors = [
    { name = "Thomas Monks", email = "generic@genericemail.com" },
]
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11", 
    "Programming Language :: Python :: 3.12",

]
dependencies = [
    "matplotlib>=3.1.3",
    "numpy>=1.26.1",
    "pandas>=2.0.1",
]

[project.urls]
Homepage = "https://github.com/health-data-science-OR/pypi-template"
"Bug Tracker" = "https://github.com/health-data-science-OR/pypi-template/issues"

[tool.hatch.version]
path = "analysis_package/__init__.py"

[tool.hatch.build.targets.sdist]
include = [
    "/analysis_package",
]
```

### The build system

The package management system we are going to use to for our installable python package is `hatch`. I have found `hatch` to be intuitive (with easy to remember commands!), fast and useful for building a package and testing the code in multiple Python versions. It can also optionally be used to upload your package to PyPI. I'll cover the essentials here, but there [hatch documentation](https://hatch.pypa.io/latest/) can also be consulted for more advanced use.

To specify the build system in `pyproject.toml` we use the `build-backend`.  Notice that we specify `hatchling` here and not `hatch`. The **back-end** is is the tool `hatch` will call when you ask it to perform the build - `hatchling` is the work horse so to speak.  

The package `hatch` is a **front-end** build tool. Its purpose is to provide a simple to use command line interface for common package management actions (that may use different back ends). This includes running the back-end to build the Python package (more on what the build process outputs shortly).  

If this the first time building an installable python package the difference between build front and back ends may be confusing.  The good news is that while you are learning you can just use include the TOML below in your `pyproject.toml` and `hatch` will work as expected.

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

```{admonition} Are there alternative tools available?
:class: information, dropdown
An alternative popular tool for Python package management (that has been recommended to me, but I do not have experience of using) is [Poetry](https://python-poetry.org/). Poetry does a bit more than hatch for example, it also manages and resolves dependencies for a project. But that is the tip of the iceburg. For a very clear overview of the options avilable to you you can read this [excellent blog post by Anna-Lena Popkes](https://alpopkes.com/posts/python/packaging_tools/).
```

### Managing the versioning your package

All python packages should behave in this way:

```python
>>> import analysis_package
>>> print(analysis_package.__version__)
'0.1'
```
We need an `__init__.py` file for our package to reference a version number AND we need to include a version number in the TOML file.

Rather than hard coding the version in two places, we can set the package version attribute to *dynamic* and use `hatch` to read it from the `__init__.py` file.

```toml
[project]
dynamic = ["version"]

[tool.hatch.version]
path = "analysis_package/__init__.py"
```

```{admonition} How do I hard code the version in TOML?
:class: information, dropdown
If you did want to hard code the version of your package you just need to replace the `dynamic=['version']` line with `version="0.1.0"` as shown in the snippet below. Note that this should match the version in `__init__.py`. Personally I have found that the dynamic method is preferable - it avoids me forgetting to update it in two places.   

```toml
[project]
version = "0.1.0"
```

### Including data in your package

For a data science project you may want to include some example or test data within your package. 

As an example, the package in the template repo includes a subdirectory `test_package/data` containing a single (dummy) CSV.

One thing I learnt **the hard and annoying way** is that data is not included in your python package by default!  

To make sure data is included you can take two steps:

#### Tell `setup()` that it is expecting data

There are a couple of options here.  Here's the firs:

```python
    # Tells setup to look in MANIFEST.in
    include_package_data=True,
```

The above snippet tells the `setup()` function to look in a top level file called `MANIFEST.in`.  This contains a list of files to include in the package:

```
include *.txt
recursive-include test_package/data *.csv
```

As an alternative you can use:

```python
    # use instead of MANIFEST.in
    package_data={"test_package": ["data/*.csv"]},
```

Note that the second way I've described requires you to set `include_package_data=False`

* Some extra help can be found here in the setup tools manual: https://setuptools.readthedocs.io/en/latest/userguide/datafiles.html 

### Local installation and uninstallation of your package

Now that we have a `setup.py` and have installed `setuptools` we can use them to install our package locally!  Navigate to the repo on your local machine and run the command below.

`pip install .`

**Exercise**: Test out your install by launching the python interpreter.

```python
# this should work!
import test_package
print(test_package.__version__)
```

If you have used the default package settings then you will have installed a package called `pypi-template` (version = 0.1).  To uninstall use the package name:

`pip uninstall pypi-template`

## Publishing your package on PyPI

The first thing to say is that **there is a PyPI test site!**  This is incredibly helpful.  I found that I made mistakes the first couple of times I tried to get this to work e.g. no data was included in my package.  Once it is published on the testpypi site you can install it!

You need to go to https://testpypi.python.org and create an account.  

### Including source and wheel distributions

It is recommended that you include both a **source** and **wheel** distribution in your python package on pypi. Wheels are an advanced topic and it took me a while to get my head around what a wheel distribution actually is and why it is useful!  A nice phrase I came across is that '*wheels make things go faster*'

* A source is just what you think it is.  It is your source code!

* A wheel (.whl) is a ready-to-install python package i.e. no build stage is required. This is very useful for example if you have written custom C or Rust extensions for python. The wheel contains your extensions compiled and hence skips the build step.  Wheel's therefore make installation more efficient.  

> You can create universal wheel's i.e. applicable to both python 2 and 3 or pure python wheels i.e. applicable to only python 3 or python 2, but not both.

To install wheel use

```bash
$ pip install wheel
```

To produce the source and the wheel run 

```bash
$ python setup.py sdist bdist_wheel
```

* Now take a look in ./dist.  You should see both a zip file containing the source code and a .whl file containing the wheel.

A .whl file is named as follows:

```
{dist}-{version}-{build}-{python}-{abi}-{platform}.whl
```

For additional information on wheels I recommend checking out [https://realpython.com/python-wheels/](https://realpython.com/python-wheels/)

### Using twine and testpypi

To publish on pypi and testpypi we need to install an simple to use piece of software called `twine`

```bash
$ pip install twine
```

It is sensible to check for any errors before publishing!  To do this run the code below

```bash
$ twine check dist/*
```
This will check your source and wheel distributions for errors and report any issues.

> Before you push to testpypi you need to have a unique name for your package!  I recommend making up your own name, but if you are feeling particularly unimaginative then use `pypi_template_{random_number}`. Set this in `setup.py`. **Check if it has been created and exists on testpypi first!**

To publish on testpypi is simple.  The code below will prompt you for your username and password.

```bash 
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

If this uploads successfully you can then `pip` install from testpypi as follows.  The URL for your package is available on the project page for testpypi.

```bash
$ pip install -i https://test.pypi.org/simple/{your_package_name}==0.1.0
```

### Publish on pypi production

First I just want to say that you shouldn't really publish on the main production pypi site for unless you need to.  Use it when necessary to help your own research, work or colleagues, but not for testing purposes: use testpypi instead.  **You will need a separate account for PyPI.**.  If you intend to publish to pypi I recommend searching the index first in order to identify any potential name clashes.  

When you are ready you can upload use `twine`

```bash
$ twine upload dist/*
```

## Building publishing into your workflow with GitHub Actions

The manual steps I've outlined here are somewhat historical.  Most modern projects make use of version control in the cloud such as GitLab or GitHub.  These include ways to automatically publish updates to pypi.  One such way is with GitHub actions.  For example, I use **the publish to pypi action** when code is merge into the 'main' branch.

To set this up you will need to supply GitHub with a username and password for pypi.  Its stored securely, but you may rightly have concerns about privacy and security. My approach has been to create a secondary maintainer account for pypi rather than storing my main PyPI credentials to GitHub. I will leave it up to you to make a decision about if you feel this is necessary.  It can always be updated at a later date.

You can read more about Github actions [here](https://docs.github.com/en/actions)


