from pyspark import SparkConf, SparkContext
from thunder import ThunderContext

def getContext():
    sc = SparkContext()
    thunderContext = ThunderContext(sc)

    return thunderContext