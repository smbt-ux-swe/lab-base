# Password Security Tool - Lab

Build a password strength checker and password generator using Python fundamentals.

## 📝 Your Tasks

### TODO 1: Password Strength Checker

Implement `check_password_strength(password)` that analyzes a password and returns a strength score.

**Scoring rubric:**
- 8+ characters: 20 points
- 12+ characters: 30 points (replaces the 20)
- Has number: 20 points
- Has uppercase: 20 points
- Has lowercase: 20 points
- Has special char: 20 points
- Not common: 10 points

**Return format:**
```python
{
    "password": "Hello123!",
    "score": 90,
    "strength": "Strong"  # "Weak" (0-39), "Medium" (40-69), "Strong" (70-100)
}
```

### TODO 2: Password Generator

Implement `generate_password(length=12, use_special=True)` that creates a random secure password.

**Requirements:**
- Include uppercase, lowercase, and numbers
- Include special characters if `use_special=True`
- Minimum length of 8 characters
- Must actually contain all required character types!

## 🚀 Getting Started

1. Open `password_tool.py`
2. Complete TODO 1 (password checker)
3. Quick check: `python password_tool.py`
4. Complete TODO 2 (password generator)
5. Quick check: `python password_tool.py`
6. Run full tests: `python test_password_tool.py`

## 💡 Hints

### For TODO 1:
- Use string methods: `char.isdigit()`, `char.isupper()`, `char.islower()`
- Check special chars: `char in string.punctuation`
- Loop through password or use `any()`

### For TODO 2:
- Character sets: `string.ascii_uppercase`, `string.ascii_lowercase`, `string.digits`
- Random selection: `random.choice(chars)`
- Think about: How do you guarantee each type is included?

## ✅ Testing Your Code

**Quick check (during development):**
```bash
python password_tool.py
```
This shows if your functions are implemented and return the correct types.

**Full test suite (when complete):**
```bash
python test_password_tool.py
```

You should see:
```
✓ Test 1: Basic scoring
✓ Test 2: Weak password detection
✓ Test 3: Common password detection
✓ Test 4: Strong password detection
✓ Test 5: Generator length
✓ Test 6: Generator character types
✓ Test 7: Generated passwords are strong

Results: 7 passed, 0 failed
🎉 All tests passed! Great work!
```

## 🎓 Submission

1. Complete both TODO 1 and TODO 2
2. Ensure `python test_password_tool.py` passes all tests
3. Commit and push your code
4. Submit your repository link on bCourses

Good luck!