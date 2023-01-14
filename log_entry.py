from datetime import date, datetime, timedelta
import os
import webbrowser
from mdutils.mdutils import MdUtils
from dotenv import load_dotenv
load_dotenv()

from prompts import get_random_prompt

# Variables
folder_path = os.getenv("JOURNAL_FOLDER")
obsidian_path = os.getenv("OBSIDIAN_PATH")
first_entry = "2013-07-15"

def get_last_entry(folder_path:str)->str:
    """
    Returns the last date from files in the folder
    :param folder_path: Path of the folder
    :type folder_path: str
    :return: Last date from the files
    :rtype: str
    """
    try:
        files = os.listdir(folder_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: {folder_path} not found")
    except:
        raise Exception(f"Error accessing {folder_path}")

    last_date = ""
    for file in files:
        if file.endswith(".md"):
            date_str = file.split(" - ")[1].split(".")[0]
            if not last_date:
                last_date = date_str
            elif date_str > last_date:
                last_date = date_str
    return last_date


def generate_date(date_string: str) -> date:
    """
    Generates a date object from a string
    :param date_string: Date string in the format "YYYY-MM-DD"
    :type date_string: str
    :return: A date object
    :rtype: date
    """
    try:
        date_object = datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Error: Invalid date format. Expected format YYYY-MM-DD, got {date_string}")
    return date_object


def log_entry(date: date) -> str:
    """
    Returns a journal entry template for a given date.
    :param date: A date object for which the template is generated.
    :type date: date
    :return: A formatted string containing the journal entry template.
    :rtype: str
    """
    today = date.strftime("%Y-%m-%d")
    today_abbr = date.strftime("%a")
    yesterday = (date - timedelta(days=1)).strftime("%Y-%m-%d")
    tomorrow = (date + timedelta(days=1)).strftime("%Y-%m-%d")

    template = f"""---
    type: journal
    date: {today}
    ---
    # {today_abbr} - {today}  -
    << [[Journal/J - {yesterday}|Yesterday]] || [[Journal/J - {tomorrow}|Tomorrow]] >>
    On this day: {generate_previous_dates(today)}

    ---


    ### Prompt: {get_random_prompt()}


    ### Success of the Day


    ### Gratitude / What I liked about the day?
    -
    -
    -

    ### Laskavost


    """
    # Strip white spaces
    template = '\n'.join(line.strip() for line in template.split('\n'))

    filename = f"{folder_path}J - {date.strftime('%Y-%m-%d')}.md"
    # If file already exists, open it
    if os.path.exists(filename):
        webbrowser.open(f"{obsidian_path}{date.strftime('%Y-%m-%d')}")
    # Else create a file and open it
    else:
        try:
            with open(filename, "w") as file:
                file.write(template)
            webbrowser.open(f"{obsidian_path}{date.strftime('%Y-%m-%d')}")
        except:
            raise Exception(f"Error: Unable to create {filename}")


def get_next_entry_date(date: date) -> date:
    """
    Returns the next extry date
    :param date: A date object
    :type date: date
    :return: A date of next entry
    :rtype: date
    """
    next_entry_date = date + timedelta(days=1)
    return next_entry_date

def create_or_open_last(date: date, folder_path: str, last_entry_date: date):
    """
    Open or Create a file based on a given date
    :param date: A date object
    :type date: date
    """
    today = date.today()
    if date > today:
        # Open the last created entry:
        webbrowser.open(f"{obsidian_path}{last_entry_date.strftime('%Y-%m-%d')}")

    else:
        # Try create a new entry
        log_entry(date)


def generate_previous_dates(log_entry: date):
    """
    Generates dates for the same date as log_entry but for previous years within a given range
    :param log_entry: The last date in the range
    :type log_entry: str
    :return: A list of dates
    :rtype: list
    """
    first_entry_date = datetime.strptime("2013-07-15", "%Y-%m-%d")
    log_entry_date = datetime.strptime(log_entry, "%Y-%m-%d")
    previous_years_dates = []
    for year in range(first_entry_date.year, log_entry_date.year):
        previous_date = log_entry_date.replace(year=year)
        if previous_date > first_entry_date and previous_date != log_entry_date:
            previous_years_dates.append(datetime.strftime(previous_date, "%Y-%m-%d"))

    last_years_string = ""
    for date in previous_years_dates:
        last_years_string += (f"[[Journal/J - {date}|{date[:4]}]] | ")
    last_years_string = last_years_string.rstrip(" | ")
    return last_years_string



last_entry = get_last_entry(folder_path)
last_entry_date = generate_date(last_entry)
next_entry_date = get_next_entry_date(last_entry_date)
create_or_open_last(next_entry_date, folder_path, last_entry_date)
