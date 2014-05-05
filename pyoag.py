import requests
import json
import re
import time
import urllib

BASE_HEADERS = {'Accept':'application/json'}
SERVICE_URL = 'http://howopenisit.org/lookup/'
DOI_REGEX = re.compile("\\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?![\\/\"&\'<>])\\S)+)\\b")

class Request:
    def __init__(self, query = None,
                 norequest = False,
                 delay = 2,
                 limit = 1000,
                 verbose = False,
                 timeoutdelay = 120):
                 
        self.start_time = time.time()
        self.query = query
        self.delay = delay
        self.querylimit = limit
        self.verbose = verbose
        self.timeoutdelay = timeoutdelay
        
        if query and not norequest:
            response = self.get()
            
    def get(self):
        if not self.query:
            return False

        doilist = self._formatdoilist(self.query)
        batches = self.batch(doilist, self.querylimit)

        response = []
        unmatched = [doi for doi in doilist]
        
        for batch in batches:
            try:
                resp = self._getbatch(batch)
                response.extend(resp)
                returned = [r.get('identifier')[0].get('id') for r in response]
                [unmatched.remove(doi) for doi in returned if doi in unmatched]
                time.sleep(self.delay)

            except requests.exceptions.HTTPError, e:
                print 'HTTPError', e
                time.sleep(self.delay if self.delay < 10 else 10)
                
            except ValueError:
                print response.text
                break

            
        while len(unmatched) > 0 and (self.timeout() == False):
            try:
                unmatcheddois = self.batch(unmatched, self.querylimit)[0]
                resp = self._getbatch(unmatcheddois)
                response.extend(resp)
                returned = [r.get('identifier')[0].get('id') for r in response]
                [unmatched.remove(doi) for doi in returned if doi in unmatched]
                if self.timesincestart() < 60:
                    time.sleep(self.delay)
                else:
                    time.sleep(30)
            except requests.exceptions.HTTPError, e:
                print 'HTTPError', e
                time.sleep(self.delay if self.delay < 10 else 10)
                
            except ValueError:
                print response.text

        print "Successfully obtained OAG response for %s of %s articles" % (
                                                    len(response),
                                                    len(doilist)
                                                                    )

        self.unmatched = unmatched
        self.response = response        
        return response

        
    def _getbatch(self, doibatch):
        """Construct and return a single query for less than 1000 DOIs
        
        :rtype :json
        :param doibatch: iterator containing dois
        """
        
        query = self._formatquery(doibatch)
        url = self._formaturl(query)

        response = requests.post(url, headers = BASE_HEADERS, data = query)
        print "Response Status Code:", response.status_code
        response.raise_for_status()
        return response.json().get('results')


    def _formatdoilist(self, dois):
        """Take input DOIs and convert to a list of DOIs"""
        
        #doilist = DOI_REGEX.findall(','.join(dois))
        doilist = dois
        return doilist
        
    def _formatquery(self, doibatch):
        return json.dumps(doibatch)
        
    def _formaturl(self, query):
        return SERVICE_URL


    def timeout(self):
        """
        Simple function to timeout continuing requests to OAG
        """

        return time.time() > (self.start_time + self.timeoutdelay)
        
    def timesincestart(self):
        return time.time() - self.start_time

    def batch(self, iterator, batchsize):
        numbatches = len(iterator)/batchsize + 1
        batches = []
        for batch in range(numbatches):
            start = batch * batchsize
            stop = (batch+1) * batchsize if (batch+1)*batchsize < len(iterator) else len(iterator)
            batches.append(iterator[start:stop])
        return batches
