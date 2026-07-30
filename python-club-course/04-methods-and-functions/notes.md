# 1.4 — Methods & Functions

## Methods

```python
my_list = [3, 1, 2]
my_list.sort()  # method called on the list object
print(my_list)   # → [1, 2, 3]

my_str = 'hello'
print(my_str.upper())          # → 'HELLO'
print(my_str.replace('l','r'))  # → 'herro'
```

## Defining Functions

```python
# Define a function
def greet(name):
    return 'Hello, ' + name + '!'

# Call the function
print(greet('Alice'))  # → 'Hello, Alice!'
print(greet('Bob'))     # → 'Hello, Bob!'

# Function with default parameter
def power(base, exp=2):
    return base ** exp

print(power(3))     # → 9 (exp defaults to 2)
print(power(3, 3))  # → 27
```

---

## 📝 Practice Test: Methods & Functions

1. Write a function called `add(a, b)` that returns the sum of two
   numbers.
2. What does the `return` keyword do?
3. Write a function with a default parameter value. Show an example call.
4. What is the difference between a function and a method?
5. What is a docstring? Write a function with one.

<details>
<summary>✅ Answers</summary>

1. ```python
   def add(a, b):
       return a + b
   ```
2. It sends a value back to wherever the function was called, and
   immediately ends the function.
3. ```python
   def greet(name="friend"):
       return f"Hello, {name}!"

   greet()        # "Hello, friend!"
   greet("Ali")    # "Hello, Ali!"
   ```
4. A function is standalone, called by name like `add(2,3)`. A method is
   a function that belongs to an object, called using dot notation, like
   `my_list.append(5)`.
5. ```python
   def add(a, b):
       """Returns the sum of a and b."""
       return a + b
   ```

</details>
