import requests

def main():
    url = 'http://127.0.0.1:8000/'
    message = input("Enter your message: ")

    response = requests.post(url, data=message.encode('utf-8'))

    print(response.text)

if __name__ == '__main__':
    main()