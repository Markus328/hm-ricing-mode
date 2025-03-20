{ lib , python3Packages , ... }:

python3Packages.buildPythonApplication rec {
  pname = "hm-ricing-mode";
  version = "0.1.0";

  src = ./..;

  mipmip = {
    name = "Pim Snel";
    email = "post@pimsnel.com";
    github = "mipmip";
    githubId = 658612;
  };

  meta = {
    homepage = "https://github.com/mipmip/hm-ricing-mode";
    license = lib.licenses.mit;
    maintainers = [ mipmip ];
  };
}
