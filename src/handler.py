import runpod
import subprocess
import requests
from bs4 import BeautifulSoup

def handler(job):
    """Scrape webpage content from the provided URL in job.input"""

    url = job['input']
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the document data (for example, the text content)
        document_data = soup.get_text()
        
        return document_data
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"

runpod.serverless.start({"handler": handler})