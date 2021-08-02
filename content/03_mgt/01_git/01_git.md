# The case for version control

```{admonition} "Wait.. you DON'T use version control for your code?!"
I'm going to be very honest and say that I find it odd that I still need to have a conversation with people who code about basic version control. I can't really understand why it isn't taught routinely and second nature to everyone. Its actually best not to admit you don't use it when I'm in the room.  

I'm old, and in my professional career, I can't remember a time I didn't use version control software. I think its so important for data science that I'm going to admit a few embarrassing (in a geeky sort of way) things about my history with version control. My first admission is that I first ventured into the world of version control in the summer of 2001 for a summer VB6(!) coding job. At the time I was doing my undergrad in Computer Science and let me tell you - I made a lot of mistakes in my coding!  My second admission is that I used to be an avid MS Windows user (so sorry Stallman) and from around 2003-2008 I used TortoiseSVN. This is a GUI extension of the excellent subversion software for version control. I switched to equally excellent Git after I returned to university to study for a PhD (introduced courtesy of the Warwick Computing Society) where I used it to control R, S-PLUS(!), and C# code. It was not until June 28th 2011 that I pushed my first commit to the now famous GitHub (some dodgy C# code to automate a commerical simulation package via the Windows Common Object Model - yuk!).  

You don't need to remember any of that, just take home the message, that I'm pro version control for one single reason. Part of any data science study is carefully controlling and managing your code. If you don't then you will fail to get it producing the same results or perhaps even working again in 6 months time! **You should view your code as a first class citizen in data science.  Do your code, yourself and others a favour - use version control.**
```

## Why use version control?

### Scenario 1

Consider a scenario where you take up a position as a data scientist in a government organisation.  On your first day you are told that your predecessor has left already, but all code needed for your job is saved to the server.  You log in and have a look in the directory:

```
uber_import_gov_proj
├── 20190320_main_v2.py
├── archive
│   ├── 20190504_v3_main_not_final.py
│   ├── tests_before_fix.py
│   ├── v1_main.py
│   └── v3_main_final.py
├── v2_main_20190320.py
├── v3_main_final.py
├── v2v3_main_final_TM_MP_MA_DC(MA_conflicted_copy).py
└── v3_main_final_TMonks_Conflicted_Copy.py
```
Take a moment to take in the mess of this project.  Perhaps you can laugh about it.  The questions you should be asking yourself are:

* have you ever ended up in a mess like this even though you have had the most noble of intentions at the start of a project?
* have you ever worked with someone who has managed work in this way?

In my experience this sort of structure turns up surpursingly often, for all sorts of data science and non-data science projects.  It is certaintly more common than a cleanly organised data science project.  This is a totally unnecessary situation.  With version control we actually only need this structure:

```
uber_import_gov_proj
├── main.py
```

### Scenario 2

Even though the code is a complete mess, you are still working for that government organisation several months later.  It is a Monday morning and you stroll into work with the intention of trying again to work out if you should run the analysis code in `v3_main_final.py` or `archive/v3_main_final.py`.  But alas your plans are interrupted!  Some organisation critical code originally written years ago, by an analyst long since departed, failed to run over the weekend. It's your job to fix it!  You open up the code and after the initial horror of finding its a single 'god function' with a repeating verbose code, begin to try and make sense of the problem.  Your initial findings are:

* Its clear from mments in the code that it has been modified by several people over the years, but it is not clear how many times, who the coders were, what the changes were made and in what order.  
* There's no 'archive' folder listing older versions of the code and no documentation.  So there's no way to roll back changes.
* There's no code to test if the main analysis code runs as expected.

Before you laugh again this is actually a situation I found myself in many years ago. It wasn't fun (at all - especially as I had lots of people checking if "I'd fixed it yet?" quite frequently). It did turn out that a change had introduced the bug under a given set of conditions. So, after quite a while, I fixed what turned out to be an extrememly important piece of code for the organisation.  There was no version control system in place so I carefully documented the changes both in the code via comments and in external documentation. 

Can you think of any software that's open source and free that would have made this a bit easier?

### Scenario 3:
