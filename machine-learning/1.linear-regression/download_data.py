import urllib
import os
import requests
import sys
import argparse
class Cfg(object):
  
    def __init__(self):
        super(Cfg, self).__init__()
        self.data_urls = ["https://github.com/DatacollectorVN/Frameworks-Machine-Learning/releases/download/5/Iris.xls", 
                          "https://github.com/DatacollectorVN/Frameworks-Machine-Learning/releases/download/6/insurance.csv"]
    
    def down_data(self, destination_dir, data_type):
        assert data_type != None, "Datatype can't be None"

        if 'iris' in data_type:
            data_url = self.data_urls[0]
        elif 'insurance' in data_type:
            data_url = self.data_urls[1]

        print ('Start to download, this process take a few minutes')

        destination = os.path.join(destination_dir, data_url.split('/')[-1])
        urllib.request.urlretrieve(data_url, destination)
        print("Downloaded dataset - {} to- '{}'".format(data_url, destination))

def main(destination_dir, data_type=None):
    cfg = Cfg()
    cfg.down_data(destination_dir = destination_dir, data_type = data_type)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dest', help= 'Destination to save model', type= str,
                        default= './dataset/', dest = 'dest')
    parser.add_argument('--data_type', help= 'data_type for downloading', type= str,
                        default= None, dest = 'data_type')

    args = parser.parse_args()
    os.makedirs(args.dest, exist_ok = True)
    main(destination_dir = args.dest, data_type = args.data_type)
