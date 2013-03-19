# -*- coding: utf-8 -*-
from django.http import HttpResponse
import requests
import xmltodict
import json


def cleanCollections(dataDict):
    for key in dataDict:
        if key == "StatementCodes":
            dataDict[key] = dataDict[key]["StatementCode"]
        elif key == "Statements":
            dataDict[key] = dataDict[key]["Statement"]
        elif key == "GradeLevels":
            dataDict[key] = dataDict[key]["GradeLevel"]
    return dataDict


def index(request, coreString=None):
    if not coreString is None:
        coreString = coreString.strip("/")
        r = requests.get("http://www.corestandards.org/"+coreString+".xml")
        if r.status_code is 200:
            d = xmltodict.parse(r.text)
            if not 'page' in d:
                d["LearningStandards"] = d["LearningStandards"]["LearningStandardItem"]
                d["meta"] = {}
                if type(d["LearningStandards"]) is list:
                    for i in range(len(d["LearningStandards"])):
                        print i
                        d["LearningStandards"][i] = cleanCollections(d["LearningStandards"][i])
                    d["meta"]["count"] = len(d["LearningStandards"])
                else:
                    d["LearningStandards"] = cleanCollections(d["LearningStandards"])
                d["meta"]["requested_standard"] = coreString
                d["meta"]["copyright"] = u"© Copyright 2010. National Governors Association Center for Best Practices and Council of Chief State School Officers. All rights reserved."
            else:
                d = {"error": "Could not find common core standard: "+coreString}
        else:
            d = {"error": "Request error"}
    else:
        coreString = "None"
        d = {"error": coreString+" is not a Common Core standard."}

    return HttpResponse(json.dumps(d), content_type='application/json')
