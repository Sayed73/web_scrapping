import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/."

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the elements containing movie titles and rankings
    movie_elements = soup.find_all("div", class_="listicle_listicle__item__OCDTx")
    

    result = {} 

    # Extract and print the titles and rankings
    for movie_element in movie_elements:
        title = movie_element.find(
            "h3", class_="listicleItem_listicle-item__title__hW_Kn"
        ).get_text(strip=True)

        values = title.split(") ", 1)

        result[values[0]] = values[1]

    for rank, title in result.items():
        print(f"Rank: {rank} Title : {title}")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
