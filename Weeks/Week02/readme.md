# Week 2: Data in Urban Studies

January 10, 2022
## Agenda

*   This class will be recorded (remind me if I forget!)
*   Log in to the class JupyterHub using the [UP206A Git Puller](https://jupyter.idre.ucla.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fyohman%2F22W-UP206A&urlpath=lab%2Ftree%2F22W-UP206A%2F&branch=master) to avoid the bottleneck
*   Welcome to week 2
    * Concerns? Questions?
    * Office hours - we're here for you!
    * Week 1 assignments may be submitted this week without penalty
*   Logistics: Next week is a holiday!
    * Plan is to do a condensed session on January 18, 2pm Tuesday afternoon (maybe 2 hours or so)
    * Session will be recorded
    * Attend in-person (virtually) if you can (you will get more out of it!) 
*   Python review
*   Group creation
*   Break
*   Lab session
*   A discussion on a selection from last week's thinking cap

## Hands on
First, grab the course material, and "pull" it into your JupyterHub space:

* [UP206A Git Puller](https://jupyter.idre.ucla.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fyohman%2F22W-UP206A&urlpath=lab%2Ftree%2F22W-UP206A%2F&branch=master) (This link will automatically launch JupyterHub and clone the course material into your directory)

Topics: 
*   [Python Boot Camp Review](W201-PythonReview.ipynb)
*   [Intro to the geopandas library using Metro data](W202-PythonandMetro.ipynb)

# Assignments (due 23:59 Sunday, the day before class)

## Group Assignment #1: Project Proposal
The course will largely be guided by your final project, which will be conducted in pairs. Consider that your final project will be a representation of what you learn in this course, and how you apply it on a project level. Consider also that your final project can serve to showcase your data science and mapping skills, which may become a valuable asset for your career moving forward.

Meet with your partner, discuss and identify a research question, identify and collect data, articulate how you intend to use and analyze it, and begin to speculate how the data can answer your research inquiry. Understand that this may change later, especially as we learn more about what we can do with our methods, and also, as you find the data sources that can or cannot support your research.

Next, identify and download at least two datasets that you believe can guide your research. Make sure that at least one of them has a spatial component. For example, if one of your datasets comes from the census, identify which survey you will use (e.g. Decennial or American Community Survey), and which variables you will select. Note that we will be covering census data in detail in Week 3. Your second dataset should come from a separate source. For example, you may want to do a crime analysis and obtain data from the LA Data Portal.

First, create a group repo. 

1. Select a member of the group who will be the main account holder of the repo
2. Create a new repository for your group project
3. Go to Settings, Manage Access, and add your partner as a collaborator
1. Create a Group Assignments folder (hint: click on Add File, Create new File, and enter "Group Assignments/readme.md" in the text box)
4. Create a markdown file for your project proposal

Your project proposal should include the following:
*   An introduction of your research question
*   An explanation of why it is important to you, why it matters to others, and what is at stake
*   A description of the spatial scope (e.g. Boyle Heights or Hong Kong), and why space and/or time matters for your project
*   A preliminary but definitive description of data sources (at least two) that you will use
    * Include datasource with links
*   A scope that explains the intended analysis and resulting visualizations for your project
*   A concluding paragraph of what insights you expect to gain from your research

Submit your assignment [here](https://github.com/yohman/22W-UP206A/discussions/9)

## Individual assignment: Data Exploration

### Create a token

In order to pull and push content to GitHub, you must first create a token, which will serve as your password. Refer to this tutorial to create your token:

* [How to create a token](../../Git%20related/Create%20a%20token.md)

### Clone your repo

This is your first code assignment submission. Before you begin, create a clone of your repo in JupyterHub.

* [How to clone your repo into JupyterHub](../../Git%20related/Clone%20repo%20to%20hub.md)

### Submission guidelines:

Find and download a dataset of your choice. This can be a shapefile, csv file, or json file. 

Launch JupyterHub, go to your `up206a` repo folder, and create a `week01` folder.

Load the dataset to the `up206a/week01` folder.

Create a new python notebook (**do not** work on a copy of the lab notebook):

<kbd><img src="images/notebook.png"></kbd>

Right click on the `Untitled.ipynb` tab and rename the notebook to `week 1 assignment.ipynb`

<kbd><img src="images/rename.png"></kbd>

Add an introductory markdown cell with a title (header) and paragraph that describes what you are doing.

Import the data, and conduct data exploration, making sure to document your steps and your preliminary findings. At minimum, run the following commands:

* `.shape`
* `.info`
* `.head()`
* `.plot()`
* `.value_counts()`
* run a query on the data that filters it in some way

For each code cell, add a markdown cell that explains what you are doing.

Add markdown cells that describe the output of each operation.

Save your notebook.

### Commit your changes to your GitHub class repo.

Commit your changes to your GitHub repo by following these instructions:

* [How to commit and push to your repo](../../Git%20related/Commit%20and%20push.md)

### Submit your assignment 

The last step is to submit your assignment to the class repo discussion section [here](https://github.com/yohman/22W-UP206A/discussions/7).
