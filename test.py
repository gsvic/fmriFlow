from workflow import Workflow

flow = Workflow("mouse-images").extract().visualize()
print "EXPLAIN\n", flow.explain()
flow.execute()

print "END"