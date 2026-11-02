# Expenses Tracker

A simple expenses tracker for India. Add what you spend and receive, import a bank statement file, and read a clear report every month. Rupees and English only at launch. Sign in with Google. Free for now.

Status: planning and design are done. No application code yet. Coding starts after the design is approved.

## Folders

- `design/boards/` : every screen as an HTML board, plus `canvas.json` (the layout of the design canvas).
  - Mobile screens: `SignIn`, `Home`, `Add`, `Transactions`, `Import`, `Budgets`, `Report` (390 wide).
  - Web screens: the same names with a `Web` prefix (1280 wide).
  - Landing page: `Landing` (desktop) and `LandingMobile`. Share card: `ShareCard`.
  - `Main` is the foundations board (colours, type, spacing, components).
  - The boards are plain HTML. They preview best inside the Claude Design canvas.
- `design/images/web/` : compressed images used in the landing page.
- `design/images/originals/` : full-size generated images, kept as source files.
- `tools/` : Python scripts that generate the web and landing boards. They contain paths from the original workspace, so adjust the paths before running them.
- `docs/` : the product plan and the image prompts (export them from the Docs and add them here).

## Design decisions

- Black and white base. Blue for filters, selected items and links. Green for money received and "on track". Red for money spent.
- Category colours: Food orange, Rent blue, Travel teal, Shopping purple, Bills pink, Others slate. Others holds anything that does not fit; if it grows past 10 percent of spending, the monthly report asks the user to sort those items.
- Font: Inter. Outline icons. No emojis anywhere.
- Status is never shown by colour alone (every chip has words). Touch targets are at least 44px.
- Money is stored as whole paise (integers) to avoid rounding errors.

## Planned stack

- Web app (PWA first): Next.js, TypeScript, Tailwind, Recharts.
- API: NestJS. Database: MongoDB (Atlas, Mumbai) with Mongoose.
- Background jobs: BullMQ with Redis. Sign-in: Google OAuth.
- Monitoring: Sentry and PostHog.

## Roadmap

- v1: manual entry, CSV and Excel statement import, budgets, monthly report.
- v1.5: bank connection, only if a legal Account Aggregator route is found.
- v2: AI analysis of the monthly report.
- v3 or v4: families.
