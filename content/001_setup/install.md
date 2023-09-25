# Install python and an IDE

The code in this book is written in using python 3.8.8 and a list of dependencies.

## Local installation

For beginners it is is recommended that users first install 'Anaconda'. This bundles python along with data science centric IDEs called `Spyder` and `Jupyter Notebook` (I recommend the more modern Jupyter-Lab over basic notebook, but there is no requirement to use it.)

https://www.anaconda.com/download/

```{admonition} See also
:class: tip
Anaconda includes 'conda' (a package manager).  An optional step is to follow our notes to use [conda](conda.md) to create a virtual environment that includes python 3.8.12 and Jupyter-Lab 3.x
```

```{admonition} My personal preferences
:class: tip
Alternatively (and my preference) you can install substantially smaller [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and install the packages you need using the provided conda environment or by selecting them yourself.  I tend to use packages installed from [conda-forge](https://conda-forge.org/), but the packages in the Anaconda channel (defaults) are equally good.
```


## Run our code via Binderhub or Google Colab

```{note}
You have the option of running our code in the cloud without the need to install on your local machine.
```

When you navigate to books pages and exercises that contain code cells you will see a image of a 'rocketship' in the top right hand corner of the screen.  Move you mouse over the image and you can choose to either open the notebook in BinderHub (will take ~1 minute to open) or [Google Colab](https://colab.research.google.com). You will need a Google account to use Google Colab.