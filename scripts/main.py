from datetime import datetime

print("PRINT FROM PYTHON: ACTION 1.2 - STARTED")

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
tt = github.event.inputs.version
print('tt is', tt)

with open('log.md', 'w') as f:
    #f.write(f'# {timestamp}')
    f.write(f'# {tt}')
    
print("PRINT FROM PYTHON: ACTION 1.2 - COMPLETED")
