import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch the HTML content
url = "https://remoteok.com/remote-dev-jobs"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Step 2: Find all job listings
jobs = soup.find_all("tr", class_="job")

# Step 3: Prepare data for CSV
job_data = []

for job in jobs[:10]:  # Limit to top 10
    title = job.find("h2", itemprop="title").text.strip() if job.find("h2", itemprop="title") else "N/A"
    company = job.find("h3", itemprop="name").text.strip() if job.find("h3", itemprop="name") else "N/A"
    location = job.find("div", class_="location").text.strip() if job.find("div", class_="location") else "Remote"

    job_data.append([title, company, location])

# Step 4: Save to CSV
with open("jobs.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location"])  # Header row
    writer.writerows(job_data)

print("✅ Job data has been saved to 'jobs.csv'")
