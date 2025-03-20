import json, os, sys, shutil
from pathlib import Path
from _version import __version__

def version():
    print("Home Manager Ricing Mode, "+__version__)
    print()

def usage():
    print("Usage: hmrice <command>")
    print()
    print("Commands:")
    print()
    print(" rice      set all known apps in ricing mode")
    print(" unrice    remove ricing copies and restore nix-store symlinks and set locked mode")
    print(" status    get current rice mode: locked/ricing")
    print(" help      print usage")
    print(" version   print version")

def replace_vars_in_path(mypath):
    return mypath.replace('$HOME', HOMEDIR)

def read_conf():
    conf = {}
    with open(HOMEDIR + '/.config/hm-ricing-mode/apps.json') as f:
        conf = json.load(f)
    return conf

def make_backup_path_from_org(mypath):
   return Path(str(mypath) + ".rice_backup")

def rice_mode_for_path(mypath):

    destpath_rice_mode_backup = make_backup_path_from_org(mypath)

    if(destpath_rice_mode_backup.exists() and mypath.is_dir() ):
        return "RICING"
    else:
        return "MANAGED"

def backup_managed_dir(mypath):
    destpath_rice_mode_backup = make_backup_path_from_org(mypath)
    mypath.rename(destpath_rice_mode_backup)

def restore_managed_dir(mypath):
    destpath_rice_mode_backup = make_backup_path_from_org(mypath)
    destpath_rice_mode_backup.rename(mypath)


# Start your app
def main():

    if (len(sys.argv) == 1):
        print("Err: called without command\n")
        usage()
    else:

        arguments = sys.argv[1:]
        command = arguments[0]

        if command == 'help':
            usage()

        elif command == 'version':
            version()

        elif command == 'rice':

            print("Command: "+command)
            for app, appconf in CONF.items():
                destpath = Path(HOMEDIR + "/" + appconf['dest_dir'])
                if(rice_mode_for_path(destpath) == "MANAGED" ):

                    backup_managed_dir(destpath)

                    if(appconf['type']=="symlink"):
                        sourcepath = Path(replace_vars_in_path(appconf['source_dir']))
                        destpath.symlink_to(sourcepath, target_is_directory=True)

                    elif(appconf['type']=="backport"):
                        destpath_rice_mode_backup = make_backup_path_from_org(destpath)
                        shutil.copytree(destpath_rice_mode_backup, destpath, symlinks=False)

        elif command == 'unrice':
            print(command)

            for app, appconf in CONF.items():
                destpath = Path(HOMEDIR + "/" + appconf['dest_dir'])
                if(rice_mode_for_path(destpath) == "RICING" ):
                    if(destpath.is_symlink()):
                        destpath.unlink()
                        restore_managed_dir(destpath)
                    elif(destpath.is_dir()):
                        shutil.rmtree(destpath)
                        restore_managed_dir(destpath)

        elif command == 'status':
            print("Command: "+command)
            for app, appconf in CONF.items():
                print("\nApp:  "+ app)
                destpath = Path(HOMEDIR + "/" + appconf['dest_dir'])
                print("Path: "+ str(destpath))
                print("Mode: " + rice_mode_for_path(destpath))

        else:
            print("Err: unknown command: "+ command + "\n")
            usage()
            exit

HOMEDIR = os.getenv("HOME")
CONF = read_conf()

if __name__ == "__main__":
    main()

