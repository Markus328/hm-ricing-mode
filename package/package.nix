{ lib
, python3Packages
#, python
, ...
 }:

python3Packages.buildPythonApplication rec {
  pname = "hm-ricing-mode";
  version = "0.1.0";

  src = ./..;

  #dependencies = [(python.withPackages (ps: with ps; [
  #]))];

  meta = {
    homepage = "https://github.com/mipmip/hm-ricing-mode";
    license = lib.licenses.mit;
    maintainers = with lib.maintainers; [ mipmip ];
  };
}
