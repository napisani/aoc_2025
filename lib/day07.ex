defmodule Day07 do
  defp process(lines, idx) when idx == 0 do
    IO.puts("Processing line first #{idx}")
    line = Map.get(lines, idx)
    line |> Enum.map(&if &1 == ?S, do: ?|, else: &1)
    Map.put(lines, idx, line)
  end

  defp process(lines, idx) do
    IO.puts("Processing line #{idx}")

    line = Map.get(lines, idx)
    last_line = Map.get(lines, idx - 1)

    new_line =
      Enum.zip(line, last_line)
      |> Enum.map(fn {a, b} ->
        if b == ?| and a == ?^ do
          ?X
        else
          a
        end
      end)

    Map.put(lines, idx, new_line)
  end

  def print_lines(lines) do
    lines
    |> Enum.each(fn line ->
      line |> Enum.each(fn char -> IO.write(<<char>>) end)
      IO.puts("")
    end)
  end

  def solve() do
    # Read input file
    input_path = Path.join([__DIR__, "..", "input", "day7.txt"])

    lines =
      input_path
      |> File.read!()
      |> String.trim()
      |> String.split("\n", trim: true)
      |> Enum.map(&String.to_charlist/1)

    IO.puts(IO.inspect(lines))
    print_lines(lines)

    new_lines =
      lines
      |> Enum.with_index()
      |> Enum.reduce(%{}, fn {line, idx}, acc ->
        Map.put(acc, idx, line)
      end)

    processed_lines =
      new_lines
      |> Enum.reduce(fn a ->
        IO.puts("Processing line #{a}")
       a 
      end)

    IO.puts("New Lines:")

    IO.puts(IO.inspect(processed_lines))
    # # Example solution - process the input
    # lines |> Enum.each(&IO.inspect/1)
    # IO.puts("")
    # new_lines |> Enum.each(&IO.inspect/1)
  end
end

# Run the solution
Day05.solve()
