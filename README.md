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

### Define and execute a Workflow
A new workflow can be defined in a Python script just like the example above. In detail:
<ol>
  <li>
    Define the workflow by providing a Spark Context and an input path(.nii file)
    <code>flow1 = Workflow(datapath, sc)</code>
  </li>
  <li>
    Add some operators
    <code>flow1 = Workflow(datapath, sc).extract().clustering(k=5).visualize()</code>
  </li>
  <li>
    Execute the workflow
    <code>flow1.execute()</code>
  </li>
  <li>
    Or print the execution plan
    <code>print flow1.explain()</code>
  </li>
  </ol>
  Currently the available operators are:
  <ul>
    <li>extract(): Extracts features into time series</li>
    <li>clustering(k): K-Means clustering</li>
    <li>visualizeBrain(): Visualizes a specific slice of the brain</li>
    <li>visualize(nsamples): Visualizes nsamples data points</li>
  </ul>

### Bash Commands
It is also possible to execute operations via bash using the scripts in the /scripts folder with the following parameters:
<br>
<code>run.sh</code>
<ul>
  <li><code>--path</code> the input path</li>
  <li><code>--operator</code> the operator</li>
  <li><code>--path</code> the input path</li>
  <li><code>--model</code> a serialized model from previous execution</li>
  <li><code>--vector</code> a neuron-vector to be given as input to the model above in order to compute its corresponding cluster</li>
</ul>
Examples
<ul>
  <li>Train and save a model: <code>sbin/run.sh --path ../bold_dico.nii --operator ts</code>: Runs a K-Means clustering on the input dataset and serializes it in disk</li>
  <li>Load a trained model: <code>sbin/run.sh --operator pr --model model --vector "[...]"</code>: Predicts the cluster center of the input vector using the input model</li>
</ul>
Other Scripts
<ul>
  <li><code>visualizeBrain.sh $INPUT</code></li>
  <li><code>visualizeData.sh $INPUT $NSAMPLES</code></li>
  <li><code>visualizeClusters.sh $INPUT $K</code></li>
</ul>


## Additional Info

###
Understanding fMRI Data
https://www.youtube.com/watch?v=oBDpv2PQX9k

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
