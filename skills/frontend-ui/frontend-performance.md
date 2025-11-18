---
name: frontend-performance
description: Optimize web application performance. Master code splitting, lazy loading, bundling, Core Web Vitals, and web performance metrics.
---

# Frontend Performance Optimization

## Core Web Vitals

Monitor three essential metrics:

```javascript
// Measure Core Web Vitals
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

getCLS(console.log); // Cumulative Layout Shift
getFID(console.log); // First Input Delay
getFCP(console.log); // First Contentful Paint
getLCP(console.log); // Largest Contentful Paint
getTTFB(console.log); // Time to First Byte
```

### Targets
- LCP (Largest Contentful Paint): < 2.5s
- FID (First Input Delay): < 100ms
- CLS (Cumulative Layout Shift): < 0.1

## Code Splitting

### React Code Splitting
```javascript
import { lazy, Suspense } from 'react';

const HeavyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <HeavyComponent />
    </Suspense>
  );
}
```

### Route-based Code Splitting
```javascript
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Settings = lazy(() => import('./pages/Settings'));

const routes = [
  { path: '/dashboard', element: <Dashboard /> },
  { path: '/settings', element: <Settings /> },
];
```

## Image Optimization

```html
<!-- Modern image delivery -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg" alt="Description" loading="lazy">
</picture>
```

### Next.js Image Component
```javascript
import Image from 'next/image';

<Image
  src="/image.jpg"
  alt="Description"
  width={400}
  height={300}
  priority={false}
/>
```

## Bundle Analysis

```bash
# Webpack bundle analyzer
npm install --save-dev webpack-bundle-analyzer

# View results
npm run build
```

## Performance Tips

✅ Use production builds
✅ Enable gzip compression
✅ Lazy load images & components
✅ Tree-shake unused code
✅ Minify CSS/JS
✅ Use CDN for static assets
✅ Cache assets effectively
✅ Monitor Core Web Vitals

## Tools

- **Lighthouse** - Chrome DevTools audit
- **PageSpeed Insights** - Google tool
- **WebPageTest** - Detailed analysis
- **Bundle Analyzer** - Webpack plugin
- **Sentry** - Performance monitoring

## Next Steps

1. Measure current performance
2. Identify bottlenecks
3. Implement optimization
4. Monitor improvements
5. Set performance budget
