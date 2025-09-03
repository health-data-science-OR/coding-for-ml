<h1 align="center">
  <a href="https://github.com/health-data-science-OR/coding-for-ml"><img src="./content/imgs/title_logo.png" alt="P4HDS" width="700"></a>
</h1>


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8377497.svg)](https://doi.org/10.5281/zenodo.8377497)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/health-data-science-OR/coding-for-ml/HEAD)

An open-source, interactive textbook for learning practical Python skills in health data science and machine learning. The material is available as a free online Jupyter Book:  
👉 **[Read the Book](https://www.pythonhealthdatascience.com)**


## 👥 Who This Is For

- Healthcare researchers and practitioners new to programming
- Data scientists looking to specialize in health applications  
- Students in health data science, health informatics, biostatistics, or related fields
- Anyone interested in applying Python to real-world health problems
- NHS or healthcare data scientists


## 👨‍💻 About

Created and maintained by [Thomas Monks](https://github.com/TomMonks) and contributors.


## ✨ Features

- **Interactive Jupyter Book**: Step-by-step guides, hands-on code examples, and exercises
- **Health Data Focus**: Real health data scenarios and healthcare-specific best practices  
- **Open and Free**: Fully open-source and accessible to everyone
- **Multiple Access Options**: Read online, run in the cloud, or install locally
- **Reproducible Environment**: All dependencies managed via Conda



## 📋 Prerequisites

- Basic familiarity with Python (helpful but not required)
- Interest in health data and healthcare applications
- Access to a computer with internet connection


## 🚀 Quick Start

### 1. Read Online

- Browse all book contents at: **[pythonhealthdatascience.com](https://www.pythonhealthdatascience.com)**

### 2. Run Code in the Cloud

- Launch an interactive version via **[Binder](https://mybinder.org/v2/gh/health-data-science-OR/coding-for-ml/HEAD)** with all dependencies pre-installed.

### 3. Local Installation

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

All required packages and dependencies are specified in `binder/environment.yml`.

---

## 📚 Table of Contents

- [Introduction and prerequisites](https://www.pythonhealthdatascience.com/content/001_setup/contributing.html)
- [Algorithms and computational modelling](https://www.pythonhealthdatascience.com/content/01_algorithms/01_design.html)
- [Statistical programming](https://www.pythonhealthdatascience.com/content/02_stat_prog/01_pandas_front_page.html)
- [Managing data science projects](https://www.pythonhealthdatascience.com/content/03_mgt/03_vc_front_page.html)



## 📝 Citation

If this book or its code helps your work, please cite the Zenodo record:

```
@software{monks_thomas_2023_8377497,
  author       = {Monks, Thomas},
  title        = {{Python for health data science: a hands-on 
                   introduction}},
  month        = sep,
  year         = 2023,
  note         = {{Please cite this software using the 
                   metadata from this file.}},
  publisher    = {Zenodo},
  version      = {v2.0.1},
  doi          = {10.5281/zenodo.8377497},
  url          = {https://doi.org/10.5281/zenodo.8377497}
}
```


## 🤝 Contributing

Contributions, suggestions, and feedback are welcomed! Please open an issue or fork and issue a pull request on the GitHub repository.


## 📄  License

Distributed under the MIT License. See `LICENSE` for more information.

---