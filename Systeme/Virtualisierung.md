- Resourcen auf Kunden / Programme aufgeteilt
- erzeugen von virtuellen Hard-und Softwarekomponenten

## Virtuelle Maschine
- nachgebildeter Rechner
- isolierte Umgebung
- direkter Zugriff auf einige Komponenten, andere emuliert

- Virtueller Server / PC (Virtualbox)
- Virtuelles Betriebssystem (container)
- Virtuelle RAM (swap)
- Virtuelle Festplatte (RAID)
- Virtuelle Netze (VLAN)

## Vorteile
-   Bessere Energie-Effizienz, Kostensenkung der Hardware  
-   Gesteigerte Ausfallsicherheit, Redundanz
-   Vereinfachte Administration (Anzahl der physischen Server reduziert sich)  
-   Effiziente Nutzung der Hardware (Zusammenlegen vieler virtueller Server auf möglichst wenigen physikalischen Servern)  
-   Ressourcen können flexibel erweitert werden
-   Vereinfachte Bereitstellung (neue Server können sehr schnell erzeugt werden)
-   Erhöhung der Verfügbarkeit (Migration von Servern im laufenden Betrieb, Leichte Vervielfältigung und Sicherung der virtuellen Maschinen)  
-   Hardwareunabhängigkeit
-   Höhere Sicherheit (Isolierung der virtuellen Maschinen von den anderen VMs)  
-   Einfache Verwaltung mehrerer Systeme
-   Verfügbarkeit verschiedener Systeme für Tests

## Nachteile
-   Geringere Performance als eine reale Maschine
-   Nicht jede Hardware kann emuliert werden
-   _Single Point of Failure_: Bei Ausfall eines Hosts können mehrere virtuelle Server ausfallen
-   Zusätzliches know-how ist notwendig

# Hypervisor
Virtual Machine Monitor (VMM)
- Verwaltung von Resourcen
- bereitstellung Schnittstelle zwischen host und guest
- bereitstellung Management-Software

![Pasted image 20230425164141](../Info/Pasted%20image%2020230425164141.png)

Typ1-Hypervisor:
- direkt auf Hardware
- kein host OS
- Microsoft Hyper-V, Oracle VM

Typ2-Hypervisor:
- Software-Schnittstelle
- emuliert Geräte
- KVM, Container, VMWare


## Funktion
- Normale Befehle des Gastsystems: direkt auf Prozerror im user mode
- System calls: Hypervisor -> Interrupt Handler -> Gastsystem
- Hardware Interrupts: Hypervisor -> Interrupt handler des Gastsystems
- Privilegierte Instructions: Hypervisor -> emuliert -> Gastsystem


# Arten
## Full Virtualization
- gesamte Hardware virtualisiert
- Gastsystem hat vollständige virtuelle Maschine
- Hardware des Hosts verborgen
- VMWare, Virtualbox

**Vorteile:**
- wenig Änderungen an Host und Guest
- Flexibilität
**Nachteile:**
- Kontextwechsel
- schlechte Performance

## Para Virtualization
- keine simulation / emulation von Hardware
- Hypervisor stellt Schmittstelle zu physischen Resourcen zur verfügung
- guest kommuniziert mit Hypervisor
- Oracle VM, Xen

**Vorteile:**
- gute Performance
- Anpassung der Hardware
**Nachteile:**
- Anpassung von Gast

## Servier-Virtualizierung
- auslastung von Serverhardware erhöhen
- mehrere virtuelle Instanzen auf 1 Server

## Betriebssystem-Virtualisierung
- Software in Container aufgerufen
- alle Anwendungen gleicher Kernel
- Programme geschlossen -> Container geschlossen
- Container auf verschiedener Hardware und Betriebssystem
- Geringer Resourcenbedarf
- hohe Performance

## Hardware-Emulation
- komplette nachbildung der Hardware

**Vorteile:**
- kein Anpassung an Betriebssystem / Anwendung
- verschiedene Architekturen
**Nachteile:**
- sehr aufwändug
- schlechtere Performance

## Applikationsvirtualisierung
- Programme in isolierten Enviroments
- keine Änderungen an Betriebssytem / Dateisystem
- Abstraktionsschicht zwischen Anwendung und Betriebssystem

**Vorteile:**
- Plattformunabhängig
- einfaches Einbinden und Entfernung
- Sicherheit
- Applikation verwendbar ohne installation
**Nachteile:**
- Performance
- Komplex
- nicht immer möglich

## Desktop-Virtualisierung
- virtuelle instanz in Rechenzentrum
- hostbasiert:
	- virtuelle Desktops direkt auf Server
	- Rechenleistung von Server-Hardware
	- Thick, Thin, Zero Clients oder Tablet / Handy
- clientbasiert:
	- Resourcen des Clients
	- Thick Client


# Emulation / Simulation
## Simulation:
- nachbildung der Realität
- so gut wie möglich
- Schaltungssimulation

## Emulation:
- nachbildung des Ergebnisses
- Emulator ganz anders als Original
- QEMU

