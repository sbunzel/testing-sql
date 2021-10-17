import pandas as pd
from testing_sql.preparation import sales_by_category_pd, sales_by_category_sql


def test_sales_by_category_pd(transactions_df, items_df):
    # Test data for transactions and items is defined as fixtures in conftest.py
    expected = pd.DataFrame({"category": ["B", "A"], "amount": [300, 150]})

    # Call the pandas version of the function on our test data
    result = sales_by_category_pd(transactions_df, items_df)

    # Assert that the result is what we expect
    pd.testing.assert_frame_equal(result, expected)


def test_sales_by_category_sql(postgres_engine, transactions_df, items_df):
    # Write the test data to our local Postgres database
    transactions_df.to_sql(
        name="transactions", con=postgres_engine, if_exists="replace"
    )
    items_df.to_sql(name="items", con=postgres_engine, if_exists="replace")
    # Define the expected result
    expected = pd.DataFrame({"category": ["B", "A"], "amount": [300, 150]})

    # Call the SQL version of the function on our test data and get the result as a dataframe
    query = sales_by_category_sql()
    result = pd.read_sql(query, postgres_engine)

    # Assert that the result is what we expect
    pd.testing.assert_frame_equal(
        result, expected, check_dtype=False
    )  # TODO: Check dtypes
