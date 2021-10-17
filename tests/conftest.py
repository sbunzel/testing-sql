import pandas as pd
import pytest
from sqlalchemy import create_engine


@pytest.fixture()
def transactions_df():
    """Creates test transactions - actually, GitHub Copilot created most of these..."""
    return pd.DataFrame(
        {
            "user_id": [1, 1, 1, 2, 2, 2, 3, 3, 3],
            "item_id": [11, 22, 22, 11, 22, 33, 33, 33, 44],
            "amount": [10, 20, 30, 40, 50, 60, 70, 80, 90],
        }
    )


@pytest.fixture()
def items_df():
    """Creates test items"""
    return pd.DataFrame({"item_id": [11, 22, 33, 44], "category": ["A", "A", "B", "B"]})


@pytest.fixture()
def postgres_engine():
    """Creates a local postgres instance"""
    return create_engine(
        "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
    )
