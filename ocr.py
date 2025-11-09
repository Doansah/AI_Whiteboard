
import requests
import json

'''

PURPOSE:
1) Given a Photo, Extract the 'text' and turn it into LATEX
2) Decide what text should be extracted (ie. random notes versus solution) ignoring for now...

'''
from tkinter import Image

source_url ="made_up_url"

class SolutionAttempt:
    def __init__(self,expressions=[], confidence=1000000):
        self.expressions = expressions
        self.confidence = confidence

    def getExpressions(self):
        return self.expressions

    def getConfidence(self):
        return self.confidence

    def toString(self):
        return str(self.getExpressions().toString(), str(self.getConfidence()))


# Convert returns MathPIX response
def getPhotoData(imageURL):
    r = requests.post("https://api.mathpix.com/v3/text",
                      json={
                          "src": "https://mathpix-ocr-examples.s3.amazonaws.com/cases_hw.jpg",
                          "math_inline_delimiters": ["$", "$"],
                          "rm_spaces": True
                      },
                      headers={
                          "app_id": "APP_ID",
                          "app_key": "APP_KEY",
                          "Content-type": "application/json"
                      }
                      )
    print(json.dumps(r.json(), indent=4, sort_keys=True))
    return r.json()

def buildSolutionAttempt(response)-> SolutionAttempt:
    rawLatex = response.get("latex_styled")
    convertLatexToExpresionList(rawLatex)
    confidence = response.get("confidence")

    solutionAttempt = SolutionAttempt(rawLatex, confidence)

    return solutionAttempt








# in mathpix lines are separated with \n

# String latex_style -> List[] equationLines

'''
params:
numbers_default_to_math: true
rm_spaces

'''



def convertLatexToExpresionList(latexString):
    expressionList = latexString.strip().split('\n')
    print(expressionList) #4 debugging
    return expressionList







