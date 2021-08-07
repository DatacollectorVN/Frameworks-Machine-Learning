import urllib
import os
import requests
import argparse
class Cfg(object):
  
    def __init__(self):
        super(Cfg, self).__init__()
        self.data_urls = ['https://github.com/DatacollectorVN/Frameworks-Machine-Learning/releases/download/1/sinh_vien_VL.csv']
    
    def down_data(self, destination):
        data_url = self.data_urls[0]
        print ('Start to download, this process take a few minutes')
        urllib.request.urlretrieve(data_url, destination)
        print("Downloaded dataset - {} to-'{}'".format(data_url, destination))

def main(dest):
    cfg = Cfg()
    cfg.down_data(destination = dest)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dest', help= 'Destination to save model', type= str,
                        default= './dataset/')

    args = parser.parse_args()
    os.makedirs(args.dest, exist_ok = True)
    dest = os.path.join(args.dest, 'sinh_vien_VL.csv')
    main(dest= dest)
