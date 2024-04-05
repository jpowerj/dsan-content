**DSAN 5500 HW3 Corrections**: (Auto-updated if you use Colab)

* [*Friday, April 5, 4am EST*]: There is an issue with Part 5, since Prefect doesn't seem to support the `COUNT` syntax for RRule strings; to fix this, please use the following as your `__main__` code (within the cell with `%%writefile` at the top):
    ```python
    if __name__ == "__main__":
      from dateutil.rrule import rrule, SECONDLY
      import datetime
      cur_dt = datetime.datetime.now()
      delta_10s = datetime.timedelta(seconds=10)
      delta_60s = datetime.timedelta(seconds=60)
      rrule_obj = rrule(freq=SECONDLY, interval=10, dtstart=cur_dt + delta_10s, until=cur_dt + delta_60s)
      rrule_str = str(rrule_obj)
      scrape_quote.serve(
        name="quote-scraper",
        rrule=rrule_str
      )
    ```
* [*Friday, April 5, 3am EST*]: If you restart your runtime after you've authenticated with `!prefect cloud login`, the code cell for this login will run forever. To fix this, you can replace the cell containing this `!prefect cloud login` command with the following code:
    ```python
    workspace_result = !prefect cloud workspace ls
    if 'Currently not authenticated' in workspace_result[0]:
      !prefect cloud login -k "$my_api_key"
    else:
      print("You're already authenticated with Prefect Cloud! Using workspace:")
      !prefect cloud workspace ls
    ```
* [*Thursday, April 4, 11pm EDT*]: Line 10 of the cell titled Q4-response should have `field_validator` added as an additional import from `pydantic` (in addition to `BaseModel`, `FilePath`, etc.), so that the code still runs when exported as a `.py` file!
