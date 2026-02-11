"""
Created on Wed Feb  4 14:21:53 2026

Title: State Tax Libary

@author: Craig A. Willits Jr



v1.0.5: State tax (NONE-only)
"""

# 2025 state income tax system typev1.0.5: State tax (NONE-only)
# 'none' = no state income tax
# 'flat' = flat income tax
# 'graduated' = bracketed income tax

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
    s = user_input.strip().upper()
    return STATE_ALIASES.get(s, s)

def calculate_state_tax_none_only(taxable_income: float, state_code: str):
    """
    v1.0.5 behavior:
      - If state has NO income tax ('none'): return $0.00 + label
      - Otherwise: return None (N/A) + label, and skip calculation
    Returns: (state_tax_or_None, label)
    """
    tax_type = STATE_TAX_TYPE_2025.get(state_code)

    if tax_type == 'none':
        return 0.0, 'No state income tax'

    if tax_type in ('flat', 'graduated'):
        return None, 'N/A (not implemented yet)'

    return None, 'N/A (unknown/unsupported state)'

