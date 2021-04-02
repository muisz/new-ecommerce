def checkIfExist(cls, **kwargs):
    try:
        response = cls.objects.get(**kwargs)
        return response
    except:
        return False