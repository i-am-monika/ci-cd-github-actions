from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello from Mounika's CI/CD Pipeline!", "status": "healthy"}

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

## 📄 `app/requirements.txt`
```
flask==3.0.0
pytest==7.4.0