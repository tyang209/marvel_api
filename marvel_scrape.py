import requests
import hashlib, time, json
import glob
from datetime import datetime


def createMarvelRequest():

	apiKeyPublic = 'acdc3d46f60c2e1d7fcf9849710b18d0'
	apiKeyPrivate = '8d00a10c3178e831755efe99d8bd7fa303597aca'


	chararcter_url_root = 'http://gateway.marvel.com:80/v1/public/characters?'
	# limit=100&

	for x in range(1,17): #there are just over 1400 characters as of 05/31/2014
		m= hashlib.md5()	
		offset = 'offset=' + str((x)*100)
		limit = 'limit=100&'
		
		dt = datetime.now()
		ts = str(dt.microsecond)

		m.update(ts+apiKeyPrivate+apiKeyPublic)
		hashkey = m.hexdigest()

		url = chararcter_url_root + limit 
		if (x!=1):
			url=url+offset
	
		api_parameters = {
					'ts': ts,
					'apikey': apiKeyPublic,
					'hash': hashkey
					}
			
		req = requests.request('GET', url,params=api_parameters)
		print req.url
		downloadMarvelJSON(req, x*100)		


def downloadMarvelJSON(apiRequest, charNumber):
	data =  apiRequest.json()
	# data = json.load(apiRequest.json())
	fileName = 'marvelCharacters' +str(charNumber)	+'.json'
	with open (fileName,'wb') as outfile:
		json.dump(data, outfile)

def checkDataExists(jsonFile):
	pass

def readJsonFile(fileName):

	json_data=open(fileName)	
	data = json.load(json_data)
	return data

def returnAllCharacters():
	fileList = glob.glob('marvelCharacters*.json')
	characterArray = []
	resultArray = []
	for x in fileList:
		characterArray.append(readJsonFile(x))
	for x in characterArray:
		
		for result in x['data']['results']:
			resultArray.append(result)
	
	character_dict = {'filetype':'characters',
						'results': resultArray}
	json_characters = json.dumps(character_dict)
	return json_characters


def returnAllCharacterID():

	json_data = open('allCharacterJSON.json')

	data = json.load(json_data)
	characterList =[]
	for x in data['results']:
		characterList.append(x['id'])

	return characterList

def pullAllComics(characterIDs):

	apiKeyPublic = 'acdc3d46f60c2e1d7fcf9849710b18d0'
	apiKeyPrivate = '8d00a10c3178e831755efe99d8bd7fa303597aca'
	chararcter_url_root = 'http://gateway.marvel.com:80/v1/public/characters?'
		# limit=100&

	for x in range(1,17): #there are just over 1400 characters as of 05/31/2014
		m= hashlib.md5()	
		offset = 'offset=' + str((x)*100)
		limit = 'limit=100&'
		
		dt = datetime.now()
		ts = str(dt.microsecond)

		m.update(ts+apiKeyPrivate+apiKeyPublic)
		hashkey = m.hexdigest()

		url = chararcter_url_root + limit 
		if (x!=1):
			url=url+offset
	
		api_parameters = {
					'ts': ts,
					'apikey': apiKeyPublic,
					'hash': hashkey
					}
			
		req = requests.request('GET', url,params=api_parameters)
		print req.url
		downloadMarvelJSON(req, x*100)		