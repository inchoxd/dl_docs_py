import requests
import argparse

class dl_docs:
    def dl(self, url, end_page, dl_path=None, start_page=1, z_padding=None):
        if dl_path is None:
            dl_path = './'
        else:
            if dl_path[-1] != '/':
                dl_path = f'{dl_path}/'

        if 'http' not in url:
            return False
            
        splt_url = url.split('.')
        tmp_name = splt_url[-2]
        dl_name = tmp_name.split('/')[-1]
        ext = splt_url[-1]
        dl_path = f'{dl_path}{dl_name}.{ext}'

        r = requests.get(url=url)
        status_code = r.status_code
        if status_code != 200:
            return False
            
        data = r.content
        with open(dl_path, 'wb') as f:
            f.write(data)

        return True
