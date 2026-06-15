import pdfplumber
import pandas as pd
import os
with pdfplumber.open("arajbill.pdf") as pdf:
    page= pdf.pages[0]
    text = page.extract_text()
    print(text)

lines = text.split("\n")
data ={
    "supplier": "Anthropic,PBC",
    "invoice_number": "",
    "date": "",
    "subtotal": "",
    "total": ""
}
for line in lines:
    if "Invoice number" in line:
        data["invoice_number"] = line.split("Invoice number ")[-1].strip().replace("\x00","")
    if "Date of issue" in line:
        data["date"] = line.split("Date of issue ")[-1].strip()
    if "Subtotal" in line:
        data["subtotal"] = line.split("Subtotal ")[-1].strip()
    if "Total" in line and "excluding" not in line and "Amount" not in line:
        data["total"] = line.split("Total ")[-1].strip()
print(data)

df = pd.DataFrame([data])
df.to_excel("invoice_report.xlsx", index=False)
print("Saved to invoice_report.xlsx")