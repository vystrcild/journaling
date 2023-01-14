
from export_dayone import parse_entry
from datetime import date, datetime, timedelta
import os
from log_entry import generate_previous_dates


directory = "/Users/mac20/Desktop/DayOne_export/"

def log_entry(creation_date, headline, entry_text):
    date = datetime.strptime(creation_date[:10], "%Y-%m-%d").date()
    today = date.strftime("%Y-%m-%d")
    today_abbr = date.strftime("%a")
    yesterday = (date - timedelta(days=1)).strftime("%Y-%m-%d")
    tomorrow = (date + timedelta(days=1)).strftime("%Y-%m-%d")

    template = f"""---
    type: journal
    date: {today}
    ---
    # {today_abbr} - {today}  - {headline}
    << [[Journal/J - {yesterday}|Yesterday]] || [[Journal/J - {tomorrow}|Tomorrow]] >>
    On this day: {generate_previous_dates(today)}

    ---
    ### Entry:
    {entry_text}


    """
    template = '\n'.join(line.strip() for line in template.split('\n'))

    filename = f"{directory}J - {date.strftime('%Y-%m-%d')}.md"

    try:
        with open(filename, "w") as file:
            file.write(template)
    except:
        raise Exception(f"Error: Unable to create {filename}")


for file in os.listdir(directory):
    if file.endswith(".doentry"):
        print(file)
        data = parse_entry(f"{directory}{file}")
        creation_date = data["creation_date"]
        headline = data["headline"]
        entry_text = data["entry_text"]
        log_entry(creation_date, headline, entry_text)
