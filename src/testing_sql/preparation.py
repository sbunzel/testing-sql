import pandas as pd


def sales_by_category_pd(
    transactions: pd.DataFrame, items: pd.DataFrame
) -> pd.DataFrame:
    """Groups transactions by category and sums the amounts.

    Args:
        transactions (pd.DataFrame): Transactions dataframe.
        items (pd.DataFrame): Items dataframe with category information.

    Returns:
        pd.DataFrame: Dataframe of sums of amounts by category.
    """

    return (
        transactions.merge(items, on="item_id")
        .groupby(["category"])
        .agg(amount=("amount", "sum"))
        .sort_values("amount", ascending=False)
        .reset_index()
    )


def sales_by_category_sql() -> str:
    """Returns a SQL query to get the sales amount by category."""

    query = """
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
    return query
