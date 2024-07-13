# Password Manager Guide

Welcome to the Password Manager! This guide will help you understand how to use the GUI-based password manager that can also generate strong passwords for users.

## How to Use

1. **Start the App:**
   - The app will open a window titled "Password Manager".

2. **Add Credentials:**
   - **Website:** Enter the name of the website for which you want to save the credentials.
   - **Username/Email:** Enter the username or email associated with the website.
   - **Password:** Enter the password manually or use the "Generate password" button to create a strong password.

3. **Generate a Password:**
   - Click the "Generate password" button to create a random password.
   - The generated password will be inserted into the password entry field.

4. **Save Credentials:**
   - Click the "Add information" button to save the entered credentials.
   - The credentials will be stored in a file named `data.txt`.

5. **Input Validation:**
   - Ensure that all fields (Website, Username/Email, Password) are filled before saving the information.
   - If any field is left empty, a warning message will be displayed.

## Customization

- **Customize Password Generation:** You can customize the length and composition of the generated passwords by modifying the ranges in the `g_pass` function.

## Additional Information

- The app uses the Tkinter library for the GUI.
- The `data.txt` file stores the saved credentials in the format `Website | Email | Password`.
- The app helps in managing and generating strong passwords, enhancing security and convenience.

Enjoy using the Password Manager to securely store and generate passwords!
