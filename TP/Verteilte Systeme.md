>  Zusammenschluss unabhängiger Computer, die sich für den Benutzer als ein einziges System präsentieren
>  _Andrew S. Tanenbaum_

> eine Menge interagierender Prozesse (oder Prozessoren), die über keinen gemeinsamen Speicher verfügen und daher über Nachrichten miteinander kommunizieren
> _Peter Löhr_

# Vorteile
- echte Nebenläufigkeit
- Skalierbarkeit (hinzufügen weiterer Rechner = mehr Performance)
- Bereitstellung entfernter Ressourcen
- erhöhte Ausfallsicherheit (Redundanz)
- preis (viele günstige Computer > 1 Supercomputer)

Beispiel: Folding@Home
- Simulation von Proteinfaltung für COVID-19 Forschung
- 1.5 exaFLOPS (7x so schnell wie schnellster Supercomputer, SUMMIT)

# Nachteile
- kein single point of failure
- Fehle und Ausfälle steigen mit Anzahl an Prozessen
- erkennen und beheben von Teilausfällen schwierig (Heartbeat / ping)
- Synchronisierung wichtig da verschiedene Systeme Aufgaben verschieden schnell lösen (Deadlocks)
- kein gemeinsamer Speicher:
	- Kommunikation über Nachrichten
	- sehr Fehleranfällig
	- können verfälscht, verloren oder dupliziert werden
	- Nachrichtenlaufzeit unvorhersehbar (System kann ausgefallen sein oder lange Antwortzeit haben)
	- kann unsicher sein
- Administration schwierig