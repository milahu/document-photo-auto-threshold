{
  pkgs ? import <nixpkgs> {}
}:

let
  my-python = pkgs.python38;
  my-python-packages = python-packages: with python-packages; [
    numpy
    opencv3
    #opencv4
    scikitimage # skimage
    Wand # wand = imagemagick bindings
  ]; 
  python-with-my-packages = my-python.withPackages my-python-packages;
in

python-with-my-packages.env # replacement for pkgs.mkShell

/*
pkgs.mkShell {
  buildInputs = [ python-with-my-packages ];
  shellHook = ''
    PYTHONPATH=${python-with-my-packages}/lib/python3.9/site-packages
  '';
}
*/
