while count <= 50:
    # getting details for first page
    if count == 1:
        first_page = 'https://rentberry.com/de/apartments/s/berlin-germany'
        # request the response
        response = get(first_page)
        # parsing html 
        html_soup = BeautifulSoup(response.text, 'html.parser')
        # in the html of the page, find all the bins with <li> and class:
        house_data = html_soup.find_all('div', class_="apartment-item ng-star-inserted")
        # I like to print where the program is on the screen so we can follow its progress and where any errors happened
        print(first_page)
        
        # if the response was not empty (if something was actually scraped)
        if house_data != []:
            # add to the list houses
            houses.extend(house_data)
            # random wait times
            value = random()
            print(value)
            time.sleep(value)
    # pages other than the first
    elif count != 1:
    # collect four and wait random times 
        url = 'https://rentberry.com/de/apartments/s/berlin-germany?page=' + str(count) + '&sort=relevance'
        print(url)
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        print(response)
        house_data = html_soup.find_all('div', class_="apartment-item ng-star-inserted")

        if house_data != []:
            houses.extend(house_data)
            value = random()
            print(value)
            time.sleep(value)

        # if you get empty response, stop the loop
        else:
            print('empty')
            break
            

    count += 1
