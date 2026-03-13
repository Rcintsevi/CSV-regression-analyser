# CSV Regression Analyser

A web application that performs **linear regression using gradient descent from scratch** — no ML libraries used for the model. Upload any CSV file, set your hyperparameters, and watch the model train in real time.

🔗 **Live Demo**: [csv-regression-analyser.onrender.com](https://csv-regression-analyser.onrender.com)

---

## What it does

- Accepts any two-column CSV (X, y)
- Runs linear regression using manually implemented gradient descent
- Returns a regression plot and a cost-vs-iterations convergence curve
- Displays dataset preview, final model parameters (w, b), cost, and R² score
- Tracks experiment history so you can compare different hyperparameter runs

---

## How it works

The model is built entirely from scratch using NumPy — no `sklearn` for training.

**Hypothesis:**

$$f_{w,b}(x) = wx + b$$

**Cost Function (MSE):**

$$J(w, b) = \frac{1}{2m} \sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})^2$$

**Gradient Descent Update Rules:**

$$w := w - \alpha \frac{\partial J}{\partial w}, \quad b := b - \alpha \frac{\partial J}{\partial b}$$

Where:
- $\alpha$ = learning rate
- $m$ = number of training examples
- Gradients are computed analytically over all samples (batch gradient descent)

---

## Tech Stack

| Layer | Technology |
|---|---|
| ML Logic | Python, NumPy (from scratch) |
| Backend | Flask |
| Plotting | Matplotlib |
| Data | Pandas |
| Frontend | HTML, CSS, Vanilla JS |
| Deployment | Render |

---

## Project Structure

```
csv-regression-analyser/
├── app.py               # Flask server, API routes
├── regression.py        # Gradient descent, cost, gradient, R² — all from scratch
├── requirements.txt
├── templates/
│   └── index.html       # Frontend UI
└── static/
    ├── style.css
    └── index.js         # Fetch API calls, DOM updates
```

---

## Run Locally

```bash
git clone https://github.com/Rcintsevi/CSV-regression-analyser.git
cd CSV-regression-analyser
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## Usage

1. Prepare a CSV file with exactly two columns — first column is X (feature), second is y (target)
2. Upload the file and set your hyperparameters:
   - **w** — initial weight
   - **b** — initial bias
   - **α** — learning rate (try `0.01` to start)
   - **Iterations** — number of gradient descent steps
3. Click **Upload** — the model trains and returns plots + metrics instantly
4. Experiment with different hyperparameters and track results in the history table

**Sample CSV format:**
```
x,y
1,2
2,4
3,6
4,2
5,13
```

---

## Hyperparameter Tips

| Scenario | Suggestion |
|---|---|
| Cost not decreasing | Reduce α (e.g. `0.001`) |
| Cost decreasing too slowly | Increase iterations or α slightly |
| Cost exploding / NaN | α is too large, reduce it |
| Good convergence | Cost-vs-iterations curve flattens smoothly |

---

## Key Implementation Details

- Gradient descent is implemented **without any ML library** — just NumPy loops
- R² score is computed manually: `1 - (SS_res / SS_tot)`
- Plots are saved to `/tmp/plots/` on the server and served via a Flask route
- Experiment history persists in the browser session (not stored server-side)

---

## Future Improvements

- Feature normalization / standardization
- Multivariate linear regression (multiple features)
- Train/test split with evaluation on held-out data
- Persistent experiment history (database or localStorage)

---

