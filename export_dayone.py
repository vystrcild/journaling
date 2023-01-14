import xml.etree.ElementTree as ET

def parse_entry(file: str) -> dict:
    """
    Parses an XML file and extracts the creation date, headline and entry text from it.

    :param file: The file path of the XML file.
    :type file: str
    :return: A dictionary containing the creation date, headline and entry text.
    :rtype: dict
    """
    tree = ET.parse(file)
    root = tree.getroot()

    log_entry = {}

    # Find the 'date' element
    creation_date = root.find("./dict/date").text
    log_entry["creation_date"] = creation_date

    # Find the 'string' element with the key 'Entry Text'
    entry_text = root.find("./dict/[key='Entry Text']/string").text
    headline, entry = entry_text.split("\n", 1)

    # Get headline
    log_entry["headline"] = headline

    # Get rest of the text
    log_entry["entry_text"] = entry
    return log_entry
