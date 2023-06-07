Transport Layer Security

- Verschlüsselungsprotokoll
- TLS Handshake (session key)
- TLS Record (Datenaustausch)

![[Pasted image 20230425170547.png]]

- private und public key
- Zertifikat beinhaltet: Domänenname, öffentlichen Schlüssel, Ablaufdatum, bestätigung
- Stammzertifikate (von Zertifizierungsstellen) in Browser hinterlegt

- DV (domain validadtion): Domänenname wird validiert
- OV (organization validation): Domänenname und Handelsregisterauszug validiert
- EV (extended validation): + Telefonnummer und Adresse validiert

Beispiel HTTP-Request:
- Client sendet HTTP-Request, fragt nach Zertifikat + öffentlichen Schlüssel
- Server authentifiziert mit digitaler Signatur / Zertifikat + öffentlichen Schlüssel
- Client überprüft, authentifiziert öffentlichen Schlüssel
- Client generiert symmetrischen Schlüssel (session key), verschlusselt ihn mit öffentlichen Schlüssel des Servers
- Server verwendet privaten Schlüssel um Schlussel des Clients zu erhalten

# TLS-Handshake
## TLS 1.2
![[Pasted image 20230425172227.png]]
![[Pasted image 20230425173252.png]]

## TLS 1.3
![[Pasted image 20230425172235.png]]


## STARTTLS
startet verschlüsselete TLS-Verbindung
![[Pasted image 20230425172504.png]]

