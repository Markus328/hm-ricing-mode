# HM Rice

HM Ricing Mode is a utility to put Home Manager managed apps in ricing mode.

When tweaking your applications you need instant feedback. Change a setting in a
dotfile; reload the application and see if it worked. Having to build all
home-manager nix files take way too long to give this instant feedback.

**HM Ricing Mode** helps. When running `hmrice rice`, it replaces the Nix-store symlinks
with an temporary editable copy of all the files for debugging and ricing
purposes. When your finished, and backported the changes into the nix-files in
home-manager, the command `hmrice unrise` restores the original nix-symlinks.

## INSTALL

```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    home-manager.url = "github:nix-community/home-manager";
    hm-ricing-mode.url = "github:mipmip/hm-ricing-mode";
  };

  outputs = { nixpkgs, home-manager, hm-ricing-mode, ... }: {
    homeConfigurations."«username»" = home-manager.lib.homeManagerConfiguration {
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
      modules = [ hm-ricing-mode.homeManagerModules.hm-ricing-mode ];
    };
  };
}
```

## CONFIGURATION

You need to enable hm-ricing-mode. Add this to your Home Manager configuration:

```nix
programs.hm-ricing-mode.enable = true;
```

Every application which you want to allow in ricing mode should be added to the `apps` option.

When you have implemented the app-configuration using nix options. You should
choose the `backport` type. hmrice will then make a static copy and replace all
symlinks with real files.

```nix
{
    programs.hm-ricing-mode.apps.ghostty = {
      dest_dir = ".config/ghostty";
      type = "backport"; # symlink | backport (default)
    };
}
```

When you have implemented the app-configuration with the
`home.file.recursive=true` method. You can choose the symlink-type. This saves
you the need of backporting all changes into Nix configuration. You should set
a correct source_dir where your original files are located.

```nix
{
  programs.hm-ricing-mode.apps.neovim = {
    dest_dir = ".config/nvim";
    source_dir = "$HOME/nixos/home/pim/_hm-modules/programs/neovim/nvim";
    type = "symlink"; # symlink | backport (default)
  };
}
```

## USAGE

```
Usage: hmrice <command>

Commands:

 rice      set all known apps in ricing mode
 unrice    remove ricing copies and restore nix-store symlinks and set locked mode
 status    get current rice mode: managed/ricing
 help      print usage
 version   print version
```

## CONTRIBUTE

### Issues, Bugs, and Feature Requests

File issue requests [in this repo](https://github.com/mipmip/hmrice/issues/new)

### Open Source & Contributing

HM-Ricing-Mode is open source and we appreciate contributions and positive feedback.

### Docs for Project Maintainers

Read the docs and roadmaps

- [Release runbook](RELEASE-RUNBOOK.md)
- [Roadmap](TODO.md)
- [Changelog](CHANGELOG.md)

## License and Copyright

Copyright 2025 Pim Snel | Published under the [MIT](LICENSE).
