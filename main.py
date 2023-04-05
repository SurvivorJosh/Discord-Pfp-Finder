
import os 
try:
    from bing_image_downloader import downloader
except:
    os.system("pip install bing-image-downloader")
try:
    import requests, logging
except:
    os.system("pip install requests")
try:
    import asyncio
except:
    os.system("pip install asyncio")
try:
    import base64, random, string
except:
    os.system("pip install base64")

EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif']

def mainHeader(token):
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
        'accept': '*/*',
        'accept-language': 'en-US',
        'Content-Type': 'application/json',
        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
        'Authorization': token,
        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        'X-Discord-Locale': 'en-US',
        'X-Debug-Options': 'bugReporterEnabled',
        'origin': 'https://discord.com',
        'DNT': '1',
        'connection': 'keep-alive',
        'Referer': 'https://discord.com',
        'cookie': f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'TE': 'Trailers',
    }

async def main():
    print()
    print("[!] Random Pfp Changer based on search query\n")
    print("[!] Made by fymjosh#1337")
    print()
    
    
    q = input("Search Query: ")
    limit = int(input("How many images to download?: "))
    token = input("token: ")
    print("""
      [1] Pfp
      [2] Banner
    """)
    dict = input("Choose: ")
    if dict == "1":
        dict = "pfp"
        num = 1
    elif dict == "2":
        dict = "banner"
        num = 0
        ss = f"{q} banner"
    else:
        dict = "pfp"
        num = 1
    
    downloader.download(q, limit=limit, output_dir=dict, adult_filter_off=True, force_replace=False, timeout=50)
   
    if dict == "pfp":
        
        pictures = [i for i in os.listdir(f"pfp/{q}/") if any(i.endswith(ten) for ten in EXTENSIONS)]
        rand_pic = random.choice(pictures)
        img_type = ""
        if rand_pic.endswith('png'):
            img_type = 'png'
        elif rand_pic.endswith('gif'):
            img_type = 'gif'   

        elif rand_pic.endswith('jpg'):
            img_type = 'jpeg'

        else:
            img_type = 'jpeg'
        
        with open(f'pfp/{q}/{rand_pic}', 'rb') as ifile:
            encoded_str = base64.b64encode(ifile.read())
                         
        headers=mainHeader(token)
        json = {
            'avatar': f"data:image/{img_type};base64,{(encoded_str.decode('utf-8'))}",
        }
        r = requests.patch('https://discord.com/api/v10/users/@me', headers=headers, json=json)
        if r.status_code == 200:
            print(f"Succesfully Changed Pfp for [{token}]")
            
        else:
            print(f"Error Changing Pfp | {r.status_code}")
    
    elif dict == "banner":
        
        pictures = [i for i in os.listdir(f"banner/{q}/") if any(i.endswith(ten) for ten in EXTENSIONS)]
        rand_pic = random.choice(pictures)
        img_type = ""
        if rand_pic.endswith('png'):
            img_type = 'png'
        elif rand_pic.endswith('gif'):
            img_type = 'gif'   

        elif rand_pic.endswith('jpg'):
            img_type = 'jpeg'

        else:
            img_type = 'jpeg'
        
        with open(f'banner/{q}/{rand_pic}', 'rb') as ifile:
            encoded_str = base64.b64encode(ifile.read())
                         
        headers=mainHeader(token)
        json = {
            'banner': f"data:image/{img_type};base64,{(encoded_str.decode('utf-8'))}",
        }
        r = requests.patch('https://discord.com/api/v10/users/@me', headers=headers, json=json)
        if r.status_code == 200:
            print(f"Succesfully Changed Pfp")
            
        else:
            print(f"Error Changing banner | {r.status_code}")
            
    await asyncio.sleep(1)
    dicts = [i for i in os.listdir(f"{dict}/{q}/")]
    for d in dicts:
        try:
            os.remove(f"{dict}/{q}/{d}")
        except:
            print("couldn't delete pfps")
    
    direct = f"{dict}/{q}"   
    os.rmdir(direct)
    await asyncio.sleep(1)    
            
    await main()
    
if __name__ == "__main__":
    asyncio.run(main())