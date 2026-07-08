# React Project Guidelines

## React Commands

```bash
# Development
npm run dev              # Start dev server with HMR
npm run build            # Production build
npm run preview          # Preview production build

# Testing
npm test                 # Run tests
npm run test:watch       # Watch mode
npm run test:coverage    # With coverage report

# Linting and formatting
npm run lint             # ESLint
npm run lint:fix         # ESLint with auto-fix
npm run format           # Prettier
npm run typecheck        # TypeScript check
```

## React Standards

### Project Structure

```
project/
├── src/
│   ├── components/
│   │   ├── ui/          # Reusable UI primitives
│   │   └── features/    # Feature-specific components
│   ├── hooks/           # Custom React hooks
│   ├── lib/             # Utilities and helpers
│   ├── pages/           # Page components (if using file-based routing)
│   ├── types/           # TypeScript type definitions
│   ├── App.tsx
│   └── main.tsx
├── tests/
├── public/
├── package.json
├── tsconfig.json
├── vite.config.ts
└── CLAUDE.md
```

### Component Patterns

```tsx
// Prefer functional components with TypeScript
interface ButtonProps {
  variant?: "primary" | "secondary";
  disabled?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
}

export function Button({
  variant = "primary",
  disabled = false,
  onClick,
  children,
}: ButtonProps) {
  return (
    <button
      className={cn("btn", `btn-${variant}`)}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
```

### Hooks

- Extract reusable logic into custom hooks
- Name hooks with `use` prefix
- Keep hooks focused on a single concern
- Handle cleanup in `useEffect` return functions

```tsx
function useDebounce<T>(value: T, delay: number): T {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebouncedValue(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debouncedValue;
}
```

### State Management

- Use React's built-in state (`useState`, `useReducer`) for local state
- Use Context for shared state that doesn't change frequently
- Consider Zustand/Jotai for complex global state
- Avoid prop drilling beyond 2-3 levels

### TypeScript

- Define explicit types for props and state
- Use `interface` for object shapes, `type` for unions/intersections
- Avoid `any` - use `unknown` if type is truly unknown
- Export types that consumers need

### Styling

- Use Tailwind CSS for utility-first styling
- Use `cn()` utility for conditional classes (typically from `@/lib/utils`)
- Keep component styles co-located with components
- Use CSS variables for theming

### Testing

- Use Vitest + React Testing Library
- Test behavior, not implementation details
- Use `screen` queries over container queries
- Prefer `userEvent` over `fireEvent`

```tsx
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";

test("button calls onClick when clicked", async () => {
  const handleClick = vi.fn();
  render(<Button onClick={handleClick}>Click me</Button>);

  await userEvent.click(screen.getByRole("button", { name: /click me/i }));

  expect(handleClick).toHaveBeenCalledOnce();
});
```

### Performance

- Use `React.memo()` sparingly and measure first
- Use `useMemo`/`useCallback` for expensive computations or stable references
- Lazy load routes and heavy components with `React.lazy()`
- Avoid inline object/array creation in render

### Accessibility

- Use semantic HTML elements
- Include proper ARIA attributes when needed
- Ensure keyboard navigation works
- Test with screen readers when possible

### API Integration

- Create typed API client functions in `lib/`
- Handle loading, error, and success states
- Use React Query/SWR for server state (if applicable)
- Implement proper error boundaries

### Environment Variables

- Prefix with `VITE_` for client-side access (Vite)
- Never expose secrets to the client
- Use `.env.local` for local overrides (gitignored)
- Document required variables in README
