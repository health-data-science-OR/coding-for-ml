# GitHub

All source code, Jupyter notebooks and markdown is available from the authors repo: 
* https://github.com/health-data-science-OR/coding-for-ml

## Repo Structure

```
coding-for-ml
├── binder
│   └── environment.yml
├── _config.yml
├── content
│   ├── 001_setup
│   │   ├── conda.md
│   │   ├── contributing.md
│   │   ├── docker.md
│   │   └── git.md
│   ├── 01_algorithms
│   │   ├── 01_design
│   │   │   ├── 01_primes.ipynb
│   │   │   ├── 02_better_design.ipynb
│   │   │   ├── 03_micro_opt.ipynb
│   │   │   └── 04_summing_up.ipynb
│   │   ├── 01_design.ipynb
│   │   ├── 02_oop
│   │   │   ├── 01_python_classes.ipynb
│   │   │   ├── 02_oop_sim.ipynb
│   │   │   └── text_adventure
│   │   │       ├── advanced_game.py
│   │   │       ├── basic_game.py
│   │   │       ├── __init__.py
│   │   │       └── __pycache__
│   │   │           ├── advanced_game.cpython-37.pyc
│   │   │           ├── advanced_game.cpython-38.pyc
│   │   │           ├── basic_game.cpython-37.pyc
│   │   │           ├── basic_game.cpython-38.pyc
│   │   │           ├── __init__.cpython-37.pyc
│   │   │           └── __init__.cpython-38.pyc
│   │   ├── 02_oop.ipynb
│   │   ├── 03_numpy
│   │   │   ├── 01_numpy_101.ipynb
│   │   │   ├── 01_performance.ipynb
│   │   │   ├── 02_intermediate_numpy.ipynb
│   │   │   ├── 02_vectors.ipynb
│   │   │   ├── 03_slicing.ipynb
│   │   │   ├── 04_algebra.ipynb
│   │   │   ├── 05_statistics.ipynb
│   │   │   ├── 06_sampling.ipynb
│   │   │   ├── 07_advanced_iter.ipynb
│   │   │   ├── 08_cs1.ipynb
│   │   │   ├── 09_cs2.ipynb
│   │   │   ├── 10_cs3.ipynb
│   │   │   ├── data
│   │   │   │   └── minor_illness_ed_attends.csv
│   │   │   ├── my_array.csv
│   │   │   └── TSP_abandoned.ipynb
│   │   ├── 03_numpy.ipynb
│   │   ├── 04_exercises
│   │   │   ├── 01_science_funcs.ipynb
│   │   │   ├── 02_array.ipynb
│   │   │   ├── 02_basic_oop.ipynb
│   │   │   ├── 03_int_numpy.ipynb
│   │   │   ├── big_special_str.txt
│   │   │   ├── data
│   │   │   │   ├── bank_arrivals.csv
│   │   │   │   ├── breach.csv
│   │   │   │   ├── dtocs.csv
│   │   │   │   ├── lysis.csv
│   │   │   │   ├── moviedb.csv
│   │   │   │   └── pieces
│   │   │   │       ├── p10.csv
│   │   │   │       ├── p1.csv
│   │   │   │       ├── p2.csv
│   │   │   │       ├── p3.csv
│   │   │   │       ├── p4.csv
│   │   │   │       ├── p5.csv
│   │   │   │       ├── p6.csv
│   │   │   │       ├── p7.csv
│   │   │   │       ├── p8.csv
│   │   │   │       └── p9.csv
│   │   │   ├── ex_templates
│   │   │   │   ├── ex1_quickstart.py
│   │   │   │   ├── ex2_quickstart.py
│   │   │   │   └── lab4_debug_challenge.py
│   │   │   └── im
│   │   │       ├── all_overlap.png
│   │   │       ├── brb_sol.png
│   │   │       ├── one_piece.PNG
│   │   │       ├── only_one_piece.png
│   │   │       ├── outline_pane.PNG
│   │   │       └── valid_layout.png
│   │   ├── 04_exercises.ipynb
│   │   ├── 05_debug
│   │   │   ├── 01_debug_numpy.md
│   │   │   └── debug_numpy_py.py
│   │   ├── 05_debug.md
│   │   ├── 06_solutions
│   │   │   ├── 01_science_funcs.ipynb
│   │   │   ├── 02_array.ipynb
│   │   │   ├── 02_basic_numpy.ipynb
│   │   │   ├── 02_basic_oop.ipynb
│   │   │   ├── 03_int_numpy.ipynb
│   │   │   ├── big_special_str.txt
│   │   │   └── Untitled.ipynb
│   │   ├── 06_solutions.md
│   │   ├── data
│   │   │   ├── hist.csv
│   │   │   ├── minor_illness_ed_attends.csv
│   │   │   ├── salaries.csv
│   │   │   └── salaries_extended.csv
│   │   └── im
│   │       ├── gsearch.PNG
│   │       ├── salaries_extended.PNG
│   │       └── salaries.PNG
│   ├── 02_stat_prog
│   │   ├── 01_pandas
│   │   │   ├── 01_intro_pandas.ipynb
│   │   │   ├── 02_files.ipynb
│   │   │   ├── 03_non_standard_download.ipynb
│   │   │   ├── 04_datetimes.ipynb
│   │   │   ├── 05_analysing.ipynb
│   │   │   └── 06_cs_combining.ipynb
│   │   ├── 01_pandas_front_page.md
│   │   ├── 02_matplotlib
│   │   │   ├── 01_matplotlib.ipynb
│   │   │   ├── 02_matplotlib2.ipynb
│   │   │   ├── 02_plotting_time_series.ipynb
│   │   │   ├── 03_cs_hm.ipynb
│   │   │   ├── explore.png
│   │   │   └── stacked.png
│   │   ├── 02_visual_front_page.md
│   │   ├── 03_exercises
│   │   │   ├── 00_dataframes.ipynb
│   │   │   ├── 01_data_wrangling_matplotlib.ipynb
│   │   │   ├── 02_stroke_data_wrangling.ipynb
│   │   │   ├── 03_visualise_ts.ipynb
│   │   │   ├── data
│   │   │   │   ├── di_counts.csv
│   │   │   │   ├── di_rq_to_test.csv
│   │   │   │   ├── di_test_to_report.csv
│   │   │   │   ├── sw_imaging.csv
│   │   │   │   ├── synth_lysis.csv
│   │   │   │   └── total_referrals.csv
│   │   │   └── hosp_1_ed.png
│   │   ├── 03_exercises_front_page.md
│   │   ├── 04_solutions
│   │   │   ├── 00_dataframes.ipynb
│   │   │   ├── 01_data_wrangling_matplotlib_solutions.ipynb
│   │   │   ├── 02_stroke_data_wrangling_solutions.ipynb
│   │   │   └── 03_visualise_ts_SOLUTIONS.ipynb
│   │   └── 04_solutions_front_page.md
│   ├── 03_mgt
│   │   ├── 01_git
│   │   │   ├── 01_why.md
│   │   │   ├── 02_git.md
│   │   │   ├── 03_cs_1.md
│   │   │   ├── 04_cs_2.md
│   │   │   └── 05_cs_3.md
│   │   ├── 02_packaging
│   │   │   ├── 01_python_packages.ipynb
│   │   │   ├── example.ipynb
│   │   │   └── ts_emergency
│   │   │       ├── data
│   │   │       │   ├── syn_ts_ed_long.csv
│   │   │       │   └── syn_ts_ed_wide.csv
│   │   │       ├── datasets.py
│   │   │       ├── __init__.py
│   │   │       ├── plotting.py
│   │   │       └── __pycache__
│   │   │           ├── datasets.cpython-38.pyc
│   │   │           ├── __init__.cpython-38.pyc
│   │   │           └── plotting.cpython-38.pyc
│   │   ├── 03_mgt_front_page.md
│   │   ├── 03_pypi
│   │   │   ├── 01_pypi.md
│   │   │   ├── environment.yml
│   │   │   ├── LICENSE
│   │   │   ├── MANIFEST.in
│   │   │   ├── requirements.txt
│   │   │   ├── setup.py
│   │   │   └── test_package
│   │   │       ├── data
│   │   │       │   └── test_data.csv
│   │   │       ├── __init__.py
│   │   │       ├── __pycache__
│   │   │       │   └── __init__.cpython-38.pyc
│   │   │       └── test.py
│   │   ├── 03_vc_front_page.md
│   │   ├── 04_binder
│   │   │   └── 01_binder.md
│   │   ├── 04_exercises
│   │   │   ├── 01_python_packages.ipynb
│   │   │   ├── 02_conda.ipynb
│   │   │   ├── 02_use_conda.md
│   │   │   ├── 03_binder.md
│   │   │   └── im
│   │   │       ├── detrended.jpg
│   │   │       └── diag.jpg
│   │   ├── 04_exercises_front_page.md
│   │   ├── 05_solutions
│   │   │   ├── 01_python_packages_solutions.ipynb
│   │   │   ├── im
│   │   │   │   ├── detrended.jpg
│   │   │   │   └── diag.jpg
│   │   │   └── ts_emergency
│   │   │       ├── data
│   │   │       │   ├── syn_ts_ed_long.csv
│   │   │       │   └── syn_ts_ed_wide.csv
│   │   │       ├── datasets.py
│   │   │       ├── __init__.py
│   │   │       ├── plotting
│   │   │       │   ├── __init__.py
│   │   │       │   ├── __pycache__
│   │   │       │   │   ├── __init__.cpython-38.pyc
│   │   │       │   │   ├── tsa.cpython-38.pyc
│   │   │       │   │   └── view.cpython-38.pyc
│   │   │       │   ├── tsa.py
│   │   │       │   └── view.py
│   │   │       └── __pycache__
│   │   │           ├── datasets.cpython-38.pyc
│   │   │           ├── __init__.cpython-38.pyc
│   │   │           └── plotting.cpython-38.pyc
│   │   └── 05_solutions_front_page.md
│   ├── appendix
│   │   ├── fp_lectures.md
│   │   ├── fp_practicals.md
│   │   ├── labs
│   │   │   ├── 01_basics.ipynb
│   │   │   ├── 02_basics.ipynb
│   │   │   ├── debug1.md
│   │   │   ├── debug2.md
│   │   │   └── src
│   │   │       ├── cinema_exercise.py
│   │   │       ├── list_comprehensions.py
│   │   │       ├── moviedb.csv
│   │   │       ├── py_finance.py
│   │   │       ├── string_manipulation.py
│   │   │       ├── test_finance.py
│   │   │       ├── week1_debug_challenge1.py
│   │   │       └── wk2_debug_challenge.py
│   │   └── lectures
│   │       ├── Lecture1.ipynb
│   │       └── Lecture2.ipynb
│   ├── front_page.md
│   ├── imgs
│   │   ├── title_cropped.png
│   │   ├── title_cropped.png~
│   │   └── title.odg
├── Dockerfile
├── images
│   ├── binder_1.png
│   ├── binder_2.png
│   ├── detrended.jpg
│   └── diag.jpg
├── LICENSE
├── README.md
└── _toc.yml

```

