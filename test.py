import os.path as pth
from workflow import Workflow
import thunder
import nibabel as nbl

from pyspark import SparkContext

sc = SparkContext()

datapath = pth.join(pth.dirname(pth.realpath(thunder.__file__)), 'utils/data/fish/images')
#data = nbl.load("/home/user/Dev/fMRI/bold_dico.nii").get_data()

flow1 = Workflow(datapath, sc).extract().visualize().clustering(k=5).visualize().visualizeBrain()

flow1.execute()