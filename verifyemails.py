#!/usr/bin/python3

from googleapiclient.discovery import build
#from re import search

first_name = ''
last_name = ''
all_mails = []

#change to own cse and apikey
cse_id = "<your cse id>"
dev_key = "<your key>"

def google_search(search_term, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=dev_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def search_results(domain,option,domain_name):
    global first_name
    global last_name
    global all_mails

    start_offset = 1

    if option != 6:
        for page in range(0,5): # 3 result pages
            results = google_search(domain, cse_id, num=10, start=start_offset, cr='countryNL', gl='NL')
            for result in results:
                all = result['pagemap']['metatags']

                #title = result['title'].lower()
                #title = title.replace(" ", "")
                #test = result['link']

                #if search(domain_name, title):
                #    print ("Found: " + domain_name + " in title: " + title + "link: " + test)
                #else:
                #    print ("Did not find: " + domain_name + " in title: " + title + "link: " + test)

                for item in all:
                    first_name = str(item.get('profile:first_name'))
                    last_name = str(item.get('profile:last_name'))
                    check = item.get('profile:last_name')

                    if check is not None:
                        if option == 1:
                            fixed_last_name = last_name.replace(" ", "")
                            email = first_name[0] + "." + fixed_last_name + "@" + domain #h.degroot@test.nl
                            all_mails.append(email.lower())
                        elif option == 2:
                            fixed_last_name = last_name.replace(" ", "")
                            email = first_name[0] + fixed_last_name + "@" + domain #hdegroot@test.nl
                            all_mails.append(email.lower())
                        elif option == 3:
                            fixed_last_name = last_name.replace(" ", ".")
                            email = first_name[0] + fixed_last_name + "@" + domain #h.de.groot@test.nl
                            all_mails.append(email.lower())
                        elif option == 4:
                            fixed_last_name = last_name.replace(" ", ".")
                            email = first_name + "." + fixed_last_name + "@" + domain #hugo.de.groot@test.nl
                            all_mails.append(email.lower())
                        elif option == 5:
                            fixed_last_name = last_name.replace(" ", "")
                            email = first_name + fixed_last_name + "@" + domain #hugodegroot@test.nl
                            all_mails.append(email.lower())

            start_offset += 10

def main():
    global all_mails
    global domain
    all_options = []

    with open("workemails.txt", 'r', encoding='utf-8') as file:
        for domain in file:
            domain = domain.strip("https://www.")
            domain_name = domain.replace(".nl\n", "")
            print("Choose email format for: " + domain + """
                1: h.degroot@test.nl
                2: hdegroot@test.nl
                3: h.de.groot@test.nl
                4: hugo.de.groot@test.nl
                5: hugodegroot@test.nl
                6: Skip
            """)
            option = int(input("Format:"))
            all_options.append(option)

            search_results(domain,option,domain_name)
            print("Found emails: " + "".join(all_mails))

    with open("workemailsoutput.txt", 'a', encoding='utf-8') as file:
        file.write("".join(all_mails))
        print("Found emails: " + "".join(all_mails))

    with open("savedoptions.txt", 'a', encoding='utf-8') as file:
        file.write("\n".join(map(str, all_options)))
        print(all_options)

if __name__ == '__main__':
    main()
