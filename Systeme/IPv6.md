3001:0da8:75a3:0000:0000:8a2e:0370:7334
- 128 bits
- nullen am anfang entfernt:
	- 3001:**da8**:75a3:0000:0000:8a2e:**370**:7334
- nur nullen -> 1 null:
	- 3001:da8:75a3:**0**:**0**:8a2e:370:7334
- > 2 * 0 -> :: (nur 1 mal):
	- 3001:da8:75a3::8a2e:370:7334

- 3001:0da8:75a3:0000
	- Netzwerk (Netzwerk identifizieren, routing)
	- 3001:0da8:75a3
		- Unicast Address / Routing-Präfix
	- 0000
		- Subnet ID
- 0000:8a2e:0370:7334
	- Interface ID
	- generiert von MAC-Adresse (11-11-22-22-33-33):
		- in hälfte teilen (11-11-22 | 22-33-33)
		- FFFE einfügen (11-11-22 FFFE 22-33-33)
		- linke seite zu binär (0001 0001 0001 0001 0010 0010)
		- 7. bit invertieren     (0001 00**1**1 0001 0001 0010 0010)
			- 0 = manuelle EUI
			- 1 = aus MAC generiert
		- => 1311-22FF-FE22-3333

## SLAAC
FE80::/10 + Interface-ID
- Link-Local
- nicht routbar
- neighbour discovery

## NDP 
Neighbour Discovery Protocol
erhalten von Präfixen des Routers um global unicast address (public address) zu erstellen

**Router solicitation**:
- Fragepaket an FF02::2
- Liste von verfügbaren Routern

**Router advertisement:**
- periodisch (4 bis 10 minuten)
- an FF02::1 oder Antwort auf router solicitation

**Neighbour solicitation:**
- address resolution, neighbour unreachability detection, duplicate address detection
- austausch der Link-Layer-Address

**Neighbour advertisement:**
- wenn Host Adresse ändert
- antwort auf neighbour solicitation

# IPv6 Präfixe

## Unicast Präfixe
**Link-Local**
FE80::/10

**Unique Local**
FC00::/7

**Global unicast**
2000::/3

**Loopback**
::1/128

## Multicast Präfixe
- IPv4 Broadcast
- FF + 4 bit flags + 4 bit scope + group ID (FF00:0000:0000:0000:0000:0000:0000:0000)
- FF02::1 : alle Nodes auf Link
- FF02::2 : alle Router auf Link
- FF02::5 : OSPF-Router auf Link