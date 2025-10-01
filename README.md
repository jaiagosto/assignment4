# 📦 Project Setup

---

# 🧩 1. Install Homebrew (Mac Only)

> Skip this step if you're on Windows.

Homebrew is a package manager for macOS.  
You’ll use it to easily install Git, Python, Docker, etc.

**Install Homebrew:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Verify Homebrew:**

```bash
brew --version
```

If you see a version number, you're good to go.

---

# 🧩 2. Install and Configure Git

## Install Git

- **MacOS (using Homebrew)**

```bash
brew install git
```

- **Windows**

Download and install [Git for Windows](https://git-scm.com/download/win).  
Accept the default options during installation.

**Verify Git:**

```bash
git --version
```

---

## Configure Git Globals

Set your name and email so Git tracks your commits properly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Confirm the settings:

```bash
git config --list
```

---

## Generate SSH Keys and Connect to GitHub

> Only do this once per machine.

1. Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

(Press Enter at all prompts.)

2. Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

3. Add the SSH private key to the agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

4. Copy your SSH public key:

- **Mac/Linux:**

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

- **Windows (Git Bash):**

```bash
cat ~/.ssh/id_ed25519.pub | clip
```

5. Add the key to your GitHub account:
   - Go to [GitHub SSH Settings](https://github.com/settings/keys)
   - Click **New SSH Key**, paste the key, save.

6. Test the connection:

```bash
ssh -T git@github.com
```

You should see a success message.

---

# 🧩 3. Clone the Repository

Now you can safely clone the course project:

```bash
git clone <repository-url>
cd <repository-directory>
```

---

# 🛠️ 4. Install Python 3.10+

## Install Python

- **MacOS (Homebrew)**

```bash
brew install python
```

- **Windows**

Download and install [Python for Windows](https://www.python.org/downloads/).  
✅ Make sure you **check the box** `Add Python to PATH` during setup.

**Verify Python:**

```bash
python3 --version
```
or
```bash
python --version
```

---

## Create and Activate a Virtual Environment

(Optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🐳 5. (Optional) Docker Setup

> Skip if Docker isn't used in this module.

## Install Docker

- [Install Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
- [Install Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)

## Build Docker Image

```bash
docker build -t <image-name> .
```

## Run Docker Container

```bash
docker run -it --rm <image-name>
```

---

# 🚀 6. Running the Project

- **Without Docker**:

```bash
python main.py
```

(or update this if the main script is different.)

- **With Docker**:

```bash
docker run -it --rm <image-name>
```

---

# 📝 7. Submission Instructions

After finishing your work:

```bash
git add .
git commit -m "Complete Module X"
git push origin main
```

Then submit the GitHub repository link as instructed.

---

# 🔥 Useful Commands Cheat Sheet

| Action                         | Command                                          |
| ------------------------------- | ------------------------------------------------ |
| Install Homebrew (Mac)          | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| Install Git                     | `brew install git` or Git for Windows installer |
| Configure Git Global Username  | `git config --global user.name "Your Name"`      |
| Configure Git Global Email     | `git config --global user.email "you@example.com"` |
| Clone Repository                | `git clone <repo-url>`                          |
| Create Virtual Environment     | `python3 -m venv venv`                           |
| Activate Virtual Environment   | `source venv/bin/activate` / `venv\Scripts\activate.bat` |
| Install Python Packages        | `pip install -r requirements.txt`               |
| Build Docker Image              | `docker build -t <image-name> .`                |
| Run Docker Container            | `docker run -it --rm <image-name>`               |
| Push Code to GitHub             | `git add . && git commit -m "message" && git push` |

---

# 📋 Notes

- Install **Homebrew** first on Mac.
- Install and configure **Git** and **SSH** before cloning.
- Use **Python 3.10+** and **virtual environments** for Python projects.
- **Docker** is optional depending on the project.

---

# 📎 Quick Links

- [Homebrew](https://brew.sh/)
- [Git Downloads](https://git-scm.com/downloads)
- [Python Downloads](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [GitHub SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

Assignment 4 - Professional Command-Line Calculator Application
A modular, professional-grade command-line calculator application built in Python with comprehensive testing, error handling, and continuous integration.


What This Is

This is a calculator app I built for my Python class. It's got a command-line interface where you can do basic math operations, and it keeps track of everything you calculate. The main focus was on writing clean code, handling errors properly, and getting 100% test coverage.

Features

What it does:

Basic math: add, subtract, multiply, divide
Interactive mode - keeps running until you tell it to stop
Saves your calculation history for the session
Checks your inputs to make sure they're valid
Handles errors without crashing (like dividing by zero)

Commands you can use:

help - Shows you what commands are available
history - Shows all the calculations you've done
exit - Closes the program

Project Structure

Here's how the files are organized:

calculator-app/
│
├── app/
│   ├── calculator/          # Main calculator logic
│   ├── calculation/         # Handles individual calculations
│   └── operation/           # Basic math operations
│
├── tests/                   # All the test files
│
├── requirements.txt         # Python packages needed
└── README.md               # This file
Getting Started
What you need:

Python 3.8 or newer
Git

Setup steps:

Clone this repo

bash   git clone https://github.com/yourusername/calculator-app.git
   cd calculator-app

Make a virtual environment

Windows:

bash   python -m venv venv
   venv\Scripts\activate
Mac/Linux:
bash   python3 -m venv venv
   source venv/bin/activate

Install what you need

bash//   
pip install -r requirements.txt

How to Use It

Run the calculator:
bash//
python -m app.calculator

Example of what it looks like:

Welcome to the Calculator!
Type 'help' for commands, or 'exit' to quit.

> add 5 3
Result: 8.0

> multiply 4 7
Result: 28.0

> divide 10 2
Result: 5.0

> history
Your calculations:
1. 5.0 + 3.0 = 8.0
2. 4.0 * 7.0 = 28.0
3. 10.0 / 2.0 = 5.0

> exit
Goodbye!

How It's Built
I organized the code into separate modules to keep things clean:

Operations are in their own folder
Calculations get managed separately
The main calculator runs the interface

I used the Factory pattern to create calculations based on what the user types in. Everything follows the DRY principle (Don't Repeat Yourself) so I'm not copying code all over the place.

Testing

Run the tests:

bash//
pytest

Check test coverage:
bash//
pytest --cov=app tests/

I wrote tests for everything - all the math operations, the calculation history, error handling, all of it. The project has 100% test coverage, which means every single line of code gets tested.

The tests include:

Regular unit tests for individual functions
Parameterized tests that check multiple scenarios at once
Edge case tests (like what happens when you divide by zero)

Error Handling
The app handles errors in two different ways (this was part of the assignment):
LBYL (Look Before You Leap)

Checks things before doing them
Like checking if a number is zero before dividing

EAFP (Easier to Ask Forgiveness than Permission)

Just tries to do something and catches errors if they happen
Uses try-except blocks

Errors it handles:

Division by zero
Invalid inputs (like typing letters instead of numbers)
Bad commands
Anything else that could crash it

Code Quality
I tried to keep the code clean and readable:

Follows Python style guidelines
Added comments where things might be confusing
Wrote docstrings for functions
Used meaningful variable names

All my commits have clear messages explaining what I changed.

Author: Jailene Agosto
Date: 9/29/2025
Course: Python - IS501-855