# Conda virtual environment

The code examples in this book have been created using the conda virtual environment `hds_code`

To create the conda environment, enter the following commands into the terminal:

```console
git clone https://github.com/health-data-science-OR/coding-for-ml
cd coding-for-ml
conda update conda
conda env create -f binder/environment.yml
conda activate hds_code
```

The dependencies `hds_code` will install via conda are:

```yaml
name: hds_code
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
  - nodejs=22.5.1
  - numpy=2.0.1
  - pandas=2.2.2
  - pip=24.0
  - python=3.11
  - pytest=8.3.2
  - py7zr=0.21.1
  - rich=13.7.1
  - scikit-learn=1.5.1
  - scipy==1.14.0
  - statsmodels=0.14.2    
```
