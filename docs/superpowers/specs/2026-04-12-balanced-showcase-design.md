# Balanced Showcase Design

## Goal

Upgrade the repository so it presents the Bank Management project as a stronger recruiter-facing portfolio piece while preserving both interfaces as equally important parts of the project.

The result should make the repository feel intentional and polished:

- The `CLI` version remains a clear demonstration of Python logic, file handling, and banking workflows.
- The `Streamlit` version becomes a modern demo experience with better visual polish, smoother flow, and useful dashboard stats.
- The `README` explains how the two interfaces complement each other rather than looking like duplicate implementations.

## Scope

This design covers:

- A recruiter-focused `README` rewrite
- A visual and UX refresh of `bank_app.py`
- Small supporting project improvements needed to present the repository cleanly

This design does not include:

- Rebuilding the project around a database
- Adding authentication
- Major backend architecture changes
- Removing the CLI version

## Product Positioning

The repository should be framed as a dual-interface banking project:

- `CLI Experience`: a straightforward console workflow that highlights the underlying account operations and persistence logic
- `Streamlit Experience`: a polished dashboard-driven interface that makes the same project easier to demo visually

The story for recruiters is that the project shows both foundational Python capability and the ability to package the same problem into a more presentation-ready interface.

## README Design

The `README.md` should be rewritten to feel like a portfolio project page rather than a plain text assignment summary.

Planned sections:

1. Project title and concise value proposition
2. Badges and quick metadata
3. Overview of the project and what problem it simulates
4. Why the project stands out for recruiters
5. Dual-interface section describing `CLI` and `Streamlit` equally
6. Core feature highlights
7. Tech stack
8. Project structure
9. Run instructions for `CLI`
10. Run instructions for `Streamlit`
11. Data storage explanation
12. Future improvements
13. Author/contact section

Tone and presentation goals:

- concise and professional
- easy to skim
- visually structured with tables, callouts, and code blocks where helpful
- explicit about what skills the project demonstrates

## Streamlit UI Design

The `Streamlit` app should move from a basic form collection to a small banking dashboard demo.

Planned visual direction:

- portfolio-style dashboard aesthetic
- deep navy base with teal or cyan highlights
- card-based sections with clear spacing
- stronger hierarchy for headings, metrics, and actions
- more polished layout than the default Streamlit look

Planned UX improvements:

- top-level dashboard metrics such as total accounts, total funds, average balance, and highest balance
- clearer action grouping for create, deposit, withdraw, show details, update, and delete
- better empty states and validation messages
- clearer confirmation feedback after each action
- stronger presentation of account details than raw JSON output

Navigation should remain easy to understand and maintain. The implementation can use sidebar navigation, top-level sections, or a hybrid approach, but the experience should feel cohesive and faster to demo than the current version.

## Data and Logic Expectations

The current JSON-backed persistence model stays in place.

Implementation should preserve existing banking actions while improving the presentation and interaction quality. Small logic cleanup is acceptable where needed to support smoother UI behavior, but the project should remain lightweight and beginner-readable.

## Error Handling

The refreshed app should handle common cases clearly:

- invalid account number or PIN
- underage account creation attempts
- malformed PIN input
- deposit or withdrawal with invalid amounts
- insufficient funds
- missing or empty data states

Messages should be specific and friendly enough for a demo setting.

## Testing and Verification

Validation for completion should include:

- running the `Streamlit` app successfully
- verifying all six banking flows still work
- checking that `README` instructions match actual commands and file names
- reviewing the final repository presentation for clarity and consistency

## Implementation Notes

- Keep both interfaces visible and valuable in the final presentation
- Prefer focused cleanup over large refactors
- Avoid introducing unnecessary dependencies unless they materially improve presentation
- If screenshots are added later, they should support the recruiter-first README story
