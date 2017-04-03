## Google CSE API

1. Make sure the dependencies are met:
  * latest version of Python2
  * pip

2. Install Google APIs Client Library for Python: 
  ```
  sudo pip install --upgrade google-api-python-client
  ```
(For more details, see: https://developers.google.com/api-client-library/python/start/installation)

3. Create a basic search engine using the Control Panel (http://www.google.com/cse/manage/all). In "Basic" tab, switch on "Image search" and "Search the entire web but emphasize included sites" (the "included sites" can be empty). Put "Search engine ID" on the first line of "googleapi.key". 
4. Create API key: Create a project at Google Developers Console (https://console.developers.google.com/). Turn on "Custom Search API". APIs & auth > Credentials > Public API access > create new Key > Server key > API KEY. Put API Key on the second line of "googleapi.key". 

## Bing Search API

> Note that Microsoft Azure DataMarket WebSearch API has been deprecated since Dec. 15 2016. Please check [bing/ms_congnitive_image_download.py](https://github.com/suhangpro/search-api-wrapper/blob/master/bing/ms_congnitive_image_download.py) for an example using the newer [Microsoft Cognitive Services](https://www.microsoft.com/cognitive-services). 


1. Make sure the dependencies are met:
  * latest version of Python2
  * pip

2. Install Requests (https://github.com/kennethreitz/requests): 
  ```
  sudo pip install --upgrade requests
  ```
3. Sign up for Bing Search API at https://datamarket.azure.com/dataset/bing/search 
4. Copy API key (https://datamarket.azure.com/account/keys) to "bingapi.key". 

