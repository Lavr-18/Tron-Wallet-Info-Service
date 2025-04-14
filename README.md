## Примеры использования

### POST `/wallet-info/`

Запрашивает информацию о кошельке и сохраняет её в БД.

**Пример запроса:**

```json
{
  "address": "TLa6n6KbtqVvfTjHbg76vX91XYmK6Mok2X"
}


GET /wallet-info/?skip=0&limit=10
Получить список последних запросов

Запуск тестов:
pytest test_main.py
