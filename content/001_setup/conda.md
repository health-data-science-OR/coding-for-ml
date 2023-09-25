# Conda virtual environment

The code examples in this module have been created in using the conda virtual environment `hds_code`

To create the conda environment issues the following command on a terminal

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
  - jupyterlab=3.4.6
  - matplotlib=3.5.3
  - nodejs=18.8.0
  - numpy=1.23.2
  - pandas=1.4.4
  - pip=22.2.2
  - python=3.8.12
  - scipy==1.9.1
  - statsmodels=0.13.2
  - pip:   
    - rich==12.5.1
    - scikit-learn==1.1.2
    - py7zr==0.20.0
```
