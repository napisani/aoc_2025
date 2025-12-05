# Advent of Code 2025

Solutions for Advent of Code 2025.

## Project Structure

```
.
├── day01/
│   └── main.go         # Go solution for day 1
├── day02/
│   └── main.py         # Python solution for day 2
├── day03/
│   └── main.go         # Go solution for day 3
├── day04/
│   └── main.py         # Python solution for day 4
├── day05/
│   └── main.exs        # Elixir solution for day 5
└── input/
    ├── day1.txt
    ├── day2.txt
    ├── day3.txt
    ├── day4.txt
    └── day5.txt
```

Each day has its own directory with a `main` file in the appropriate language. This structure allows you to have multiple `main()` functions in Go without package conflicts, and keeps solutions organized by day.

## Running Solutions

### Go Solutions

Run a Go solution from the project root:

```bash
go run ./day01
go run ./day03
```

Or navigate to the day's directory:

```bash
cd day01
go run .
```

### Python Solutions

Run a Python solution from the project root:

```bash
python day02/main.py
python day04/main.py
```

Or navigate to the day's directory:

```bash
cd day02
python main.py
```

### Elixir Solutions

Run an Elixir solution from the project root:

```bash
elixir day05/main.exs
```

Or navigate to the day's directory:

```bash
cd day05
elixir main.exs
```

## Adding New Days

To add a new day:

1. Create a new directory: `dayXX/` (with zero-padded number, e.g., `day06`, `day15`)
2. Create your solution file:
   - Go: `main.go`
   - Python: `main.py`
   - Elixir: `main.exs`
3. Add the input file to `input/dayX.txt`
4. Use relative path `../input/dayX.txt` to read the input file

### Language-Specific Notes

**Go**: Each day is its own package with its own `main()` function. Run with `go run ./dayXX`

**Python**: Standard Python scripts. Run with `python dayXX/main.py`

**Elixir**: Use `.exs` (Elixir Script) files for standalone scripts. The `__DIR__` variable helps locate the input files. Run with `elixir dayXX/main.exs`
