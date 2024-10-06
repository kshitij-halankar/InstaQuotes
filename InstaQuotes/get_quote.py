import requests

quote_url = "https://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en"

def print_quote():
    try:
        quote_response = requests.get(quote_url)
        if quote_response.status_code == 200:
            quote_json_data = quote_response.json()

            if 'quoteText' in quote_json_data:
                print(quote_json_data['quoteText'])

            if 'quoteAuthor' in quote_json_data:
                print("-",quote_json_data['quoteAuthor'])
            return quote_json_data
        else:
            print("Error in data")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

print_quote()
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
