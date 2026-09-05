---
layout: default
title: Maintain data dictionaries
parent: Repository practices
nav_order: 5
---

# Maintain data dictionaries

A data dictionary helps a collaborator understand a table without tracing the code that produced it. For each column, explain its type, units, possible missing values, allowed categories, and how it was derived.

Small details matter. Read identifiers as strings so leading zeros survive, and say which date an age refers to. In this example, the demographic `age` is age on December 31, 2019; it can differ from age at the selected measurement.

The R simulator generates the input dictionaries, and the Python pipeline writes a dictionary for the cleaned output. The [data contract](../reference/io_contract.md) explains rules that span columns or rows, such as unique identifiers and the choice of a representative measurement.

When you change a column, update its contract, the code that generates its dictionary, affected tests, and any downstream code that reads it. Compare the written TSV with the dictionary to check that they agree. If a unit or scientific threshold is unclear, resolve its meaning with the person responsible for the analysis before encoding an assumption.

The [contract template](../templates/data-contract.md) gives you a starting point for a new dataset or an extension to this example.
