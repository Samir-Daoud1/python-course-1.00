# 1.3 — Python Statements

## if / elif / else

```python
age = 18
if age < 13:
    print('Child')
elif age < 18:
    print('Teenager')
elif age == 18:
    print('Just turned adult!')
else:
    print('Adult')
# Output: 'Just turned adult!'
```

## for Loops

```python
# Loop through a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Loop a set number of times with range()
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i)

# Loop through a string
for letter in 'Python':
    print(letter)
```

## while Loops + break/continue

```python
count = 0
while count < 5:
    print(count)
    count += 1  # IMPORTANT: update count or loop never ends

# break — exit the loop immediately
# continue — skip to the next iteration
for i in range(10):
    if i == 3:
        continue  # skip 3
    if i == 7:
        break  # stop at 7
    print(i)  # prints 0 1 2 4 5 6
```

## The return Keyword

`return` is used inside a function to send a value back to wherever the
function was called from, and it immediately ends the function (any code
after `return` won't run). This is different from `print()`, which just
displays something on screen but doesn't give the value back to your
program to use.

```python
def add(a, b):
    return a + b  # sends the result back

result = add(3, 4)  # result now holds 7
print(result)         # → 7

def check_isdigit(user_input):
    return user_input.isdigit()  # returns True or False
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
8. What does the `return` keyword do, and how is it different from
   `print()`?

<details>
<summary>✅ Answers</summary>

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
8. `return` sends a value back from a function to where it was called, and
   ends the function. `print()` only displays text on screen — it doesn't
   give a value back to the program.

</details>
