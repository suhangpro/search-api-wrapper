#!/usr/bin/python2

import requests # Get from https://github.com/kennethreitz/requests
import string
import argparse

class BingSearchAPI():
    bing_api = "https://api.datamarket.azure.com/Bing/Search/v1/Composite?"
    
    def __init__(self, key):
        self.key = key

    def replace_symbols(self, request):
        # Custom urlencoder.
        # They specifically want %27 as the quotation which is a single quote '
        # We're going to map both ' and " to %27 to make it more python-esque
        request = string.replace(request, "'", '%27')
        request = string.replace(request, '"', '%27')
        request = string.replace(request, '+', '%2b')
        request = string.replace(request, ' ', '%20')
        request = string.replace(request, ':', '%3a')
        return request
        
    def search(self, query, start=1,total=10,searchImage=False):
        if searchImage:
            request_prefix = 'Sources="image"'
        else:
            request_prefix = 'Sources="web"'
        request_prefix += '&Query="'  + str(query) + '"'
        request_prefix += '&$format=json'

        cnt = 0;
        skip = start - 1
        resList = []
        while cnt < total:
            num = min(50,total-cnt)
            request = request_prefix + '&$top=' + str(num) + '&$skip=' + str(skip)
            request = self.replace_symbols(request)
            res = requests.get(self.bing_api+request, auth=(self.key, self.key)).json()
            skip = skip + num
            cnt = cnt + num
            if searchImage:
                for i in range(len(res[u'd'][u'results'][0][u'Image'])):
                    resList.append(res[u'd'][u'results'][0][u'Image'][i][u'MediaUrl'])
            else:
                for i in range(len(res[u'd'][u'results'][0][u'Web'])):
                    resList.append(res[u'd'][u'results'][0][u'Web'][i][u'Url'])
        return resList

def main(): 

    parser = argparse.ArgumentParser()
    parser.add_argument('query',help="query string")
    parser.add_argument('-n',help="number of results to return [10]",type=int,default=10)
    parser.add_argument('-i','--image',help="search images [False]",action='store_true',default=0)
    parser.add_argument('-k','--key-file',help="file storing API key [bingapi.key]",default='bingapi.key');
    args = parser.parse_args()
    
    # 1050 results at most
    if args.n >1050:
        raise ValueError("Bing Search API returns at most 1050 results for each query")
    
    # read key from file
    key_file = open(args.key_file,'r')
    apiKey = key_file.readline().rstrip()
    key_file.close()

    # api call
    bing = BingSearchAPI(apiKey)
    results = bing.search(query=args.query,total=args.n,searchImage=args.image)
    
    # display results
    for url in results: 
        print(url)

if __name__ == "__main__":
    main()
