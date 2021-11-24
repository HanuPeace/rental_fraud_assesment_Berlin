# initialize a list called houses 
houses = []
# initialize loop variable for running through pages
count = 1
while count <= 50:
    # getting details for first page
    if count == 1:
        first_page = 'https://rentberry.com/de/apartments/s/berlin-germany'
        # request the response
        response = get(first_page)
        # parsing html 
        html_soup = BeautifulSoup(response.text, 'html.parser')
        # find bings with <div> with the class below as it hold the packet details of each house
        house_data = html_soup.find_all('div', class_="apartment-item ng-star-inserted")
        
        # data appended if scrapped sucessfully
        if house_data != []:
            # add to the list houses
            houses.extend(house_data)
            # random wait times
            value = random()
            print(value)
            time.sleep(value)
    # pages other than the first
    elif count != 1:
    # collect wait random times 
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
