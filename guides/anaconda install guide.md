# How to install Anaconda with spatial libraries

1. Install Anaconda
1. Go to "Environments" and create new
1. Name it "geo"
1. Right click on the geo environment and launch terminal
1. Enter the following command:

`conda install --channel conda-forge geopandas`

Then,

`pip install --upgrade --force-reinstall shapely`
