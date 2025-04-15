
# 🌱 Git Version Control

## 🔧 1. Initial Setup

### ✅ Configure Git (only once)
```bash
git config --global user.name "Abhaya Shrestha"
git config --global user.email "email"
```

---

## 🆕 2. Start a New Project

### 📁 Create a local Git repository
```bash
mkdir KOL389COM-OSD-portfolio
cd KOL389COM-OSD-portfolio
git init
```

### 📄 Add files and commit
```bash
touch README.md
git add README.md
git commit -m "Initial commit"
```

---

## ☁️ 3. Connect to a Remote Repository

### 🔗 Add a remote (e.g. GitHub)
```bash
git remote add origin https://github.com/Abhaya23/KOL389COM-OSD-portfolio.git
```

### 🚀 Push your code to the remote
```bash
git push -u origin main
```

> 📝 First push uses `-u` to link local `main` with remote `main`.

---

## 📥 4. Clone an Existing Repository

### 📦 Clone from GitHub
```bash
git clone https://github.com/Abhaya23/KOL389COM-OSD-portfolio.git
cd KOL389COM-OSD-portfolio
```

---

## 🛠 5. Make Changes and Save

### 🔍 Check file status
```bash
git status
```

### 🧠 Stage changes
```bash
git add yatzy.py
```

### ✅ Commit with a message
```bash
git commit -m "Add feature"
```

---

## 🔄 6. Push & Pull Changes

### 🚀 Push to remote
```bash
git push origin main
```

### 📥 Pull latest changes from remote
```bash
git pull origin main
```

---

## 🌿 7. Work with Branches

### 🌱 Create a new branch
```bash
git checkout -b main
```

### 🏗 Switch between branches
```bash
git checkout main
```

### 🔀 Merge branch into main
```bash
git checkout main
git merge main
```

> 💡 Resolve conflicts if any before merging.

---

## ❌ 8. Optional: Undo Mistakes

### Unstage a file
```bash
git reset yatzy.py
```

### Discard changes in file
```bash
git checkout -- yatzy.py
```

---

## 🧼 9. Check History & Log

### See commit history
```bash
git log
```

### One-line summary
```bash
git log --oneline
```

---
