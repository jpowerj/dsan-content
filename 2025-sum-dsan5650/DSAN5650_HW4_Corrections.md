**DSAN5650 HW4 Corrections**

The public tests for **Question 2.1.2** have a typo, where variable names were placed in quotes, so that they don't actually check for non-`None` values. The public test cell should instead be:

```py
# @title Q2.1.2-public-tests
q2_1_2_public_tests = {
    'pr_dohire_nocon filled': '✅ Passed!' if pr_dohire_nocon is not None else "🔲 Value of 'pr_dohire_nocon' should not be None",
    'pr_dohire_con filled': '✅ Passed!' if pr_dohire_con is not None else "🔲 Value of 'pr_dohire_con' should not be None",
}
q2_1_2_public_tests
```
