#!/usr/bin/python2

import requests # Get from https://github.com/kennethreitz/requests
import string
import argparse
from py_ms_cognitive import PyMsCognitiveImageSearch  # https://github.com/tristantao/py-ms-cognitive
import urllib, cStringIO
from PIL import Image
import pickle
import os


def get_search_results(search_term, key, num_results):
    # search_service = PyMsCognitiveImageSearch(key, search_term, silent_fail=True)
    search_service = PyMsCognitiveImageSearch(key, search_term)
    if num_results <= 50:
        result_list = search_service.search(limit=num_results, format='json')
    else:
        result_list = search_service.search_all(quota=num_results, format='json')

    return result_list


def save_images(outDir, result_list):
    # get images from the JSON search results and save them

    if not os.path.exists(os.path.join(outDir, 'images')):
        os.makedirs(os.path.join(outDir, 'images'))

    for i, search_result in enumerate(result_list):
        file = cStringIO.StringIO(urllib.urlopen(search_result.content_url).read())
        print search_result.name + '\n'
        img = Image.open(file)
        img_fn = os.path.join(outDir, 'images', str(i)+'.jpg')
        img.save(img_fn)


def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('-q','--query',help="query string")
    parser.add_argument('-n',help="number of results to return [10]",type=int,default=10)
    # parser.add_argument('-i','--image',help="search images [False]",action='store_true',default=0)
    parser.add_argument('-k','--key-file',help="file storing API key [ms-cognitive.key]",default='ms-cognitive.key')
    parser.add_argument('-o','--out-dir',help="output directory for results",default='./data')
    args = parser.parse_args()

    # read key from file
    key_file = open(args.key_file,'r')
    apiKey = key_file.readline().rstrip()
    key_file.close()

    # search results as JSON
    res_list = get_search_results(unicode(args.query,'utf-8'), apiKey, args.n)
    save_images(args.out_dir, res_list)

    # save results JSON list as pickle
    pickle.dump(res_list, open( os.path.join(args.out_dir, "search_result_pickle.p"), "wb" ) )


if __name__ == "__main__":
    main()
