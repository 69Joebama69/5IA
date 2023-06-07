- Benutzer interagiert mit user agent
- mail mit Mail / Message Transfer Agents (MTA) gesendet / empfangen
	- sendmail
![[Pasted image 20221024084010.png]]

## MTA
- client sendet commands an Server
- Server antwortet mit numerischen reply codes und Zeichenketten
- normalerweise systemprozesse auf mail server
- port 25
- email format:
	- user@domain

## User agent -> MTA -> Mail relay
- user agent fügt Header hinzu (Date, Reply-To, ...)
- MTA fügt header hinzu (To, From, ...)
- Local MTA -> relay MTA -> relay MTA -> local MTA

## Header
- To
- From
- CC
- Bcc
- Date
- Reply-To
- Subject

## MIME
- Multipurpose Internet Mail Extension
- senden von dateien
- Header
	- MIME version
	- Content Transfer Encoding (base64, ...)
	- Content Type (text/plain, multipart/..., ...)
	- ...