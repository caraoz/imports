import requests
import zipfile
import os

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open("data/"+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename


for year in range(1990,2016+1):
	year = str(year)
	yearzipURL = "http://www.bls.gov/cew/data/files/"+year+"/csv/"+year+"_qtrly_singlefile.zip"
	print(yearzipURL)
	dlFile = download_file(yearzipURL)
	print(dlFile)
	with zipfile.ZipFile("data/"+dlFile,"r") as zip_ref:
		zip_ref.extractall("data")
	try:
		os.remove("data/"+dlFile)
	except OSError:
		pass
	print("removed","data/"+dlFile)


