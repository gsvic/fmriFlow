from pyspark import SparkConf, SparkContext
from thunder import ThunderContext

def getContext(sc):
    thunderContext = ThunderContext(sc)

    return thunderContext