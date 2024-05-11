import requests

method_input ='''
def greet(self, name):
        print(f"Hello, {name}!")
'''

url = "http://localhost:8000/summary/invoke/"
data = {
    "input" :
        {
            "method": method_input
        }
    }

response = requests.post(url, json=data)

print(response.json()['output'])