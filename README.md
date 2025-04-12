# **🔒 Password Checker**  
A Python-based password strength checker that evaluates user passwords and suggests improvements for better security.

## **✨ Features**
✔ Checks for minimum password length (**8 characters**)  
✔ Detects **spaces** in passwords (not allowed)  
✔ Validates presence of **digits**, **uppercase**, and **lowercase** letters  
✔ Encourages use of **special characters** for stronger security  
✔ Provides **color-coded feedback** for easy assessment:  
   - 🔴 **Red** → Weak Password  
   - 🟡 **Yellow** → Medium Strength Password  
   - 🟢 **Green** → Strong Password  
   - 🟣 **Magenta** → Recommended password variations  
✔ Generates **recommended stronger password variations**  
✔ Runs in a continuous loop with an **exit option**  

---

## **🛠 Installation**
Ensure you have **Python** installed.  
Then, follow these steps:

1️⃣ Clone the repository:
   ```bash
   git clone https://github.com/ChetanyaGarg/Password_Checker.git
   ```
2️⃣ Navigate to the directory:
   ```bash
   cd Password_Checker
   ```
3️⃣ Install dependencies:
   ```bash
   pip install colorama
   ```

---

## **🚀 How to Use**
Run the script using:
```bash
python password_checker.py
```
Then enter passwords to check their strength. Type **`exit`** to quit.

---

## **📌 Example Output**
```
[+] Starting Password Strength Checker
Enter Your Password (Type 'exit' to quit): P@ssw0rd
✅ Strong Password, It Is A Reliable Password
🟣 Recommended Passwords: P@ssw0rdG374$, P@ssw0rdK825&, P@ssw0rdF129!
```

---

## **📚 Technologies Used**
- 🐍 **Python**
- 🎨 **Colorama** (for colored output)
- 🔍 **Regular Expressions (`re`)** for pattern matching
- 🎲 **Random module** for password recommendations  

---

## **💡 Contributing**
Contributions are welcome! You can:  
✔ Improve password validation rules  
✔ Enhance security features  
✔ Add a **GUI-based interface**  
✔ Optimize code performance  

Simply **fork the repository**, make your changes, and open a **pull request**.

---

## **📜 License**
This project is licensed under the **MIT License** – feel free to use, modify, and distribute it!  

**🔗 GitHub Repo:** [Password_Checker](https://github.com/ChetanyaGarg/Password_Checker)  

---
