# 1.3 — Python Statements

## if / elif / else

An `if` statement lets your program make a decision — it runs a block of
code only when a condition is `True`, and skips it otherwise. Python knows
which lines belong to the `if` because they're indented underneath it.

```python
temperature = 40

if temperature < 32:
    print("It's freezing!")
```

Since `temperature` is 40, the condition is `False`, so nothing prints.
Often you want an alternative path when the condition fails — that's
`else`:

```python
temperature = 40

if temperature < 32:
    print("It's freezing!")
else:
    print("Above freezing.")
# → 'Above freezing.'
```

When you have more than two possibilities, `elif` ("else if") lets you
check additional conditions in order. Python checks each one top to bottom
and stops at the first one that's `True`:

```python
grade = 82

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
else:
    print('F')
# → 'B', because 82 is not >= 90, but it IS >= 80
```

## for Loops

A `for` loop repeats a block of code once for every item in something —
a list, a string, or a range of numbers. Use it whenever you already know
what you're iterating over.

```python
colors = ['red', 'green', 'blue']
for color in colors:
    print(color)
# red
# green
# blue
```

When you want to loop a specific number of times rather than over an
existing list, `range()` generates the numbers for you on the fly:

```python
for i in range(4):        # 0, 1, 2, 3 — starts at 0 by default
    print(i)

for i in range(2, 7):      # 2, 3, 4, 5, 6 — starts where you tell it to
    print(i)
```

You can also loop directly over a string, one character at a time:

```python
for letter in 'Hi!':
    print(letter)
# H
# i
# !
```

## while Loops + break/continue

A `while` loop keeps repeating as long as its condition stays `True`,
use it when you don't know in advance how many times you'll need to loop.

```python
fuel = 3
while fuel > 0:
    print(f"Fuel remaining: {fuel}")
    fuel -= 1   # IMPORTANT: this has to change, or the loop never ends!
# Fuel remaining: 3
# Fuel remaining: 2
# Fuel remaining: 1
```

Inside any loop, `break` immediately stops the loop altogether, while
`continue` just skips the rest of the current pass and jumps to the next
one:

```python
for number in range(10):
    if number % 2 != 0:
        continue    # skip odd numbers entirely
    if number == 8:
        break        # stop the loop as soon as we hit 8
    print(number)
# 0
# 2
# 4
# 6
```

---

## 📝 Practice Test: Python Statements

1. Write an if/else that prints `'Pass'` if `score >= 60`, else prints
   `'Fail'`.
2. Write a for loop that prints every number from 1 to 10.
3. What does `range(2, 10, 2)` produce?
4. What is the difference between `break` and `continue`?
5. Write a while loop that prints `'tick'` 3 times then stops.
6. What happens if you forget to increase the counter in a while loop?
7. Write a for loop that loops through a dictionary and prints each key
   and value.


<details>
<summary>Answers</summary>

1. ```python
   if score >= 60:
       print("Pass")
   else:
       print("Fail")
   ```
2. ```python
   for i in range(1, 11):
       print(i)
   ```
3. `2, 4, 6, 8` — starts at 2, stops before 10, counting by steps of 2.
4. `break` exits the loop entirely. `continue` skips the rest of the
   current iteration and moves to the next one.
5. ```python
   count = 0
   while count < 3:
       print("tick")
       count += 1
   ```
6. The condition never becomes `False`, so the loop runs forever — this is
   called an infinite loop.
7. ```python
   for key, value in my_dict.items():
       print(key, value)
   ```

</details>
