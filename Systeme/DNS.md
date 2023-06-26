- Zuordnung Rechnername -> Ip-Adresse
- Namensauflösung
- UDP
- FQDN (Full Qualified Domain Name)
- Synchronisation DNS-Server
- Verwaltung von Resource Records
- Unterteilung DNS-Namensraum in Zonen
- FQDN relativ zu root referenziert

## DNS-Namensraum
- 13 Root Server
- Internet Network Information Center (InterNIC):
	- Verantwortung über root server
	- Verwaltung der obersten ebene (TLD)
	- Zulassung der gTLD (generic Top Level Domains)
	- Zuteilung des IP-Adressraums

## Top Level Domains (TLD)
- gTLD:
	- .edu
	- .com
	- .net
	- .org
	- .mil
	- .gov
- geografische Domains:
	- .it
	- .de

## Second Level Domain (SLD) und Subdomains
- Second Level Domain
	- FQDN: SLD.TLD. (tfobz.net.)
- Subdomain
	- FQDN: subdomain.SLD.TLD. (informatik.tfobz.net.)
- Hostname
	- FQDN: hostname.domain.domain-suffix.

## Rrsource Records (RR)
- NAME (TTL) Class Type RDATA
	- A (IPv4 Adresse)
	- NS (Authorative Name Server)
	- CNAME (Canonical Name, Alias)
	- SOA (Start of Zone Authority)
	- PTR (Domain Name Pointer)
	- AAAA (IPv6-Adresse)
- Abfrage:
	- Client-Server
	- DNS-Query / Response
	- nslookup, dig
	- nur hostname angeben (Unqualifizierte Abfrage)

## Zonen
- DNS-Content-Server
	- Zone: "tfobz.net" (ohne Subdomains)
- Nameserver der Subdomain
	- "informatik.tfobz.net"
- Zonendatei
	- zugeordnete RR einer Zone