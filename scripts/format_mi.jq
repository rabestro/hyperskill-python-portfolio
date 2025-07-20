# Define headers for the Markdown table
["File", "MI Score", "Rank"],
["-", "-", "-"],

# Process the JSON input from radon
# 1. Convert the top-level object to key-value entries
# 2. For each entry, create an array with the file, formatted score, and rank
# 3. Format the output as Tab-Separated Values (TSV)
(to_entries[] | [.key, ((.value.mi * 100 | round) / 100), .value.rank]) | @tsv
