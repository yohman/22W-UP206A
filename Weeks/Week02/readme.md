# Week 2: Data in Urban Studies: The challenge in data acquisition

## Agenda
*   Attention! **Next class is on Wednesday, January 20th, at 6pm**
*   Welcome to week 2
    * Concerns? Questions?
    * Office hours - we're here for you!
*   Lab session
*   Break
*   Group creation
    * Breakout rooms based on interests
    * Google doc to enter your group pairings
*   A discussion on a selection from last week's readings
*   [Our class data library](https://docs.google.com/spreadsheets/d/1m67s0-SptURpRLr6ISq6Fy7e_66LcSPLjfPjqhZxC8M/edit?usp=sharing)

## Hands on
*   [Python Boot Camp Review](W201-PythonReview.ipynb)
*   [Intro to the geopandas library using Metro data](W202-PythonandMetro.ipynb)

## Assignments (due 23:59 Sunday, the day before class)
### Group Assignment #1: Project Proposal
The course will largely be guided by your final project, which will be conducted in pairs. Meet with your partner, discuss and identify a research question, and begin the collection of data, its analysis, and determine how it may answer your question. Understand that this may change later, especially as we learn more about what we can do with our methods, and also, as you find the data sources that can or cannot support your research.

Next, identify and download at least two datasets that you believe begins to guide your research. Make sure that at least one of them has a spatial component. For example, if one of your datasets comes from the census, identify which survey you will use (e.g. Decennial or American Community Survey), and which variables you will select. Note that we will be covering census data in detail in Week 3. Your second dataset should come from a separate source. For example, you may want to do a crime analysis and obtain data from the LA Data Portal.

First, create a group repo. 

1. Select a member of the group who will be the main account holder of the repo
2. Create a new repository for your group project
3. Go to Settings, Manage Access, and add your partner as a collaborator
1. Create a Group Assignments folder (hint: click on Add File, Create new File, and enter "Group Assignments/readme.md" in the text box)
4. Create a markdown file for your project proposal

Create a markdown page (optionally, you may choose to upload a PDF), which will be your group's project proposal. Make sure to include the following:
*   An introduction of your research question
*   An explanation of why it is important to you, why it matters to others, and what is at stake
*   A description of the spatial scope (e.g. Boyle Heights or Hong Kong), and why space and/or time matters for your project
*   A preliminary but definitive description of data sources (at least two) that you will use
    * Include datasource with links
*   A scope that explains the intended analysis and resulting visualizations for your project
*   A concluding paragraph of what insights you expect to gain from your research

### Individual assignment: Data Exploration
*   Find and download a dataset of your choice. This can be a shapefile, csv file, or json file. If you do not have a dataset, you can download one from the [Los Angeles Times' "Mapping L.A. Boundaries"](http://boundaries.latimes.com/sets/) page.
*   Launch JupyterHub and pload the dataset to your JupyterHub space
*   Create a new python notebook (do not work on a copy of the lab notebook)
*   Add an introductory markdown cell with a title (header) and paragraph that describes what you are doing
*   Import the data, and conduct data exploration, making sure to document your steps and your preliminary findings. At minimum, run the following commands:
    * `.shape`
    * `.info`
    * `.head()`
    * `.plot()`
    * `.value_counts()`
    * run a query on the data that filters it in some way
*   For each code cell, add a markdown cell that explains what you are doing
*   Add markdown cells that describe the output of each operation
*   Add your first data exploration Jupyter Notebook to your GitHub repository

### Reading assignment:

![Silvia](https://knowledge.luskin.ucla.edu/wp-content/uploads/2016/11/rsz_silvia.jpg)

Next week we begin our first episode of our "Conversation Series." Our guest will be [Silvia Gonzales](https://luskin.ucla.edu/person/silvia-gonzalez), a former director of the [Center for Neighborhood Knowledge](https://knowledge.luskin.ucla.edu/), and the department's most recent PhD graduate. Read her paper on gentrification, and prepare to ask her some questions next week.

*   ["Triangulating Neighborhood Knowledge to Understand Neighborhood Change: Methods to Study Gentrification" by Anastasia Loukaitou-Sideris, Silvia Gonzales, and Paul Ong](../../readings/sideris_gonzales_ong.pdf)

Additional readings on the state of the census:

*   ["Counting California: Challenges for the 2020 Census" by The Public Policy Institute of California](https://www.ppic.org/publication/counting-california-challenges-for-the-2020-census/)
*   [Every Angeleno Counts: The 2020 Census in Los Angeles](https://usc.data.socrata.com/stories/s/Every-Angeleno-Counts-The-2020-Census-in-Los-Angel/anyu-vh6b/)
