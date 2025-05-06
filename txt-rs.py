import math

input_file = "ascii-animation.txt"
num_frames = 68 
output_file = "ascii_frames.rs"

# Read the ASCII art
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Remove trailing newlines and empty lines
lines = [line.rstrip() for line in lines if line.strip()]
total_lines = len(lines)

# Calculate lines per frame (~56)
lines_per_frame = math.ceil(total_lines / num_frames)

# Split into frames
frames = [lines[i * lines_per_frame:(i + 1) * lines_per_frame] for i in range(num_frames)]

# Generate Rust code
with open(output_file, "w", encoding="utf-8") as f:
    f.write("pub fn get_ascii_frames() -> Vec<Vec<String>> {\n")
    f.write("    vec![\n")
    
    for frame in frames:
        f.write("        vec![\n")
        for line in frame:
            # esccaping backslashes 
            escaped_line = line.replace("\\", "\\\\").replace("\"", "\\\"")
            f.write(f"            \"{escaped_line}\".to_string(),\n")
        f.write("        ],\n")
    
    f.write("    ]\n")
    f.write("}\n")

print(f"Generated {num_frames} frames with ~{lines_per_frame} lines each in {output_file}")