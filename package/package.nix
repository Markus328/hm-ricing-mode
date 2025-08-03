{ lib , python3Packages , ... }:

python3Packages.buildPythonApplication rec {
  pname = "hm-ricing-mode";
  version = "0.1.0";

  src = ./..;

  meta = let
    mipmip = {
      name = "Pim Snel";
      email = "post@pimsnel.com";
      github = "mipmip";
      githubId = 658612;
    }; 
  in {
    homepage = "https://github.com/mipmip/hm-ricing-mode";
    license = lib.licenses.mit;
    maintainers = [ mipmip ];
  };
}
