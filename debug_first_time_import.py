import time
from viztracer import VizTracer

tracer = VizTracer()
tracer.start()

start_time = time.time()

import torch

end_time = time.time()

tracer.stop()
tracer.save() # also takes output_file as an optional argument

execution_time = end_time - start_time
print(f"Code execution time: {execution_time:.4f} seconds")

# ui.perfetto.dev for analysis.