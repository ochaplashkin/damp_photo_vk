import vk
import os
import sys
import urllib.request

SETTINGS = {}

def setup():
	if len(sys.argv) <= 2:
			print("WARNING: missing 2(or 1) required positional arguments: 'token' and 'peer_id'")
			print("Please, restart this script: python3 main.py your_token your_peer_id [name_folder] ")
			print("[name_folder] - optional argument")
			exit(0)
			
	SETTINGS['token'] = sys.argv[1]
	SETTINGS['peer_id'] = sys.argv[2]
	SETTINGS['folder'] = sys.argv[3] if len(sys.argv) > 3 else "photos"
		
	try:
		os.mkdir(SETTINGS['folder'])
	except OSError:
		print("LOGGER: directory " + SETTINGS['folder'] + " already created")
	os.chdir(SETTINGS['folder'])

	
def download_and_save(url,k):
	try:
		file_name = "photo" + "_" + str(k) + ".jpg"
		urllib.request.urlretrieve(url, file_name)
		print(file_name + "......... ok")
	except Exception as inst:
		print (file_name + " : " + inst)
		print("URL: " + url)
	
	
def parse():
	session = vk.Session(access_token=SETTINGS['token'])
	api = vk.API(session, v="5.80")
	
	content = api.messages.getHistoryAttachments(peer_id=SETTINGS['peer_id'],media_type="photo",count=200)
	
	counter = 0
	while True:
		for item in content['items']:
			for size in item['attachment']['photo']['sizes']:
				if size['type'] == 'z':
					download_and_save(size['url'], counter)
					counter+=1
		if 'next_from' in content:
			content = api.messages.getHistoryAttachments(peer_id=SETTINGS['peer_id'],media_type="photo",start_from=content['next_from'],count=200)
		else:
			break
	print("Done")

if __name__ == "__main__":
	setup()
	parse()