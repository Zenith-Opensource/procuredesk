# Assigned issues

# Compare delivered costs

A buyer has five quotations for one item and several partially delivered orders. Help the buyer compare delivered costs, see what is overdue and judge supplier reliability.

Expected behavior: For a single order in paise, return units times unit price plus the once-per-order delivery charge.

Reproduce with python3 -m unittest -v from the track directory. Inspect the failing quote examples and trace one input through demo.py. Add one fresh boundary regression and demonstrate the corrected output.


# Identify overdue orders

A buyer has five quotations for one item and several partially delivered orders. Help the buyer compare delivered costs, see what is overdue and judge supplier reliability.

Expected behavior: Day numbers use the same calendar. An order is overdue strictly after its due day when units remain outstanding and the order is active.

Reproduce with python3 -m unittest -v from the track directory. Inspect the failing late examples and trace one input through demo.py. Add one fresh boundary regression and demonstrate the corrected output.


# Explain supplier reliability

A buyer has five quotations for one item and several partially delivered orders. Help the buyer compare delivered costs, see what is overdue and judge supplier reliability.

Expected behavior: Return the percentage of completed orders delivered on time, rounded to one decimal. Return None when no orders are complete. Pending orders are excluded.

Reproduce with python3 -m unittest -v from the track directory. Inspect the failing reliability examples and trace one input through demo.py. Add one fresh boundary regression and demonstrate the corrected output.


