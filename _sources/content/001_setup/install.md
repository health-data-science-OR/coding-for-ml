# Install python and an IDE

The code in this book is tested using python 3.12 and a list of dependencies.  These can be found in the main repository in `binder/environment.`

## Local installation

For beginners it is is recommended that users first install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and install the packages you need using the provided conda environment. The environment bundles Python 3.12 along with a data science centric IDEs called `Jupyter-Lab`.

```{admonition} See also
:class: tip
Miniconda includes 'conda' (a package manager).  Its good practice to have an environment per data science project. It allows you to create a "reproducible software box" on your computer that contains the version of Python you used along with the right versions of the other software (e.g. `numpy` and `pandas`).Instructions to setup the virtual environment are provided below, and we will cover reproducible environments in more detail later in the book.
```

```{admonition} An alternative to conda
:class: tip, dropdown
Alternatively you can install substantially faster and more Open Source friendly [Mamba via miniforge](https://github.com/conda-forge/miniforge) and install the packages you need using the provided conda environment or by selecting them yourself.  By default `mamba` will install packages from conda-forge community channel. It is a slot in replacement for `conda` so simply replace all text that says `conda` with `mamba` below.  Its my personal perference and what I use in all my contemporary research.
```

### Install the dependencies

1. **Clone this repository**:
   ```sh
   git clone https://github.com/health-data-science-OR/coding-for-ml.git
   cd coding-for-ml
   ```

2. **Install the virtual environment**:
   ```sh
   conda env create -f binder/environment.yml
   conda activate hds_code
   ```

3. **Launch JupyterLab**:
   ```sh
   jupyter-lab
   ```

For reference the latest version of the book uses these packages:

```yml
name: hds_code
channels:
  - conda-forge
dependencies:
  - black
  - flake8
  - hatch
  - jupyterlab=4.4.6
  - jupyterlab-spellchecker=0.8.4
  - matplotlib=3.10.6
  - nbqa
  - nodejs=24.4.1
  - numpy=2.3.2
  - pandas=2.3.2
  - pip=25.2
  - python=3.12
  - pytest=8.4.1
  - py7zr=1.0.0
  - rich=14.1.0
  - scikit-learn=1.7.1
  - scipy==1.16.1
  - statsmodels=0.14.5    
```

## Run our code via Binderhub or Google Colab

```{note}
You have the option of running our code in the cloud without the need to install on your local machine.
```

When you navigate to books pages and exercises that contain code cells you will see a image of a 'rocketship' in the top right hand corner of the screen.  Move you mouse over the image and you can choose to either open the notebook in BinderHub (will take ~1 minute to open) or [Google Colab](https://colab.research.google.com). You will need a Google account to use Google Colab.