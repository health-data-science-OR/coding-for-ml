# Introducing Git

Congratualations, you have reached **a very important topic** in your data science studies!  Before we get into **Git** I want to acknowledge there other high quality version control tools available for your python or code in any other language; for example, subversion.

Git is a distributed version control system for files.  Git was originally developed by Linus Torvolds (who famously created the **Linux kernel**).

> The origin of the name Git is quite amusing.  I will leave you to look these stories up and enjoy!

I'm going to teach you about Git not because its the best, but because **it is software I use on a daily basis** and also its the software I see most researchers using (which isn't that many!). For most data science tasks I've also found it robust and easy to use (although like all software there is always a few head scratching moments!).  

> I am managing the material I am writing for this book using Git. 

## A simple example

Before we look at setting up Git and issuing some commands let's just look at a simple use case and understand the benefits.

Let's assume you create a file `main.py` and add the following code:

```python
'''
main module

'''

def do_something():
    pass

if __name__ == '__main__':
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

if __name__ == '__main__':
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

In the output above the first line ends with `(HEAD -> master)`. This the the latest commit (the **head**).

Git commits track the changes to files between commits (or the history of changes to a file).  We can view changes between specific commits. This is called the **difference** or **diff**. For example for our two simple commits Git outputs:

```shell
diff --git a/main.py b/main.py
index 38056d8..431d04e 100644
--- a/main.py
+++ b/main.py
@@ -6,5 +6,9 @@ main module
 def do_something():
     pass
 
+def do_something_else():
+    pass
+
 if __name__ == '__main__':
     do_something()
+    do_something_else()

```

This output is designed to be fairly intuitive.  The `+` at the start of a line indicates that this is new code in the second commit.  This is incredibly helpful when you need to understand what has changed and how this might affect an analysis (or introduce bugs). If we had removed a line of code the it would have been prefixed with a `-`.

> Side note: commits become harder to followed the more changes are included.  So try to avoid huge commits where many many files and lines of code have been changed.  Commit often and thoughtfully.

Now imagine a scenario where you arrive at work the next day, re-run your analysis code and realise that you have made a mistake in the modified `main.py`: do_something_else() is  not needed and in fact the new code has broken the original analysis.  You need to roll back to the first iteration of the code that you know works.  This is called a **rollback**. After the rollback the git log looks like:

```bash
commit 2e09f233e392448fdcf82b3c8ed45cd8a72c3e0e (HEAD -> master)
Author: Tom Monks <not_my_real_email@gmail.com>
Date:   Mon Aug 2 16:11:58 2021 +0100
```
Referring back to our previous log we can see that the `HEAD` is now the original commit. Indeed `main.py` has reverted to:

```python
'''
main module

'''

def do_something():
    pass

if __name__ = '__main__':
    do_something()
```

> This is what is called a **hard** reset.  In practice, for a bug, you may want to do a **soft** reset.  In contrast a soft reset will roll back the last commit, but the files in your local repository will still be modified.  You can then edit them to fix a bug (test it works!), restage and then commit.   

## Distributed?

A defining feature of Git is that it is **distributed**.  This means that each git **repository** is a complete history of a project and that multiple users are required to merge their changes together.   

## Other Git resources

In addition to the resources in this book I very much recommend exploring the Git material provided by [Software Carpentry](https://swcarpentry.github.io/git-novice/).  This is wonderful novice friendly material that is open and free to use.
