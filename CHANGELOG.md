# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Dates formatted as YYYY-MM-DD as per [ISO standard](https://www.iso.org/iso-8601-date-and-time-format.html).

Consistent identifier (represents all versions, resolves to latest): [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10026326.svg)](https://doi.org/10.5281/zenodo.10026326)

## [v3.0.0]() UNRELEASED

### Changed for 2025/26

* ENV: updated to python 3.12
* ENV: updated packages as of August 2024. 
* BOOK: Install instructions updated.  Removed Anaconda. Now recommend miniconda or mamba
* BOOK: Conda environment page merged into installation instructions.

### Changed for 2024/25

* ENV: updated to python 3.11 and added linting packages and `hatch` for packaging.
* ENV: upgraded packages to latest as of Jul 2024 including numpy > 2.0. Tested all numpy notebooks
* Coding Scientific functions exercises: Added new exercise 3 that implements $W_q$ and $P_n$ from a M/M/1 queue.
* Updated python packaging section.  Retired `setuptools` approach in favour of `hatch`. Split sections on installable packages, github install, PyPI install and automation.
* Removed redundant numpy notebooks from old intro python course.
* Removed `seaborn` dependency from visualise time series exercise.
* Minor typo and sentence fixes.

## v2.0.2

### Fixed

Two small patches to numpy material are included in this release

* Fixed silent bug in `python_bootstrap` function from numpy case study 1. - This led to a mistake in overestimating numpy performance
* Fixed variable name runtime error when calling OLS regression code

## v2.0.1 (2023-09-25) 

### Release Highlights

* Patched conda install instructions
* Added contributors
* Added `CHANGELOG.md`
