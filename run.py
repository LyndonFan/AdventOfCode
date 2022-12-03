# add new python file in folder corresponding to year

from datetime import datetime
import os
import argparse

import requests
from bs4 import BeautifulSoup

CWD = os.path.dirname(os.path.abspath(__file__))

today_day = datetime.today().day
today_month = datetime.today().month
today_year = datetime.today().year

with open("template.py.txt", "r") as f:
    py_text = f.read()


def fetch(year: int, day: int):
    print("Creating new directory and files... ", end="")
    dir = os.path.join(CWD, str(year), f"{day:02}")
    os.makedirs(dir, exist_ok=True)

    with open(os.path.join(dir, "run.py"), "w+") as f:
        _text = py_text.replace("DAY", str(day)).replace("YEAR", str(year))
        f.write(_text)
    with open(os.path.join(dir, "test.txt"), "w+") as f:
        f.write("")
    with open(os.path.join(dir, "input.txt"), "w+") as f:
        f.write("")

    print("Done")

    print("Fetching input text...", end="")
    input_url = f"https://adventofcode.com/{year}/day/{day}/input"
    response = requests.get(input_url)
    print(response.status_code)
    if response.status_code == 200:
        with open(os.path.join(dir, "input.txt"), "w+") as f:
            f.write(response.text)
        print("Downloaded input")
    else:
        print("Met unexpected status code", response.status_code)
        print(response.text)

    print("Fetching original website...", end="")
    page_url = f"https://adventofcode.com/{year}/day/{day}"
    response = requests.get(page_url)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # find first <code> tag
        code_tag = soup.find("code")
        if code_tag:
            with open(os.path.join(dir, "test.txt"), "w+") as f:
                f.write(code_tag.text)
            print("Added test input")
        # find last <code> tag
        code_tag = soup.findAll("code")[-1]
        print(code_tag)
        desc = soup.find("article", class_="day-desc")
        if code_tag:
            with open(os.path.join(dir, "run.py"), "w+") as f:
                to_write = py_text.replace("DAY", f"{day}")
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


def main(year: int, day: int):
    fetch(year, day)


parser = argparse.ArgumentParser()
parser.add_argument("year", type=int, default=today_year)
parser.add_argument("day", type=int, default=today_day)
if __name__ == "__main__":
    args = parser.parse_args()
    main(args.year, args.day)
