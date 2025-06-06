# @title Assignment Corrections (Run Cell to Fetch / Refresh)
import base64, datetime, json, pytz
from urllib.request import urlopen
from IPython.display import display, Markdown
def fetch_github(gh_url):
  md_data = json.load(urlopen(gh_url))
  md_content_b64 = md_data['content']
  md_content = base64.b64decode(md_content_b64).decode('utf-8')
  return md_content
exec_timestamp = datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%Y-%m-%d %H:%M:%S %Z")
corrections_url = "https://api.github.com/repos/jpowerj/dsan-content/contents/2025-sum-dsan5650/DSAN5650_HW1_Corrections.md?ref=main"
md_content = fetch_github(corrections_url)
corrections_content = md_content + f"\n\nLast fetched: {exec_timestamp}"
display(Markdown(corrections_content))
