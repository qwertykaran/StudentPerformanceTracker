# Student Performance Tracker 📊

A Python-based command-line application to manage and track student performance, storing data in an SQLite database. Easily add students, record marks, view performance analytics, and manage records.

---

## Features ✨
- **Add Students**: Store student details (name, age, class).
- **Record Marks**: Input subject-wise marks for each student.
- **View Analytics**: Check average marks, grades, and individual performance.
- **Delete Records**: Remove student entries as needed.
- **Local Database**: All data persists in `students.db` (SQLite).

---

## Tech Stack 🛠️
- **Python 3.x** (with `sqlite3` standard library)
- **SQLite3** (lightweight, file-based database)

---

## File Structure 🌳
```
project-root/
├── database.py # SQLite DB setup and table creation
├── operations.py # CRUD operations (add, view, delete)
├── main.py # CLI interface
└── students.db # Database file (auto-generated)
```


---

## Setup Guide 🚀

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/student-performance-tracker.git
   cd student-performance-tracker
   ```
2. **Run the application**
   ```bash
   python main.py
   ```
---

## Usage Example 📝
```
$ python main.py
---------------------------------
STUDENT PERFORMANCE TRACKER MENU:
---------------------------------
1. Add New Student
2. Add Marks for Student
3. View Student Performance
4. Delete Student
5. Exit
---------------------------------
Enter choice: 1
```
---
## Future Enhancement
Web UI: Build a Flask/Dash frontend.

Data Export: Add CSV/Excel report generation.

Authentication: Secure access with a login system.

Visualizations: Plot performance trends with Matplotlib.

---
## Contribute 🤝
Pull requests welcome! For major changes, open an issue first.
---
## License: MIT
**Maintainer: Karan Soni**
