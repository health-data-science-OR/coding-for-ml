# Git

Congratualations, you have reached **a very important topic** in your data science studies!  Before we get into **Git** I want to acknowledge there other high quality version control tools available for your python or code in any other language; for example, subversion.

I'm going to teach you about Git not because its the best, but because **it is software I use on a daily basis** and also its the software I see most researchers using (which isn't that many!). For most data science tasks I've also found it robust and easy to use (although like all software there is always a few head scratching moments!).

## What is Git?

Git is a distributed version control system for files.  Git was originally developed by Linus Torvolds (who famously created the **Linux kernel**).  

> The origin of the name Git is quite amusing.  I will leave you to look these stories up and enjoy!

Let's assume you create a file `main.py` and add the following code:

```python
'''
main module

'''

def do_something():
    pass

if __name__ = '__main__':
    do_something()
```

Using version control you **commit** this file to a **repository**: a complete history of a project including all changes that have been made to files and directories within it. 

A few weeks later you modify `main.py`. 

```python
'''
main module

'''

def do_something():
    pass

def do_something_else():
    pass

if __name__ = '__main__':
    do_something()
    do_something_else()
```

With version control you don't need to create a new version of `main.py`.  Instead you save the changes to file, **stage** them and **commit** them to the repository.   This means we can view the history of commits!  For example, with this project git has a log that reports:

```bash
commit 4be943efd265dd58020d64af770ff63d229fd8d8 (HEAD -> master)
Author: Tom Monks <not_my_real_email@gmail.com>
Date:   Mon Aug 2 16:13:24 2021 +0100

    MAIN: added do_something_else()

commit 2e09f233e392448fdcf82b3c8ed45cd8a72c3e0e
Author: Tom Monks <not_my_real_email@gmail.com>
Date:   Mon Aug 2 16:11:58 2021 +0100

    MAIN: main.py -> do_something()

```

### Distributed?

A defining feature of Git is that it is **distributed**.  This means that each git **repository** is a complete history of a project and that multiple users are required to merge their changes together.   


