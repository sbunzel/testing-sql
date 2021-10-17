# Testing SQL

[![tests](https://github.com/sbunzel/testing-sql/actions/workflows/tests.yml/badge.svg)](https://github.com/sbunzel/testing-sql/actions/workflows/tests.yml)

A minimal example of how to test SQL queries in Python.

This example illustrates testing SQL queries using Python's testing framework [pytest](https://docs.pytest.org/en/latest/). It was built with the following setup in mind:

* You're working on a Python application that reads data from a SQL database.
* You want to run non-trivial data preparation logic in the SQL layer.
* What happens afterwards in the Python application doesn't matter for this example.

The example shows how to:

* Set up a local test database (using PostgreSQL in this example), in a VSCode [devcontainer](https://code.visualstudio.com/docs/remote/containers) and in continuous integration (using GitHub Actions).
* Define test data for unit tests of logic in SQL queries.
* Run unit tests on the test database.

## But - why?

When I started using more data from SQL databases in my Python applications, I was wondering how I could apply the best practices I had learned about testing Python code to SQL queries. This example consolidates the gist of the approach I've ended up using. Hopefully, it's a good starting point for you to try out testing your own SQL code.

## Resources

* [Blog post](https://ianwhitestone.work/testing-sql/) on testing SQL by [@ianwhitestone](https://twitter.com/ianwhitestone) I drew a lot of inspiration from
* [Creating PostgreSQL service containers in GitHub Actions](https://docs.github.com/en/actions/using-containerized-services/creating-postgresql-service-containers)
* [Devcontainer template for Python & PostgreSQL](https://github.com/microsoft/vscode-dev-containers/tree/main/containers/python-3-postgres)

## Contact

[Steffen Bunzel](https://steffenbunzel.com/contact/)
