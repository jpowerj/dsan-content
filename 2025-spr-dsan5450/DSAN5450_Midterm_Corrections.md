**DSAN5450 Midterm Corrections:**

* For **Question 1.6**: click "Show Code" and then replace `q1_5_response` with `q1_6_response`
* *[Optional]* You can create a new code cell under the **Q1.5-response** cell and copy-and-paste the following code, to create a public test for Q1.5:

  ```
  # @title Q1.5-public-tests
  q1_5_public_tests = {
      'q1_5_response defined': '✅ Passed!' if 'q1_5_response' in vars() else "🔲 No variable named 'q1_5_response' exists in Python memory"
  }
  q1_5_public_tests
  ```
