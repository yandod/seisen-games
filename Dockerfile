FROM python:3.11-slim

RUN pip install --no-cache-dir pyxel

WORKDIR /app
COPY . .

COPY <<'EOF' /app/build.sh
#!/bin/bash
set -e
mkdir -p build
for dir in apps/*/; do
  name=$(basename "$dir")
  pyxel package "$dir" "$dir/main.py"
  pyxel app2html "${name}.pyxapp"
  mv "${name}.html" "build/${name}.html"
  mv "${name}.pyxapp" "build/${name}.pyxapp"
done
python scripts/generate_index.py build/
echo "--- Build complete. Files in build/:"
ls -la build/
EOF

RUN chmod +x /app/build.sh

CMD ["/app/build.sh"]
