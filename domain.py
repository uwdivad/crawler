from urllib.parse import urlparse

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

def get_domain_name(url):
    try:
        '.'.join(get_sub_domain_name(url).spit('.')[-2::])
    except:
        return ''