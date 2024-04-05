**DSAN 5500 HW3 Corrections**: (Auto-updated if you use Colab)

* [*Friday, April 5, 3am EST*]: If you restart your runtime after you've authenticated with `!prefect cloud login`, the code cell for this login will run forever. To fix this, you can change the cell containing this `!prefect cloud login` command with the following code:
    ```python
    workspace_result = !prefect cloud workspace ls
    if 'Currently not authenticated' in workspace_result[0]:
      !prefect cloud login -k "$my_api_key"
    else:
      print("You're already authenticated with Prefect Cloud! Using workspace:")
      !prefect cloud workspace ls
    ```
* [*Thursday, April 4, 11pm EDT*]: Line 10 of the cell titled Q4-response should have `field_validator` added as an additional import from `pydantic` (in addition to `BaseModel`, `FilePath`, etc.), so that the code still runs when exported as a `.py` file!
