# **Password Checker**

🔒 **Password Checker** is a Python script designed to evaluate the strength of user-entered passwords and provide real-time feedback on improving security. The script enforces basic password strength rules and uses **Colorama** to display responses with appropriate colors.

## **Features**
- ✅ Checks for minimum length (**8 characters**)
- ✅ Detects **spaces** in passwords (not allowed)
- ✅ Verifies the presence of **digits**, **uppercase**, and **lowercase** letters
- ✅ Encourages the use of **special characters** for stronger security
- ✅ Color-coded feedback:
  - 🔴 **Red** for **weak passwords**
  - 🟡 **Yellow** for **medium-strength passwords**
  - 🟢 **Green** for **strong passwords**
- ✅ Continuous password evaluation loop with an **exit option**

## **Installation**
Ensure you have **Python** installed on your system.

1. Clone the repository:
   ```bash
   git clone https://github.com/ChetanyaGarg/Password_Checker.git
   ```
2. Navigate to the directory:
   ```bash
   cd Password_Checker
   ```
3. Install dependencies:
   ```bash
   pip install colorama
   ```

## **Usage**
Run the script:
```bash
python password_checker.py
```
Enter passwords to check their strength. Type **`exit`** to quit.

## **Example Output**
```
[+] Starting Password Strength Checker
Enter Your Password (Type 'exit' to quit): P@ssw0rd
✅ Strong Password, It Is A Reliable Password
```

## **Technologies Used**
- 🐍 **Python**
- 🎨 **Colorama** (for colored output)
- 🔍 **Regular Expressions (`re`)** for pattern matching

## **Contributing**
Feel free to contribute by improving the logic, adding more features, or optimizing the code. Open a pull request or submit an issue!

## **License**
📝 This project is licensed under the **MIT License**. You are free to use, modify, and distribute it.

---
