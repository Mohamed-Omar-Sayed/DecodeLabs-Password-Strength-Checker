# Password Strength Checker 🔐

A simple Python script that checks how strong your password is before you go and use "123456" again.

## What it does

- Checks if your password has uppercase, lowercase, digits, and special characters
- Makes sure the length is between 8 and 20 characters
- Compares it against a list of common passwords so you don't end up with "password123"
- Gives you a score and tells you exactly what's missing

## How to run

You'll need a `commen.txt` file with a list of common passwords (one per line).  
You can grab a list online — there are plenty of them.

```bash
python password_checker.py
```

## Scoring

| Condition | Points |
|---|---|
| Length between 8–20 | +1 |
| Has all 4 character types | +4 |
| Found in common passwords list | score = 0, game over |

Score > 4 → you're good  
Score ≤ 4 → fix what's missing and try again

## Requirements

Just Python. No libraries needed outside the standard `string` module.

---

Feel free to fork it, break it, improve it — whatever works for you.
