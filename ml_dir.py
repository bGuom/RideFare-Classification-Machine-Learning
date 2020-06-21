

import requests

count = 921
headers = {'User-Agent': 'Mozilla/5.0'}



import csv

with open('train_dist.csv', mode='wb') as dist_file:
    dist_writer = csv.writer(dist_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open('test_.csv','rt')as f:
      data = csv.reader(f)
      for row in data:
            count+=1
            PARAMS = {'wp.0': row[8] + ',' + row[9], 'wp.1': row[10] + ',' +row[11] , 'key':'ArgL4oeKp-O5PNEcJhCu9OmgRa59tdyT6ONMBjJyCFbBEd3hgPyyadVvUfIb0ieu' }
            
            URL = 'https://dev.virtualearth.net/REST/V1/Routes'
            r = requests.get(url = URL, params = PARAMS)
            data = r.json()
            try:
                distance = data['resourceSets'][0]['resources'][0]['travelDistance']
            except:
                distance = 0
            dist_writer.writerow([distance])
            if(count%1000==0): print count

    print 'done..'
        
        


