import os
import requests
import bs4


# Telecharge les photos de Wordpress
def download_model(url, dirname, tag='img'):
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text)
    for img in soup.find_all('img'):
        src = img.get('src')
        if img.has_attr('width') and src.endswith('.jpg'):
            req = requests.get(img.get('src'))
            fpath = os.path.join(dirname, os.path.basename(src))
            with open(fpath, 'wb') as f:
                for chunk in req.iter_content(256):
                    f.write(chunk)


def download_model_list(url_list, dirpath):
    for url in url_list:
        pic_set = url.split('/')[-2]
        dname = ' '.join([x.title() for x in pic_set.split('-')])
        dd = os.path.join(dirpath, dname)
        os.mkdir(dd)
        download_model(url, dd)


# Telecharge les photos avec .php extension
def build_links(url, tagname):
    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text)
    links = []
    for x in soup.find_all('a'):
        href = x.get('href')
        if href.endswith('.php'):
            link = href.replace('.php', '.jpg')
            links.append((os.path.join(url, link), link))
    return links


def download_links(dirpath, links):
    for link, fname in links:
        dlreq = requests.get(link, stream=True)
        with open(os.path.join(dirpath, fname), 'wb') as f:
            for chunk in dlreq.iter_content(256):
                f.write(chunk)


def batch_download(url_list, dirpath, tagname):
    """Telecharge les photos avec .php extension
    
    Args:
        url_list (TYPE): Description
        dirpath (TYPE): Description
        tagname (TYPE): Description
    
    Returns:
        TYPE: Description
    """
    for url in url_list:
        links = build_links(url, tagname)
        child_dir_name = ' '.join([x.title() for x in url.split('/')[-2].split('_')])
        dpath = os.path.join(dirpath, child_dir_name)
        os.mkdir(dpath)
        download_links(dpath, links)


if __name__ == '__main__':
    dirpath = '/Users/mero/Downloads'
    url_list_wp = []
    # batch_download(url_list_wp, dirpath, 'a')
    download_model_list(url_list_wp, dirpath)
