"""
State Income Tax Module

Provides state tax data and calculation functions for all 50 states.
Supports: no state income tax, flat tax, and graduated (progressive) tax systems.
"""

# 2025 State Income Tax System Types
STATE_TAX_TYPE_2025 = {
    'AK': 'none', 'AL': 'graduated', 'AR': 'graduated', 'AZ': 'flat',
    'CA': 'graduated', 'CO': 'flat', 'CT': 'graduated', 'DC': 'graduated',
    'DE': 'graduated', 'FL': 'none', 'GA': 'flat', 'HI': 'graduated',
    'IA': 'flat', 'ID': 'flat', 'IL': 'flat', 'IN': 'flat',
    'KS': 'graduated', 'KY': 'flat', 'LA': 'flat', 'MA': 'graduated',
    'MD': 'graduated', 'ME': 'graduated', 'MI': 'flat', 'MN': 'graduated',
    'MO': 'graduated', 'MS': 'flat', 'MT': 'graduated', 'NC': 'flat',
    'ND': 'graduated', 'NE': 'graduated', 'NH': 'none', 'NJ': 'graduated',
    'NM': 'graduated', 'NV': 'none', 'NY': 'graduated', 'OH': 'graduated',
    'OK': 'graduated', 'OR': 'graduated', 'PA': 'flat', 'RI': 'graduated',
    'SC': 'graduated', 'SD': 'none', 'TN': 'none', 'TX': 'none',
    'UT': 'flat', 'VA': 'graduated', 'VT': 'graduated', 'WA': 'flat',
    'WI': 'graduated', 'WV': 'graduated', 'WY': 'none',
}

# State name to abbreviation mapping
STATE_ALIASES = {
    'TEXAS': 'TX',
    'FLORIDA': 'FL',
    'NEVADA': 'NV',
    'WASHINGTON': 'WA',
    'ALASKA': 'AK',
    'NEW HAMPSHIRE': 'NH',
    'SOUTH DAKOTA': 'SD',
    'TENNESSEE': 'TN',
    'WYOMING': 'WY',
}


def normalize_state(user_input: str) -> str:
    """
    Convert state input to two-letter abbreviation.
    Handles full state names and ensures uppercase.
    
    Args:
        user_input (str): User-entered state (abbreviation or full name)
    
    Returns:
        str: Two-letter state abbreviation in uppercase
    """
    s = user_input.strip().upper()
    return STATE_ALIASES.get(s, s)


def get_state_tax_type(state_code: str) -> str:
    """
    Get the tax system type for a given state.
    
    Args:
        state_code (str): Two-letter state abbreviation
    
    Returns:
        str: 'none', 'flat', 'graduated', or 'unknown'
    """
    return STATE_TAX_TYPE_2025.get(state_code, 'unknown')


def calculate_state_tax(taxable_income: float, state_code: str):
    """
    Calculate state income tax for given income and state.
    Currently implements 'none' states only.
    
    Args:
        taxable_income (float): Taxable income after deductions
        state_code (str): Two-letter state abbreviation
    
    Returns:
        tuple: (state_tax_or_None, label_str)
            - state_tax_or_None: Dollar amount or None if not implemented
            - label_str: Description of tax status or reason not calculated
    """
    tax_type = get_state_tax_type(state_code)

    if tax_type == 'none':
        return 0.0, 'No state income tax'

    if tax_type == 'flat':
        return None, 'N/A (flat tax not yet implemented)'

    if tax_type == 'graduated':
        return None, 'N/A (graduated tax not yet implemented)'

    return None, 'N/A (unknown/unsupported state)'


# Legacy function name for backward compatibility
def calculate_state_tax_none_only(taxable_income: float, state_code: str):
    """Deprecated: use calculate_state_tax() instead."""
    return calculate_state_tax(taxable_income, state_code)

