- Process Management
- Interrupts
- Memory Management
- File system
- Drivers
- Networking
- Security (Process / Memory protection)
- I/O

- stellt Schnittstelle zwischen Hardware und Applikationen zur Verfügung
- Jedes Programm bekommt Prozess

# Kernel
- verwendet firmware und driver
- grundlegende Kontrolle für Hardware:
	- Ram Zugriff
	- zuteilung von Resourcen
	- Verwaltung CPU

# Architektur
Ring 0:  [#Kernel](#Kernel)
Ring 1:  Device Drivers
Ring 2:  Device drivers
Ring 3:  Applications