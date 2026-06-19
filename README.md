# Job Automation Tool 🤖

A Python tool that automatically finds remote jobs, matches them to your skills, generates professional application emails using Claude AI, and saves everything to a PostgreSQL database.

## What it does

- Fetches live remote Python jobs from Remotive API and Canadian jobs from Adzuna API
- Matches jobs to your skills and ranks them by match percentage
- Generates personalized application emails using Claude AI
- Saves jobs and emails to PostgreSQL database and CSV files

## Tools and Technologies

- Python
- Remotive API and Adzuna API
- Claude AI (Anthropic)
- PostgreSQL
- pandas, psycopg2, python-dotenv

## Files

- `jobfetcher.py` — fetches remote jobs and generates emails
- `canadian_job.py` — fetches Canadian jobs using Adzuna API
- `pdf_extractor.py` — extracts data from PDF invoices to Excel
- `chatbot.py` — Claude AI powered chatbot with Flask UI

## Setup

1. Clone the repo
2. Create a `.env` file with your API keys
3. Run `pip install -r requirements.txt`
4. Run `python jobfetcher.py`

## Built by

Araj Sahi — Python Developer based in Toronto 🇨🇦
github.com/arajsahi
