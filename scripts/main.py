from datetime import datetime
import os

print("PRINT FROM PYTHON: ACTION 1.2 - STARTED")

for a in os.environ:
    print('Var: ', a, 'Value: ', os.getenv(a))
print("all done")

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('log.md', 'w') as f:
    f.write(f'# {timestamp}')
    
print("PRINT FROM PYTHON: ACTION 1.2 - COMPLETED")
