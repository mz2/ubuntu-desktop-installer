#!/usr/bin/env bash
/usr/bin/swtpm socket --ctrl type=unixio,path=vm/win11.swtpm-sock --terminate --tpmstate dir=vm --tpm2 &
/usr/bin/qemu-system-x86_64 -name win11,process=win11 -pidfile vm/win11.pid -enable-kvm -machine q35,smm=on,vmport=off -no-hpet -global kvm-pit.lost_tick_policy=discard -global ICH9-LPC.disable_s3=1 -cpu host,kvm=on,+hypervisor,+invtsc,l3-cache=on,migratable=no,hv_frequencies,kvm_pv_unhalt,hv_reenlightenment,hv_relaxed,hv_spinlocks=8191,hv_stimer,hv_synic,hv_time,hv_vapic,hv_vendor_id=1234567890ab,hv_vpindex -smp cores=4,threads=2,sockets=1 -m 8G -device virtio-balloon -smbios type=2,manufacturer="Quickemu Project",product=Quickemu,version=3.15,serial=0xDEADBEEF,location=quickemu.com,asset=win11 -device qxl-vga,ram_size=65536,vram_size=65536,vgamem_mb=64 -display sdl,gl=on -device usb-ehci,id=input -device usb-kbd,bus=input.0 -device usb-tablet,bus=input.0 -audiodev pa,id=audio0,out.mixing-engine=off,out.stream-name=quickemu-win11,in.stream-name=quickemu-win11 -device intel-hda -device hda-duplex,audiodev=audio0 -rtc base=localtime,clock=host,driftfix=slew -spice disable-ticketing=on,port=5930 -device virtio-serial-pci -chardev socket,id=agent0,path=vm/win11-agent.sock,server=on,wait=off -device virtserialport,chardev=agent0,name=org.qemu.guest_agent.0 -chardev spicevmc,id=vdagent0,name=vdagent -device virtserialport,chardev=vdagent0,name=com.redhat.spice.0 -chardev spiceport,id=webdav0,name=org.spice-space.webdav.0 -device virtserialport,chardev=webdav0,name=org.spice-space.webdav.0 -device virtio-rng-pci,rng=rng0 -object rng-random,id=rng0,filename=/dev/urandom -device qemu-xhci,id=spicepass -chardev spicevmc,id=usbredirchardev1,name=usbredir -device usb-redir,chardev=usbredirchardev1,id=usbredirdev1 -chardev spicevmc,id=usbredirchardev2,name=usbredir -device usb-redir,chardev=usbredirchardev2,id=usbredirdev2 -chardev spicevmc,id=usbredirchardev3,name=usbredir -device usb-redir,chardev=usbredirchardev3,id=usbredirdev3 -device pci-ohci,id=smartpass -device usb-ccid -chardev spicevmc,id=ccid,name=smartcard -device ccid-card-passthru,chardev=ccid -monitor none -serial mon:stdio -device virtio-net,netdev=nic -netdev user,hostname=win11,hostfwd=tcp::22220-:22,smb=/home/mz2/Public,id=nic -global driver=cfi.pflash01,property=secure,value=on -drive if=pflash,format=raw,unit=0,file=/usr/share/OVMF/OVMF_CODE_4M.secboot.fd,readonly=on -drive if=pflash,format=raw,unit=1,file=vm/OVMF_VARS.fd -drive media=cdrom,index=0,file=Win11_22H2_English_x64v1.iso -drive media=cdrom,index=1,file=Win11_22H2_English_x64v1.iso -drive media=cdrom,index=2,file=virtio-win-0.1.229.iso -device virtio-blk-pci,drive=SystemDisk -drive id=SystemDisk,if=none,format=qcow2,file=vm/win11.qcow2 -chardev socket,id=chrtpm,path=vm/win11.swtpm-sock -tpmdev emulator,id=tpm0,chardev=chrtpm -device tpm-tis,tpmdev=tpm0
