# Quarto troubleshooting tips

## Rendering the book

Activate the shared Python venv before running `quarto render`, otherwise Quarto will use the system Python which lacks Jupyter/nbformat:

```bash
source ~/GitHub_repos/pyenv/bin/activate
quarto render
```

This venv at `~/GitHub_repos/pyenv/` is the standard environment for all Python work on this machine.

## Sending code chunks to IPython REPL (Iron.nvim)

Multi-line Python functions with blank lines inside (e.g., blank lines in docstrings) break chunk-sending in the standard `python3` REPL — blank lines terminate the block. The fix is to use IPython with bracketed paste mode.

**Current setup in `~/.config/nvim/init.lua`:**
- Iron.nvim launches IPython with `--no-autoindent` (prevents progressive indentation)
- `send_to_current_repl()` wraps Python code in bracketed paste escape sequences (`\x1b[200~`...`\x1b[201~`) so IPython receives the whole block at once
- R chunks are unaffected (the bracketed paste path is gated on `repl == "python"`)

IPython may show extra blank lines and duplicated `In []` numbers in the output — this is cosmetic, the code runs correctly.

## Cross-references not resolving

- **Blank lines:** Quarto requires a blank line before and after a figure, table, or equation block for it to be parsed as a block element. Missing blank lines are easy to miss if there are trailing spaces on the preceding line.
- **Stray characters beyond closing `}` in a figure block** Even a `.` after the closing curly brace will mess things up.
- **Missing image file:** A cross-reference to a figure whose image file doesn't exist will not resolve. Check that the file path is correct and the file has been exported.
- **Build errors in other chapters:** A rendering error in any chapter can prevent cross-references from resolving book-wide. Check the `quarto render` output for errors.

## MathJax macros not working

- **Digits in macro names:** MathJax macro names must be letters only. A name like `\kgpm3ps` will silently fail because MathJax stops parsing at the `3`. Use all-letter names (e.g., `\kgpmcps`).
- **Wrong config key:** The `mathjax-config` key in `_quarto.yml` is not valid. Use `include-in-header` with an inline `<script>` block instead (see `_quarto.yml`).

## Equation labels

- **Label placement:** The equation label must be on the same line as the closing `$$`, separated by a space:
  ```
  $$
  \frac{dT}{dt} = c \cdot (T - T_{air})
  $$ {#eq-my-label}
  ```
  Putting `{#eq-my-label}` on its own line below `$$` will break the reference.

## Chunk options (Python vs R syntax)

Python chunks use YAML-style cell options, not R/knitr inline syntax. For example:

```
```{python}
#| eval: false
```

Not `{python,eval=FALSE}` (that's knitr syntax and will be silently ignored by Quarto for Python chunks).

## Figures

- **Quotes in captions:** Do not wrap figure captions in quotes inside `![...]()`. The quotes will appear literally in the rendered output.
- **Multi-page xopp exports:** If a Xournal++ file has multiple pages, `xopp2png.sh` will produce `name-1.png`, `name-2.png`, etc. rather than `name.png`. Keep drawings to a single page.
