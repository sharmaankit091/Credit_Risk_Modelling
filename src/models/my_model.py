# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 04:12:41 2022

@author: Ankit Sharma
"""

import pandas as pd


def my_credit_risk_model(accounts_customer: pd.DataFrame) -> pd.Series:
    """
    Dummy function to calculate Probability of Default (PD)

    Args:
        accounts_customer: Input Customer Data

    Returns:
        Pandas Series holding Probability of Default (PD)

    """
    return pd.Series(1., name="pd_pit")
