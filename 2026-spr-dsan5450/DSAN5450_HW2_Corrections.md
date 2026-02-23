**DSAN5450 HW2 Corrections**:

* If you're getting a **404 Error** when submitting, click "Show code" in the submission cell at the bottom of your notebook, and check whether the code contains the older server URL `http://jag.soc240036.projects.jetstream-cloud.org/` on **line 26**. If it does, please replace it within that code with the new URL, `https://jah-submit-83645199100.us-east4.run.app/`
* Remove the cell with title **Q3.3b-response** (the cell whose code has the first line `# @title Q3.3b-response`). This was left in by accident when I removed several questions!
* Remove all the `a`'s from the response cell titles and Python variables throughout **Question 3**. Meaning:
  * Find the cell whose code starts with `# @title Q3.1a-response`, and replace this first line with just `# @title Q3.1-response`.
  * Immediately below this, replace the python variable name `q3_1a_response` with just `q3_1_response`.
  
  Do the same for Q3.2 and Q3.3, and a likely source of 500 errors will be fixed!
