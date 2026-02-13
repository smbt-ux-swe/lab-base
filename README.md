# Lab 2: External API Integration with Flask

**INFO 153B/253B — Spring 2025**
**Due: Friday, February 20, 2026, 9:00 AM PT**

---

## Overview

In this lab, you will integrate an **external API (OpenAI ChatGPT)** into an existing Flask application. The CRUD endpoints for managing student records are already provided — your job is to add two new endpoints that call OpenAI's API to generate academic advice for each student based on their major.

---

## Setup

### 1. Create a virtual environment

Before installing anything, create a **virtual environment (venv)**. A virtual environment is an isolated Python environment that keeps this project's dependencies separate from your system Python and other projects. Without it, installing packages globally can cause version conflicts between projects — for example, one project might need Flask 2.x while another needs Flask 3.x. With venv, each project gets its own clean set of packages.

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate it
# macOS / Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

Once activated, your terminal prompt will show `(venv)` at the beginning. From now on, all `pip` / `pip3` commands will install packages only inside this environment.

### 2. Install dependencies

```bash
pip install flask openai python-dotenv
```

(You can also use `pip3` instead of `pip` — inside an activated venv, both work the same.)

### 3. Set up your OpenAI API key

Your API key is a secret credential that lets your code talk to OpenAI's servers. **It must never be committed to git** — if someone gets your key, they can use your account and you'll be charged for their usage. Leaked keys on public GitHub repos are automatically scraped by bots within minutes.

That's why we use a `.env` file (which is listed in `.gitignore` so git ignores it) instead of pasting the key directly into our code.

**For this lab**, I have shared an API key on **bCourses → Assignments → Lab 2**. Use that key so you don't need to set up billing. The steps below are for your reference if you ever need your own key in the future.

<details>
<summary><strong>How to get your own OpenAI API key (reference only)</strong></summary>

1. Go to [https://platform.openai.com/](https://platform.openai.com/) and sign up or log in.
2. In the left sidebar, click **API keys**.
3. Click **Create new secret key**.
4. Enter a name (e.g. `lab2-key`) and click **Create secret key**.
5. **Copy the key immediately** — you won't be able to see it again after closing the dialog.
6. Save it somewhere secure (password manager, notes app, etc.).

</details>

**To configure your project:**

```bash
# Copy the example file to create your real .env
cp .env.example .env
```

Then open `.env` in any text editor and replace the placeholder with your actual key:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

> ⚠️ **`.env` is already in `.gitignore` so git will ignore it. Never commit it. Never share your API key in code, commits, or screenshots.**

### 4. Run the app

```bash
python3 app.py
```

You should see output like:

```
 * Running on http://127.0.0.1:5000
```

The server is now running locally. Keep this terminal open.

---

## How to Test: Using `curl`

`curl` (short for "Client URL") is a command-line tool that sends HTTP requests — think of it as a browser that runs in your terminal and shows you the raw response. When your Flask server is running, you can use `curl` to hit your API endpoints and see the JSON that comes back, just like a frontend app or Postman would.

Open a **new terminal window** (keep the server running in the first one) and try:

```bash
curl http://127.0.0.1:5000/students
```

This sends a **GET** request to your server's `/students` endpoint. You should see something like:

```json
{
  "students": [
    {"id": 1, "name": "Alice Smith", "email": "alice@berkeley.edu", "major": "Data Science"},
    {"id": 2, "name": "Bob Jones", "email": "bob@berkeley.edu", "major": "Computer Science"},
    {"id": 3, "name": "Carol White", "email": "carol@berkeley.edu", "major": "Information Systems"},
    {"id": 4, "name": "David Park", "email": "david@berkeley.edu", "major": ""}
  ],
  "total": 4
}
```

A few more examples with the existing CRUD endpoints:

```bash
# Get a single student
curl http://127.0.0.1:5000/students/1

# Create a new student
# -X POST sets the HTTP method, -H sets a header, -d sends the request body
curl -X POST http://127.0.0.1:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "Eve Lee", "email": "eve@berkeley.edu", "major": "HCI"}'

# Update a student's major
curl -X PUT http://127.0.0.1:5000/students/2 \
  -H "Content-Type: application/json" \
  -d '{"major": "Machine Learning"}'

# Delete a student
curl -X DELETE http://127.0.0.1:5000/students/3

# Try a student that doesn't exist — should return 404
curl http://127.0.0.1:5000/students/999
```
---

## What's Already Done (Do NOT Modify)

The following CRUD endpoints are fully implemented in `app.py`:

| Method | Endpoint | Description |
|--------|------|-------------|
| GET | `/students` | List all students |
| GET | `/students/<id>` | Get one student |
| POST | `/students` | Create a student |
| PUT | `/students/<id>` | Update a student |
| DELETE | `/students/<id>` | Delete a student |

---

## Your Tasks

You need to implement **two endpoints** inside `app.py`. Look for the `TODO` comments.

### Endpoint A — `POST /students/<id>/advice`

Generate advice for a student by calling OpenAI, then save it.

- **Success (200):**
  ```json
  {"id": 1, "major": "Data Science", "advice": "Put effort in making perfect portfolio!"}
  ```
- **Errors:**
  - Student not found → `404`
  - Student has no major → `400`
  - OpenAI call fails → `502`

### Endpoint B — `GET /students/<id>/advice`

Retrieve previously saved advice for a student.

- **Success (200):**
  ```json
  {"id": 1, "advice": "Put effort in making perfect portfolio!"}
  ```
- **Errors:**
  - Student not found → `404`
  - No advice saved yet → `404`

---

## Expected Results

Once you've implemented both endpoints, here's what you should see.

### Generate advice for Alice:

```bash
curl -X POST http://127.0.0.1:5000/students/1/advice
```

Expected — `200` with generated advice:

```json
{"id": 1, "major": "Data Science", "advice": "Focus on building strong statistical foundations and real-world data projects."}
```

*(The actual advice text will vary each time since it's AI-generated.)*

### Retrieve saved advice for Alice:

```bash
curl http://127.0.0.1:5000/students/1/advice
```

Expected — `200` with the same advice that was just saved:

```json
{"id": 1, "advice": "Focus on building strong statistical foundations and real-world data projects."}
```

### Error cases you should also verify:

```bash
# Student doesn't exist → should return 404
curl -X POST http://127.0.0.1:5000/students/999/advice

# Student 4 (David Park) has an empty major → should return 400
curl -X POST http://127.0.0.1:5000/students/4/advice

# Student 2 never had advice generated → should return 404
curl http://127.0.0.1:5000/students/2/advice
```

If all of the above behave as described, you're done!

---

## Checklist

- [ ] `POST /students/<id>/advice` calls OpenAI, returns advice, and saves it to the student
- [ ] `GET /students/<id>/advice` returns previously saved advice
- [ ] 404 for missing students on both endpoints
- [ ] 400 when student has no major
- [ ] 502 when OpenAI call fails
- [ ] API key loaded from `.env`, not hardcoded
- [ ] `.env` is in `.gitignore`

## Submission

1. Push your completed code to your repository.
2. Submit your repo URL to **Lab 2** on bCourses by **Friday 2/20, 9:00 AM**.