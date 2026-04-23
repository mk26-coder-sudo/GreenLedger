
# 🌱 GreenLedger Backend

A backend system for **optimizing tree plantation across urban zones** and simulating environmental impact.

# 🚀 Tech Stack

* Python
* FastAPI
* Pydantic
* Graph (BFS)
* Heap (Priority Queue)

---

# ⚙️ How to Run

### 1. Clone the repo

```bash
git clone <https://github.com/mk26-coder-sudo/GreenLedger.git>
cd GreenLedger
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start server

```bash
uvicorn main:app --reload
```

👉 Runs on:
`http://127.0.0.1:8000`

👉 API Docs:
`http://127.0.0.1:8000/docs`

---

# 📌 What We Have Built

* 📊 **Zone Scoring System**
  Calculates environmental score using NDVI, population, heat, and flood risk

* 🌳 **Optimization Engine**
  Selects top zones and allocates saplings using heap-based logic

* 🔁 **Impact Simulation**
  Uses BFS to simulate how plantation affects nearby zones

* 📉 **Before vs After Analysis**
  Shows score reduction and overall impact after planting

---

# 🔗 Key APIs

* `GET /zones` → Get all zones
* `GET /optimize?k=3` → Get best zones + allocation
* `POST /plant` → Apply plantation and see impact

🔗 Link to GreenLedger Demo:
https://drive.google.com/file/d/1jwM0caK2I57kTFN-bEn-76uoRKu8M8sb/view?usp=sharing

