**DSAN 5500 HW1: Corrections:**

* (2024-01-28, 9pm EST) Since the first two corrections are not breaking, I have **auto-updated your notebooks** to fix them
  * (So, you **don't need to worry about them**, unless you made a **local copy** of the `.ipynb` file, in which case you'll need to apply the fixes to your local copy). I also **moved the `mypy` installation command** out of the first block and into the code block directly before **Question 2.1**. This should now mean that the top-of-file code block, which fetches these corrections, runs much faster!

(Issues auto-fixed in Colab versions:)

* *(2024-01-30, 7:00pm EST)* *In the second public test for **Question 5.2**, extraneous parentheses after `FancyLinkedList` removed; now updated to be `len(signature(FancyLinkedList.append).parameters) == 2`*
* *(2024-01-28, 8:44pm EST)* *In **Question 4.1**, the description of the `Swimmer` class is from an older version of the homework, which had `favorite_event` instead of `favorite_swim_style`. So, please replace "`compute_favorite_event()`" with "`compute_favorite_swim_style()`" and replace "`favorite_event` instance variable" with "`favorite_swim_style` instance variable". Thank you to Yanfeng for discovering this issue!*
* *(2024-01-28, 8:46pm EST)* *At the **end of the starter code** and in the **public tests** for **Question 4.2**, please replace the dictionary key `'average'` with the dictionary key `'favorites'` (matching the Q4.2 instructions). Thank you again Yanfeng for finding this!*
