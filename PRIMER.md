# AKSI – Legal & Signing Bootstrap PR

Этот PR добавляет юридический пакет и инфраструктуру криптоподписей (Ed25519) для релизов коннектора AKSI.

- Лицензия (proprietary)
- Манифест `.aksi/manifest.json` с UID и алгоритмом подписи
- Публичный ключ `.aksi/aksi_public_ed25519.pem` (заполнить)
- Скрипты `scripts/sign_release.py` и `scripts/verify_release.py`
- GitHub Actions: `verify.yml` и `sign-selfhosted.yml`

⚠️ Приватный ключ не хранится в репозитории. Его нужно держать локально: `~/.aksi/aksi_private_ed25519.pem`.
