# Gerador de Cards — Fabíola Rocha (Instagram 4x5, 1080×1350)

Site de arquivo único (`index.html`, abre no navegador; fontes Google e JSZip vêm da internet). Modelo: gerador da Elleva (`../../Site Cards`). Layouts: Card A / Capa B de `../Fabiola-Rocha_APRENDIZADOS.md`, desenhados em canvas.

## Fluxo (cada etapa só libera após validar a anterior)
1 Dados (título, código, tipo, m², dorm., suítes, vagas, destaques da capa) → 2 Foto de capa → 3 Validar capa (Capa A com Fabíola ou Capa B onda) → 4 Demais fotos, **cada uma com seu destaque (linha 3)** → 5 Pré-visualização (6 por página) → 6 Download ZIP (`Capa-A_CÓDIGO.png`, `Corpo-NN_CÓDIGO.png`; opção de incluir a outra capa).
- Linha 4 é montada dos números (zeros/vazios somem; singular/plural automático).
- Corpo = Card A sem Fabíola, logo no canto inferior direito.
- "Carregar exemplo (18.524)" usa `exemplo.js` (fotos reduzidas do imóvel de teste).

## Fluxo 3 — Stories 9x16 (1080×1920), com a Fabíola em todos (validado 2026-11)
Etapas 7 (gerar/validar) e 8 (download ZIP, `Story-NN_CÓDIGO.png`). Cada story = 3 fotos (capa + demais, mesma ordem); o último é completado com a 1ª/2ª foto. Seletor de modelo (vale para todos os stories); destaque de cada story = o da foto do meio, editável.
- Modelo 1: fotos 640 px, painel ondulado entre fotos 1/2 (tipo + título + destaque + números; código à direita no painel), logo acima da cabeça da Fabíola (topo do story = área de segurança, sem elementos), Fabíola 640 px.
- Modelo 2: fotos 470 px, base escura ondulada a partir de y=1330, pílula do tipo sobre o filete 1/2, texto à esquerda, números empilhados, Fabíola 780 px, logo no topo direito.
- Modelo 3: fotos 640 px, título e destaque centrados abaixo das pílulas (tipo + código) sobre o topo da foto 2, selos de números no canto inferior esquerdo com degradê começando em y≈1690, Fabíola 700 px.
- Fonte dos protótipos: `_proto/` (não publicar). Rascunho de ajustes feitos um a um com o usuário.
- Pendente: vídeo MP4 dos stories (Fluxo 4, modelo a definir).

## Arquivos
`_src.html` (fonte editável, placeholders `{{MARCA}}`,`{{FAB}}`,`{{AURA}}`) + `_assets.json` + `build.py` → gera `index.html`. Edite `_src.html` e rode `python build.py`. `vercel.json` = noindex.
