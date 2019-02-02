import json
import webbrowser

class Parsejson:
    def __init__(self, json):
        self.json = json

    def parsejson(self):
        res = str(self.json['payload']['displayName'])
        if res == 'Kyle_Rozanitis':
             webbrowser.open("https://weather.com/")

#/Users/franklin/SSW690/Smart-Home/src/frontEnd/parsejson.py
#
# def main():
#     json = {
#         'payload':{
#             'displayName': 'Kyle_Rozanitis'
#         }
#     }
#     parsejson(json)
#
# if __name__ == '__main__':
#     main()