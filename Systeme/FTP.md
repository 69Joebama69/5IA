- Übertragen von Daten
- Datenaustausch, afulisten von Verzeichnissen und Daten, Änderung der Daten
- TCP
- 2 Verbindungen
	- Datenübertragung (z.B. Port 20)
	- Steuerung (Port 21)

## Verbindung (Active FTP)
- Client öffnet random Port N
- Sendet mit PORT ip und port an port 21

## Verbindung (Passive FTP)
- Wenn z.B. client hinter Firewall oder clienseitig NAT
- client sendet PASV
- Server öffnet random Port
- Server sendet ip und port

## FTP Replies
- Steurungs verbindung
- Status-Code (3 Ziffern), Nachricht

### Status Code
- Erste Ziffer
	- 1: Anfrage erhalten
	- 2: Success
	- 3: Mehrere Informationen notwendig
	- 4: Fehler, nochmal wiederholen
	- 5: Permanenter Fehler
- Zweite Ziffer
	- 1: Syntax Problem
	- 2: Information
	- 3: Login Problem
	- 4: Nicht spezifiziert
	- 5: Dateisystem
- Dritte Ziffer
	- Spezifisches Problem