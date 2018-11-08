import cli

if __name__ == '__main__':
    try:
        shell = cli.NsPortalShell()
        shell.cmdloop()
    except KeyboardInterrupt:
        print("Exiting the CLI ...")
