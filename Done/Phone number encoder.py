#  Q18
import re

a = re.compile('[0-9]{4}[^-]')
b = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

c = a.sub('****\n', b)
print(c)
