"""
Main Tax Calculator Application

User interface and application flow for the U.S. Federal Tax Calculator.
Orchestrates user input, validation, and output display.

@author: Craig A. Willits Jr
"""

import calculator
import state_tax


def get_income(filing_status):
    """
    Prompt user for gross income based on filing status.
    
    Args:
        filing_status (str): 'single' or 'mfj'
    
    Returns:
        float: Gross income amount
    """
    if filing_status == "single":
        prompt = "Enter your gross income: "
    elif filing_status == "mfj":
        prompt = "Enter your household gross income: "
    else:
        print("Invalid filing status.")
        return 0.0
    
    raw_income = input(prompt)
    try:
        income = float(raw_income.replace(",", ""))
        return income
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_income(filing_status)


def apply_standard_deduction(filing_status, income):
    """
    Prompt user for deduction choice and calculate taxable income.
    
    Args:
        filing_status (str): 'single' or 'mfj'
        income (float): Gross income
    
    Returns:
        tuple: (taxable_income, deduction_amount, deduction_label)
    """
    choice = input('Do you want to use the standard deduction? (Y/N): ').lower()
    
    if choice == 'y':
        deduction = calculator.get_standard_deduction(filing_status)
        if filing_status == 'single':
            deduction_type = "Standard Deduction (Single)"
        else:
            deduction_type = "Standard Deduction (MFJ)"
    elif choice == 'n':
        raw_deduction = input('Enter your total custom deduction: ')
        try:
            deduction = float(raw_deduction.replace(',', ''))
            deduction_type = 'Custom Deduction'
        except ValueError:
            print("Invalid input. Using standard deduction.")
            return apply_standard_deduction(filing_status, income)
    else:
        print('Invalid choice. Defaulting to standard deduction.')
        deduction = calculator.get_standard_deduction(filing_status)
        if filing_status == "single":
            deduction_type = 'Standard Deduction (Single)'
        else:
            deduction_type = 'Standard Deduction (MFJ)'
    
    taxable_income = income - deduction
    if taxable_income < 0:
        taxable_income = 0
    
    return taxable_income, deduction, deduction_type


def get_and_confirm_income(filing_status):
    """
    Get income from user and confirm before proceeding.
    
    Args:
        filing_status (str): 'single' or 'mfj'
    
    Returns:
        float: Confirmed gross income
    """
    while True:
        income = get_income(filing_status)
        print(f"Income entered: ${income:,.2f}")
        
        confirm = input('Is this correct? (Y/N): ').lower()
        
        if confirm == 'y':
            break
        elif confirm == 'n':
            print('Okay, let\'s re-enter your income.\n')
        else:
            print('Please enter Y or N.\n')
    
    return income


def display_tax_breakdown(breakdown):
    """
    Display federal tax breakdown by bracket.
    
    Args:
        breakdown (list): List of tuples (rate, amount, tax, lower, upper)
    """
    print('Federal Tax Bracket Breakdown')
    print('-' * 50)
    for rate, amount, tax, lower, upper in breakdown:
        upper_text = 'and up' if upper is None else f'${upper:,.0f}'
        print(f'{rate*100:.0f}% on ${lower:,.0f} to {upper_text}: '
              f'taxed ${amount:,.2f} -> ${tax:,.2f}')
    print('-' * 50)


def display_tax_summary(filing_status, income, deduction, deduction_type, 
                        taxable_income, total_tax, state, state_tax, state_label, 
                        marginal_rate, effective_rate, after_tax_income):
    """
    Display comprehensive tax summary.
    
    Args:
        filing_status (str): Filing status
        income (float): Gross income
        deduction (float): Deduction amount
        deduction_type (str): Type of deduction
        taxable_income (float): Taxable income
        total_tax (float): Total federal tax
        state (str): State code
        state_tax (float or None): State tax amount
        state_label (str): State tax label
        marginal_rate (float): Marginal tax rate
        effective_rate (float): Effective tax rate
        after_tax_income (float): Income after federal tax
    """
    print("\n=== Federal Tax Summary (Simplified) ===")
    print(f"Filing status: {filing_status.upper()}")
    print(f"Gross income: ${income:,.2f}")
    print(f"Deduction used: {deduction_type} — ${deduction:,.2f}")
    print(f"Taxable income: ${taxable_income:,.2f}")
    print("--------------------------------------")
    print(f"Total federal income tax: ${total_tax:,.2f}")
    if state_tax is None:
        print(f"State income tax ({state}): {state_label}")
    else:
        print(f"State income tax ({state}): ${state_tax:,.2f} ({state_label})")
    print("--------------------------------------")
    print(f"Marginal tax rate: {marginal_rate*100:.0f}%")
    print(f"Effective tax rate: {effective_rate*100:.2f}%")
    print(f"After-tax income (federal only): ${after_tax_income:,.2f}")


def main():
    """Main application loop."""
    while True:
        # Get filing status
        while True:
            filing_status = input("Please enter your filing status (single/mfj): ").lower()
            if filing_status in ('single', 'mfj'):
                break
            else:
                print("Please enter 'single' or 'mfj'.\n")
        
        # Get and confirm income
        income = get_and_confirm_income(filing_status)
        print('Income confirmed. Moving on...')
        print("\n" + "=" * 40 + "\n")
        
        # Apply deduction
        taxable_income, deduction, deduction_type = apply_standard_deduction(filing_status, income)
        
        print(f"{deduction_type} applied: ${deduction:,.2f}")
        print(f"Your taxable income is: ${taxable_income:,.2f}")
        print('\n' + '-' * 40 + '\n')
        
        # Get state
        state = state_tax.normalize_state(input("Please indicate your state (e.g., TX): "))
        state_tax_amount, state_label = state_tax.calculate_state_tax(taxable_income, state)
        
        print(f"Your taxable income is: ${taxable_income:,.2f}")
        
        # Calculate federal taxes
        brackets = calculator.get_federal_brackets(filing_status)
        total_tax, breakdown = calculator.calculate_tax_breakdown(taxable_income, brackets)
        
        # Display breakdown
        display_tax_breakdown(breakdown)
        print(f"\nTotal federal income tax owed: ${total_tax:,.2f}\n")
        
        # Calculate rates
        marginal_rate = calculator.get_marginal_rate(taxable_income, brackets)
        effective_rate = calculator.calculate_effective_rate(total_tax, income)
        after_tax_income = income - total_tax
        
        # Display rates
        print("=" * 40)
        print(f"\nMarginal tax rate: {marginal_rate * 100:.0f}%")
        print(f"Effective tax rate: {effective_rate * 100:.2f}%")
        print(f"After-tax income (federal only): ${after_tax_income:,.2f}")
        
        # Display summary
        display_tax_summary(
            filing_status, income, deduction, deduction_type, taxable_income,
            total_tax, state, state_tax_amount, state_label,
            marginal_rate, effective_rate, after_tax_income
        )
        
        # Restart prompt
        print()
        again = input("Run another calculation? (Y/N): ").lower()
        if again != "y":
            print("Thank you for using the Tax Calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
