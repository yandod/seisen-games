#!/usr/bin/env python3
import sys
import os
import glob

def generate_index(build_dir):
    html_files = sorted(glob.glob(os.path.join(build_dir, "*.html")))
    games = []
    for f in html_files:
        name = os.path.splitext(os.path.basename(f))[0]
        games.append(name)

    game_cards = ""
    for name in games:
        display_name = name
        pyxapp_exists = os.path.exists(os.path.join(build_dir, f"{name}.pyxapp"))
        download_link = ""
        if pyxapp_exists:
            download_link = f"""
          <a href="{name}.pyxapp" class="download-link" download>⬇ .pyxapp をダウンロード</a>"""
        game_cards += f"""
        <div class="game-card">
          <a href="{name}.html" class="game-play">
            <div class="game-icon">🎮</div>
            <h2>{display_name}</h2>
          </a>{download_link}
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pyxel Games</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 40px 20px;
      color: #fff;
    }}
    h1 {{
      font-size: 2.5rem;
      margin-bottom: 10px;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}
    .subtitle {{
      color: #aaa;
      margin-bottom: 40px;
      font-size: 1rem;
    }}
    .games {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 30px;
      max-width: 900px;
      width: 100%;
    }}
    .game-card {{
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 16px;
      padding: 40px 20px 20px;
      text-align: center;
      color: #fff;
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .game-card:hover {{
      background: rgba(255,255,255,0.15);
      transform: translateY(-5px);
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }}
    .game-play {{
      text-decoration: none;
      color: #fff;
      display: block;
      width: 100%;
    }}
    .game-icon {{
      font-size: 3rem;
      margin-bottom: 15px;
    }}
    .game-card h2 {{
      font-size: 1.3rem;
      font-weight: 500;
    }}
    .download-link {{
      display: inline-block;
      margin-top: 20px;
      padding: 8px 16px;
      font-size: 0.85rem;
      color: #cfe3ff;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.2);
      border-radius: 20px;
      text-decoration: none;
      transition: all 0.2s ease;
    }}
    .download-link:hover {{
      background: rgba(255,255,255,0.18);
      color: #fff;
    }}
  </style>
</head>
<body>
  <h1>🎮 Seisen Games</h1>
  <p class="subtitle">Pyxelで作ったゲーム集</p>
  <div class="games">{game_cards}
  </div>
</body>
</html>"""

    output_path = os.path.join(build_dir, "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {output_path} with {len(games)} games")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_index.py <build_dir>")
        sys.exit(1)
    generate_index(sys.argv[1])
