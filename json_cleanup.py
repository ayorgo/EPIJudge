import sys
import re

json = ''.join(sys.stdin.readlines())

json = re.sub(r'"C\+\+[\s\S]*?},\s*', '', json)
json = re.sub(r'"Java[\s\S]*?},\s*', '', json)

print(json)
