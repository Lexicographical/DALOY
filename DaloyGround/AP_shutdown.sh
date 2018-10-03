if [ "$EUID" -ne 0 ]
	then echo "Must be root"
	exit
fi

sudo service hostapd stop
sudo service dnsmasq stop

systemctl disable hostapd
systemctl disable dnsmasq


rm /etc/dnsmasq.conf
cp backup_conf/dnsmasq.conf /etc/

rm /etc/hostapd/hostapd.conf

rm /etc/network/interfaces
cp backup_conf/interfaces /etc/network/

rm /etc/default/hostapd
cp backup_conf/hostapd /etc/default/

rm /etc/dhcpcd.conf
cp backup_conf/dhcpcd.conf /etc/



echo "All done! Please reboot"