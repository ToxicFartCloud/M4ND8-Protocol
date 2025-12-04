# UI Checklist — Universal Minimum (v4.4)

## Authority

- **Source of Truth:** `m4nd8_pro/ui.yaml`
- **Enforcement:** `m4nd8_pro/director.yaml` (Part II: Law)
- **Auditor Role:** `auditor` agent (from `director.yaml` workforce)
- **Failure Consequence:** **HARD_STOP → ESCALATE** if any **MUST** rule fails

---

## Scope & Intent

This checklist defines the minimum bar for:

- Accessibility  
- Interaction  
- Contract conformance  
- System-wide UI coherency  

It is **not** a visual blueprint. Teams retain full creative latitude.

Audits verify invariants only:

- Contrast  
- Focus visibility  
- Keyboard navigation  
- Target sizes  
- Token usage  
- Reduced motion  
- Required states  
- Uniformity across all UI surfaces  

Audits **must not** fail a UI because of brand choices (colors, shape language, density, shadows, micro-interactions) if invariants pass.

---

## 🛑 Non-Destructive Directive (Additive Only)

This checklist is strictly **ADDITIVE**.

- DO NOT remove, replace, or standardize existing UI to comply.  
- DO add missing features, states, tokens, or coherency to bring secondary surfaces **up** to the standard of the primary view.  
- Large additions or upgrades require a **Deprecation Record** in the local `cofo.md` only if replacing a legacy pattern—never for pure addition.

---

## References

- **Policy:** `m4nd8_pro/ui.yaml` (baseline rules; `scope = invariants_only`)  
- **Wiring / Ledger:** `hub.md` / `cofo.md`  
- **Final certification:** `m4nd8_pro/fnl_chk.yaml` (`C133` / `C134` prevent bulldozers)

---

## MUST — Invariants (Add Missing Features; Never Remove)

### A. Accessibility & Interaction

- [ ] **ID: WCAG-2.2-AA-contrast** — Add contrast-compliant text and interactive elements in all modes (light / dark / high-contrast).  
  Target ratios: text **4.5:1**, large text **3.0:1**, UI components **3.0:1**.
- [ ] **ID: Focus-Visible** — Add visible focus indicators for all interactive components (keyboard & programmatic focus).
- [ ] **ID: Keyboard-Nav** — Add full keyboard navigation: `Tab` / `Shift+Tab` traversal; `Enter` / `Space` activation; arrow keys where expected. Add **Escape-to-close** for dialogs/menus and a **focus trap** in modals.
- [ ] **ID: Hit-Target-Size** — Add hit targets **≥ 44px** for primary interactive controls.
- [ ] **ID: Motion-Reduction** — Add support for `prefers-reduced-motion`: animations must become fade/opacity-only.
- [ ] **ID: No-Text-On-Glass** — Add opaque backgrounds or separation layers for all text; enforce contrast.
- [ ] **ID: Directionality-Support** — Add LTR / RTL support where applicable.

### B. Token & Theming Contract (Anti-Slop)

- [ ] **ID: Semantic-Tokens-Used** — Add semantic tokens (for example, `text/default`, `brand/on-primary`) to all components; remove raw hex / inline styles by replacing with tokens, not deletion.
- [ ] **ID: Mode-Aware-Tokens** — Add proper token resolution for light / dark / high-contrast modes.
- [ ] **ID: No-Inline-Styles** — Add token-based styling; if inline styles exist, upgrade them to tokens—do not delete the component.

### C. Required States & Feedback (Nielsen's Heuristics)

- [ ] **ID: Component-States** — Add required states: hover, focus, active, disabled, invalid, loading to every interactive component.
- [ ] **ID: Immediate-Feedback** — Add immediate visual feedback on user actions (success / error patterns, `aria-describedby` for errors).
- [ ] **ID: Error-Prevention** — Add confirmation dialogs for destructive actions (for example, delete).
- [ ] **ID: User-Control** — Add **Undo** or **Cancel** for multi-step flows.

### D. Dialogs & Overlays

- [ ] **ID: Dialog-Contract** — Add roles, labeled titles, focus trap, Escape-to-close, and focus restoration to all dialogs.
- [ ] **ID: Tooltip-Contract** — Add dismissible, focus/hover-accessible tooltips; do not use tooltips for essential instructions.

### E. UI Coherency (System-Wide Uniformity — Additive Enforcement)

- [ ] **ID: UI-COHERENCY** — Add missing design language, tokens, and interaction patterns to **all** UI surfaces—primary views, modals, menus, settings panels, error dialogs, and system alerts—so they match the main view. **Do not** downgrade the main view.
- [ ] **ID: NO-DEFAULT-COMPONENTS** — Add design system components to replace any raw `<button>`, `<input>`, or browser-native dialogs. Do not remove functionality—upgrade it.
- [ ] **ID: TOKEN-CONSISTENCY** — Add token-based spacing, color, and typography to all surfaces; remove hardcoded values by replacing with tokens.
- [ ] **ID: STATE-UNIFORMITY** — Add consistent hover, focus, active, disabled, and error states to all instances of a component type.

### F. Non-Destructive Governance

- [ ] **ID: No-Normalization** — Preserve all custom visuals/tokens/variants. Add to them; do not replace.
- [ ] **ID: Deprecation-Record** — If a legacy pattern is replaced (not just augmented), add a Deprecation Record in `cofo.md` with rationale and migration path.

---

## SHOULD — Strong Recommendations

_Add if missing; override only with rationale._

### A. Motion & Performance

- [ ] **ID: Frame-Budget** — Add frame-optimized animations (**≤ 16.7ms**); limit heavy effects (**≤ 3** shadows, blur **≤ 8px**).
- [ ] **ID: Performance-Budget** — Add duration budgets: fast (~100ms), normal (~180ms), slow (~260ms); never exceed ~300ms.

### B. Enterprise Tables & Density

- [ ] **ID: Table-Features** — Add fixed headers, column resize, and optional column locking to data tables.
- [ ] **ID: Table-Density** — Add density modes: compact / comfortable / spacious (**hit targets ≥ 36px**).

### C. Copy & Messaging

- [ ] **ID: Feedback-Copy** — Add clear success (“Saved”, “Done”) and error recovery (“Try again”, “Check connection”) patterns.
- [ ] **ID: Sensory-Feedback** — Add optional, user-controllable auditory/haptic feedback (mute toggle; light/medium haptics).

### D. Theming & Extensions

- [ ] **ID: Custom-Tokens** — Add project-specific token namespaces (for example, `brand/*`, `app/*`) for custom styling.
- [ ] **ID: Variant-Documentation** — Add new component variants (for example, `button/brand`) to `cofo.md`.

### E. Modern Chat UI (If Applicable)

- [ ] **ID: CHAT-UI-BASELINE** — If the app is conversational, add the `modern_chat_ui` reference pattern: auto-resizing input, streaming responses, per-message action toolbar, rich content support, sidebar with history.

---

## MAY — Style & Brand Options (Purely Aesthetic — No Enforcement)

- [ ] Unique color ramps, shadows, and shapes (maintain AA contrast).  
- [ ] Typography families/sizes beyond the baseline (maintain minimum body size ≈ 16px).  
- [ ] Micro-interactions that heed reduced-motion and frame budgets.

---

## How to Audit (Additive Fast Path)

### Coherency Check (Critical)

- Do **not** compare secondary views to a generic standard—compare them to the **main view**.  
- If the main view has branded buttons, modals must be upgraded to use the same—not replaced with a neutral button.  
- If a settings panel uses raw HTML inputs, add design system components—do **not** remove the settings.

### Token & State Check

- Flag **missing** tokens/states—do not flag “non-standard” tokens.  
- Upgrade, don’t delete: replace `#155EEF` with `brand/primary`; replace `<div onclick>` with `<button>`.

### Governance

- If you add a new pattern, document it in `cofo.md`.  
- If you replace a legacy component, add a **Deprecation Record**.

### Evidence to Capture (for `fnl_chk.yaml`)

- [ ] Report listing added contrast ratios, tokens, and states.  
- [ ] Coherency report: list of upgraded secondary surfaces.  
- [ ] Governance: links to `cofo.md` Change Notes for additions or replacements.

### Exceptions

If a **MUST** cannot be met, open a HALT with:

- The exact rule ID  
- The impacted component/page  
- User impact  
- The proposed additive mitigation (for example, “Will add tokenized button in next step”)  

Add a Change Note to the affected directory’s `cofo.md` and route through the escalation protocol.

---

Remember: **This is a minimum checklist.**  
Preserve brand and craft. Pass the invariants by **adding what’s missing**—never by removing what’s unique.
