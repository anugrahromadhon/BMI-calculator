# BMI Calculator

The **BMI Calculator** is a Python application with a graphical user interface (GUI) that allows users to calculate their Body Mass Index (BMI) based on their weight and height. It also categorizes the BMI into different health categories.

---

## Features
- User-friendly GUI built with `tkinter`.
- Calculates BMI based on user input (weight in kilograms and height in centimeters).
- Categorizes BMI into:
  - Underweight
  - Normal weight
  - Overweight
  - Obesity
- Provides real-time error handling for invalid inputs.

---

## Prerequisites
1. Python 3.x installed on your system.
2. No additional libraries are required as the project uses the built-in `tkinter` module.

---

## How to Use
1. Clone or download the repository.
2. Open the `bmi_calculator.py` file in your Python IDE or text editor.
3. Run the script:
   ```bash
   python main.py
   ```
4. Enter your weight (in kilograms) and height (in centimeters) in the input fields.
5. Click on the **Calculate BMI** button.
6. View your BMI value and category displayed in the application.

---

## Example
### Input:
- Weight: `70 kg`
- Height: `170 cm`

### Output:
- BMI: `24.22`
- Category: `Normal weight`

---

## File Structure
- `main.py`: The main Python script for the BMI Calculator.

---

## Notes
- Ensure that the weight and height inputs are positive numbers.
- The height should be entered in centimeters, and the weight in kilograms.
- The application uses the formula:
  ```
  BMI = weight (kg) / (height (m)^2)
  ```

---

## License
This project is licensed under the MIT License. Feel free to modify and distribute it as needed.

