# Object-Oriented Chat System & OOP Practices 🐍💬

Welcome to my repository showcasing fundamental and advanced **Object-Oriented Programming (OOP)** concepts implemented in Python. This repository contains solutions to core assignment questions alongside a complete, modular **OOP Chat System** mini-project.

## 🚀 Try it instantly with GitHub Codespaces!

This repository is fully configured for cloud development. You don't need to install anything locally to run or play with the code!

1. Click the green **"Code"** button at the top right of this repository.
2. Switch to the **Codespaces** tab.
3. Click **"Create codespace on main"**.
4. Once the environment loads, open your terminal and run:
   ```bash
   python chat_system.py
   ```

---

## 🛠️ Included Projects & Core Concepts

### 1. 💬 Mini Project: OOP Chat System (`chat_system.py`)
A simulated chat room ecosystem built entirely around object interactions and class architectures using three foundational blueprints:
* **`User` Class:** Manages individual profiles and identity handles.
* **`Message` Class:** Bridges communication by binding specific `User` objects directly to raw string contents (`Composition`).
* **`ChatRoom` Class:** Serves as the central backend hub managing connection states (`join_room`/`leave_room`), enforcing message permissions, and managing logs sequentially.

### 2. 🧬 Multiple Inheritance Structure (`inheritance.py`)
Demonstrates how multiple structural traits can be cleanly inherited simultaneously. It utilizes explicit parent resolutions to completely avoid hidden Method Resolution Order (MRO) compiler loops when constructing complex relational networks (like an omnivore subclass branching from strict carnivore/herbivore trees).

### 3. ⚖️ Simulating Constructor Overloading (`constructor_overloading.py`)
Python natively lacks method signature overloading. This script provides the standard alternative, leveraging **default parameter blocks** to cleanly adapt initialization requirements dynamically (allowing structures to accept 1, 2, or 3 variables without breaking compilation).

---

## 🖥️ Sample Executions & Output

When running the core Chat System execution routine, the terminal output seamlessly routes system hooks alongside user exchanges:

```text
[SYSTEM] Alice joined 'Python Devs'.
[SYSTEM] Bob joined 'Python Devs'.

--- History for 'Python Devs' ---
Alice: Hey Bob! Is the OOP project complete?
Bob: Yes! Working perfectly.

[SYSTEM] Alice left 'Python Devs'.
[ERROR] Alice must join the room first to send messages.
```

---
*Maintained as part of an active backend software engineering study profile.*
