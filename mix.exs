defmodule Aoc2025.MixProject do
  use Mix.Project

  def project do
    [
      app: :aoc_2025,
      version: "0.1.0",
      elixir: "~> 1.14",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  def application do
    [
      extra_applications: [:logger]
    ]
  end

  defp deps do
    [
      # Add any dependencies you need for AoC here
      # {:dep_name, "~> 1.0"}
    ]
  end
end
