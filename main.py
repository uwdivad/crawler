import threading
from queue import Queue
from spider import Spider
from domain import *
from utils import *

PROJECT_NAME = 'theparticle'
HOMEPAGE = 'http://theparticle.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = f'sites/{PROJECT_NAME}/queue.txt'
CRAWLED_FILE = f'sites/{PROJECT_NAME}/crawled.txt'
NUMBER_OF_THREADS = 8

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target=work)
        thread.daemon = True
        thread.start()

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(f'{str(len(queue_links))} links in the queue')
        create_jobs()

if __name__ == "__main__":
    create_workers()
    crawl()