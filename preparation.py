def sales_by_category_pd(transactions, items):
    return (
        transactions.merge(items, on="item_id")
        .groupby(["category"])
        .agg(amount=("amount", "sum"))
        .sort_values("amount", ascending=False)
        .reset_index()
    )
