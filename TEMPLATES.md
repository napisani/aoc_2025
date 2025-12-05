# Templates

Quick start templates for each language.

## Elixir Template (main.exs)

```elixir
defmodule DayXX do
  def solve() do
    # Read input file
    input_path = Path.join([__DIR__, "..", "input", "dayX.txt"])
    
    lines =
      input_path
      |> File.read!()
      |> String.trim()
      |> String.split("\n", trim: true)
    
    # Part 1
    part1_result = part1(lines)
    IO.puts("Part 1: #{part1_result}")
    
    # Part 2
    part2_result = part2(lines)
    IO.puts("Part 2: #{part2_result}")
  end
  
  defp part1(lines) do
    # Your part 1 solution here
    0
  end
  
  defp part2(lines) do
    # Your part 2 solution here
    0
  end
end

# Run the solution
DayXX.solve()
```

## Go Template (main.go)

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	fileName := "../input/dayX.txt"
	file, err := os.Open(fileName)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	
	scanner := bufio.NewScanner(file)
	lines := []string{}
	
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	
	if err := scanner.Err(); err != nil {
		panic(err)
	}
	
	// Your solution here
	fmt.Println("Part 1:", part1(lines))
	fmt.Println("Part 2:", part2(lines))
}

func part1(lines []string) int {
	// Your part 1 solution here
	return 0
}

func part2(lines []string) int {
	// Your part 2 solution here
	return 0
}
```

## Python Template (main.py)

```python
def part1(lines):
    # Your part 1 solution here
    return 0

def part2(lines):
    # Your part 2 solution here
    return 0

def main():
    with open("../input/dayX.txt") as f:
        lines = f.read().strip().split("\n")
    
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

if __name__ == "__main__":
    main()
```
