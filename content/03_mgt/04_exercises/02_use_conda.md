# Using `conda`

To help you with your deployment either via PyPi, Binder or handing over a local python package it is a good idea to improve your `conda` package manager skills and working with conda virtual environments.  

> If you are working on a Windows OS I recommend running these commands from Anaconda prompt.  If you are working on a Mac or a Linux machine then use a terminal.

> For more detail on conda check out the [docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

## Exercise 1

* List the `conda` environments on your computer.

```bash
$ conda env list
```

## Exercise 2

* By default you will be in the `base` conda environment.  List the packages installed.

```bash
$ conda list
```

## Exercise 3

Let's practice creating an empty environment, activating it, checking it is empty and then remove it.


* Create an empty conda environment `empty_env`

```bash
$ conda create --name empty_env
```

> You will be prompted if you want to proceed.  Answer Yes!

* Activate the environment

```bash
$ conda activate empty_env
```

* List the packages installed

```bash
$ conda list
```

> There should be no packages!  If they are then you are probably in the wrong environment.  Check this with `conda env list`.  The active env is marked with `*`

* Deactivate the env to return to `base`

```bash
$ conda deactivate
```

* Remove the environment

```bash
$ conda env remove --name empty_env
```

* Verify the environment is removed using list

```bash
$ conda env list
```

## Exercise 4

Now let's create an environment and install a few packages from the command line.

* Create an environment called `test_env` 
* Activate `test_env`
* Install `python` version 3.8.8 and `numpy` 1.20.3 

```bash
$ conda install python=3.8.8 numpy=1.20.3
```

> Conda will report what dependencies are going to be installed.  This might vary depending on what operating system you use.  You will also be prompted if you are happy to proceed.  It will take a few seconds to install.

* List all the packages installed in `test_env`.  Check that the `python` and `numpy` versions match those you used.


## Exercise 5

Staying with `test_env `create a `environment.yml` file that contains **only** the packages you installed from the command line.

* Issue the following export command. Make sure you include the `--from-history` option or you will get a full list of everything in the environment.  The output you should is is displayed below as well.

```bash
$ conda env export --from-history

name: test_env
channels:
  - defaults
dependencies:
  - numpy=1.20.3
  - python=3.8.8
```

* It is also possible to export this to a named file (typically `environment.yml`)

```bash
$ conda env export --from-history -f environment.yml
```

> Remember this will export the file to the current working directory.  For simplicity I recommend working in the same directory as your code.  This makes even more sense for example if you have a git repo.

## Exercise 6

Now let's practice creating a conda env from file.  I recommend working in the same directory as exercise 5.

* Deactivate the `test_env` environment
* Remove the `test_env` 
* Create the conda environment from file

```bash
$ conda env create -f environment.yml
```

> This (re)creates `test_env`.

* Activate `test_env`
* Check what packages are installed.







