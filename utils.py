import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print(f'Creating project {directory}')
        os.makedirs(directory)

create_project_dir('testsite')