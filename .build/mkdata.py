import json
B = json.load(open('/tmp/claude-0/wash/book_clean.json'))
Q = []
for f in "ABC":
    for i, ln in enumerate(open(f"/tmp/claude-0/wash/build/q{f}.txt", encoding="utf-8").read().strip().split("\n")):
        s, ch, q, a, w1, w2, w3, e = ln.split("|")
        Q.append({"id": f"{s}{i+1:03d}", "s": s, "c": int(ch), "q": q, "o": [a, w1, w2, w3], "e": e})
C = []
for i, ln in enumerate(open("/tmp/claude-0/wash/build/cards.txt", encoding="utf-8").read().strip().split("\n")):
    d, f, b = ln.split("|"); C.append({"id": f"k{i+1:03d}", "d": d, "f": f, "b": b.split(";;")})
open("/tmp/claude-0/wash/app/data.js", "w", encoding="utf-8").write(
    "// 세탁기능사 컬러 교재(2026년 11월 6일 기준) 내용과, 그 교재만 근거로 만든 문제·암기카드\n"
    "window.BOOK=" + json.dumps(B, ensure_ascii=False, separators=(",", ":")) + ";\n"
    "window.QS=" + json.dumps(Q, ensure_ascii=False, separators=(",", ":")) + ";\n"
    "window.CARDS=" + json.dumps(C, ensure_ascii=False, separators=(",", ":")) + ";\n")
print(len(Q), len(C))
