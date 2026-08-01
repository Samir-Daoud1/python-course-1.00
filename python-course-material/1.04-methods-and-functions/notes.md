# 1.4 — Methods & Functions

## Methods

A method is a small tool that already belongs to a value, and you call it
by writing a dot after that value, then the method's name. You've actually
been using methods since section 1.1 (`.upper()`, `.append()`,
`.isdigit()` are all methods), this section just puts a name to the
pattern and shows how they fit into the bigger picture.

```python
numbers = [5, 3, 8, 1]
numbers.sort()          # a method that belongs to lists
print(numbers)            # → [1, 3, 5, 8]

text = 'hello world'
print(text.title())        # a method that belongs to strings
                             # → 'Hello World'
```

Different data types have different methods available, because a method
only makes sense for the kind of data it works with — you can `.upper()` a
string, but you can't `.upper()` a list.

## Defining Functions

A function is a named, reusable block of code that you write yourself.
Instead of copy-pasting the same lines over and over, you define the logic
once, give it a name, and then just "call" that name whenever you need it.


```python
def square(number):
    return number * number # return is discussed below

print(square(4))    # → 16
print(square(7))    # → 49
```

Here, `square` is the function's name, `number` is a **parameter** which is a
placeholder for whatever value gets passed in. Every time you call `square(...)` with a different
number, the function runs the same logic on that new value.

Now you probably saw the `return` keyword and asked what it does.
Basically, `return` is used inside a function to send a value back to whoever called
that function, and it immediately ends the function right there — any
code written after `return` in that function never runs. This is
different from `print()`, which only displays something on the screen;
`print()` doesn't hand a value back to the rest of your program to use.

```python
def double(number):
    return number * 2

result = double(9)   # result now holds 18
print(result)          # → 18

def is_even(number):
    return number % 2 == 0   # returns True or False
```

You can give a function more than one parameter, and you can give a
parameter a **default value** so the caller doesn't always have to supply
it:

```python
def greet(name, greeting='Hello'):
    return f'{greeting}, {name}!'

print(greet('Maya'))              # → 'Hello, Maya!'          (uses the default)
print(greet('Maya', 'Welcome'))   # → 'Welcome, Maya!'         (overrides the default)
```

Remember section 1.02's `check_isdigit` preview? Here's that exact idea,
now that you know how `def` actually works:

```python
def check_isdigit(user_input):
    return user_input.isdigit()

answer = input('Enter a number: ')
if check_isdigit(answer):
    print("That's a valid number!")
else:
    print("That's not a number.")
```

All `check_isdigit` does is wrap `.isdigit()` in a function so you can
reuse that exact check anywhere in your program just by calling
`check_isdigit(answer)`, instead of retyping `answer.isdigit()` every
time.

Finally, you can attach a short description to a function using a
**docstring** which is a string right under the `def` line, in triple quotes,
explaining what the function does. This is purely for humans (and tools);
Python doesn't require it, but it's good practice:

```python
def square(number):
    """Returns the square of a number."""
    return number * number
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
<summary>Answers</summary>

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
