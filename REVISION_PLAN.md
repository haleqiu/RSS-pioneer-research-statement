# RSS Pioneers 2026 Research Statement — Revision Plan

## 1. Internalized Style and Context

### RSS Pioneers Evaluation Criteria (from official Apply page)

The research statement is evaluated for:

1. **Motivation** — Why does this research matter?
2. **Clarity** — Well-defined and scoped problem
3. **Related work** — Brief review of the field
4. **Contributions** — Applicant's approaches, novelty, advantages over existing
5. **Future directions** — Overview of planned research

### Format Constraints

- **Length:** 2 pages max (main content); references may extend to page 3
- **Template:** RSS LaTeX (IEEEtran) — margins, font, spacing must not be tampered with
- **Anonymization:** Mandatory. Omit author names and paper titles in self-citations. Use "Anonymous authors" and generic citation format.
- **No:** external links, grant numbers, videos, code repos that reveal identity

### Style Analysis from 5 Accepted RSS Pioneers 2025 Statements

**Analyzed:** Long (uncertainty/control), Ren (LiDAR MAVs), Pan (neural scene rep), Ho (continual learning), Ding (4D radar)

#### Structural Patterns

| Feature | Pattern across all 5 |
|---------|---------------------|
| **Sections** | 3 main sections: Intro/Motivation → Past Work → Future. Numbered (I, II, III) using IEEE format |
| **Subsections** | Past work organized into 2–4 clear subsections (A, B, C...), each a named research thrust |
| **Future work** | 2–3 named directions, each with bold header, 1 paragraph, clear goal |
| **Figures** | All 5 have at least 1 figure (overview/demo) within the 2 content pages |
| **References** | Range from ~21 (Ho) to ~48 (Long); median ~24 |
| **"Significance" section** | None of the 5 have this as a separate section; it's woven into intro and future |
| **Related work** | Either merged into Introduction (Long, Ren, Ho, Ding) or merged with Motivation (Pan). Never a standalone section |

#### Writing Style

| Element | Observation |
|---------|-------------|
| **Opening** | Lead with the big-picture vision, then narrow to specific gap and your approach (within ~4 sentences) |
| **Personal voice** | "My research focuses on…", "I aim to…", "We propose…" — active, first-person throughout |
| **Contribution framing** | Each past contribution gets a bolded name, 1 paragraph, concrete results (numbers) |
| **Transitions** | Between past-work subsections, brief sentences link one thrust to the next |
| **Density** | Very dense; every sentence carries content. No filler. ~700–900 words for content pages |
| **Research questions** | Some (Ren) frame explicit research questions; most embed them in motivation |
| **"Implications"** | Ho uses "Implications:" sub-headers to highlight impact of each contribution |

#### Key Contrasts with Yuheng's Current Draft

| Yuheng's draft | Accepted examples | Action |
|----------------|-------------------|--------|
| 5 sections (Motivation, Related Work, Contributions, Future, Significance) | 3 sections (Intro, Past Work, Future) | Consolidate: merge Related Work into Introduction; merge Significance into Future or drop |
| No figure | All have 1–2 figures | Add overview figure (pipeline/framework diagram) |
| "Related Work" is standalone paragraph | Related work woven into Intro or Motivation | Merge into Introduction |
| "Significance" section | Not present in any example | Remove; weave key message into intro/future |
| Uses `\section{}` in paper_template.tex; uses `\subsection*{}` in formal_proposal.tex | Numbered sections (I, II, III) with lettered subsections (A, B, C) | Use numbered `\section{}` and `\subsection{}` |
| Contributions listed by bold name (good) but no subsection letters | Subsections A, B, C for each thrust | Add lettered subsections under Past Work |
| Future directions are 1 sentence each | Future directions are 1 paragraph each with rationale | Expand each future direction slightly |

### Scientific Writing Principles (from SKILL.md)

- **BLUF:** Lead each paragraph with its main claim; readers grasp purpose in 1–2 sentences
- **Williams:** Characters as subjects, actions as verbs, old before new, get to verb quickly
- **Concision:** Cut filler ("in order to" → "to"), avoid nominalizations, prefer affirmative
- **Style:** No em dashes; one sentence per line in `.tex`
- **Anti-patterns:** Don't bury the main point; avoid vague quantifiers without numbers

---

## 2. Current Draft Assessment

### Strengths

- **Narrative** — Clear unifying theme: learned uncertainty as the currency of spatial perception
- **Contributions** — Four concrete thrusts with citations (MAC-VO, AirIMU/AirIO, QuantMAC-VO/COME, MAC-I²)
- **Future** — Three named directions (MACVIO, MACSLAM, MAC-IO)
- **Anonymization** — Uses `anonymous2025`/`anonymous2026` style; paper titles omitted in text
- **Bold sub-headers** within contributions section — mirrors the accepted style

### Areas for Revision

| Area | Observation | Priority |
|------|-------------|----------|
| **Section structure** | 5 sections → should be 3 (Intro, Past Work, Future) | **High** |
| **Missing figure** | All accepted examples have 1–2 figures | **High** |
| **Related Work standalone** | Should merge into Introduction | **High** |
| **Significance section** | Not in any accepted example; remove/merge | **Medium** |
| **Subsection numbering** | Add A, B, C under Past Work (and optionally Future) | **Medium** |
| **BLUF** | Motivation opens with dual challenge; consider leading with the core thesis first | **Medium** |
| **Future directions** | Too brief (1 sentence each); expand to 1 paragraph each | **Medium** |
| **Concision** | Phrases like "at the same time," some long compound sentences | **Low** |
| **One sentence per line** | Multiple sentences per line in `.tex` | **Low** |

---

## 3. TODO and Schedule

### Phase 1: Structural Restructuring (highest impact)

- [ ] **Restructure to 3 sections:** I. Introduction (merge Motivation + Related Work + vision), II. Past and Current Research (rename "Approaches and Contributions"), III. Future Work (merge in Significance)
- [ ] **Add lettered subsections** under Past Work (A. Learned Visual Uncertainty, B. Learned Inertial Uncertainty, C. Compute-Efficient Deployment, D. Robust Visual-Inertial Fusion)
- [ ] **Add a figure:** Overview diagram of the "learned uncertainty" framework showing how the pieces connect (MAC-VO → AirIMU → efficiency → fusion → SLAM)
- [ ] **Use numbered sections** (`\section{}` not `\subsection*{}`) to match IEEE convention used by all accepted examples
- [ ] **Remove "Significance" section:** Weave the "any robot, anywhere" message into the Introduction's opening and Future Work's closing

### Phase 2: Content Alignment with Accepted Style

- [ ] **Introduction:** Open with big-picture vision (1–2 sentences), narrow to gap (1–2 sentences), state your approach/thesis (1–2 sentences). Weave related work inline with citations. Keep to ~1/3 page
- [ ] **Past Work subsections:** Each subsection: 1 topic sentence (what you did), 2–3 sentences (how, what's novel), 1 sentence (result with numbers). Add transitions between subsections
- [ ] **Future Work:** Expand each direction from 1–2 sentences to a full paragraph with: current gap → proposed approach → expected outcome
- [ ] **Concrete numbers:** Ensure each contribution cites a quantitative result (e.g., "X% improvement," "Y× speedup," "Best Paper at Z")

### Phase 3: Scientific Writing Polish

- [ ] **BLUF check** — Read only topic sentences; ensure they convey the argument
- [ ] **Williams pass** — Subjects as actors, verbs as actions; fix nominalizations
- [ ] **Concision** — Remove filler, tighten long sentences, fix fragments ("Achieves 1.83×...")
- [ ] **Format** — One sentence per line in `.tex`
- [ ] **Anonymization** — Re-verify all self-citations; ensure no paper titles or identifying links

### Phase 4: Final Checks

- [ ] Compile with RSS template; verify 2-page limit and margins
- [ ] Read aloud for flow and sentence variety
- [ ] Cross-check against evaluation criteria: Motivation? Clarity? Related work? Contributions? Future?

---

## 4. Suggested Timeline

| Phase | Effort | Priority |
|-------|--------|----------|
| Phase 1 | ~1 hour | **Do first** — structural changes have the highest impact |
| Phase 2 | ~45 min | Content alignment |
| Phase 3 | ~30 min | Line-level polish |
| Phase 4 | ~15 min | Before submission |

**Total:** ~2.5 hours of focused revision.

---

## 5. Proposed New Structure (Target)

```
I. INTRODUCTION
   - Big-picture vision: robust, generalizable, efficient spatial perception
   - Gap: uncertainty is treated as afterthought; hand-tuned, platform-specific
   - Thesis: learned uncertainty is the unifying principle
   - Brief related work woven in (3–4 citations)
   - [FIGURE 1: Overview of framework]

II. PAST AND CURRENT RESEARCH
   A. Learned Visual Uncertainty (MAC-VO, ICRA 2025 Best Paper)
   B. Learned Inertial Uncertainty (AirIMU, AirIO)
   C. Compute-Efficient Deployment (QuantMAC-VO, COME)
   D. Robust Visual-Inertial Fusion (MAC-I²)

III. FUTURE WORK
   A. Cross-Modal Uncertainty Fusion (MACVIO) — 1 paragraph
   B. Uncertainty-Aware SLAM (MACSLAM) — 1 paragraph
   C. Self-Supervised Inertial Odometry (MAC-IO) — 1 paragraph
   - Closing: "any robot, anywhere" vision (1–2 sentences)

REFERENCES (page 3)
```

---

## 6. Key Takeaways

- Your content is strong. The main improvement is **structural alignment** with accepted examples.
- The 3-section format (Intro → Past Work → Future) is universal across all 5 analyzed statements.
- Adding a figure is important; every accepted statement has one.
- The "learned uncertainty" narrative is a clear differentiator; keep it front and center in the Introduction.
- Related work should be woven into the Introduction, not standalone.
- Future directions need more substance (1 paragraph each, not 1–2 sentences).
