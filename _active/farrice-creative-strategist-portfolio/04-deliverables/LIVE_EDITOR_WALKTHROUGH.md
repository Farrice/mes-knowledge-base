# Live Editor Walkthrough

## Edit One Line

1. Open the editor:

   `http://127.0.0.1:8766/editor.html`

2. Click **Open live editor**.

3. Click any outlined text on the portfolio. Example: the hero eyebrow:

   `Creative strategist · DTC paid social`

4. Type your replacement text directly into the page.

5. Click **Save text**.

6. Click **Regenerate PDF**.

7. Open the regenerated PDF:

   `../90-exports/Farrice-Cain-Creative-Strategist-Portfolio.pdf`

## Publish After Editing

For a static site:

1. Run `node build-public.mjs`.
2. Publish `dist/`.

For after-publish editing:

1. Host the Node server instead of only `dist/`.
2. Set `CMS_TOKEN`.
3. Open `/?edit=1`.
4. Click **Set CMS token**.
5. Edit and save.

## Safety Notes

- Normal visitors do not see the editor toolbar.
- The static `dist/` folder excludes the edit-mode UI.
- The CMS-backed server requires a token for writes when `CMS_TOKEN` is set.
