# Air Raid Monitor for Raspberry Pi 

This device shows the current status of air raid sirens in Ukraine. 

Modified version that pulls data using alerts.in.ua API.


![display](docs/display_2.png)

### Bill of materials

* Raspberry Pi Zero W
* Waveshare eInk 2.13 v3
* microSD
* micro-usb cable for power
* UPS Lite

### Installation

1. Turn on SPI and I2C via `sudo raspi-config`
    ```
    Interfacing Options -> SPI
    Interfacing Options -> I2C
   ```
2. Run installation script
    ```
   ./install.sh
    ```
3. Run the application
    ```
    python3 ~/air-raid-monitor/main.py
    ```
   or run the application as a service if you installed it as a service
   ```
      sudo systemctl start air-raid-monitor
   ```

### Install as a Service
If you didn't install the application as a service, you can do it by running the following command:
```bash
   sudo ./setup-service.sh
```
To start/restart/stop the service:
```bash
   sudo systemctl start air-raid-monitor
   sudo systemctl restart air-raid-monitor
   sudo systemctl stop air-raid-monitor
```




