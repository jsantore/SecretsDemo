
import requests


def main():
    loc = "http://universities.hipolabs.com/search?name=Young"
    results = requests.get(loc)
    print(results)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
