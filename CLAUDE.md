# Gerador de Cards — Fabíola Rocha (Instagram 4x5, 1080×1350)

Site de arquivo único (`index.html`, abre no navegador; fontes Google e JSZip vêm da internet). Modelo: gerador da Elleva (`../../Site Cards`). Layouts: Card A / Capa B de `../Fabiola-Rocha_APRENDIZADOS.md`, desenhados em canvas.

## Fluxo (cada etapa só libera após validar a anterior)
1 Dados (título, código, tipo, m², dorm., suítes, vagas, destaques da capa) → 2 Foto de capa → 3 Validar capa (Capa A com Fabíola ou Capa B onda) → 4 Demais fotos, **cada uma com seu destaque (linha 3)** → 5 Pré-visualização (6 por página) → 6 Download ZIP (`Capa-A_CÓDIGO.png`, `Corpo-NN_CÓDIGO.png`; opção de incluir a outra capa).
- Linha 4 é montada dos números (zeros/vazios somem; singular/plural automático).
- Corpo = Card A sem Fabíola, logo no canto inferior direito.
- "Carregar exemplo (18.524)" usa `exemplo.js` (fotos reduzidas do imóvel de teste).

## Arquivos
`_src.html` (fonte editável, placeholders `{{MARCA}}`,`{{FAB}}`,`{{AURA}}`) + `_assets.json` + `build.py` → gera `index.html`. Edite `_src.html` e rode `python build.py`. `vercel.json` = noindex.
