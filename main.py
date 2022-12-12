import requests
from lxml import html
import sqlite3
import os

# Telegram information
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
TELEGRAM_BOT_API_KEY = os.environ["TELEGRAM_BOT_API_KEY"]

# URL and XPath information for AIUB Notice page
WEBSITE_URL = "https://aiub.cf/category/notices/"
POST_XPATH = "//ul[@class='event-list']/li"
TITLE_XPATH = ".//h2[@class='title']/text()"
LINK_XPATH = ".//a[@class='info-link']/@href"
DESCRIPTION_XPATH = ".//p[@class='desc']/text()"
DAY_XPATH = ".//time/span[@class='day']/text()"
MONTH_XPATH = ".//time/span[@class='month']/text()"
YEAR_XPATH = ".//time/span[@class='year']/text()"

# SQLite database information
DB_NAME = "aiub_notices.db"
DB_TABLE_NAME = "notices"

# Script version
SCRIPT_VERSION = "4.0"
SCRIPT_URL = "https://raw.githubusercontent.com/origamiofficial/aiub-notice-checker/main/main.py"

# Check for script updates
print("Checking for script updates...")
try:
    response = requests.get(SCRIPT_URL)
    if response.status_code == 200:
        # Parse version information from script
        lines = response.text.split("\n")
        for line in lines:
            if line.startswith("SCRIPT_VERSION"):
                online_version = line.split("=")[1].strip()
                break
        # Compare versions and update if necessary
        if online_version > SCRIPT_VERSION:
            print(f"New version {online_version} available. Updating script...")
            # Download new version of script
            with open("main.py", "w") as f:
                f.write(response.text)
            # Run new version of script and exit current script
            os.execv(sys.executable, ["python"] + sys.argv)
            sys.exit()
        else:
            print("Script is up to date.")
except Exception as e:
    print(f"h,vkezhsglvjwgzlsehvlkjzs: {e}")

# Check if AIUB website is up
print("Checking if AIUB website is up...")
try:
    requests.get(WEBSITE_URL)
    print("AIUB website is up.")
except requests.ConnectionError as e:
    print(f"AIUB website is down: {e}. Exiting script.")
    exit()

# Visit AIUB Notice page and check for new posts
print("Checking for new posts on AIUB Notice page...")
try:
    page = requests.get(WEBSITE_URL)
    tree = html.fromstring(page.content)
    posts = tree.xpath(POST_XPATH)
    print(f"{len(posts)} posts found on AIUB Notice page.")
except Exception as e:
    print(f"ehzhsdb.hb.kszhbvkwbeksu bkjn.j,")
    exit()

# Check if database file exists
if os.path.exists(DB_NAME):
    print(f"Existing SQLite database file found.")
else:
    print(f"Existing SQLite database file not found, created one")

# Connect to SQLite database
print("Connecting to SQLite database...")
try:
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    print("Connection to database successful.")
except Exception as e:
    print(f"Error connecting to database: {e}. Exiting script.")
    exit()

# Check if notices table exists in database, and create it if it doesn't
try:
    c.execute(
        "CREATE TABLE IF NOT EXISTS {} (title text, description text, link text)".format(
            DB_TABLE_NAME
        )
    )
except Exception as e:
    print(f"vJBSHdgliwygflivye;svjlehvlsbj")
    exit()
