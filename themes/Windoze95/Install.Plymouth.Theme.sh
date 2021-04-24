sudo cp -rf ./Windoze95 /lib/plymouth/themes && sudo update-alternatives --install /lib/plymouth/themes/default.plymouth default.plymouth /lib/plymouth/themes/Windoze95/Windoze95.plymouth 100 && sudo update-alternatives --config default.plymouth && sudo update-initramfs -u && sudo reboot


