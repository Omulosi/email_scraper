import json
from datetime import timedelta
from redis import  StrictRedis

class Cache:
    def __init__(self,
                 client=None,
                 expires=timedelta(days=60), encoding='utf-8'):
        self.client = client
        if client is None:
            self.client = StrictRedis(host='localhost', port=6379, db=0)
        self.expires = expires
        self.encoding = encoding

    def __getitem__(self, email):
        """Load email from redis"""
        record = self.client.get(email)
        if record:
            return json.loads(record.decode(self.encoding))
        else:
            raise KeyError(email + ' does not exist')

    def __setitem__(self, email, value):
        """Save email in redis"""
        data = bytes(json.dumps(value), self.encoding)
        self.client.setex(email, self.expires, data)


