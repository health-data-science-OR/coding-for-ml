# Conda virtual environment

The code examples in this module have been created in using the conda virtual environment `hds_code`

To create the conda environment issues the following command on a terminal

```console
git clone https://github.com/health-data-science-OR/coding-for-ml
cd coding-for-ml
conda update conda
conda create -f binder/environment.yml
conda activate hds_code
```

The dependencies `hds_code` will install via conda are:

```yaml
name: hds_code
channels:
  - conda-forge
dependencies:
  - jupyterlab=3.0.9
  - matplotlib=3.3.4
  - nodejs=10.13.0
  - numpy=1.19.2
  - pandas=1.2.3
  - pip=21.0.1
  - python=3.8.8
  - scipy==1.6.1
  - statsmodels=0.11.1
  - pip:
    - scikit-learn==0.24.1
    - py7zr==0.14.1
```
