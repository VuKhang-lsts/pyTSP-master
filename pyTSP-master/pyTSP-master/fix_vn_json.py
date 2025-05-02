import json

# Đọc JSON gốc
with open('data/vn_cities.json', encoding='utf-8') as f:
    raw = json.load(f)

fixed = []
for idx, c in enumerate(raw, start=1):
    fixed.append({
        "id": idx,
        "name": c["city"],
        "latitude": float(c["lat"]),
        "longitude": float(c["lng"]),
        "population": int(c["population"]) if c["population"] else 0
    })

# Ghi ra file mới
with open('data/vn_cities_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(fixed, f, ensure_ascii=False, indent=2)

print("Đã tạo data/vn_cities_fixed.json với", len(fixed), "bản ghi.")
