#!/usr/bin/python2

# HSU

from apiclient.discovery import build
import argparse

def cse_search(query,engineId,apiKey,start=1,total=10,searchImage=False):
    service = build('customsearch', 'v1', developerKey=apiKey)
    cnt=0
    resList = []
    while cnt < total:
        num = min(10,total-cnt)
        # image search
        if searchImage: 
            res = service.cse().list(
                q=query,
                cx=engineId,
                searchType='image',
                imgColorType='color',
                start= start,
                num=num
                ).execute()
        # web search
        else: 
            res = service.cse().list(
                q=query,
                cx=engineId,
                start= start,
                num=num
                ).execute()
        start = start + num
        cnt = cnt + num
        resList.append(res)
        for i in range(len(res[u'items'])):
            print(res[u'items'][i][u'link'])
    return resList
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('query',help="query string")
    parser.add_argument('-n',help="number of results to return [10]",type=int,default=10)
    parser.add_argument('-i','--image',help="search images [False]",action='store_true',default=0)
    parser.add_argument('-k','--key-file',help="file storing API key [googleapi.key]",default='googleapi.key');
    args = parser.parse_args()
    
    # 100 results at most
    if args.n >100:
        raise ValueError("Google Custom Search Engine returns at most 100 results for each query")
    
    # read key from file
    key_file = open(args.key_file,'r')
    engineId = key_file.readline().rstrip()
    apiKey = key_file.readline().rstrip()
    key_file.close()
    
    res = cse_search(query=args.query,total=args.n,searchImage=args.image,engineId=engineId,apiKey=apiKey)

if __name__ == '__main__':
  main()
