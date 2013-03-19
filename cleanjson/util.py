import json
from django.http import HttpResponse


def recursive_clean(data):
    if type(data) is dict and 'fields' in data:
        data['fields']['pk'] = data['pk']
        data['fields']['model'] = data['model']
        data = data['fields']
        for item in data:
            data[item] = recursive_clean(data[item])
            pass
    elif type(data) is list:
        for i in range(len(data)):
            data[i] = recursive_clean(data[i])
            pass

    return data


def clean_serialized_model(data, meta=None):
    data = json.loads(data)

    if data is None or len(data) <= 0:
        return None

    data = recursive_clean(data)
    if len(data) is 1:
        data = data[0]

    outDict = {"data": data}
    if not meta is None:
        outDict['meta'] = meta

    return json.dumps(outDict)


def jsonResponse(request, data):
    meta = {
        'type': request.method,
        'ajax': request.is_ajax()
    }
    data = clean_serialized_model(data, meta)
    if 'callback' in request.GET:
        data = request.GET['callback'] + '(' + data + ')'
    return HttpResponse(data, content_type='application/json')
