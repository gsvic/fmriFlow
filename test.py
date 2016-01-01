import os.path as pth
from workflow import Workflow
import thunder
from pyspark import SparkContext

sc = SparkContext()
datapath = pth.join(pth.dirname(pth.realpath(thunder.__file__)), 'utils/data/mouse/images')

flow1 = Workflow(datapath,sc).extract().clustering(k=5).visualize()
flow2 = Workflow(datapath, sc).extract().visualize()

print flow1.explain()
print flow2.explain()

flow1.execute()

print "END"