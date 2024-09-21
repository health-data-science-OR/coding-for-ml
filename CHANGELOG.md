# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Dates formatted as YYYY-MM-DD as per [ISO standard](https://www.iso.org/iso-8601-date-and-time-format.html).

Consistent identifier (represents all versions, resolves to latest): [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10026326.svg)](https://doi.org/10.5281/zenodo.10026326)

## [v3.0.0]() UNRELEASED

### Changed

* ENV: updated to python 3.11 and added linting packages and `hatch` for packaging.
* ENV: upgraded packages to latest as of Jul 2024 including numpy > 2.0. Tested all numpy notebooks for compatibility.
* Coding Scientific functions exercises: Added new exercise 3 that implements $W_q$ and $P_n$ from a M/M/1 queue.
* Updated python packaging section.  Retired `setuptools` approach in favour of `hatch`. Split sections on installable packages, github install, PyPI install and automation.
* Removed redundant numpy notebooks from old intro python course.
* Removed `seaborn` dependency from visualise time series exercise.
* Minor typo and sentence fixes.

###

## 2.0.1 (2023-09-25) 

### Release Highlights

* Patched conda install instructions
* Added contributors
* Added `CHANGELOG.md`
