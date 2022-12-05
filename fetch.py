# add new python file in folder corresponding to year

from datetime import datetime
import os
import argparse

import requests
from bs4 import BeautifulSoup
from lxml import html

from dotenv import load_dotenv

load_dotenv()

CWD = os.path.dirname(os.path.abspath(__file__))

today_day = datetime.today().day
today_month = datetime.today().month
today_year = datetime.today().year

with open("template.py.txt", "r") as f:
    py_text = f.read()


def fetch(year: int, day: int):
    print(f"Fetching data for {year=}, {day=}")
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
    headers = {"cookie": f"session={os.environ.get('AOC_COOKIE','')}"}
    response = requests.get(input_url, headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        if "Please log in " in response.text:
            print("Please provide a AOC_COOKIE env variable.")
            print("The value needed is the cookie as you visit aoc website.")
        else:
            with open(os.path.join(dir, "input.txt"), "w+") as f:
                f.write(response.text)
            print("Downloaded input")
    else:
        print("Met unexpected status code", response.status_code)
        print(response.text)

    print("Fetching original website...", end="")
    page_url = f"https://adventofcode.com/{year}/day/{day}"
    response = requests.get(page_url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        print(response.text)
        return
    tree = html.fromstring(response.text)

    test_input = None
    possible_xpaths = [
        "//*[contains(text(),'For example,')]//code",
        "//*[contains(text(),'For example,')]/following::code",
        "//pre",
        "//code",
    ]
    print("Finding test input", end="... ")
    for xpath in possible_xpaths:
        elem = tree.xpath(xpath)
        if elem:
            test_input = elem[0].text_content()
            break
    if test_input:
        with open(os.path.join(dir, "test.txt"), "w+") as f:
            f.write(test_input)
        print("Added test input")
    else:
        print("Unable to find test input")

    # last <code> tag should be test output
    test_output = ""
    code_elems = tree.xpath("//code")
    if code_elems:
        test_output = code_elems[-1].text_content()
    else:
        print("Unable to find test output")
    with open(os.path.join(dir, "run.py"), "r") as f:
        to_write = f.read()
    with open(os.path.join(dir, "run.py"), "w") as f:
        if test_output:
            replace_string = "A_RESPONSE"
            if replace_string not in to_write:
                replace_string = "B_RESPONSE"
            try:
                temp = int(test_output)
                to_write = to_write.replace(f'"{replace_string}"', test_output)
            except ValueError:
                to_write = to_write.replace(replace_string, test_output)
            print("Updated with test solution")
        f.write(to_write)


def main(year: int, day: int):
    fetch(year, day)


parser = argparse.ArgumentParser()
parser.add_argument("--year", "-y", type=int, default=today_year)
parser.add_argument("--day", "-d", type=int, default=today_day)
if __name__ == "__main__":
    args = parser.parse_args()
    main(args.year, args.day)
