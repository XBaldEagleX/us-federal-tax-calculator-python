# U.S. Federal Tax Bracket Calculator (Python)
A command-line Python application that estimates U.S. federal income tax using progressive tax brackets.

This project was built as a learning exercise to better understand how marginal tax brackets actually work while reinforcing core Python programming concepts.

## Overview
The calculator walks a user through income input, deduction selection, and tax calculation, then produces a clear summary showing how income is taxed across brackets.

It emphasizes the difference between marginal and effective tax rates; a concept that is often misunderstood.

## What's New in v1.0.5 (State Tax Phase 1)
- Added initial **state income tax** support!
- Handles the 9 states with **no state income tax** (AK, FL, NV, NH, SD, TN, TX, WA, WY) → returns $0.00 automatically.
- Users enter their state (e.g., "TX" or "Texas"), and it displays in the summary: "No state income tax" or "N/A (not implemented yet)" for flat/graduated states.
- Modular `state_tax.py` file for easy future expansion (flat and graduated brackets planned next).
- Updated output now shows federal + state tax side-by-side.
- Closes GitHub Issue #1.

## Features
- Supports Single and Married Filing Jointly filing statuses
- Accepts income input with or without commas
- Allows standard or custom deductions
- Progressive federal tax calculation by bracket
- Displays:
  - Bracket-by-bracket tax breakdown
  - Marginal tax rate
  - Effective tax rate
  - After-tax income (federal only)
- Clean summary output
- Restartable CLI workflow

## How to Run
Requirements
- Python 3.9+ recommended

Run the program
- tax_calculator.py

Follow the prompts to enter filing status, income, and deductions.

## Example Output
=== Federal Tax Summary ===
- Gross income: $64,200
- Taxable income: $32,700
- Total federal tax: $3,447
- Marginal rate: 12%
- Effective rate: 5.37%

## What This Does NOT Include
- Payroll taxes (FICA)
- State or local taxes
- Credits or phaseouts

## Why I Built This
I wanted a hands-on way to understand how U.S. tax brackets actually work
instead of relying on online calculators. This project helped reinforce and build upon both Python fundamentals and real-world economic concepts.

## Roadmap of Improvemnets
Planned enhancements are tracked in the GitHub Issues tab and include:
- FICA estimates
- Additional fillinf statueses (HOH, MFS)
- State Tax Implementation
- Export results into CSV
