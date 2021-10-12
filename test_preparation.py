import pandas as pd
import pytest
from sqlalchemy import create_engine

from preparation import sales_by_category_pd


@pytest.fixture()
def transactions_df():
    return pd.DataFrame(
        {
            "user_id": [1, 1, 1, 2, 2, 2, 3, 3, 3],
            "item_id": [11, 22, 22, 11, 22, 33, 33, 33, 44],
            "amount": [10, 20, 30, 40, 50, 60, 70, 80, 90],
        }
    )


@pytest.fixture()
def items_df():
    return pd.DataFrame({"item_id": [11, 22, 33, 44], "category": ["A", "A", "B", "B"]})


@pytest.fixture()
def expected():
    return pd.DataFrame({"category": ["B", "A"], "amount": [300, 150]})


def test_sales_by_category_pd(transactions_df, items_df, expected):
    result = sales_by_category_pd(transactions_df, items_df)
    pd.testing.assert_frame_equal(result, expected)


def test_sales_by_category_sql(transactions_df, items_df, expected):
    engine = create_engine(
        "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
    )
    transactions_df.to_sql(name="transactions", con=engine, if_exists="replace")
    items_df.to_sql(name="items", con=engine, if_exists="replace")
    sql = """
        WITH transactions_category_amounts AS (
            SELECT t.user_id, i.category, t.amount
            FROM transactions AS t
            JOIN items AS i
            ON t.item_id = i.item_id
        )
        SELECT category, SUM(amount) AS amount
        FROM transactions_category_amounts
        GROUP BY category
        ORDER BY amount DESC;
    """
    result = pd.read_sql(sql, con=engine)
    pd.testing.assert_frame_equal(result, expected, check_dtype=False)
