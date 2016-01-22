import os.path as pth
import thunder
import utils

from workflow import Workflow

from pyspark import SparkContext

sc = SparkContext()

#data = pth.join(pth.dirname(pth.realpath(thunder.__file__)), 'utils/data/fish/images')
data = utils.readNifti("/home/vic/Dev/fMRI/bold_dico.nii")[:,:,:,:100]


flow1 = Workflow(data, sc)\
      .extract()\
      .visualize()\
      .clustering(12)\
      .visualize()\
      .visualizeBrain()

print "\n=====PLAN====\n" \
      "%s" \
      "=====PLAN=====\n"%flow1.explain()

flow1.execute()
