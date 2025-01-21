import json as js
from pathlib import Path
import os,fire
#Helper to convert json from academic tracker into a bibtex file
#Author: Jake Bergquist

def logInfo(message,logFile=None):
	'''
	I know I know I know that logging exists, but it is so finnicky
	and I got frustrated
	So here we are with my own simple logger
	'''
	print(message)
	if logFile is not None:
		with open(logFile, "a") as log:
			log.write(message)


def stringCleaner(inStr):
	#cleans up common artifacts from the academic tracker
	removeList = ['...']
	for rm in removeList:
		inStr=inStr.replace(rm,'')
	replaceDict={}
	for k in replaceDict.keys():
		inStr=inStr.replace(k,replaceDict[k])
	return inStr

def jsonAuthorToBibtex(authors):
	authorString = ''
	for author in authors:
		authorString+=f'{author['initials']} {author['lastname']} and '
	authorString = authorString[:-4]
	authorString = bibFieldFormat(authorString,'author')
	return authorString

def bibFieldFormat(inStr,name,clean=False):
	if clean:
		inStr = stringCleaner(inStr)
	inStr = bibBracketWrap(inStr)
	if len(name)<4:
		name = name + '\t'
	inStr = name + '\t=\t' + inStr
	return inStr

def bibBracketWrap(inStr):
	if inStr is None:
		inStr = ''
	if type(inStr) is list:
		inStr = ', '.join(inStr)
	return "{" + inStr + "}"

class pub:
	def __init__(self,key,title,authors,journal,year,pubType,otherFields):
		self.pubKey=key
		self.authors=authors
		self.title=title
		self.journal=journal
		self.year=year
		self.pubType=pubType
		self.fields = ['title','authors','year','journal']
		[print(f'Adding {field}') for field in self.fields]
		for key in otherFields.keys():
			print(f'adding {key}')
			setattr(self,key,otherFields[key])
			self.fields.extend([key])
		print(f'Publication set up with these fields: {self.fields}')

	
	@classmethod
	def from_json_dict(cls,pubDict):
		firstAuthor = pubDict['authors'][0]
		authorKey = firstAuthor['lastname'][0:3]
		year = f"{pubDict['publication_date']['year']}"
		date = f"{year}-{pubDict['publication_date']['month']}"

		pubKey = authorKey+year
		title 	= bibFieldFormat(pubDict['title'], 'title')
		authors = jsonAuthorToBibtex(pubDict['authors'])
		journal = bibFieldFormat(pubDict['journal'],'journal',True)
		year 	= bibFieldFormat(year, 'year')
		#other fields:
		doi 	= bibFieldFormat(pubDict['doi'], 'doi')
		date 	= bibFieldFormat(date, 'date')
		pmid 	= bibFieldFormat(pubDict['pubmed_id'], 'pmid')
		pmcid 	= bibFieldFormat(pubDict['PMCID'],'pmcid')
		grants 	= bibFieldFormat(pubDict['grants'], 'grants')

		otherFields = dict(zip(['doi','date','pmid','pmcid','grants'],[doi,date,pmid,pmcid,grants]))
		pubType = 'article'
		if "proceedings" in title.lower():
			pubType = 'InProceedings'
		return cls(pubKey,title,authors,journal,year,pubType,otherFields)








	def __str__(self):
		baseStr = "@" + self.pubType + "{" + self.pubKey + ",\n"
		for field in self.fields:
			baseStr += f'\t{getattr(self,field)},\n'
		baseStr=baseStr[:-2]#remove last comma
		baseStr+='\n}\n'
		return baseStr

	def __repr__(self):
		return self.__str__()



def convertJson(inFile,outFile='out.bib',keyPrefix="SCI:"):
	print(f'Loading {inFile}')
	with open(inFile) as f:
		inputData = js.load(f)
	Path(outFile).touch()
	with open(outFile,'w') as f:
		f.write('')
	for pubId in inputData.keys():
		print(f"working on {pubId}")
		pubDict = inputData[pubId]
		currentPublication = pub.from_json_dict(pubDict)
		currentPublication.pubKey =keyPrefix + currentPublication.pubKey
		with open(outFile,'a') as f:
			f.write(str(currentPublication))
		



if __name__=="__main__":
	fire.Fire({'convert':convertJson})