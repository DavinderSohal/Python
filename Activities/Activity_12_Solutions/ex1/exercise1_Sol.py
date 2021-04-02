import re
data = '''
Apr 12, 5:00, S=70%
APR 14, 6:30, S=60%  
#Server restarts
Apr 14, 6:35, S=15%
#Holiday
APR 16, 13:35, S=80%
May11, 15:22, S=14%
This is a test line
'''

pattern = re.compile("^([a-zA-Z]+) ?([0-9]+)[, ]*[0-9:]+[^,]+, ?S=([-0-9]+)d?[$%]")

for data_line in data.split('\n'):
    match = pattern.match(data_line)
    
    if match:
        print(data_line)
    