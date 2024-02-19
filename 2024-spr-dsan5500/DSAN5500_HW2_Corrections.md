**DSAN 5500 HW2 Corrections:**

* *(2024-02-18, 11:30pm EST)* Within the cell titled `define-alpha-hasher`, line 40 should be changed from `return AlphaHasher.compute_position_in_alphabet(first_letter)` to `return self.compute_position_in_alphabet(first_letter)`. If you are working within Colab, your notebook has been auto-updated to reflect this. *(Thank you to Yifan for finding this!)*
