import requests
import argparse
import re

class dl_docs:
    def dl(self, url, end_page=0, dl_path=None, z_padding=False, force=False, trials=0):
        exts = ['.pdf', '.PDF', '.pptx', '.docx', '.png', ',PNG', '.jpg', '.JPG', '.jpeg', '.JPEG']
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
        str_num = re.compile(r'\d+').findall(dl_name)[0]
        ext = splt_url[-1]
        if ext not in exts:
            return False

        if z_padding:
            fills = int(len(str_num))
        else:
            fills = None

        loop_st = True
        start_page = int(str_num)
        while(loop_st or start_page <= end_page):
            if fills:
                str_num = str_num.zfill(fills)
                
            r = requests.get(url=url)
            status_code = r.status_code
            if status_code != 200:

                return False
            
            data = r.content
            with open(dl_path, 'wb') as f:
                f.write(data)

        return True


    def ln_arg(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('url')
