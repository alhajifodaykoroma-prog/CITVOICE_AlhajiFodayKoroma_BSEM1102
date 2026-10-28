CITIZENVOICE (CITVOICE)

Citizen Reporting and Public Infrastructure Response System

Course: PROG211 – Object-Oriented Programming 1
Institution: Limkokwing University, Sierra Leone
Language: Python

1. Project Overview

CITIZENVOICE (CITVOICE) is a Python command-line prototype designed to demonstrate how public infrastructure problems can be documented, categorised, and tracked.

The system focuses on three categories:

- Electricity
- Road Safety
- Road Infrastructure

The project applies object-oriented programming concepts to a practical community-related problem.

2. Problem Statement

Citizens may encounter public infrastructure problems without having a simple, organised way to document and track them. CITVOICE demonstrates how such concerns could be recorded and organised using a basic computer program.

3. Features

- Register public infrastructure reports.
- Generate report reference numbers.
- Assign reports to simulated service departments.
- View all registered reports.
- Search reports by reference number.
- Update report statuses.
- Display statistics by category and status.
- Validate required fields, priority levels, and status values.

4. Technologies Used

- Python 3
- Visual Studio Code
- Git and GitHub

5. Object-Oriented Programming Concepts

The project uses four classes:

Class| Responsibility
"PublicReport"| Stores report details and validates report values.
"ServiceDepartment"| Represents a service department.
"ReportRecord"| Connects a report to a department and reference number.
"CITVOICE"| Manages the main application functions.

The project demonstrates instance methods, a class method, a static method, a class attribute, and object interaction.

6. Data Structures

- List: Stores multiple report records.
- Tuple: Stores permitted report statuses and priority values.

7. Requirements

- Python 3 installed on the computer.
- A code editor or terminal.
- The "citvoice.py" source file.

No third-party Python packages are required by the current implementation.

8. How to Run the Project

1. Download or clone the repository.
2. Open the project folder in Visual Studio Code or a terminal.
3. Open a terminal in the project folder.
4. Run:

python citvoice.py

If your computer uses the "python3" command, run:

python3 citvoice.py

5. Follow the displayed menu and enter the number corresponding to the operation you want to perform.

9. Example Usage

A user can select Register a Report, choose Electricity, enter a problem such as a damaged electricity pole, provide its location and description, and select a priority.

The system creates a report record and displays a reference number, such as "CIT1".

The user can then select View All Reports or Search for a Report to inspect the record during the current program session.

10. Screenshots

The "screenshots/" folder contains evidence captured from the running application.

- "figure1-main-menu.png" — Main menu.
- "figure2-register-report.png" — Registering a report.
- "figure3-view-reports.png" — Viewing reports.
- "figure4-report-statistics.png" — Report statistics.

Replace these descriptions with the final screenshot filenames if they differ.

11. Limitations

This is an educational prototype. It stores reports in memory, so records are lost when the program terminates. It does not communicate with real government agencies, verify completed repairs, or provide permanent database storage.

12. Future Improvements

Future versions could introduce database storage, user authentication, a web or mobile interface, photo attachments, GPS-based locations, notifications, and authorised integration with relevant public service organisations.

13. Open-Source and Privacy Considerations

The source code can be shared for educational use under an appropriate open-source licence. The project uses a modular class structure and is designed to avoid requiring personal identifiers for its current demonstration.

A real deployment would need additional privacy protections, access controls, security testing, and suitable arrangements with the relevant service organisations.

14. Academic Purpose

This project was developed as an individual academic assignment for PROG211 – Object-Oriented Programming 1 to demonstrate the application of Python OOP concepts and data structures to a practical problem.