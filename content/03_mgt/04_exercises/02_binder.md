# Binderhub exercises

> For this exercise you will need a Github account. Sign-up via [https://github.com/](https://github.com/). 

In exercises 1 to 4 you are going to upload a Jupyter notebook to Github and share it via Binderhub.

## Exercise 1:

First create the Github repo and insert a notebook file.

**Task**:

* Create a Github repo.  You can use any repo name you choose.  If you cannot decide a suggestion is 'binder_exercise'
* Make a local copy of the notebook that contains the solutions to ED data wrangling exercise.
* Push the notebook to the repo.

**Hints**
* If you do not know how to use GitHub you can create the repository and then click on the green **upload** button.  This will allow you to select the notebook and add a commit message.
* If you prefer to do this via git then I recommend creating the remote repo first, cloning locally, add (and stage), commit the notebook.  Finally push using `git push`.  Depending on your authentication method you may be asked for your GitHub username and password.

## Exercise 2:

You now need to create a conda environment file so that binderhub knows what version of python and data science packages to install.

**Task**:
* Create a directory in the repo called `binder``
* Create a conda environment file in `binder/environment.yml`  with the appropriate libraries. A suggestion is:

```YAML
name: binder_ex
channels:
  - defaults
  - conda-forge
dependencies:
  - matplotlib=3.4.2
  - numpy=1.20.3
  - pandas=1.3.1
  - python=3.8.8
```

* Commit the changes and push to github using your preferred method.


## Exercise 3:

You are now ready to share your notebook via binder

**Task**
* Copy the URL of your GitHub repo's main page.
* Using your browser navigate to [https://mybinder.org](https://mybinder.org)
* Paste the URL of your Github repo and click on 'launch' (the build will take several minutes)

## Exercise 4:

Let's add a 'launch binder badge' to a `README.md` file in your repo.

**Task**:
* From the BinderHub setup page copy the markdown text that you will use to create the badge.
* If required (i.e. you don't already have one). Create a `README.md` file and add it to your GitHub repo.
* Open `README.md` for editing.  At the top paste in the copied launch binderhub markdown.
* Push the update to your GitHub repo.
* Navigate to your GitHub repo and click on the badge to launch binderhub!


## Exercise 5:

**Task**
* Use BinderHub to share the more advanced `ts_emergency` package you created in the exercises. 