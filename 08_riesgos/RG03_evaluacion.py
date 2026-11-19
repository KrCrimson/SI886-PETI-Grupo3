# 08_riesgos/RG03_evaluacion.py
import pandas as pd, numpy as np, matplotlib.pyplot as plt
import os

r = pd.read_csv("RG02_registro.csv")
r["valor"] = r.P * r.I
r["nivel"] = pd.cut(r.valor, [0,6,11,14,25],
                    labels=["Bajo","Medio","Alto","Crítico"])
r = r.sort_values("valor", ascending=False)
r.to_csv("RG03_evaluado.csv", index=False)

print("=== REGISTRO DE RIESGOS DEL PLAN (MUNICIPALIDAD DE ALTO SELVA) ===")
print(r[["id","Categoría","P","I","valor","nivel"]].to_string(index=False))
print(f"\nRiesgos evaluados : {len(r)}")
print(r.nivel.value_counts().reindex(["Crítico","Alto","Medio","Bajo"]).fillna(0).astype(int).to_string())

CATS = ["Presupuestal","Patrocinio","Capacidad de ejecución","Personal clave",
        "Resistencia al cambio","Proveedor","Técnico","Normativo","De alcance"]
faltan = [c for c in CATS if c not in set(r["Categoría"])]
print(f"\nCategorías SIN riesgo identificado: {faltan or 'ninguna ✔'}")
if faltan:
    print("→ Cada categoría omitida debe justificarse explícitamente en sección 8.")

criticos = r[r.valor >= 15]
print(f"\n=== RIESGOS ≥ 15 — requieren decisión de la gerencia general / alcaldía ===")
print(criticos[["id","Categoría","valor"]].to_string(index=False))

# Mapa de calor
m = np.zeros((5,5))
for _, x in r.iterrows(): 
    m[5-x.I, x.P-1] += 1

fig, ax = plt.subplots(figsize=(8.5,7))
im = ax.imshow(m, cmap="RdYlGn_r", vmin=0, vmax=max(m.max(),1))
for i in range(5):
    for j in range(5):
        v = int(m[i,j])
        if v: ax.text(j, i, v, ha="center", va="center", fontsize=14, fontweight="bold", color="black" if v < 4 else "white")

ax.set_xticks(range(5))
ax.set_xticklabels(["1 Muy baja","2 Baja","3 Media","4 Alta","5 Muy alta"], fontsize=9)
ax.set_yticks(range(5))
ax.set_yticklabels(["5 Catastrófico","4 Mayor","3 Moderado","2 Menor","1 Insignif."], fontsize=9)
ax.set_xlabel("Probabilidad (P)", fontsize=11, fontweight="bold")
ax.set_ylabel("Impacto (I)", fontsize=11, fontweight="bold")
ax.set_title("Mapa de Calor — Riesgos de Ejecución del PETI 2026-2028\nMunicipalidad Distrital de Alto Selva", fontsize=12, fontweight="bold")

cbar = plt.colorbar(im, label="N.º de riesgos")
plt.tight_layout()

os.makedirs("../graficos", exist_ok=True)
plt.savefig("../graficos/RG_mapa_calor.png", dpi=150)
print("\n[OK] Mapa de calor guardado con éxito en ../graficos/RG_mapa_calor.png")
