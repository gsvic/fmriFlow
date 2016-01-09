# fmriFlow 
fMRI Data Analysis Workflows with Apache Spark and Thunder

## User Guide
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


## Datasets
http://psydata.ovgu.de/forrest_gump/

## Links
http://studyforrest.org/7tmusicdata.html
https://github.com/hanke/gumpdata
http://klab.smpp.northwestern.edu/wiki/images/9/9b/Big_data_klab.pdf

## Neuroimaging Background
### NifTi Data Format
Neuroimaging Informatics Technology Initiative <br>
http://nifti.nimh.nih.gov/ <br>
http://nipy.org/nibabel/
