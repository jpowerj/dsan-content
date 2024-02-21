**DSAN 5500 HW2 Corrections:** (If you are working in Colab, your notebook has been auto-updated to reflect these corrections)

* *(2024-02-20, 8pm EST)* I have added a `__len__()` function to the provided `BinarySearchTree` and `BSTNode` classes, to make it easier for you to implement the `__len__()` function in `LogarithmicHashTable` (Q4.1), since you can now use `len()` to find the number of items in any slot containing a `BinarySearchTree`. *(Thank you to Yanfeng for suggesting this!)*
* *(2024-02-19, 7pm EST)* Within the starter code for Question 1.1 (so, the cell titled `Q1.1-response`), in line 33, the call to `self.hasher.compute_letter_for_index(i)` should be changed to `self.hasher.compute_key_for_index(i)`. *(Thank you to Yifan for finding this!)*
* *(2024-02-19, 7pm EST)* Within the cell titled `define-linked-list`, line 84 should be changed from `if self.content == item or self.content.item_name == item:` to `if self.content == item or self.content[0] == item`, since `self.content` should be of type `tuple`. *(Thank you to Yanfeng for finding this one!)*
* *(2024-02-18, 11pm EST)* Within the cell titled `define-alpha-hasher`, line 40 should be changed from `return AlphaHasher.compute_position_in_alphabet(first_letter)` to `return self.compute_position_in_alphabet(first_letter)`. *(Thank you to Yifan for finding this!)*