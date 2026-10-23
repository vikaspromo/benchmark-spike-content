# Agent guidance

In this document, **operator** means the person directing the agent’s work and approving project decisions. Vikas is the operator for this project.

**Project lifecycle:** A selected idea moves through [governing-document approval](#review-and-approve-the-change) → [Roadmap gap tracking](#roadmap-and-icebox) → [implementation](#implement-the-authorized-changes) → [verification and completion](#verify-and-deliver-the-work). Ideas may be saved in [Icebox](docs/icebox.md) before adoption. Implementation or verification gaps under existing requirements enter at the Roadmap step.

## Governing documents and requirements

### Find the applicable requirements

The eight documents in the table are the **project governing documents**. Read AGENTS for every task. Before work, consult the documents that own the affected requirements and their dependencies. Keep each requirement in its owning document; other documents link to it rather than repeat it.

| Document | Owns |
|---|---|
| [AGENTS](AGENTS.md) | • Agent working instructions and communication<br>• Authorization and operator decisions for project work<br>• Planning and investigations<br>• Verification, repository delivery and recovery<br>• Maintenance of project governing documents |
| [Product](docs/product.md) | • Purpose<br>• Goals |
| [User Design](docs/userdesign.md) | • Product experience, required capabilities (including operator-facing capabilities) and supported surfaces<br>• Required information, explanations and interactions<br>• Strategic criteria, recommendations and output quality<br>• Labels, wording, presentation, language and voice<br>• Email and revision experience |
| [Architecture](docs/architecture.md) | • System components, interfaces, dependencies and processing<br>• Source acquisition, retrieval and evidence interpretation<br>• Methods for producing and checking recommendations and drafts, including reasoning in Codex<br>• Sources and retained context: meanings, identity, timing, validity, retention, updates and reuse<br>• Action execution and failures |
| [Writing Standards](docs/writing-standards.md) | • Intended readers, reader priorities and useful topic coverage<br>• Article voice, clarity, structure and style conventions<br>• Practice customization, clinician selection and geographic relevance<br>• Medical claims, factual support, attribution and necessary qualifications<br>• Article length, headings, links and calls to action |
| [Data Model](docs/data-model.md) | • Client, clinician, treatment and location information and associations<br>• Source evidence, interpretations, limits and unknown information<br>• Assignment identity, article versions, production inputs and status meanings<br>• Article support-and-check records, assessments and unresolved issues<br>• Record retention, reviewed versions and disposable working material |
| [Engineering](docs/engineering.md) | • Product development, investigation and review discipline<br>• Mechanical, editorial, factual and presentation verification<br>• Requirement checklists, finding-specific repair recommendations and supporting evidence<br>• Verification of the exact article version and actual customer delivery<br>• Limits of verification and completion claims |
| [Release](docs/release.md) | • Production target and delivery of reviewed product changes<br>• Deployment compatibility and deployed verification<br>• Recovery from failed product operations |

Writing Standards, Data Model, Engineering and Release own the specialized subjects listed in their rows, including where another row describes broader responsibilities.

### Apply requirements and resolve conflicts

- **Follow the current requirements.** Stay within the approved scope. Choose internal implementation details yourself when they preserve required outcomes and do not expand scope. Current requirements remain in force until approval of a change.

- **Question requirements when there is a concrete reason.** If an outcome is unclear or evidence questions a requirement’s usefulness or cost, explain the problem, consequences and simplest adequate alternative. Recommend whether to clarify, retain, simplify or remove it. Past use, existing code, tests, prototypes, possible future uses and work already done do not by themselves justify keeping a requirement or artifact.

- **Get approval before expanding scope.** Expansion includes a new capability, another independently usable way to operate the system, or a substantial new ongoing responsibility. Explain the change and its effects before implementing it unless already authorized. Approval applies only to the specified decision or action, within its stated scope and conditions.

- **Check what a failure shows.** Determine whether the implementation failed to follow an existing requirement or the requirement needs to change. Before recommending a general rule, check evidence from relevant differing situations. If the evidence is insufficient, recommend a bounded review or defer the recommendation. Deliberate product choices can establish new requirements without prior trial results.

- **Do not create one-off exceptions.** Feedback and evaluation expectations can support reviewing a requirement; they do not authorize bypassing it for one result. Resolve a dispute through a supported correction under current requirements, an approved general change, or an explicit unresolved finding pending more evidence.

- **Report gaps and protect achieved outcomes.** Report unmet requirements with evidence and a recommended next step. If an approach would sacrifice an achieved required outcome, stop that approach, explain the tradeoff and obtain the operator’s decision before proceeding.

### Prepare an integrated revision

Apply these instructions when proposing, drafting or editing governing documents, including drafts shown in conversation.

- Integrate all findings and requested changes into their owning topics. Rewrite affected material as a coherent whole.

- Recommend retaining, moving or restoring text only when it provides a needed decision, action or safeguard not adequately covered elsewhere in the same document, in other project governing documents or in applicable shared instructions. Explain what would be lost without the text and why preventing that loss justifies the burden of keeping it. Otherwise propose removal, combination or a reference to the authoritative owner. Different wording or placement alone does not justify repetition.

- Use one project term for each defined concept. Its definition in the approved owning document is authoritative throughout the project. Before introducing a concept, check whether an existing definition covers it. Define a needed new concept once in its owning document, and use that term consistently elsewhere. When changing a term or meaning, reconcile its definition and affected uses—including alternate names, diagrams and plans—in one consolidated revision.

- Make clear what is required, who must act, when a rule applies, what must happen first, its conditions, exceptions and dependencies, and what evidence establishes completion. Use direct references. Omit details already maintained in code, schemas, configuration, tests, comments or CLI help unless they establish a requirement or boundary.

- Use H2 headings for major areas of responsibility and H3 headings for distinct tasks or decisions within them that an agent needs to find independently. Keep closely related rules together. Add a heading when it improves retrieval or makes applicability clearer; importance or paragraph length alone is insufficient.

- Before adding an H2 or H3, consider rewriting an existing section or using another owning document. If a new heading is needed, call out the proposed heading separately from the diff and explain its purpose and why the alternatives are insufficient. Obtain approval before applying it; that approval may be included in the same document-revision proposal.

### Review and approve the change

Before presenting the approval diff, check the final document’s coherence, references and required meaning, including effects on unchanged sections and related requirements. Check whether another agent can find the applicable requirements from the headings and references, understand their authority and conditions, and follow their dependencies without guessing or routinely reading every project governing document in full. Identify unresolved inconsistencies and implementation gaps explicitly.

- **Get approval before changing requirements.** For requirement or instruction changes, present the exact consolidated document diff. Obtain approval before applying the change or implementing behavior that depends on it.

- After applying an approved revision, record any resulting implementation or verification gaps in [Roadmap](#roadmap-and-icebox).

## Implementation and verification

### Resolve open questions

When a question needs investigation, state the question and required output. Produce a supported answer or concrete proposal, or identify the missing input or operator decision that prevents completion and the work that depends on it. Recommend whether to include or defer discoveries outside scope before acting on them.

### Identify the required changes

- Compare the existing code with the governing requirements and identify the changes needed to satisfy them. Review affected dependencies together and choose the simplest maintained implementation.

- Before retaining, changing or removing code, documentation or development material, identify the outcome each item is needed to achieve or verify. Retain it only while that need continues, following [Apply requirements and resolve conflicts](#apply-requirements-and-resolve-conflicts).

### Obtain required approval

Where approval is required:

- Separate preparing the proposal from applying the decision. State what each checkpoint must produce, how it will be checked, what work may proceed and what must wait.

- Record the pending decision as a blocker for any affected [Roadmap gap](#roadmap-and-icebox). Present the verified proposal and requested decision, then wait at the checkpoint.

For an authorized persistent Codex Goal, use the bounded phase’s outcome, evidence, constraints, resource boundaries and stopping conditions as its objective. Before approval, limit the Goal to the proposal phase. Do not activate the next phase automatically.

### Implement the authorized changes

- Implement the behavior required by the governing documents within the authorized scope.

- Limit changes to satisfying governing requirements, preserving required meaning and behavior, resolving inconsistencies or duplication, or removing obsolete material.

### Verify and deliver the work

- Verify affected required outcomes with suitable checks and source evidence before claiming completion. Report what was inspected or tested, its coverage and limits, and any unresolved result. Structural checks alone do not establish factual support or sound strategy.

- Before claiming the larger goal complete, distinguish resolved decisions, implementation gaps under settled requirements and decisions explicitly deferred outside its scope. Do not claim completion while an unresolved decision or implementation gap prevents the required outcome. If authorized limits prevent completion, report the evidence, remaining gap and input needed. An ended attempt or exhausted budget does not establish completion.

- Deliver implementation changes with compatible code and documentation. Check for private material before committing, and report actual commit and push results.

## Roadmap and Icebox

- **Roadmap:** Record gaps between approved governing requirements and verified implementation, including missing behavior, behavior that needs to change or be removed, and outstanding verification. Link each gap to its governing requirements and record its status, blockers and next action or decision. Remove completed work after reporting completion, then commit the update.

- **Icebox:** Hold ideas not yet adopted as governing requirements. Consult or update it only at the operator’s request.

Neither file establishes requirements or authorizes work. Their updates do not require governing-document revision approval.
