import requests


def main():
    loc = "http://universities.hipolabs.com/search?name=Young"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    print(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
