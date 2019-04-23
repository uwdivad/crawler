import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print(f'Creating project {directory}')
        os.makedirs(directory)

def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

def write_file(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()

def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def delete_file_contents(path):
    with open(path, 'w'):
        pass

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.strip())

def set_to_file(link_set, file):
    delete_file_contents(file)
    for link in sorted(link_set):
        append_to_file(file, link)