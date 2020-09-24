# Util Class
# Some functions which are different from Base

class Util():

    # Startswith filter
    def startswith(self, data, query: str):
        result = []

        for doc in data:
            if(doc['key'].startswith(query)):
                result.append(doc)

        return result

# To make dict to an object

class AttrDict():

    def __init__(self, paramdict: dict):
        for key in paramdict:
            setattr(self, key, paramdict[key])
