'''
Federal Tax Calculation Module

Handles all federal income tax calculations including:
- Tax bracket logic
- Marginal and effective rate calculations
- Tax breakdown by bracket
'''

# 2025 Federal Tax Brackets and Standard Deductions
STANDARD_DEDUCTIONS = {
    'single': 15750,
    'mfj': 31500
}

FEDERAL_TAX_BRACKETS = {
    'single': [
        (0.10, 0, 11925),
        (0.12, 11925, 48475),
        (0.22, 48475, 103350),
        (0.24, 103350, 197300),
        (0.32, 197300, 250525),
        (0.35, 250525, 626350),
        (0.37, 626350, None),
    ],
    'mfj': [
        (0.10, 0, 23850),
        (0.12, 23850, 96950),
        (0.22, 96950, 206700),
        (0.24, 206700, 394600),
        (0.32, 394600, 501050),
        (0.35, 501050, 751600),
        (0.37, 751600, None),
    ]
}


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
    breakdown = []

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


def get_marginal_rate(taxable_income, brackets):
    marginal_rate = 0.0

    for rate, lower, upper in brackets:
        if taxable_income > lower:
            marginal_rate = rate
        else:
            break

    return marginal_rate


def calculate_effective_rate(total_tax, gross_income):
    if gross_income <= 0:
        return 0.0
    return total_tax / gross_income


def get_federal_brackets(filing_status):
    return FEDERAL_TAX_BRACKETS.get(filing_status, [])


def get_standard_deduction(filing_status):
    return STANDARD_DEDUCTIONS.get(filing_status, 0.0)

