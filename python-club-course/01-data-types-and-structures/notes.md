# 1.1 — Data Types & Structures

## 1.00 — Numbers

| Syntax/Code | Meaning |
|---|---|
| `int` | Whole numbers — e.g. `2`, `-5`, `100` |
| `float` | Decimal numbers — e.g. `3.14`, `-0.5`, `4E2` |
| `+ - * /` | Add, subtract, multiply, divide |
| `**` | Exponent / power → `2**3 = 8` |
| `%` | Modulo (remainder) → `7 % 3 = 1` |
| `//` | Floor division (round down) → `7 // 2 = 3` |

**Examples**

```python
# Basic math
2 + 3      # → 5
10 - 4     # → 6
3 * 7      # → 21
10 / 3     # → 3.333...
10 // 3    # → 3 (floor division)
10 % 3     # → 1 (remainder)
2 ** 8     # → 256 (2 to the power of 8)
```

> ⚡ **Order of Operations** — Python follows standard order of operations
> (PEMDAS/BODMAS). Use parentheses to control which operations happen first.

## 1.01 — Variable Assignment

Variables let you store values under a name so you can use them later.
Python figures out the type automatically — you don't need to declare it.

```python
x = 5           # store the number 5 in 'x'
name = 'Alice'  # store text in 'name'
price = 9.99    # store a decimal

# You can reassign any time
x = x + 1  # x is now 6
x += 1     # shortcut: same as x = x + 1
```

**Variable Naming Rules**

✅ Do:
- Use lowercase letters: `my_income`
- Use underscores for spaces: `tax_rate`
- Choose descriptive names: `user_age`
- Follow PEP8 style guidelines

❌ Avoid:
- Starting with a number: `1name`
- Spaces in names: `my name`
- Special symbols: `my@name`
- Python keywords: `list`, `str`
- Confusing letters: `l`, `O`, `I` (look like 1 and 0)

## 1.02 — Strings

| Method | Meaning |
|---|---|
| `'hello'` | Single-quoted string |
| `"hello"` | Double-quoted string — same thing |
| `len(s)` | Length of string → `len('hi') = 2` |
| `s[0]` | First character (index starts at 0) |
| `s[-1]` | Last character (negative index) |
| `s[1:4]` | Slice — characters from index 1 to 3 |
| `s.upper()` | Converts to ALL CAPS |
| `s.lower()` | Converts to all lowercase |
| `s.split(',')` | Splits into a list at commas |
| `s.strip()` | Removes leading/trailing spaces |
| `.format()` | Inserts values into a string template |
| f-string | `f'Hello {name}!'` → modern formatting |

**Examples**

```python
s = 'Hello, World!'
print(len(s))          # → 13
print(s[0])             # → 'H'
print(s[-1])             # → '!'
print(s[0:5])            # → 'Hello'
print(s.upper())         # → 'HELLO, WORLD!'
print(s.split(','))      # → ['Hello', ' World!']

# f-strings (easiest way to format)
name = 'Alice'
age = 25
print(f'My name is {name} and I am {age} years old.')
# → 'My name is Alice and I am 25 years old.'
```

### User Input & Checking for Numbers

The `input()` function pauses your program and waits for the user to type
something — but it always returns the result as a **string**, even if the
user typed a number! That means before doing math with it, you usually need
to check if it's actually a valid number.

Strings have a handy method called `.isdigit()` that returns `True` if
every character in the string is a digit (0-9), and `False` otherwise.

```python
user_input = input("Enter your age: ")
print(user_input.isdigit())  # True if it's a valid whole number

# A common pattern: keep asking until the input is valid
while True:
    age = input("Enter your age: ")
    if not age.isdigit():
        print("Please enter a valid number.")
        continue  # go back to the top of the loop and ask again
    age = int(age)  # now safe to convert to int
    break  # valid input — exit the loop

print(f"You are {age} years old.")
```

You can also pull this check into its own function so you can reuse it
anywhere in your code:

```python
# You should come back to this after learning about functions!
def check_isdigit(user_input):
    return user_input.isdigit()

answer = input("Enter a number: ")
if check_isdigit(answer):
    print("That's a valid number!")
else:
    print("That's not a number.")
```

## 1.03 — Lists

| Method | Meaning |
|---|---|
| `my_list = [1,2,3]` | Create a list |
| `my_list[0]` | Access first item |
| `my_list[-1]` | Access last item |
| `my_list[1:3]` | Slice — items at index 1 and 2 |
| `.append(x)` | Add x to the end |
| `.pop()` | Remove and return last item |
| `.pop(i)` | Remove item at index i |
| `.sort()` | Sort in place (ascending) |
| `.reverse()` | Reverse in place |
| `len(list)` | Number of items |
| `.count(x)` | Count how many times x appears |
| `.index(x)` | Find index of first x |

**Examples**

```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])    # → 'apple'
print(fruits[-1])   # → 'cherry'
fruits.append('date')  # adds 'date' to end
fruits.pop()            # removes and returns 'date'
fruits.sort()            # sorts alphabetically
print(len(fruits))       # → 3

# Nested lists
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[0][1])  # → 2
```

## 1.04 — Dictionaries

| Method | Meaning |
|---|---|
| `d = {'key': 'val'}` | Create a dictionary |
| `d['key']` | Access value by key |
| `d['new_key'] = x` | Add or update a key |
| `del d['key']` | Delete a key |
| `d.keys()` | Get all keys |
| `d.values()` | Get all values |
| `d.items()` | Get all key-value pairs as tuples |
| `'key' in d` | Check if key exists → True/False |

**Examples**

```python
person = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
print(person['name'])       # → 'Alice'
person['email'] = 'a@b.com'  # add new key
print(person.keys())          # all keys
print(person.values())        # all values

# Nested dictionary
data = {'user': {'name': 'Bob', 'score': 99}}
print(data['user']['score'])  # → 99
```

## 1.05 — Tuples

```python
t = (1, 2, 3)
print(t[0])   # → 1
print(len(t))  # → 3
# t[0] = 10  # ERROR! Tuples are immutable

t2 = (1, 1, 2, 3)
print(t2.count(1))  # → 2
```

## 1.06 — Sets & Booleans

| Method | Meaning |
|---|---|
| `s = {1, 2, 3}` | Create a set |
| `s.add(4)` | Add an item |
| `s.discard(2)` | Remove an item (no error if missing) |
| `{1,2} & {2,3}` | Intersection → `{2}` |
| `{1,2} \| {2,3}` | Union → `{1,2,3}` |
| `{1,2} - {2,3}` | Difference → `{1}` |
| `True / False` | Boolean values (capital T/F) |
| `bool(0)` | → `False` (0, '', None, [], {} are falsy) |

**Examples**

```python
s = {1, 2, 3, 2, 1}
print(s)  # → {1, 2, 3} (duplicates removed!)
s.add(4)
print(4 in s)  # → True

# Convert list to set to remove duplicates
my_list = [1, 1, 2, 3, 3]
unique = set(my_list)
print(unique)  # → {1, 2, 3}
```

---

## 📝 Practice Test: Data Types & Structures

1. What is the result of: `17 % 5`?
2. What is the result of: `2 ** 10`?
3. What does `len('Python')` return?
4. How do you get the LAST item of a list called `my_list` without knowing
   its length?
5. What is the difference between a list and a tuple?
6. Write code to add the value `'mango'` to a list called `fruits`.
7. Write code to get the value associated with the key `'age'` from a dict
   called `person`.
8. What does `set([1,1,2,3,3])` produce?
9. What is the output of: `'Hello'[1:4]`?
10. Write an f-string that prints `'My score is 95'` using a variable
    `score = 95`.
11. What does the `.isdigit()` method check for, and what does it return?
12. Write a while loop that keeps asking the user for input until they
    type a valid number.

<details>
<summary>✅ Answers</summary>

1. `2` — the remainder after dividing 17 by 5 (5 goes into 17 three times,
   leaving 2).
2. `1024` — 2 raised to the power of 10.
3. `6` — the number of characters in the string `"Python"`.
4. `my_list[-1]` — negative indexing counts from the end of the list.
5. A list is mutable (can be changed after creation, e.g. `.append()`),
   while a tuple is immutable (cannot be changed once created).
6. `fruits.append('mango')`
7. `person['age']`
8. `{1, 2, 3}` — sets automatically remove duplicate values.
9. `'ell'` — characters at index 1, 2, and 3 (index 4 is excluded).
10. `f"My score is {score}"`
11. It checks whether every character in a string is a digit (0-9). It
    returns `True` if so, and `False` otherwise.
12. ```python
    while True:
        val = input("Enter a number: ")
        if val.isdigit():
            break
        print("Invalid, try again.")
    ```

</details>
