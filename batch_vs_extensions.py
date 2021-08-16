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
        "huntertran.auto-markdown-toc",
        "aaron-bond.better-comments",
        "ms-vscode.cpptools",
        "formulahendry.code-runner",
        "exodiusstudios.comment-anchors",
        "stackbreak.comment-divider",
        "karyfoundation.comment",
        "hsnazar.hyper-term-theme",
        "marvinengelmann.ibm-theme",
        "shubham-saudolla.lilac",
        "altcoda.lo-fi-loop-theme",
        "ms-toolsai.jupyter",
        "ritwickdey.liveserver",
        "bierner.markdown-preview-github-styles",
        "ntkvu.ninja-ui-vibrant",
        "tinkertrain.theme-panda",
        "esbenp.prettier-vscode",
        "mvllow.rose-pine",
        "webrender.synthwave-x-fluoromachine",
        "this-fifo.vaporwave-theme-vscode",
        "vscodevim.vim",
        "opllama.winny-95",
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
