# BaseCRM Deal Exporter
# The MIT License (MIT)
# Copyright (c) 2014 Michael Barnard, hi@michaelbarnard.info


import urllib2
import json
import csv

#Function to write the data to csv
def writeToCsv(file,data):
    for data in data:
        file.writerow([data["deal"]["id"],
                data["deal"]["stage_name"],
                data["deal"]["name"],
                data["deal"]["user_name"],
                data["deal"]["deal_account"]["name"],
                data["deal"]["scope"],
                ])


#Enter you BaseCRM API token (found at https://app.futuresimple.com/settings/account)
baseAPIToken = ""

#sets required variables
baseurl = "https://sales.futuresimple.com/api/v1/deals.json?"
headers = { 'X-Futuresimple-Token' : baseAPIToken }
file = csv.writer(open("baseDeals.csv", "a"))
stages = ['incoming', 'qualified', 'quote', 'custom1', 'custom2', 'custom3', 'closure', 'won', 'lost', 'unqualified']


# Write CSV Headers
file.writerow(["id", "stage_name", "name", "consultant","client","value"])


for stage in stages:
    stage = stage
    page = 1
    req = urllib2.Request(baseurl + "page="+str(page)+"&stage="+stage, None, headers)
    data = json.loads(urllib2.urlopen(req).read())
    while (data <> []):
        print baseurl + "page="+str(page)+"&stage="+stage
        req = urllib2.Request(baseurl + "page="+str(page)+"&stage="+stage, None, headers)
        data = json.loads(urllib2.urlopen(req).read())
        writeToCsv(file,data)
        page = page + 1
    print stage+" exported"
print "base deals exported to csv"


# The MIT License (MIT)
# Copyright (c) 2014 Michael Barnard, hi@michaelbarnard.info
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.