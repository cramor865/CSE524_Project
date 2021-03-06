**Tasks:**

1. Filter down data to train a segmentation model.

   1. Train a weakly supervised model for efficient segmentation.

   2. Train a fully unsupervised model.

2. Visualize the result on top of Google Earth view.

   1. Project Penguin Colony Visualization for a specific set of locations.

   2. Create an application for running this visualization as a desktop app.

**Progress Report:**

**Task 1: Filter down data to train a segmentation model**

*Summary:* *For the locations given, the patches are hand labelled and this information is stored in the KML files which are parsed to create relevant geometries and generate 2 images. One is the RAW Image of the location and the other one is the one that has the hand labelled guano patches. These 2 form our dataset for training and testing the segmentation model with the later being the ground truth. U-Net is used for the segmentation purpose.* 

For the 19 locations, the KML file is parsed to capture details and generate the original raw image and the Ground Truth Image for the location. This prepares the dataset for training and testing the segmentation model. This process has a series of steps as shown below:

 

1. Original Image set
   1. Read files and find bounding box and centroid and store in dictionary with place names as keys
   2. Using the dictionary save the html files for the maps
   3. Using selenium run each html file and take screenshot
   4. save screenshot with name as <location>oi

2. Ground Truth Image Set
   1. Use the geometry to mark regions on map
   2. Save the html files for the map
   3. Using selenium run each html file and take screenshot

   4. save screenshot with name as <location>gt

 

For a better understanding, we represent the process using a flowchart as below:

![img](/flochart.jpg)

 

This process captures and generates image sets as follows:

 

Capebatterbee

Original Image:

![img](/fig1.png)

Ground Truth Image:

![img](/fig2.png)

For all the locations, the images are ready for segmentation except acuna and wpec which returned the following results:

 

Acuna

Original Image:

![img](/fig3.png)

Wpec

![img](/fig4.png)

This has happened because the Sentinel 2A didn’t have a capture for these locations for the year 2019. Hence, we discard these two for the further steps of segmentation. 

Next, we create the U-Net model as follows:

![https://miro.medium.com/max/800/1*OkUrpDD6I0FpugA_bbYBJQ.png](/fig5.png)

This model is now ready for training. Hence, we take the dataset and split it into training and testing data.

**Task 2:** **Visualize the results on top of Google Earth View** 

*Summary:* *There were 19 locations provided for mapping the penguin colonies. The locations have been presented as KML files which have to be analyzed to get coordinates for the location and then these coordinates can be used to collect images of the location from specific datasets for current time. The median of the collection is then used for segmentation and the result is presented as a marker on the location which pops up a display box to show the results for the specific location. This has been achieved using Google Earth Engine python API and Folium.*

For the 19 locations provided, after the segmentation process is done, there is a marker placed at every location. Upon clicking the marker, the relevant segmentation result is displayed in a pop-up box. This has been implemented using the folium’s Iframe package and the result is shown below:

![img](/fig6.png)

 

The results are displayed currently for the 19 locations provided but the same code can be reused to perform segmentation on an unknown location and test the model’s performance. For an unknown location, the user inputs a (lat, long) tuple for the supposedly center of the location. This is a jupyter notebook application which can be run using anaconda and installing the following packages: folium, selenium, google earth engine python API.

 

 

 
