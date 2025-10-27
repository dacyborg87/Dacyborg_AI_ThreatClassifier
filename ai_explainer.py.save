import os, json
MODEL = os.getenv("MODEL_NAME", "gpt-4o-mini")

def load_summary(p="summary.json"):
    with open(p,"r") as f: return json.load(f)

def build_prompt(s):
    counts = s.get("counts", {})
    top = s.get("top_alerts", [])
    lines = [f"- [{a['severity']}] L{a['level']} | {a.get('timestamp','')} | {a.get('agent','')} | {a.get('description','')}" for a in top]
    top_text = "\n".join(lines) if lines else "No top alerts."
    return f"""You are a senior SOC analyst. Summarize succinctly.
Severity counts: {counts}
Top alerts:
{top_text}

Output:
1) Executive Summary (3-5 sentences)
2) Likely TTPs (bullets)
3) Immediate Actions (ordered)
4) Hardening (bullets)"""

def call_llm(prompt):
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        return "(AI Explainer skipped: OPENAI_API_KEY not set.)"
    from openai import OpenAI
    client = OpenAI(api_key=key)
    r = client.chat.completions.create(
        model=MODEL,
        messages=[{"role":"system","content":"Be concise, precise."},
                  {"role":"user","content":prompt}],
        temperature=0.2,
    )
    return r.choices[0].message.content.strip()

def main():
    s = load_summary()
    txt = call_llm(build_prompt(s))
    with open("analysis.md","w") as f: f.write(txt+"\n")
    if os.path.exists("report.md"):
        with open("report.md","a") as f:
            f.write("\n---\n## AI Threat Analysis\n\n"+txt+"\n")
    print("AI Explainer -> analysis.md (and appended to report.md if present).")

if __name__ == "__main__": main()
