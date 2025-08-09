**DSAN5650 HW3 Corrections**

Public tests were not included for Questions 1.3.5 and 1.4.1, though they follow the general format of the other public tests, of just making sure the variables used for grading are defined in Python memory. For public tests in your notebook, that will match the public tests used by the autograder, you can add the following two cells to your notebook:

*Underneath the cell with title **`Q1.3.5-response`***:

```py
# @title Q1.3.5-public-tests
q1_3_5_public_tests = {
    'conviction_auc defined': '✅ Passed!' if 'conviction_auc' in globals() else "🔲 No variable named 'conviction_auc' exists in Python memory",
}
q1_3_5_public_tests
```

*Underneath the cell with title **`Q1.4.1-response`***:

```py
# @title Q1.4.1-public-tests
q1_4_1_public_tests = {
    'race_model defined': '✅ Passed!' if 'race_model' in globals() else "🔲 No variable named 'race_model' exists in Python memory",
}
```
q1_4_1_public_tests
