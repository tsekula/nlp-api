import sys
import os
import logging
import json
from flask import Flask
from flask import jsonify
from flask import request
from textblob import TextBlob

app = Flask(__name__)


@app.route('/nlp/pos-tags',methods=['POST','GET'])
def nlp_postags():

    try:
        req_json = request.get_json()
        if req_json is None:

                return jsonify( error = 'this service require A JSON request' )

        else:
                if not ('text' in req_json):
                    raise Exception('Missing mandatory paramater "text"')

        text = req_json['text']
        blob = TextBlob(text)
        posTags = blob.tags

        return json.JSONEncoder().encode(posTags)

    except Exception as ex:
       app.log.error(type(ex))
       app.log.error(ex.args)
       app.log.error(ex)
       return jsonify(error = str(ex))
       
       
@app.route('/nlp/parse',methods=['POST','GET'])
def nlp_parse():

    try:
        req_json = request.get_json()
        if req_json is None:

                return jsonify( error = 'this service require A JSON request' )

        else:
                if not ('text' in req_json):
                    raise Exception('Missing mandatory paramater "text"')

        text = req_json['text']
        blob = TextBlob(text)
        nounPhrases = blob.parse().split()

        return json.JSONEncoder().encode(nounPhrases)

    except Exception as ex:
       app.log.error(type(ex))
       app.log.error(ex.args)
       app.log.error(ex)
       return jsonify(error = str(ex))

@app.route('/nlp/parse-sentences',methods=['POST','GET'])
def nlp_tokenise():

    try:
        req_json = request.get_json()
        if req_json is None:

                return jsonify( error = 'this service require A JSON request' )

        else:
                if not ('text' in req_json):
                    raise Exception('Missing mandatory paramater "text"')

        text = req_json['text']
        blob = TextBlob(text)
        
        processed = {}
        objParsedSentences = []
        
        for sentence in blob.sentences:
        	objSentence = {}
        	objWordsTags = sentence.parse().split()
        	objParsedWords = []
        
        	objSentence['original'] = sentence.raw
        
        	for word in objWordsTags[0]:
        		objWordsTags = {}
        		objWordsTags['text'] = word[0]
        		objWordsTags['tag'] = word[1]
        		objParsedWords.append(objWordsTags)

        	#app.log.info(objParsedWords)

        
        	objSentence['words'] = objParsedWords  # this the problem?
        	objParsedSentences.append(objSentence)
        
        processed['sentences'] = objParsedSentences
        app.log.info(json.dumps(processed))
	    
        return (json.dumps(processed))

    except Exception as ex:
       app.log.error(type(ex))
       app.log.error(ex.args)
       app.log.error(ex)
       return jsonify(error = str(ex))

if __name__ == '__main__':

    LOG_FORMAT = "'%(asctime)s - %(name)s - %(levelname)s - %(message)s'"
    logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT)
    app.log = logging.getLogger(__name__)

    #app.run(host="0.0.0.0",port="8080",debug=False)
    
    app.run(host=os.environ["IP"],port=os.environ["PORT"],debug=False)