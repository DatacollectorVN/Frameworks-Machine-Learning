import urllib
import os
import requests
import argparse
class Cfg(object):
  
    def __init__(self):
        super(Cfg, self).__init__()
        self.data_urls = ['https://github.com/DatacollectorVN/Frameworks-Machine-Learning/releases/download/5/Iris.xls']
    
    def down_data(self, destination_dir):
        data_url = self.data_urls[0]
        print ('Start to download, this process take a few minutes')

        destination = os.path.join(destination_dir, data_url.split('/')[-1])
        urllib.request.urlretrieve(data_url, destination)
        print("Downloaded dataset - {} to- '{}'".format(data_url, destination))

def main(destination_dir):
    cfg = Cfg()
    cfg.down_data(destination_dir = destination_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dest', help= 'Destination to save model', type= str,
                        default= './dataset/', dest = 'dest')

    args = parser.parse_args()
    os.makedirs(args.dest, exist_ok = True)
    main(destination_dir = args.dest)
