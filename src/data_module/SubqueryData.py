import requests
import json
from .fixture import historyElements_by_address, historyElement_by_id


class SubqueryData:
    url = ""
    address = ""
    history_elements = []

    def __init__(self, url, address):
        self.url = url
        self.address = address

    def getHistoryList(self):
        query = json.dumps(historyElements_by_address(self.address))
        data = self.__send_request(self.url, query)
        return json.loads(data.text)

    def getHistoryElement(self, id):
        query = json.dumps(historyElement_by_id(id))
        data = self.__send_request(self.url, query)
        return data.text

    def fetchHistory(self):
        history_list = self.getHistoryList()
        for element in history_list['data']['historyElements']['edges']:
            data = element['node']
            self.history_elements.append(data)

    def __send_request(self, url, data):
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': 'd5a1d1cffde69e7cbff6d9c0cf1cca6d'
        }
        return requests.request("POST", url, headers=headers,
                                data=data)
