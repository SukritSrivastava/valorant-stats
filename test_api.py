import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("HENRIK_API_KEY") 

HEADERS = {"Authorization": API_KEY}

name = input("Enter Valorant Name: ")
tag = input("Enter Tag (without the #): ")

url = f"https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}"
response = requests.get(url, headers=HEADERS)

if response.status_code == 200:
    api_data = response.json()
    player_info = api_data["data"]
    account_level = player_info["account_level"]
    region = player_info["region"]
    puuid = player_info["puuid"]
    
    print(f"\n--- Player Found: {name}#{tag} ---")
    print(f"Account Level: {account_level}")
    print(f"Region: {region.upper()}")
    print(f"PUUID: {puuid}")
else:
    print(f"Oops! Something went wrong. Error code: {response.status_code}")