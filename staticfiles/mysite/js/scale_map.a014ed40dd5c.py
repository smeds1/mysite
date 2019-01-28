#scale the coordinates in the usstates.js file by argv[1] to make the map
#bigger or smaller

import re
import sys

scale = float(sys.argv[1])
file = open('usstates.js')
out = open('usmap.js','w')

for line in file:
    if "{id" in line:
        line = re.sub(r'([\d|.]+),([\d|.]+)',lambda m: str(scale*float(m.group(1)))+','+str(scale*float(m.group(2))),line)
        out.write(line)
    else:
        out.write(line)

out.close()
