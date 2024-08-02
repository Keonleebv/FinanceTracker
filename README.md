# Personal Finance Tracker

# Project Reason

To develop and challenge personal abilities by creating a fullstack project integrating a multitude of languages that I am personally passionate about encapsulating self-use cases. 

Ability to store and track my personal finances but completely off-grid and localized on my PC.

This project has an emphasis on elevating version control skills, project management (Agile), Design Principles (SOLID), DSA and applying theoretical knowledge in a real-world application. 

# Project Summary

Project Overview

Goal: Develop a personal finance tracker that supports income/expense tracking, budgeting, report generation, localization, and visualizations of trends and categorized expenses.

Technology Stack:
•	Frontend: React with TypeScript
•   Backend: Flask or Django with Python
•   Database: SQLite for local development
•   Charts: Chart.js, Recharts

Agile Development Process

Sprints: Organized into multiple sprints, each focusing on different aspects:
1. Sprint 1: Basic setup and income/expense tracking
2. Sprint 2: Budgeting and localization
3. Sprint 3: Reports and graphs
4. Sprint 4: Refinement and user feedback

Local Development Setup
IDE: Visual Studio Code with relevant extensions 
- 	Version Control: Git and GitHub (public repositories)
-	Design: Figma
-	Documentation: Markdown files within the repository
-	Testing: Vite for frontend, pytest for backend, Cypress for end-to-end testing

Software Architecture
Frontend Components
-	Login/Signup
-	Dashboard
-	Transaction Management: Income/Expense Form, Transaction List
-	Budget Management: Budget Form, Budget Overview
-	Reports: Report View, Download Button
-	Graphs: Trend Graphs, Category Graphs
-	Localization
-	Settings

Backend Components
-	Authentication: User Registration, User Login
-	API Endpoints
-	Transaction Management: Add/Edit/Delete Transaction, Get Transactions
-	Budget Management: Set Budget, Get Budget
-	Generation: Generate Report, Download Report
-	Graph Data: Get Trend Data, Get Category Data
-	Localization: Language Data

Database Tables
-	Users
-	Transactions
-	Budgets
-	Localization

Monitoring and Debugging
-	Local Logging: Use Python's built-in logging module
- Browser Developer Tools: Chrome DevTools for frontend debugging

SOLID Design Principles
-	Single Responsibility Principle (SRP): Each class/module should have one responsibility.
-	Open/Closed Principle (OCP): Classes should be open for extension but closed for modification.
-	Liskov Substitution Principle (LSP): Subclasses should replace base classes without affecting functionality.
-	Interface Segregation Principle (ISP): Clients should not depend on interfaces they do not use.
-	Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules; both should depend on abstractions.

Project Structure
Frontend Directory Structure
/frontend
|-- /public
|   |-- index.html
|-- /src
|   |-- /components
|   |   |-- TransactionForm.tsx
|   |   |-- TransactionList.tsx
|   |   |-- BudgetForm.tsx
|   |   |-- BudgetOverview.tsx
|   |   |-- ReportView.tsx
|   |   |-- Graphs.tsx
|   |-- /services
|   |   |-- TransactionService.ts
|   |   |-- BudgetService.ts
|   |-- /hooks
|   |   |-- useTransactions.ts
|   |   |-- useBudgets.ts
|   |-- /context
|   |   |-- TransactionContext.tsx
|   |-- App.tsx
|   |-- index.tsx
|-- package.json
|-- tsconfig.json

Backend Directory Structure
/backend
|-- /app
|   |-- /models
|   |   |-- transaction.py
|   |   |-- budget.py
|   |-- /routes
|   |   |-- transactions.py
|   |   |-- budgets.py
|   |-- /services
|   |   |-- transaction_service.py
|   |   |-- budget_service.py
|   |-- /repositories
|   |   |-- ITransactionRepository.py
|   |   |-- SQLiteTransactionRepository.py
|   |   |-- PostgresTransactionRepository.py
|   |-- /interfaces
|   |   |-- ITransactionService.py
|   |   |-- IBudgetService.py
|   |-- main.py
|-- requirements.txt

Describe how to use your project here.
