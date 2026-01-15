#!/usr/bin/env python3
import sys
import re

def parse_row(line):
    # Split by pipe, strip whitespace
    parts = [p.strip() for p in line.strip().split('|')]
    # Remove empty first/last elements from split if line starts/ends with pipe
    if parts[0] == '': parts.pop(0)
    if parts[-1] == '': parts.pop()
    return parts

def validate_matrix(filepath):
    print(f"Validating Matrix: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    table_start = -1
    headers = []
    
    # Simple state machine to find the Markdown table
    for i, line in enumerate(lines):
        if "| Criterion |" in line or "| Criteria |" in line:
            table_start = i
            headers = parse_row(line)
            break
            
    if table_start == -1:
        print("Error: Could not find Decision Matrix table (Header starting with '| Criterion |' or '| Criteria |').")
        sys.exit(1)
        
    # We expect columns: Criterion | Weight | Option A (Raw) | Option A (Weighted) | ...
    # Indices: 0=Name, 1=Weight.
    # Logic: For every Option pair (Raw k, Weighted k+1), check if Raw * Weight == Weighted.
    
    errors = 0
    calculated_totals = {} # Map column index to running total
    
    # Skip header and separator line
    row_idx = table_start + 2 
    
    while row_idx < len(lines):
        line = lines[row_idx]
        if not line.strip().startswith("|") or "TOTAL SCORE" in line or "Conclusion" in line:
            break
            
        cols = parse_row(line)
        if len(cols) < 4:
            row_idx += 1
            continue
            
        criterion = cols[0]
        try:
            weight = float(cols[1])
        except ValueError:
            print(f"Warning: Row '{criterion}' has invalid weight '{cols[1]}'. Skipping.")
            row_idx += 1
            continue
            
        # Iterate over option pairs
        # Column 2 starts Option 1 Raw
        current_col = 2
        while current_col < len(cols) - 1:
            try:
                raw_score = float(cols[current_col])
                weighted_score = float(cols[current_col + 1])
                
                expected = raw_score * weight
                
                # Tracking totals
                if (current_col + 1) not in calculated_totals:
                    calculated_totals[current_col + 1] = 0.0
                calculated_totals[current_col + 1] += expected

                if abs(expected - weighted_score) > 0.1:
                    print(f"Math Error at '{criterion}':")
                    print(f"  Option Raw Score: {raw_score}")
                    print(f"  Weight: {weight}")
                    print(f"  Expected: {expected}, Found: {weighted_score}")
                    errors += 1
                    
            except ValueError:
                # Could be content like '-' or empty
                pass
            
            current_col += 2
            
        row_idx += 1

    if errors == 0:
        print("✅ Math Validation Passed! All weighted scores are correct.")
        
        # Print expected totals
        print("\nCalculated Totals (for verification):")
        for col_idx, total in calculated_totals.items():
            header_name = headers[col_idx] if col_idx < len(headers) else f"Col {col_idx}"
            print(f"  {header_name}: {total}")
            
    else:
        print(f"\n❌ Found {errors} math errors.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python score_matrix.py <path_to_matrix.md>")
        sys.exit(1)
    
    validate_matrix(sys.argv[1])
