# 🛸 Alien Signal Analyzer (Base-5)

This project is a web-based tool that simulates how aliens communicate using a base-5 numeral system. A received signal may contain exactly **one corrupted digit**, represented by a `'?'`. Your task is to determine the digit (`0` to `4`) that can replace `'?'` to make the entire base-5 number divisible by `7`.

---

## ✅ Features

- Accepts signal with **exactly one `'?'`**
- Replaces `'?'` with digits from `0` to `4`
- Converts the base-5 number to base-10
- Checks **divisibility by 7**
- Displays **step-by-step reasoning** on the web interface
- Simple and responsive user interface using **Flask + HTML + CSS**

---

## 💻 How to Run

1. **Clone or download the project**
2. Install Flask:
   ```
   pip install flask
   ```
3. Run the app:
   ```
   python app.py
   ```
4. Open your browser and visit:
   ```
   http://localhost:5000
   ```

---

## 🧪 Example Test Inputs

| Input Signal | Correct Digit | Explanation |
|--------------|----------------|-------------|
| `1?34`       | `-1`           | No digit makes it divisible by 7 |
| `?121`       | `1`            | 1121 (base-5) = 161 → 161 % 7 = 0 |
| `02?1`       | `1`            | 0211 (base-5) = 56 → 56 % 7 = 0   |

---

## 🧠 Logic Used

- All digits are assumed to be in **base-5** (valid digits: `0` to `4`)
- Only **one** `'?'` is allowed in the input
- After replacing `'?'`, each candidate is converted using:
  ```python
  int(candidate, 5)
  ```
- Then checked:
  ```python
  if base10 % 7 == 0
  ```

---

## 📂 Project Structure

```
alien_signal_analyzer/
├── app.py
├── static/
│   └── style.css
└── templates/
    └── index.html
```

---

## 📜 License

This project is open for academic and educational use.
