# 1.1 — Data Types & Structures

## 1.00 — Numbers

Python can work with two main kinds of numbers: **whole numbers**, called
`int` (short for integer), and **decimal numbers**, called `float` (short
for floating-point). You don't have to tell Python which one you're using
as it figures it out just from how you type the number. `7` is an `int`.
`7.0` is a `float`. That tiny difference (the decimal point) is all Python
needs.

Once you have numbers, you can do math with them using operators which are the
symbols that tell Python what operation to perform. Let's go through them
one at a time.

**Addition, subtraction, multiplication, division** work exactly like you'd
expect:

```python
print(4 + 6)   # → 10
print(4 - 6)   # → -2
print(4 * 6)   # → 24
print(4 / 6)   # → 0.6666666666666666
```

Notice that regular division (`/`) always gives you a decimal back, even
if the numbers divide evenly:

```python
print(8 / 2)  # → 4.0, not 4
```

If you only care about the whole number part of a division and want to
throw away the remainder, use **floor division** (`//`) instead:

```python
print(8 // 2)   # → 4
print(9 // 2)   # → 4  (9 divided by 2 is 4.5, floor division drops the .5)
```

Sometimes you don't want the division result at all and you just want to
know what's *left over*. That's what the **modulo** operator (`%`) gives
you:

```python
print(9 % 2)    # → 1  (9 divided by 2 is 4 remainder 1)
print(10 % 5)   # → 0  (10 divides evenly into 5, nothing left over)
```

Modulo is pretty useful. For example, it's the standard way to check
if a number is even or odd:

```python
number = 13
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
# → 'Odd', because 13 % 2 is 1, not 0
```

Finally, **exponents** (raising a number to a power) use `**`:

```python
print(3 ** 2)   # → 9   (3 squared)
print(2 ** 5)   # → 32  (2 to the 5th power)
```

One last thing worth knowing: Python follows the standard order of
operations (multiplication/division before addition/subtraction), so use
parentheses whenever you want to control what happens first:

```python
print(2 + 3 * 4)     # → 14 (multiplication happens first)
print((2 + 3) * 4)    # → 20 (parentheses force addition first)
```

**Quick reference**

| Syntax/Code | Meaning |
|---|---|
| `int` | Whole numbers — e.g. `7`, `-12`, `500` |
| `float` | Decimal numbers — e.g. `3.14`, `-0.5`, `2E3` |
| `+ - * /` | Add, subtract, multiply, divide |
| `**` | Exponent / power → `3**2 = 9` |
| `%` | Modulo (remainder) → `9 % 2 = 1` |
| `//` | Floor division (round down) → `9 // 2 = 4` |

## 1.01 — Variable Assignment

A variable is just a labeled box for storing a value so you can use it
again later without retyping it. Instead of writing `25` over and over in
your code, you can store it once under a name like `user_age` and refer to
that name everywhere. Python creates the variable the moment you assign it
a value — there's no separate "declare" step like in some other
languages.

```python
score = 0
player_name = 'Jordan'
temperature = 98.6
```

Once a variable exists, you can change what it holds at any time, you can just
assign it something new:

```python
score = 0
print(score)   # → 0

score = 10
print(score)   # → 10

score = score + 5   # take the current value and add 5 to it
print(score)   # → 15
```

That last line is so common that Python gives you a shortcut for it:

```python
score += 5   # exactly the same as: score = score + 5
print(score)  # → 20

score -= 3   # same as: score = score - 3
print(score)  # → 17
```

**Naming your variables well**

Do:
- Use lowercase letters: `total_points`
- Use underscores for spaces: `max_speed`
- Choose descriptive names: `items_in_cart`
- Follow PEP8 style guidelines

Avoid:
- Starting with a number: `2ndplace`
- Spaces in names: `total points`
- Special symbols: `total$`
- Python keywords: `list`, `str`, `sum`
- Confusing letters: `l`, `O`, `I` (look like 1 and 0)

## 1.02 — Strings

A string is just text, which can be any sequence of characters wrapped in quotes.
Python doesn't care whether you use single quotes or double quotes; they
do the same thing, so pick whichever is convenient (double quotes are
handy when your text itself contains an apostrophe, like `"it's fine"`).

```python
greeting = 'Good morning'
message = "Good morning"
```

Because a string is a sequence of characters, you can grab individual
characters out of it using their position, called an **index**. Indexing
starts counting from 0, not 1 so the first character is at position (index) 0.

```python
word = 'Python'
print(word[0])    # → 'P'  (first character)
print(word[1])    # → 'y'  (second character)
print(word[-1])   # → 'n'  (last character — negative counts from the end)
print(word[-2])   # → 'o'  (second-to-last character)
```

You can also grab a whole chunk of a string at once, this is called
**slicing**. A slice `s[start:stop]` gives you everything from `start` up
to (but not including) `stop`:

```python
word = 'Python'
print(word[0:3])   # → 'Pyt'   (characters at index 0, 1, 2)
print(word[2:5])   # → 'tho'   (characters at index 2, 3, 4)
print(word[:3])    # → 'Pyt'   (leaving out start means "from the beginning")
print(word[3:])    # → 'hon'   (leaving out stop means "to the end")
```

Strings also come with a set of built-in **methods**, which are mini-tools attached
to every string that let you transform or inspect it. You call a method by
writing a dot after the string, then the method name:

```python
sentence = 'python is fun'
print(sentence.upper())        # → 'PYTHON IS FUN'
print(len(sentence))            # → 13 (len() counts all the characters including spaces)
print(sentence.split(' '))      # → ['python', 'is', 'fun']  (breaks into a list)
```

Try chaining a couple together to see how they combine:

```python
messy = '  Hello World  '
print(messy.strip())          # → 'Hello World'   (trims outer spaces)
print(messy.strip().lower())  # → 'hello world'   (trim, then lowercase)
```

And for building strings that include variable values, an **f-string** is
the easiest way. You put an `f` before the quotes and drop variables straight
into `{ }`:

```python
player = 'Sam'
points = 42
print(f'{player} scored {points} points!')
# → 'Sam scored 42 points!'
```

**Quick reference**

| Method | Meaning |
|---|---|
| `'hello'` / `"hello"` | Single-quoted or double-quoted string — same thing |
| `len(s)` | Length of string → `len('hi') = 2` |
| `s[0]` | First character (index starts at 0) |
| `s[-1]` | Last character (negative index) |
| `s[1:4]` | Slice characters from index 1 to 3 |
| `s.upper()` | Converts to ALL CAPS |
| `s.lower()` | Converts to all lowercase |
| `s.split(',')` | Splits into a list at commas |
| `s.strip()` | Removes leading/trailing spaces |
| f-string | `f'Hello {name}!'` → modern formatting |

### User Input & Checking for Numbers

The `input()` function pauses your program and waits for the person using
it to type something. Here's the one quirk you need to remember:
**whatever they type comes back to you as a string — even if it looks like
a number.**

```python
age = input("How old are you? ")
print(type(age))   # → <class 'str'>, even if they typed 25
```

That matters because you can't do math on a string. If you tried
`age + 1` right after `input()`, Python would give you an error, since
you'd be trying to add a number to text. So before doing math with user
input, you need a way to check "is this actually a whole number?" Strings
have a built-in check for exactly that: `.isdigit()`. It looks at every
character in the string and returns `True` only if they're all digits
(0-9):

```python
print('25'.isdigit())     # → True
print('twenty'.isdigit())  # → False
print('-5'.isdigit())      # → False (the minus sign isn't a digit!)
```

A common pattern is to keep asking the person for input in a loop until
they finally type something valid:

```python
while True:
    age = input("How old are you? ")
    if not age.isdigit():
        print("That's not a valid number, try again.")
        continue   # go back to the top and ask again
    age = int(age)   # safe to convert now
    break            # got a valid number, stop asking

print(f"Got it — you're {age} years old.")
```

> ‼️ You may not fully understand this code right now and thats totally okay!
> This code contains if statements which will be disccussed in the upcoming lectures. 
> You may also see this same check wrapped up inside something called a
> **function**, like `def check_isdigit(user_input): return
> user_input.isdigit()`. Don't worry about fully understanding `def` and
> functions yet, since it also has its own topic, and we'll cover it properly (and
> revisit this exact example) in section 1.4. For now, just know that
> `.isdigit()` is the actual tool doing the work; a function is simply a
> reusable container you can put that check inside.

## 1.03 — Lists

A list is Python's way of storing many values together, in order, under a
single variable name, you think of it like a shopping list where each item
has a numbered position. Lists are written with square brackets, and the
items don't all have to be the same type.

```python
scores = [88, 92, 75, 100]
```

Just like strings, you access items in a list using their index (starting
at 0), and you can slice out a range of items the same way:

```python
scores = [88, 92, 75, 100]
print(scores[0])    # → 88   (first item)
print(scores[-1])    # → 100  (last item)
print(scores[1:3])   # → [92, 75]  (items at index 1 and 2)
```

The big difference between a list and a string is that **lists are
mutable**. This means that you can change, add, or remove items after creating them.
Strings can't be edited in place like this.

```python
scores = [88, 92, 75, 100]
scores.append(60)     # add a new item to the end
print(scores)          # → [88, 92, 75, 100, 60]

scores.pop()            # remove and return the last item
print(scores)            # → [88, 92, 75, 100]

scores.sort()             # sort the list in place, ascending
print(scores)              # → [75, 88, 92, 100]
```

Lists can even hold other lists - this is called a **nested list**, and
it's handy for representing grids or tables:

```python
grid = [[1, 2], [3, 4], [5, 6]]
print(grid[0])       # → [1, 2]   (the first inner list)
print(grid[0][1])     # → 2        (second item of the first inner list)
```

**Quick reference**

| Method | Meaning |
|---|---|
| `my_list = [1,2,3]` | Create a list |
| `my_list[0]` | Access first item |
| `my_list[-1]` | Access last item |
| `my_list[1:3]` | Slice items at index 1 and 2 |
| `.append(x)` | Add x to the end |
| `.pop()` | Remove and return last item |
| `.pop(i)` | Remove item at index i |
| `.sort()` | Sort in place (ascending) |
| `.reverse()` | Reverse in place |
| `len(list)` | Number of items |
| `.count(x)` | Count how many times x appears |
| `.index(x)` | Find index of first x |

## 1.04 — Dictionaries

A dictionary stores information as **key-value pairs** instead of a
numbered sequence. Instead of looking something up by its position (like a
list), you look it up by a meaningful label — the "key." This is perfect
for representing something like a single record with named fields.

```python
car = {'brand': 'Toyota', 'model': 'Corolla', 'year': 2021}
```

You access a value by putting its key in square brackets — not a number:

```python
car = {'brand': 'Toyota', 'model': 'Corolla', 'year': 2021}
print(car['brand'])   # → 'Toyota'
print(car['year'])    # → 2021
```

Dictionaries are mutable too, so you can add new keys or update existing
ones just by assigning to them:

```python
car['color'] = 'blue'   # adds a brand new key
print(car)                # → {'brand': 'Toyota', 'model': 'Corolla', 'year': 2021, 'color': 'blue'}

car['year'] = 2022        # updates an existing key
print(car['year'])         # → 2022
```

If you need to loop through everything a dictionary holds, it gives you
three tools for that: `.keys()` for just the labels, `.values()` for just
the data, and `.items()` for both together as pairs:

```python
car = {'brand': 'Toyota', 'model': 'Corolla', 'year': 2021}
print(car.keys())     # → dict_keys(['brand', 'model', 'year'])
print(car.values())    # → dict_values(['Toyota', 'Corolla', 2021])


**Quick reference**

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

## 1.05 — Tuples

A tuple looks almost exactly like a list — an ordered group of values —
except it's written with parentheses instead of square brackets, and once
you create it, **it cannot be changed**. No appending, no removing, no
reassigning individual items. Tuples are what you reach for when you want
to guarantee a set of values stays exactly as it was created.

```python
coordinates = (10, 20)
print(coordinates[0])   # → 10
print(len(coordinates))  # → 2

# coordinates[0] = 99   # This line would raise an error since tuples are immutable!
```

A common use for a tuple is representing something naturally fixed, like
an (x, y) point or a (red, green, blue) color — values that always come as
a group and shouldn't be edited individually.

```python
color = (255, 0, 0)   # red, as an RGB tuple
letters = ('a', 'b', 'a', 'c', 'a')
print(letters.count('a'))   # → 3   (tuples still support read-only methods like .count())
```

## 1.06 — Sets & Booleans

A set is an unordered collection that automatically throws out duplicate
values, you use it whenever you only care about *which* unique values
exist not how many times each one shows up or what order they're in.

```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)   # → {1, 2, 3}   (duplicates removed automatically)
```

Sets are great for cleaning up a list that might contain repeats:

```python
visitors = ['Ana', 'Ben', 'Ana', 'Cleo', 'Ben']
unique_visitors = set(visitors)
print(unique_visitors)   # → {'Ana', 'Ben', 'Cleo'}
```

You can add or remove items, and you can compare sets against each other like a venn diagram
using set operations like union and intersection:

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)   # → {2, 3}       (intersection: in both)
print(a | b)   # → {1, 2, 3, 4}  (union: in either)
print(a - b)   # → {1}           (difference: in a, but not in b)
```

**Booleans** are the simplest type in Python, they are just `True` or `False`
and every value in Python is secretly "truthy" or "falsy" even if it isn't
a real boolean. `0`, an empty string `''`, an empty list `[]`, and `None`
are all falsy; pretty much everything else is truthy.

```python
print(bool(0))     # → False
print(bool(''))     # → False
print(bool([]))      # → False
print(bool('hi'))     # → True
print(bool([1, 2]))    # → True
```

**Quick reference**

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

<details>
<summary>Answers</summary>

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

</details>
