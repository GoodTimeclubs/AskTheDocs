> ⚠️ **Testdaten:** Dieses Dokument wurde von Claude (Anthropic) als fiktive Testdaten für eine RAG-Pipeline generiert. Alle Namen, Zahlen und Fakten sind frei erfunden.

# Aurora Fleet REST API – v3

Basis-URL: `https://api.aurora.nordlicht.example/v3`

## Authentifizierung

Alle Anfragen brauchen einen API-Key im Header:

```http
Authorization: Bearer <API_KEY>
```

API-Keys werden im Aurora-Dashboard unter *Einstellungen → Entwickler* erstellt. Ein Key ist **90 Tage** gültig.

## Rate Limits

- Standard: **600 Anfragen pro Minute**
- Enterprise: 3.000 Anfragen pro Minute
- Bei Überschreitung: HTTP-Status `429 Too Many Requests`

## Endpunkte

### Roboter auflisten

```http
GET /robots?status=active&limit=50
```

Antwort:

```json
{
  "robots": [
    { "id": "L7M-00412", "model": "lumen7m", "status": "active", "battery": 76 }
  ],
  "next_cursor": "abc123"
}
```

### Auftrag erstellen

```http
POST /tasks
Content-Type: application/json

{
  "robot_id": "L7M-00412",
  "type": "transport",
  "from": "A-12-03",
  "to": "DOCK-2",
  "priority": "high"
}
```

Mögliche Werte für `priority`: `low`, `normal`, `high`, `critical`.

### Nothalt auslösen

```http
POST /robots/{id}/emergency-stop
```

Stoppt den Roboter sofort. Er kann danach nur vor Ort per Taster wieder freigegeben werden.

## Fehlercodes

| Code | Bedeutung |
|------|-----------|
| 400 | Ungültige Anfrage |
| 401 | API-Key fehlt oder ist abgelaufen |
| 404 | Roboter oder Auftrag nicht gefunden |
| 409 | Roboter ist bereits belegt |
| 429 | Rate Limit überschritten |
