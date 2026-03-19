# Quarto troubleshooting tips

## Cross-references not resolving

- **Blank lines:** Quarto requires a blank line before and after a figure, table, or equation block for it to be parsed as a block element. Missing blank lines are easy to miss if there are trailing spaces on the preceding line.
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

## Figures

- **Quotes in captions:** Do not wrap figure captions in quotes inside `![...]()`. The quotes will appear literally in the rendered output.
- **Multi-page xopp exports:** If a Xournal++ file has multiple pages, `xopp2png.sh` will produce `name-1.png`, `name-2.png`, etc. rather than `name.png`. Keep drawings to a single page.
