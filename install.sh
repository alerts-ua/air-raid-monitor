#!/bin/bash
cp air-raid-monitor.service /lib/systemd/system/
chmod 644 /lib/systemd/system/air-raid-monitor.service
systemctl daemon-reload
systemctl enable air-raid-monitor.service
systemctl start air-raid-monitor.service
systemctl status air-raid-monitor.service