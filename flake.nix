{
  description = "Advent of Code 2025 development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in {
        devShells.default = pkgs.mkShell {
          name = "aoc-2025";
          packages = with pkgs; [
            deno
            zig
            ruby_3_3
            go
          ];
          
          shellHook = ''
            unset DEVELOPER_DIR
          '';
        };
      });
}
