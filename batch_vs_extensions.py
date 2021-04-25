def batch_vs():
    """
    code --extensions-dir <dir>
        Set the root path for extensions.
    code --list-extensions
        List the installed extensions.
    code --show-versions
        Show versions of installed extensions, when using --list-extension.
    code --install-extension (<extension-id> | <extension-vsix-path>)
        Installs an extension.
    code --uninstall-extension (<extension-id> | <extension-vsix-path>)
        Uninstalls an extension.
    code --enable-proposed-api (<extension-id>)
        Enables proposed API features for extensions. Can receive one or more extension IDs to enable individually.
    """

    extensions = [
        "kevinkyang.auto-comment-blocks",
        "aaron-bond.better-comments",
        "ms-vscode.cpptools",
        "formulahendry.code-runner",
        "exodiusstudios.comment-anchors",
        "stackbreak.comment-divider",
        "karyfoundation.comment",
        "ms-toolsai.jupyter",
        "ritwickdey.liveserver",
        "ms-python.python",
        "maptz.regionfolder",
        "igress.python-coding-conventions",
        "msjsdiag.debugger-for-chrome",
    ]

    import os
    os.system("export PATH='$PATH:/snap/bin'")
    for _ in extensions:
        os.system("code --install-extension " + _.strip())
        print("[+] INSTALLING:    " + _)
        print()


if __name__ == "__main__":
    batch_vs()