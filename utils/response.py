from rest_framework.response import Response

def getTemplate():
    data = {
        "status":"error"
    }
    return data

def AssertionErrorResponse(msg):
    message = msg.split('::')
    resp = getTemplate()
    resp['message'] = message[0]
    return Response(resp, status = int(message[1]))

def BadRequestResponse(msg=None):
    resp = getTemplate()
    resp['error'] = "Bad Request"
    if msg:
        resp['message'] = msg
    return Response(resp, status = 400)

def NotFoundResponse(msg=None):
    resp = getTemplate()
    resp['error'] = "Not Found"
    if msg:
        resp["message"] = msg
    return Response(resp, status = 404)