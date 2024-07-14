# Password Manager Guide Version 2

Welcome to the Password Manager! This guide will help you understand how to use the GUI-based password manager that can also generate strong passwords for users.

## How to Use

### Start the App

- The app will open a window titled "Password Manager".

### Add Credentials

- **Website:** Enter the name of the website for which you want to save the credentials.
- **Username/Email:** Enter the username or email associated with the website.
- **Password:** Enter the password manually or use the "Generate password" button to create a strong password.
- Click the "Add information" button to save the entered credentials.

### Generate a Password

- Click the "Generate password" button to create a random password.
- The generated password will be inserted into the password entry field and copied to the clipboard for convenience.

### Search for Saved Credentials

- Enter the website name and click the "Search" button.
- If the website's credentials are found, they will be displayed in a message box.
- If the website's credentials are not found, an error message will be displayed.

## Customization

- **Customize Password Generation:** You can customize the length and composition of the generated passwords by modifying the ranges in the `g_pass` function.

## Data Storage

- The credentials are stored in a JSON file named `data.json`.
- The file stores the website, email, and password in a structured format.

## Input Validation

- Ensure that all fields (Website, Username/Email, Password) are filled before saving the information.
- If any field is left empty, a warning message will be displayed.

## Additional Information

- The app uses the Tkinter library for the GUI and the pyperclip library for copying the password to the clipboard.
- The `data.json` file stores the saved credentials in the format:

  ```json
  {
    "Website1": {
      "Email": "email@example.com",
      "Password": "password123"
    },
    "Website2": {
      "Email": "another@example.com",
      "Password": "password456"
    }
  }
  ```

Enjoy using the Password Manager to securely store and generate passwords!
