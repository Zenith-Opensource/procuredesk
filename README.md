# ProcureDesk

A buyer has five quotations for one item and several partially delivered orders. Help the buyer compare delivered costs, see what is overdue and judge supplier reliability.

Run these commands inside this folder (Python 3.9+, standard library only).

```sh
python3 demo.py
python3 -m unittest -v
```

The demo reads 6,000 synthetic JSONL records. Each record names an operation and its positional inputs. Edit the existing workflow module, keep passing cases green, and add a useful report of your choice. Demonstrate one record before and after your fix.

## Issue 1 · Compare delivered costs

For a single order in paise, return units times unit price plus the once-per-order delivery charge.

## Issue 2 · Identify overdue orders

Day numbers use the same calendar. An order is overdue strictly after its due day when units remain outstanding and the order is active.

## Issue 3 · Explain supplier reliability

Return the percentage of completed orders delivered on time, rounded to one decimal. Return None when no orders are complete. Pending orders are excluded.

## How to contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for the fork, branch and pull request workflow.

Complete [approach.md](approach.md), [challenges.md](challenges.md) and [optimizations.md](optimizations.md).
