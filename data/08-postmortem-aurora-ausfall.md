> ⚠️ **Testdaten:** Dieses Dokument wurde von Claude (Anthropic) als fiktive Testdaten für eine RAG-Pipeline generiert. Alle Namen, Zahlen und Fakten sind frei erfunden.

# Postmortem: Ausfall von Aurora Fleet am 03.02.2026

**Schweregrad:** SEV-1
**Dauer:** 2 Stunden 47 Minuten (06:12–08:59 Uhr MEZ)
**Betroffen:** 41 Kund*innen, ca. 2.300 Roboter
**Autorin:** Ines Haverkamp (SRE-Team Graz)

## Zusammenfassung

Nach einem Update der Datenbank von PostgreSQL 15 auf 16 konnte der Dienst `fleet-scheduler` keine Verbindung mehr aufbauen. Die Roboter fuhren daraufhin in den sicheren Ruhezustand und blieben stehen.

## Zeitverlauf

| Uhrzeit | Ereignis |
|---------|----------|
| 05:58 | Datenbank-Update gestartet |
| 06:12 | Erste Alarme: Scheduler-Verbindungsfehler |
| 06:25 | Rufbereitschaft (Paul Engström) übernimmt |
| 07:40 | Ursache gefunden: veraltete Authentifizierungsmethode `md5` |
| 08:30 | Konfiguration auf `scram-sha-256` umgestellt |
| 08:59 | Alle Roboter wieder aktiv |

## Ursache

Die Verbindungskonfiguration nutzte noch `md5`. Das wurde in der Staging-Umgebung nicht bemerkt, weil dort eine andere Konfiguration lag.

## Maßnahmen

1. Staging und Produktion nutzen ab sofort dieselbe Konfiguration (Verantwortlich: Ines Haverkamp).
2. Datenbank-Updates nur noch sonntags zwischen 02:00 und 04:00 Uhr.
3. Betroffene Kund*innen erhalten eine Gutschrift von 10 % der Monatsgebühr.

## Was gut lief

Die Roboter haben sich wie vorgesehen sicher abgeschaltet. Es gab keine Unfälle oder Schäden.
