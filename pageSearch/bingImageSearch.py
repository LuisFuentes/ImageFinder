# Import general web http libs
import httplib, urllib, base64
# Import sub key to use to fetch images from bing
from pageSearch import ocpApimSubscriptionKey

headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
    'Ocp-Apim-Subscription-Key': ocpApimSubscriptionKey,
}

def imageSearch(params=None):
    if params is None:
        params = urllib.urlencode({
            # Request parameters
            'q': 'forza horizon 3',
            'count': '10',
            'offset': '0',
            'mkt': 'en-us',
            'safeSearch': 'Moderate',
        })

    try:
        conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("POST",
                "/bing/v5.0/images/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
