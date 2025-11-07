# Lab 5 — Button Component

In this lab, you will **build your own reusable Button component** in React.

You are given:
- A project scaffold (React + Vite)
- `Button.css` that already contains all the styles
- `App.jsx` to check your implementation

Your job is to **implement the logic inside `Button.jsx`**  
and then **uncomment lines in `App.jsx`** to test your button.

---

## **Goal**

Build a reusable `<Button>` component that:
- Can display text and an optional icon
- Supports multiple visual styles (`variant`, `size`, `color`)
- Disables interaction when needed
- Applies the correct CSS classes dynamically based on props

---

## **Files to Edit**

### `src/components/Button.jsx`

You will implement the `Button` component here.

```jsx
/**
 * Lab 5
 *
 * Props:
 * - children (ReactNode): Button label or content (required)
 * - variant ("fill" | "outline" | "text"): Visual style of the button
 * - size ("small" | "medium" | "large"): Button size
 * - color ("primary" | "secondary"): Theme color
 * - disabled (boolean): Whether the button is disabled
 * - icon (ReactNode): Optional icon displayed before the text
 * - onClick (function): Click event handler
 *
 * Requirements:
 * 1. Render a <button> that:
 *    - Shows the icon (if provided) before the text.
 *    - Renders the children inside.
 * 2. Apply multiple CSS classes dynamically:
 *    "button", `variant-[fill|outline|text]`,
 *    `size-[small|medium|large]`, `color-[primary|secondary]`
 *    and add "disabled" when disabled.
 * 3. Use `disabled={disabled}` to make it unclickable.
 *
 * Tip:
 * const classes = [
 *   "button",
 *   `variant-${variant}`,
 *   `size-${size}`,
 *   `color-${color}`,
 *   disabled ? "disabled" : ""
 * ].filter(Boolean).join(" ");
 */
