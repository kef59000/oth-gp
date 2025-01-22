#!/bin/bash

# Create output file
output_file="notebook_contents.txt"
>"$output_file"

# Find all .ipynb files recursively and process them
find . -type f -name "*.ipynb" | while read -r notebook; do
  # Create a header with the file path
  echo "=== $notebook ===" >>"$output_file"
  echo "" >>"$output_file"

  # Extract and format JSON content
  cat "$notebook" | jq '.' >>"$output_file"

  # Add separator between files
  echo -e "\n\n" >>"$output_file"
done

echo "Extraction complete. Results saved to $output_file"
