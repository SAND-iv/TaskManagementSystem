# Task Manager 🗂️

**File:** `task_manager.py`
**Description:**
`task_manager.py` is a Python module that provides core functionality for a **console-based Task Management System**. It allows users to **add, view, update, and delete tasks** while handling input validation and maintaining persistent storage via text files. Each task includes a **name, description, priority (HIGH/MID/LOW), and due date (YYYY-MM-DD)**.

The module is designed with modularity in mind, making it easy to import functions into other Python scripts or extend with additional features in the future.

---

## ⚡ Features

* **Add Task:** Prompts for task details and validates input.
* **View Tasks:** Displays all tasks in a clear, numbered list.
* **Update Task:** Allows updating of task details with validation for priority and date format.
* **Delete Task:** Removes tasks safely by index.
* **Persistent Storage:** Saves tasks to a text file for tracking session history.
* **Input Validation:** Handles invalid menu options, priorities, and date formats gracefully.

---

## 🖥️ How to Use

1. **Import the Module (if using another script):**

```python
import task_manager
```

2. **Initialize the Task List:**

```python
tasks = []
```

3. **Call Functions as Needed:**

```python
# Add a new task
task_manager.add_task(tasks)

# View all tasks
task_manager.view_tasks(tasks)

# Update a task
task_manager.update_task(tasks)

# Delete a task
task_manager.delete_task(tasks)
```

4. **Run as Main Program:**
   If `task_manager.py` contains a main loop, simply run:

```bash
python task_manager.py
```

Follow the menu prompts to manage tasks interactively.

---

## 📁 File Structure

```
task_manager.py       # Core functions for managing tasks
tasks.txt             # Stores tasks persistently (generated automatically)
```

---

## 📝 Notes

* Ensure **Python 3.x** is installed.
* Task priority must be one of: **HIGH, MID, LOW**.
* Dates must follow the format: **YYYY-MM-DD**.
* All user inputs are validated to prevent errors.

Do you want me to do that?
