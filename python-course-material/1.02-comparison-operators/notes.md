# 1.2 — Comparison Operators

A comparison operator asks Python a yes-or-no question about two values,
and the answer always comes back as a boolean: `True` or `False`. These
are the building blocks you'll use to make decisions in your programs.
Things like "is the player's score high enough to win?" or "has the user
run out of tries?" are done using comparison operators.

The most basic comparisons check equality and size:

```python
print(7 == 7)     # → True   (are these equal?)
print(7 == 8)     # → False
print(7 != 8)     # → True   (are these NOT equal?)
print(10 > 3)     # → True   (is 10 greater than 3?)
print(10 < 3)     # → False
```

Two of these look similar to plain assignment but mean something very
different — `>=` and `<=` include the case where the values are equal:

```python
print(5 >= 5)   # → True   (5 is equal to 5, so "greater or equal" holds)
print(5 <= 4)   # → False
```

> ⚠️ A very common mistake: using a single `=` (assignment) where you meant
> `==` (comparison) inside an `if` statement. `=` sets a value; `==` asks
> a question.

Often you need to check more than one condition at once. That's where
`and`, `or`, and `not` come in handy since they combine boolean results together:

```python
temperature = 72
is_raining = False

# and → both sides must be True
print(temperature > 60 and not is_raining)   # → True

# or → only one side needs to be True
print(temperature > 90 or is_raining)         # → False (neither is true here)

# not → flips True to False and vice versa
print(not is_raining)   # → True
```

Try changing the values above in your head (or in a real Python shell) and
predicting the result before running it — that's the fastest way to build
intuition for `and`/`or`.

Two more operators let you check *membership* and *identity*. `in` checks
whether something exists inside a collection:

```python
attendees = ['Maya', 'Leo', 'Priya']
print('Leo' in attendees)      # → True
print('Sam' in attendees)      # → False
print('a' in 'banana')          # → True (checks substrings too!)
```

`is` looks different from `==` but is easy to confuse with it. `==` asks
"do these have the same value?" while `is` asks "are these literally the
exact same object in memory?" For beginners, stick to `==` for comparing
values, `is` is mostly used for special cases like checking `is None`.

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # → True   (same values)
print(a is b)   # → False  (two different list objects, even though equal)
```

**Quick reference**

| Operator | Meaning |
|---|---|
| `==` | Equal to → `5 == 5` is `True` |
| `!=` | Not equal to → `5 != 3` is `True` |
| `>` | Greater than → `7 > 3` is `True` |
| `<` | Less than → `2 < 8` is `True` |
| `>=` | Greater or equal → `5 >= 5` is `True` |
| `<=` | Less or equal → `3 <= 4` is `True` |
| `and` | Both conditions must be `True` |
| `or` | At least one condition must be `True` |
| `not` | Reverses `True` to `False` and vice versa |
| `in` | `'a' in 'cat'` → `True` (membership test) |
| `is` | Checks if two things are the SAME object |

---

## 📝 Practice Test: Comparison Operators

1. What is the result of: `10 == 10.0`?
2. What does `not True` evaluate to?
3. Is `3 >= 3` True or False?
4. Write a single condition that checks if `x` is between 1 and 100
   (inclusive).
5. What is the difference between `==` and `is`?
6. What does `'hello' in 'hello world'` return?
7. What is the result of `True and False`?
8. What is the result of `True or False`?

<details>
<summary>✅ Answers</summary>

1. `True` — Python compares values, not types, so an int and a float with
   the same value are equal.
2. `False` — `not` flips a boolean to its opposite.
3. `True` — `>=` includes equal values.
4. `1 <= x <= 100`
5. `==` checks if two values are equal. `is` checks if two variables point
   to the exact same object in memory.
6. `True` — `"hello"` is a substring contained within `"hello world"`.
7. `False` — `and` requires both sides to be `True`.
8. `True` — `or` only needs one side to be `True`.

</details>
