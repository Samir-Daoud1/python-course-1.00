# 1.2 — Comparison Operators

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

**Examples**

```python
# Basic comparisons
print(5 == 5)    # → True
print(5 != 3)    # → True
print(10 > 20)   # → False

# Combining with and / or / not
x = 7
print(x > 5 and x < 10)  # → True
print(x < 5 or x > 6)    # → True
print(not (x == 7))       # → False

# Membership test
fruits = ['apple', 'banana']
print('apple' in fruits)  # → True
print('mango' in fruits)  # → False
```

> ⚠️ **Common Mistake** — Using `=` (assignment) instead of `==`
> (comparison) inside an `if` statement.

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
