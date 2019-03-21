import sys
import numpy as np
from node_sorter import swc_node_sorter
from node_sorter import findchildren

path = sys.argv[1]

swc_node_sorter(path)