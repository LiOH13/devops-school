from datetime import datetime
import os

print("PRINT FROM PYTHON: ACTION 1.2 - STARTED")
print(os.name)
print(os.getenv("github.event.inputs.version"))

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('log.md', 'w') as f:
    f.write(f'# {timestamp}')
    
print("PRINT FROM PYTHON: ACTION 1.2 - COMPLETED")
