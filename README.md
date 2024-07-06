Python Project: Simulated Bank System

Overview
In this project, you'll build a simplified version of a banking system using Python. This project
will consolidate your knowledge of data structures, conditional statements, loops, and
functions by simulating real-life banking operations like creating accounts, processing deposits
and withdrawals, and maintaining user data.

Objectives
- Develop a simulated bank system that can handle multiple users.
- Use data structures to manage user details and transactions.
- Implement functions for each banking operation.
- Employ loops and conditional statements to navigate through the user operations and validate
inputs.

Functional Requirements
1. User Account Creation:
- Prompt the user for their name, initial deposit amount, and a unique user ID.
- Store these details in a data structure. Consider using dictionaries where the user ID is the
key, and the value is another dictionary with user details such as name and balance.

2. Login System:
- Allow the user to enter their user ID.
- Validate the user ID. If the user exists, grant access to the other operations; otherwise,
prompt again or offer to create a new account.

3. Deposits and Withdrawals:
- After logging in, allow the user to deposit or withdraw money.
- Update the user’s balance accordingly in your data structure.
- Ensure that the withdrawals do not exceed the available balance.

4. Account Summary:
- Users can view their current balance and recent transaction history.

- Store each user's transactions in a list as part of their account details in the data structure.

5. Loop & Conditional Statements:
- Use loops to continuously allow the user to choose different operations (like deposit,
withdrawal, view balance, exit).
- Use conditional statements to check the validity of user inputs (e.g., checking for a minimum
deposit amount, ensuring withdrawals don't exceed the current balance).

6. Exit Option:
- Allow the user to exit the system which ends the session for that user.

Instructions
1. Planning:
- Sketch out the flow of your application. Decide on the data structures you’ll use and how they
will be organized.
- Write down the functions you'll need and what each function will do.

2. Implementation:
- Start by setting up the data structure for storing user details.
- Implement functions for creating an account, logging in, depositing money, withdrawing
money, and viewing account details.
- Ensure each function uses appropriate parameters and returns relevant values.

3. User Interaction:
- Design a simple text-based interface in the console. Use input prompts to receive user
commands and print statements to show outputs.
- Validate all inputs using loops and conditional statements to ensure the system is robust
against incorrect data entry.

4. Testing:
- Test each function individually to ensure it performs its intended operation.
- Go through common scenarios such as depositing more than the current balance, entering
invalid user IDs, and attempting to withdraw a negative amount.

- Check how your system handles incorrect inputs and ensure it doesn’t crash or behave
unexpectedly.

5. Extensions (Optional):
- Implement additional features such as password protection for accounts, an admin mode to
view all accounts, interest calculations, or transfer between accounts.
- Enhance the user interface with more detailed prompts and responses to make the system
more user-friendly.

Project Submission
- Prepare a report detailing your system design, the functions implemented, and key challenges
faced during the project.
- Include suggestions for further improvement or additional features that could be added in
future versions of the system.

This project will help you apply theoretical knowledge to a practical problem, refining your
programming skills and understanding of Python.