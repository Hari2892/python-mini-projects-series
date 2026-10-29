
import requests
from urllib.parse import urlparse

url = input("Enter long URL: ").strip()

# Validate the URL
parsed_url = urlparse(url)

if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
    print("Error: Please enter a valid URL starting with http:// or https://")

else:
    api_url = "https://tinyurl.com/api-create.php"

    try:
        response = requests.get(
            api_url,
            params={"url": url},
            timeout=15
        )

        response.raise_for_status()
        short_url = response.text.strip()

        if short_url.startswith(("http://", "https://")):
            print(f"Short URL: {short_url}")
        else:
            print("Error: TinyURL returned an invalid response.")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to TinyURL.")
        print("Check your internet connection and DNS settings.")

    except requests.exceptions.RequestException as error:
        print(f"API Error: {error}")
