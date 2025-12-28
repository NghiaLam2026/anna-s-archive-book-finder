import requests
from bs4 import BeautifulSoup
import string

TEST_BOOK = "Tanenbaum & Wetherall Computer Networks"
non_alphabetic_set = set(string.punctuation)

def convert_from_ascii_to_hex(str_val:str):
    ascii_val = ord(str_val)
    return hex(ascii_val)[2:]

def convert_name_to_link(book_title: str):
    converted_name = ""
    for i in range(len(book_title)):
        if book_title[i] == " ":
            converted_name += "+"
        elif book_title[i] in non_alphabetic_set:
            converted_name += "%" + convert_from_ascii_to_hex(book_title[i]) 
        else:
            converted_name += book_title[i]
    return converted_name

def make_request_to_url_and_return_soup(url: str):
    r = requests.get(url)
    request_text = r.text
    soup = BeautifulSoup(request_text, "html.parser")
    return soup

def extract_book_links_from_soup(soup: BeautifulSoup):
    book_link = [] # Example: ["/md5/33cef5f377c85623fcb24623e322bdde", "/md5/dab66698917f1acf8ee5569660dff882", "/md5/4305eaea3087bf103f338642617ed2c7"]
    for link in soup.find_all("a", class_="custom-a block mr-2 sm:mr-4 hover:opacity-80"):
        if len(book_link) == 3:
            print("Book link list is greater than 3. Exiting loop!")
            break
        else:
            print(f"Appending {link.get('href')} to book link!")
            book_link.append(link.get("href"))
    return book_link

def main():
    book_request = input("Type in the name of the book: ")
    print(f"User requested book: {convert_name_to_link(book_request)}")
    format_request = input("Which format do you want your book to be in? ").lower()
    print(f"User wants the book to be in {format_request} format.")
    book_page_link = f"https://annas-archive.org/search?index=&page=1&sort=&ext={format_request}&display=&q={convert_name_to_link(book_request)}"
    print(f"Link to the book {book_page_link}")

    user_server_preference = input("Which server number do you want to download from? 1,2,3 ")
    print(f"User downloaded from server number slow server {user_server_preference}")

    while True:
        if user_server_preference == "1":
            print(f"User requested download from this server {'https://annas-archive.org/slow_download/' + extract_book_links_from_soup(make_request_to_url_and_return_soup(book_page_link))[0][5:] + '/0/0'}")
            break
        elif user_server_preference == "2":
            print(f"User requested download from this server {'https://annas-archive.org/slow_download/' + extract_book_links_from_soup(make_request_to_url_and_return_soup(book_page_link))[0][5:] + '/0/1'}")
            break
        elif user_server_preference == "3":
            print(f"User requested download from this server {'https://annas-archive.org/slow_download/' + extract_book_links_from_soup(make_request_to_url_and_return_soup(book_page_link))[0][5:] + '/0/2'}")
            break
        else:
            print("Invalid input, please try again or press q to quit!")
            user_server_preference = input("Which server number do you want to download from? 1,2,3 ")
            if user_server_preference == "q":
                print("Program exited successfully!")
                break
            else:
                continue

print(main())