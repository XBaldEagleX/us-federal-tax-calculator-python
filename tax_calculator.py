"""
Created on Tue Feb  3 17:34:35 2026

Title: Simple U.S. Federal Income Tax Bracket Calculator

@author: Craig A. Willits Jr

What it does:
- Select filing status: single or married filing jointly
- Enter gross income
- Choose standard deduction (default) or custom deduction
- Computes taxable income (simplified) and progressive tax per bracket
- Prints marginal bracket, bracket-by-bracket taxes, total tax, effective rate

Notes:
- This is federal INCOME tax only (no FICA, no state tax, no credits).
- Brackets and standard deductions are sourced from IRS releases. See citations in your post.
"""

while True:
# Define our income
    def get_income(filing_status):
        if filing_status == "single":
            raw_income = input("Enter your gross income: ")
        elif filing_status == "mfj":
            raw_income = input("Enter your household gross income: ")
        else:
            print("Invalid filing status.")
            return 0.0
    
        income = float(raw_income.replace(",", ""))
        return income
    
    # Input filing status
    filing_status = input("Please enter if you are filing single or mfj: ").lower()
    
    # Confirmation loop
    while True:
        income = get_income(filing_status)
        print(f"Income entered: ${income:,.2f}")
        
        confirm = input('Is this the correct? (Y/N): ').lower()
        
        if confirm == 'y':
            break
        elif confirm == 'n':
            print('Okay lets re-enter your income.\n')
        else:
            print('Please enter Y or N.\n')
            
    print('Income confirmed. Moving on...')
    print('')
    
    # Account for Standard Deduction
    def apply_standard_deduction(filing_status, income):
        choice = input('Do you want to use the standard deduction? (Y/N): ').lower()
        
        if choice == 'y':
            if filing_status == 'single':
                deduction = 15750
                deduction_type = "Standard Deduction (Single)"
            elif filing_status == 'mfj':
                deduction = 31500
                deduction_type = "Standard Deduction (MFJ)"
            else:
                print('Invalid filing status.')
                return 0.0, 0.0, 'invalid'
        elif choice == 'n':
            raw_deduction = input('Enter your total custom deduction: ')
            deduction = float(raw_deduction.replace(',', ''))
            deduction_type = 'Custom Deduction'
            
        else:
            print('Invalid choice. Defaulting to standard deduction.')
            if filing_status == "single":
                deduction = 15750
                deduction_type = 'Standard Deduction (Single)'
            else:
                deduction = 31500
                deduction_type = 'Standard Deduction (MFJ)'
            
        taxable_income = income - deduction
        if taxable_income < 0:
            taxable_income = 0
            
        return taxable_income, deduction, deduction_type
        
    taxable_income, deduction, deduction_type = apply_standard_deduction(filing_status, income)
    
    print(f"{deduction_type} applied: ${deduction:,.2f}")
    print('')
    print(f"Your Taxable income is: ${taxable_income:,.2f}")
    
    # Federal tax bracket libary
    brackets_single = [
        (0.10, 0 ,11925),
        (0.12, 11925, 48475),
        (0.22, 48475, 103350),
        (0.24, 103350, 197300),
        (0.32, 197300, 250525),
        (0.35, 250525, 626350),
        (0.37, 626350, None),
        ]
    
    brackets_mfj = [
        (0.10, 0 ,23850),
        (0.12, 23850, 96950),
        (0.22, 96950, 206700),
        (0.24, 206700, 394600),
        (0.32, 394600, 501050),
        (0.35, 501050, 751600),
        (0.37, 751600, None),
        ]
    
    if filing_status == "single":
        brackets = brackets_single
    elif filing_status == "mfj":
        brackets = brackets_mfj
    else:
        brackets = []
        
        
    # Calculate tax from libary 
    def calculate_total_tax(taxable_income, brackets):
        total_tax = 0.0
    
        for rate, lower, upper in brackets:
            if taxable_income <= lower:
                break
    
            # If upper is None, it means "no cap"
            cap = taxable_income if upper is None else min(taxable_income, upper)
    
            amount_in_bracket = cap - lower
            tax_for_bracket = amount_in_bracket * rate
            total_tax += tax_for_bracket
    
        return total_tax
    
    
    def calculate_tax_breakdown(taxable_income, brackets):
        total_tax = 0.0
        breakdown = []  # each item: (rate, amount_taxed, tax_for_bracket, lower, upper)
    
        for rate, lower, upper in brackets:
            if taxable_income <= lower:
                break
    
            cap = taxable_income if upper is None else min(taxable_income, upper)
            amount_in_bracket = cap - lower
    
            if amount_in_bracket > 0:
                tax_for_bracket = amount_in_bracket * rate
                total_tax += tax_for_bracket
                breakdown.append((rate, amount_in_bracket, tax_for_bracket, lower, upper))
    
        return total_tax, breakdown
    
    total_tax, breakdown = calculate_tax_breakdown(taxable_income, brackets)
    
    print(f"\nTotal federal income tax owed: ${total_tax:,.2f}")
    print("\n--- Bracket Breakdown ---")
    for rate, amount, tax, lower, upper in breakdown:
        upper_text = "and up" if upper is None else f"${upper:,.0f}"
        print(f"{rate*100:.0f}% on ${lower:,.0f} to {upper_text}: "
              f"taxed ${amount:,.2f} -> ${tax:,.2f}")
    
    # Marginal Rate
    def get_marginal_rate(taxable_income, brackets):
        marginal_rate = 0.0
    
        for rate, lower, upper in brackets:
            if taxable_income > lower:
                marginal_rate = rate
            else:
                break
    
        return marginal_rate
    
    # Call marginal rate
    marginal_rate = get_marginal_rate(taxable_income, brackets)
    print(f"\nMarginal tax rate: {marginal_rate * 100:.0f}%")
    
    # Effective rate
    effective_rate = total_tax / income if income > 0 else 0
    print(f"Effective tax rate: {effective_rate * 100:.2f}%")
    
    # Post tax income
    after_tax_income = income - total_tax
    print(f"After-tax income (federal only): ${after_tax_income:,.2f}")
    
    
    # Summary overall clean layout
    print("\n=== Federal Tax Summary (Simplified) ===")
    print(f"Filing status: {filing_status.upper()}")
    print(f"Gross income: ${income:,.2f}")
    print(f"Deduction used: {deduction_type} — ${deduction:,.2f}")
    print(f"Taxable income: ${taxable_income:,.2f}")
    print("--------------------------------------")
    print(f"Total federal income tax: ${total_tax:,.2f}")
    print(f"Marginal tax rate: {marginal_rate*100:.0f}%")
    print(f"Effective tax rate: {effective_rate*100:.2f}%")
    print(f"After-tax income (federal only): ${after_tax_income:,.2f}")
    
    
    # Restart the program
    again = input("\nRun another calculation? (Y/N): ").lower()
    if again != "y":
        break
