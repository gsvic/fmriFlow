"""
main.py

Used to execute operators from bash using sbin/run.sh
"""

import pickle
import argparse
import utils
import nibabel as nbl

from workflow import Workflow
from pyspark import SparkContext

""" Argument Parsing"""
parser = argparse.ArgumentParser(description="fMRI Flow: Neuroimaging with Apache Spark and Python")
parser.add_argument('--path', metavar='p', help="The data path")
parser.add_argument('--operator', metavar='o', help='The operator to be executed')
parser.add_argument('--model', metavar='m', help='A serialized model')
parser.add_argument('--vector', metavar='v', help='An input vector')
parser.add_argument('--k', metavar='k', help='k parameter for K-Means')
parser.add_argument('--nsamples', metavar='ns', help='The number of samples')

args = parser.parse_args()



""" Initial Workflow definition """
if args.path:
    sc = SparkContext()
    data = nbl.load(args.path).get_data()[:,:,:,:100]
    flow = Workflow(data, sc).extract()

op = args.operator

if op == "vb":
    flow = flow.visualizeBrain()

elif op == "v":
    nsamples = args.nsamples
    flow = flow.visualize(nsamples=int(nsamples))

elif op == "vc":
    k = args.k
    flow = flow.clustering(int(k)).visualize()

elif op == "ts":
    k = args.k
    flow = flow.clustering(int(k))
    flow.execute()
    with open("model", "a+") as output:
        pickle.dump(flow.last.result, output, pickle.HIGHEST_PROTOCOL)
        exit("Model Saved")

elif op == "pr":
    utils.predict(args.model, args.vector)
    exit()

else:
    exit("Operator not found")

flow.execute()
