#!/bin/bash

mkdir -p hyeonmun

cd hyeonmun || exit

mkdir -p detectors scoring storage tasks utils fastapi_app

touch detectors/tor.py
touch detectors/vpn_proxy.py
touch detectors/useragent.py
touch detectors/behavior.py
touch detectors/referer.py

touch scoring/engine.py

touch storage/cache.py
touch storage/database.py

touch tasks/enrich.py

touch utils/logging.py

touch middleware.py
touch fastapi_app/main.py
#touch requirements.txt
#touch README.md

echo "✅ Hyeonmun file tree setup"