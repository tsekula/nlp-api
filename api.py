import sys
import os
import logging
import json
from flask import Flask
from flask import jsonify
from flask import request
from textblob import TextBlob

text = "The test indicated that the North was developing a more sophisticated engine, South Korean officials said, declining to provide further details. Mr. Stone, a longtime associate of President Trump, is being investigated in connection with Russian interference in the 2016 election."
blob = TextBlob(text)
posTags = blob.tags

processed = {}
objParsedSentences = []


for sentence in blob.sentences:
	objSentence = {}
	objWordsTags = sentence.parse().split()
	objParsedWords = []

	objSentence['text'] = sentence.raw

	for word in objWordsTags[0]:
		objWordsTags = {}
		objWordsTags['text'] = word[0]
		objWordsTags['tag'] = word[1]
		objParsedWords.append(objWordsTags)

	objSentence['words'] = objParsedWords
	objParsedSentences.append(objSentence)

processed['sentences'] = objParsedSentences
	
print (json.dumps(processed))

