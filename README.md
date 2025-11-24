# Symptom & Medication Journal

## 📌**Overview**

The Symptom & Medication Journal helps users track their health by recording medications taken or symptoms experienced.
It allows users to log occurrences (e.g., taking a medication or feeling a specific symptom) and view a summary of their health events. 
It is a console-based, beginner-friendly program.

## 📌**Features**
* **Add Item:** Register a new medication or symptom (Name + Category/Dosage).
* **Log Occurrence:** Record an event for a specific item (increments the event count).
* **View Summary:** View a list of all tracked health items with their total occurrence counts.
* **Simple Interface:** Easy-to-use menu-driven navigation.

## 📌**Technology**
* **Language:** Python 3.7
* **Input/Output:** Standard Console I/O
* **Data Structure:** List of Dictionaries
 
## 📌**Testing Instructions**

### Test Case 1: Add a health(medication or symptoms)

Select Option 1.
Enter Name: Fever.
Enter category (Medication/Symptom): symptom.
Expected Result: Item added to journal!

### Test Case 2: Log an occurrance

Select Option 2.
Choose the number corresponding to Fever.
Expected Result: System confirms "Logged event for Fever!".

### Test Case 3: Invalid Input (Non-Functional Testing)

Select Option 2.
Enter a non-numeric value or value which is not valid (e.g., "abc").
Expected Result: System catches the error and prints "Invalid input" without crashing.

## 📌**How to Run**
1. Ensure you have Python installed.
2. Open your terminal or command prompt.
3. Run the command:
   ```bash
   python Symptom_& _Medication_Journal.py
   
## 📌**Project Structure**
Symptom & Medication Journal/
* ├── Symptom_& _Medication_Journal.py
* ├── README.md
* ├── Report.pdf
* ├── /screenshots
* └── /recordings
   
## 📌**Screenshots**
### 1.Menu Drive

<img width="510" height="219" alt="image" src="https://github.com/user-attachments/assets/cb75c46e-3a9d-4bb4-be7d-9aae04e48d84" />

### 2.Entering choice as 1

<img width="760" height="464" alt="image" src="https://github.com/user-attachments/assets/90dd2e02-324a-428d-8ae0-a635417c3a53" />

### 3.Entering choice as 2 and checking for error by entering wrong input

<img width="1130" height="380" alt="image" src="https://github.com/user-attachments/assets/c4565a72-172b-4cab-9228-4ccf4bc946c9" />

### 4.Entering choice as 2 and checking result by entering correct input

<img width="518" height="448" alt="image" src="https://github.com/user-attachments/assets/7445a030-e0c8-4820-9ed6-d0608c6b5476" />

### 5.Entering choice as 3 and checking for the summary

<img width="530" height="784" alt="image" src="https://github.com/user-attachments/assets/5977caad-315c-401a-aad9-53795b1ce00c" />

