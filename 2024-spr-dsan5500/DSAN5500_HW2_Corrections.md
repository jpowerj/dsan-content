**DSAN 5500 HW2 Corrections:** (If you are working in Colab, your notebook has been auto-updated to reflect these corrections)

* *(2024-02-19, 7:00pm EST)* Within the cell titled `define-linked-list`, line 84 should be changed from `if self.content == item or self.content[0] == item:` to `if self.content == item or self.content[0] == item`. *(Thank you to Yanfeng for finding this one!)*
* *(2024-02-18, 11:30pm EST)* Within the cell titled `define-alpha-hasher`, line 40 should be changed from `return AlphaHasher.compute_position_in_alphabet(first_letter)` to `return self.compute_position_in_alphabet(first_letter)`. *(Thank you to Yifan for finding this!)*
