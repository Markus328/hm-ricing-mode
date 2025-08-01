{
  lib,
  python3Packages,
  ...
}: let
  mipmip = {
    name = "Pim Snel";
    email = "post@pimsnel.com";
    github = "mipmip";
    githubId = 658612;
  };
in
  python3Packages.buildPythonApplication {
    pname = "hm-ricing-mode";
    version = "0.1.0";

    src = ./..;

    meta = {
      homepage = "https://github.com/mipmip/hm-ricing-mode";
      license = lib.licenses.mit;
      maintainers = [mipmip];
    };
  }
