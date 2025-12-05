defmodule Day05 do
  def solve() do
    # Read input file
    input_path = Path.join([File.cwd!(), "input", "day5.txt"])

    lines =
      input_path
      |> File.read!()
      |> String.trim()
      |> String.split("\n", trim: true)

    # Example solution - process the input
    result = process(lines)

    IO.puts("Result: #{result}")
  end

  defp process(lines) do
    # Your solution logic here
    length(lines)
  end
end
