import json as js
import os,sys,fire
#Helper to convert json from academic tracker into a bibtex file
#Author: Jake Bergquist

class pub:
	def __init__(self,key,authors,journal,date,grants,doi,otherFields):
		self.pubKey=key
		self.authors=authors
		self.journal=journal
		self.date=date
		self.grants=grants
		self.doi=doi
		self.fields = ['authors','date','journal','grants','doi']
		for 

	def __repr__(self):
		return self.__str__()
	@classmethod
	def from_json_dict(cls,dict):
		firstAuthor = pub['authors'][0]
		authorKey = firstAuthor['lastname'][0:3]
		date = pub['publication_date']
		pubKey = keyPrefix+authorKey+self.date['year']

	def __str__(self):
		baseStr = self.pubType + "{" + self.pubKey + "\n"
		for field in self.fields:
			baseStr += f"\t{getattr(self,field)}"
		baseStr+='}'
		return baseStr



def convertJson(inFile,outFile,keyPrefix="SCI:"):
	inputData=js.load(inFile)

	for pubId in inputData.keys():
		currentPublication = pub.from_json_dict(inputData[pubId])
		pubText = formatPub(pub,keyPrefix)



if __name__=="__main__":
