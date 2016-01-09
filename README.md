# fmriFlow 
fMRI Data Analysis Workflows with Apache Spark and Thunder. 

## User Guide
In this section we discuss in detail how to install and run an fmriFlow application step-by-step.
### Apache Spark Installation
<ol>
  <li>
    Download Spark from the official website: http://spark.apache.org/downloads.html
  </li>
  <li>
    Extract Spark: <code>tar -zxvf spark-1.6.0-bin-hadoop2.6.tgz</code>
  </li>
  <li>
    Set the environmental variables:
    <ol>
      <li>
        Open ~/.bashrc with your favorite editor, e.g. <code>nano ~/.bashrc</code>
      </li>
      <li>
        Append the following two lines<br>
        <code>export SPARK_HOME=(The path at which the Spark was extracted at step 2)</code><br>
        <code>export PATH=$PATH:$SPARK_HOME/bin</code>
      </li>
    </ol>
  </li>
</ol>
### Thunder Installation
<ol>
  <li>
    <code>git clone git@github.com:thunder-project/thunder.git</code>
  </li>
  <li>
    <code>cd thunder-project</code>
  </li>
  <li>
    <code>python setup.py install</code>
  </li>
  <li>
    <code>rm -rf thunder-project</code>
  </li>
</ol>

### fmriFlow Installation
Just clone this repository: <code>git clone git@github.com:gsvic/fmriFlow.git</code>

### Run the provided example
In order to run an application you just need to define the workflow in a Python file and submit it to Spark. To run the provided test.py you just type: <code>spark-submit test.py</code>. In this example we use sample input data from Thunder-Project.

## Additional Info

### Datasets
http://psydata.ovgu.de/forrest_gump/

### Links
http://studyforrest.org/7tmusicdata.html
https://github.com/hanke/gumpdata
http://klab.smpp.northwestern.edu/wiki/images/9/9b/Big_data_klab.pdf

### Neuroimaging Background
#### NifTi Data Format
Neuroimaging Informatics Technology Initiative <br>
http://nifti.nimh.nih.gov/ <br>
http://nipy.org/nibabel/

##Acknowlegments
This project was developed for the purposes of Digital Image Processing (HY620) Course of Dept. of Informatics at Ionian University.
http://di.ionio.gr/en/component/content/article/19-modules/semester-5/58-digital-image-processing.html
