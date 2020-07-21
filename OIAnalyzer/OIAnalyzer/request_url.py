
"""
created by @rahulreddy
"""
import requests

def request_page(url,header):
    return requests.get(url,headers=header)