# add new python file in folder corresponding to year

from datetime import datetime
import os
import sys

import requests
from bs4 import BeautifulSoup

day = datetime.today().day
month = datetime.today().month
year = datetime.today().year

py_text = """# day DAY solutions

\"\"\"
DESCRIPTION
\"\"\"

def qDAYa(inp):
    data = inp.split("\\n")
    return 0


def qDAYb(inp):
    data = inp.split("\\n")
    return 0


if __name__ == "__main__":
    with open("DAYtest.txt", "r") as f:
        data = f.read().strip()
    print("Testing  (a):",qDAYa(data))
    print("Expected (a):",'A_RESPONSE')
    print("Testing  (b):",qDAYb(data))
    print("Expected (b):",'B_RESPONSE')
    with open("DAY.txt", "r") as f:
        data = f.read().strip()
    print("Actual   (a):",qDAYa(data))
    print("Actual   (b):",qDAYb(data))
"""

headers = {
    'authority': 'adventofcode.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'dnt': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': f'https://adventofcode.com/{year}/day/{day}',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6,zh;q=0.5',
    'cookie': 'session=53616c7465645f5fa63be993d0c72deb962bc0aab154047bf62541ff049ef1ebda1e106bd071d683fd589b927ab172c0',
}

if month == 12 and day <= 25:
    with open(f"./{year}/{day:02}.py", "w+") as f:
        f.write(py_text.replace("DAY", f"{day:02}"))
    with open(f"./{year}/{day:02}test.txt", "w+") as f:
        f.write("")
    with open(f"./{year}/{day:02}.txt", "w+") as f:
        f.write("")

    print("Created new files")

    input_url = f"https://adventofcode.com/{year}/day/{day:02}/input"
    response = requests.get(input_url)
    print(response.status_code)
    if response.status_code == 200:
        with open(f"./{year}/{day:02}.txt", "w+") as f:
            f.write(response.text)
        print("Downloaded input")
    else:
        print(response.text)

    page_url = f"https://adventofcode.com/{year}/day/{day:02}"
    response = requests.get(page_url)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # find first <code> tag
        code_tag = soup.find("code")
        if code_tag:
            with open(f"./{year}/{day:02}test.txt", "w+") as f:
                f.write(code_tag.text)
            print("Added test input")
        # find last <code> tag
        code_tag = soup.findAll("code")[-1]
        print(code_tag)
        desc = soup.find("article", class_="day-desc")
        if code_tag:
            with open(f"./{year}/{day:02}.py", "w+") as f:
                to_write = py_text.replace("DAY", f"{day:02}")
                try:
                    temp = int(code_tag.text)
                    to_write = to_write.replace("'A_RESPONSE'", code_tag.text)
                except:
                    to_write = to_write.replace("A_RESPONSE", code_tag.text)
                to_write = to_write.replace("DESCRIPTION", desc.text)
                f.write(to_write)
            print("Added solution")
    else:
        print(response.text)
