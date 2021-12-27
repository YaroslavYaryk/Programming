import requests
import time


def get_address(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):

    file_name = response.url.split("/")[-1]
    with open(file_name, 'wb') as file:
        file.write(response.content)


def main():
    t0 = time.time()
    url = "https://loremflickr.com/320/240"
    for i in range(10):
        write_file(get_address(url))
    print(time.time() - t0)


if __name__ == '__main__':
    main()
