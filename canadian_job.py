import requests
import os
from  dotenv import load_dotenv
load_dotenv()
import csv
import anthropic

app_id = os.getenv("ADZUNA_APP_ID")
app_key = os.getenv("ADZUNA_APP_KEY")

test_cv = {
    "name": "Dipti Prakash Shahi",
    "skills": ["retail", "management", "SAP", "inventory", "supply chain", "logistics", "team leadership", "merchandising"],
    "job_title": "produce manager"
}
url =f"https://api.adzuna.com/v1/api/jobs/ca/search/1"

params ={
    "app_id": app_id,
    "app_key": app_key,
    "what": test_cv["job_title"],
    "where":"Toronto",
    "results_per_page":5

}
response = requests.get(url, params=params)
print(response.status_code)
jobs =response.json()


for job in jobs["results"]:

    print(job["title"])
    print(job["company"]["display_name"])
    print(job["location"]["display_name"])
    print(job["redirect_url"])
    print("-----")
import anthropic

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

with open("canadian_emails.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["title", "company", "location", "url", "email"])
    writer.writeheader()

    for job in jobs["results"]:
        prompt = f"Write a short professional job application email for {test_cv['name']} applying for {job['title']} at {job['company']['display_name']} in {job['location']['display_name']}. Their skills are: {', '.join(test_cv['skills'])}. Keep it under 150 words."

        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )

        email_text = message.content[0].text
        writer.writerow({
            "title": job["title"],
            "company": job["company"]["display_name"],
            "location": job["location"]["display_name"],
            "url": job["redirect_url"],
            "email": email_text
        })
        print(f"Email generated for: {job['title']} at {job['company']['display_name']}")



