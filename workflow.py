import logging
from thunder import ThunderContext
from thunder.clustering.kmeans import KMeans

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s',
                    filename="./fmriFlow.log")


class Workflow(object):
    """
        A Workflow describes a set of operators which will be executed
        sequentially. Each operator of the workflow takes as input
        operand the result of the parent operator and outputs the
        result as input to the child operator.

        [Input Data] => [Parent Operator] => [Result] => [Child Operator] => ....

    """
    def __init__(self, dataSource, sc):
        self.context = ThunderContext(sc)
        self.root = DataSource(dataSource, self.context)
        self.last = self.root

    # Adds a node to the workflow
    def addNode(self, node):
        node.input = self.last.result
        node.parent = self.last
        self.last.child = node
        self.last = node

    # Clustering with K-Means
    def clustering(self, k):
        self.addNode(NeuronClustering(self.last, k))
        return self

    # Feature Extraction
    def extract(self):
        self.addNode(FeatureExtractor(self.last))
        return self

    # Data visualization with matplotlib
    def visualize(self):
        self.addNode(Visualizer(self.last))
        return self

    # Workflow execution
    def execute(self):
        self.root.doExecute()

    # Returns the workflow execution plan as a string
    def explain(self):
        logging.info("Explain")
        cur = self.root
        st = ''
        while cur:
            st += "OPERATOR: %s => INPUT [%s] => RESULT [%s]\n"%(cur.name, type(cur.input), type(cur.result))
            cur = cur.child

        return st


class WorkflowNode(object):
    def __init__(self, parent):
        self.parent = parent
        self.name = None
        self.child = None
        self.input = parent.result
        self.result = None

    def doExecute(self):
        logging.info("Executing: %s"%(self.name))
        self.execute()
        if self.child:
            self.child.doExecute()

    def execute(self):
        pass

    def hasNext(self):
        pass


""" Operators """


class DataSource(WorkflowNode):
    def __init__(self, data, context):
        super(DataSource, self)
        self.name = "Datasource"
        self.parent = None
        self.dataPath = data
        self.input = None
        self.result = context.loadImages(data)


class FeatureExtractor(WorkflowNode):
    def __init__(self, parent):
        super(FeatureExtractor, self).__init__(parent)
        self.name = "FeatureExtractor"
        self.result = 'Features'

    def execute(self):
        self.result = self.parent.result.toTimeSeries()
        #self.child.execute()


class NeuronClustering(WorkflowNode):
    def __init__(self, parent, k):
        super(NeuronClustering, self).__init__(parent)
        self.name = "Clustering"
        self.result = 'Centers'
        self.k = k

    def execute(self):
        model = KMeans(self.k)
        self.result = model.fit(self.parent.result).centers


class Visualizer(WorkflowNode):
    def __init__(self, parent):
        super(Visualizer, self).__init__(parent)
        self.name = "Visualizer"
        self.result = self.parent.result

    def execute(self):
        import seaborn as sns
        import matplotlib.pyplot as plt
        from matplotlib.colors import ListedColormap
        cmapCat = ListedColormap(sns.color_palette("hls", 10), name='from_list')
        plt.gca().set_color_cycle(cmapCat.colors)

        if self.parent.name is "FeatureExtractor":
            plt.plot(self.parent.result.subset(nsamples=10, thresh=0.9).T)
        elif self.parent.name is "Clustering":
            plt.plot(self.parent.result.T)
        plt.show()