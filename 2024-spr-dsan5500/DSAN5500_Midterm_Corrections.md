**DSAN 5500 Midterm Corrections:**

* Q2.2.1: Please change "number of collisions" to "number of collisions per slot", and then, in the code cell for the response, you can just choose one of `q2_2_1_response = "36"` or `q2_2_1_response = "18"`.
* Q3.1: If your email is for example `abc123@georgetown.edu`, then your UID is `abc123`.
* Q3.2: Subclasses of `ShopAVehicle` or `ShopBVehicle` should contain all of the functions that are in `ShopAVehicle`/`ShopBVehicle`, but the **code** within these functions can just be the Python keyword `pass`.
  * Also note that Python classes have a special notation: whereas functions are named like `def my_function():`, classes are named like `class MyClass:`. So, if you are making a class for big vehicles, it should be called `BigVehicle` rather than `big_vehicle`.
* Q5.2: The 3rd bullet should say "before the middle bug", and the 4th bullet should say "after the middle bug" (in the distributed version, these are reversed)
  * Also for this question: You can `import math` and then use `math.floor()` and/or `math.ceil()` from Python's `math` library to round a `float` value to the nearest `int` value less than or greater than the `float` value (respectively)
