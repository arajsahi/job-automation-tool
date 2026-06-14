import requests
import os
import anthropic
import csv
from dotenv import load_dotenv
load_dotenv()
response =requests.get("https://remotive.com/api/remote-jobs?search=python")
print(response.status_code)
jobs = response.json()["jobs"]


print(f"Found {len(jobs)} jobs!")

my_skills =["python","automation","flask","scraping","api","csv"]
good_jobs =[]

for job in jobs:
    tags = [tag.lower() for tag in job["tags"]]
    matched =[skill for skill in my_skills if skill in tags]

    if len(matched)> 0:
        match_percentage = round(len(matched)/len(tags)*100,2)
        good_jobs.append({
            "title":job["title"],
            "company":job["company_name"],
            "url":job["url"],
            "matched_skills":", ".join(matched),
            "matched_percentage":match_percentage
        }
        )

good_jobs = sorted(good_jobs, key=lambda x: -x["matched_percentage"])
for i,job in enumerate(good_jobs, start=1):
    print(f"{i}.{job['title']} -{job['company']} - {job['matched_skills']} - {job['matched_percentage']} %")

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

with open("job_emails.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["title", "company", "url", "matched_skills", "email"])
    writer.writeheader()

    for job in good_jobs:
        prompt = f"Write a short professional job application email for this role: {job['title']} at {job['company']}. My name is Araj. My skills are: Python, BeautifulSoup, Flask, Claude API, pandas, CSV, Git, GitHub, Render deployment. I have built a live Nepal news dashboard and a job automation tool. I am a Python developer based in Toronto. Keep it under 150 words."
        message = client.messages.create(
            model="claude-opus-4-6",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )

        email_text = message.content[0].text
        writer.writerow({
            "title": job["title"],
            "company": job["company"],
            "url": job["url"],
            "matched_skills": job["matched_skills"],
            "email": email_text
        })
        print(f"Email generated for: {job['title']} at {job['company']}")