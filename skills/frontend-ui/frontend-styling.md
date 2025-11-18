---
name: frontend-styling
description: Master CSS, Tailwind CSS, CSS-in-JS solutions, and styling methodologies. Learn responsive design, theme management, and modern styling approaches.
---

# Frontend Styling Solutions

## CSS Fundamentals

### Flexbox Layout
```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}
```

### Grid Layout
```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}
```

## Tailwind CSS (Recommended)

Utility-first CSS framework for rapid development:

```html
<div class="flex justify-between items-center gap-4">
  <h1 class="text-2xl font-bold text-blue-600">Title</h1>
  <button class="bg-blue-500 text-white px-4 py-2 rounded">
    Click me
  </button>
</div>
```

### Benefits
✅ Fast development
✅ Responsive design built-in
✅ Dark mode support
✅ Tree-shaking (tiny bundles)
✅ Customizable theme

## CSS-in-JS

### Styled Components (React)
```javascript
import styled from 'styled-components';

const Button = styled.button`
  background-color: #0066cc;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;

  &:hover {
    background-color: #0052a3;
  }
`;
```

### Emotion (Lightweight alternative)
```javascript
import { css } from '@emotion/react';

const buttonStyles = css`
  background-color: #0066cc;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
`;
```

## Styling Comparison

| Solution | Approach | Bundle | Best For |
|----------|----------|--------|----------|
| **Tailwind** | Utility-first | ~15KB | Scalability |
| **CSS Modules** | Scoped CSS | 0KB | Simplicity |
| **Styled Comp** | CSS-in-JS | 20KB | React apps |
| **Emotion** | CSS-in-JS | 10KB | Performance |
| **SCSS** | Preprocessor | 0KB | Complex styling |

## Best Practices

✅ Use consistent naming conventions
✅ Organize styles by component
✅ Use CSS variables for theming
✅ Implement dark mode support
✅ Optimize for accessibility
✅ Keep selectors simple

## Next Steps

1. Master **one CSS solution**
2. Learn **responsive design**
3. Implement **dark mode**
4. Add **animations**
5. Optimize **bundle size**
