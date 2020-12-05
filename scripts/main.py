from datetime import datetime
import os

print("PRINT FROM PYTHON: ACTION 1.2 - STARTED")

home_dir =os.environ['HOME']
username = os.environ['USER']
print(f'{username} home directory is {home_dir}')

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('log.md', 'w') as f:
    f.write(f'# {timestamp}')
    
print("PRINT FROM PYTHON: ACTION 1.2 - COMPLETED")
