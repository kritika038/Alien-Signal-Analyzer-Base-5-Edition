from flask import Flask, render_template, request

app = Flask(__name__)

def analyze_signal(signal):
    steps = []
    signal = signal.strip().replace(" ", "")

    # Check if exactly one '?'
    if signal.count('?') != 1:
        return -1, ["❌ Error: Input must contain exactly one '?'"]

    # Try digits 0 to 4 (valid in base-5)
    for digit in '01234':
        candidate = signal.replace('?', digit)
        try:
            base10 = int(candidate, 5)  # base-5 to base-10 conversion
            remainder = base10 % 7
            steps.append(
                f"Trying '{digit}' → {candidate} (base-10: {base10}) → "
                f"{'✅ Divisible by 7' if remainder == 0 else f'❌ Not divisible (remainder {remainder})'}"
            )
            if remainder == 0:
                return digit, steps
        except ValueError:
            steps.append(f"Trying '{digit}' → {candidate} → ❌ Invalid base-5 number")

    steps.append("No digit makes it divisible by 7 ❌")
    return -1, steps

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    steps = []
    if request.method == "POST":
        signal = request.form["signal"]
        result, steps = analyze_signal(signal)
    return render_template("index.html", result=result, steps=steps)

if __name__ == "__main__":
    app.run(debug=True)
