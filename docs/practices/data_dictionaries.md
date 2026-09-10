---
layout: default
title: Describe plotting values
parent: Repository practices
nav_order: 5
---

# Describe the values a figure uses

A figure contract records its categories, values, units, order, and permitted calculations. A collaborator can understand the figure without opening a dataset.

The workshop uses these fixed invented category totals:

| Category, in display order | Group A | Group B |
| --- | ---: | ---: |
| Complete measurements | 42 | 64 |
| Missing height only | 31 | 18 |
| Missing weight only | 18 | 12 |
| Missing height and weight | 9 | 6 |

Each group totals 100; together they total 200. These invented counts live in the source. The [plotting contract](../reference/io_contract.md) and tests protect their labels, group assignments, values, and order. The [figure specifications](../reference/figure-specifications.md) define the presentation to repair.

For another project, agree on the figure's meaning with the analyst and check the source and assertions. Keep study calculations and validation in the approved analysis environment; review what may be shared with an agent.

Start with the [contract template](../templates/data-contract.md).
