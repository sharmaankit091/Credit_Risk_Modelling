# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 04:12:41 2022

@author: Ankit Sharma
"""

import pandas as pd
import pytest
from src.models import my_model as mcrm


class TestMyModel:
    def test_my_credit_risk_model(self):
        accounts_customer = pd.DataFrame(
            dict(
                age=range(20, 31)
            )
        )

        pd_pit = mcrm.my_credit_risk_model(accounts_customer)
        pd.testing.assert_series_equal(pd_pit, pd.Series(1., name="pd_pit"))
