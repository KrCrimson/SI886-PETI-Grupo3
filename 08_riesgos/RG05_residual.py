# 08_riesgos/RG05_residual.py
import pandas as pd

t = pd.read_csv("RG04_tratamiento.csv")
t["reduccion"] = t.Valor - t["Valor residual"]
t["reduccion_pct"] = (t.reduccion / t.Valor * 100).round(0)

print("=== EVALUACIÓN DEL TRATAMIENTO Y RIESGO RESIDUAL ===")
print(t[["id","Valor","Valor residual","reduccion","reduccion_pct","Decisión"]].to_string(index=False))
print(f"\nValor agregado del plan de tratamiento: {t.reduccion.sum()} puntos "
      f"({t.reduccion.sum()/t.Valor.sum():.0%} de reducción)")

sobre = t[t["Valor residual"] > 6]
print(f"\n=== RIESGOS RESIDUALES POR ENCIMA DEL CRITERIO ({len(sobre)}) ===")
print(sobre[["id","Valor residual","¿Quién acepta el residual?"]].to_string(index=False))
print("→ Cada uno requiere ACEPTACIÓN FORMAL FIRMADA antes de aprobar el plan.")
print("  Un riesgo residual sin firma no está aceptado: está ignorado.")

sin_senal = t[t["Señal temprana"].isna() | (t["Señal temprana"].astype(str).str.strip()=="")]
print(f"\nRiesgos sin señal temprana: {len(sin_senal)} → {list(sin_senal.id)}")
print("→ Sin señal observable no hay seguimiento posible: el riesgo se detecta cuando ya ocurrió.")
