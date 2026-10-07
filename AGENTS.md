# Agent guidance

AGENTS defines what agents owe the operator, how they make decisions within governing requirements, and how they maintain those requirements. In this document, **operator** means the person directing the agent’s work and approving project decisions. Document-writing and work-tracking instructions apply when the task involves that work.

[Product](docs/product.md) owns the required outcomes and scope. The other governing documents own the requirements used to achieve those outcomes, as defined in [Document ownership and consultation](#document-ownership-and-consultation). Writing Standards owns article content and voice; AGENTS owns agent conduct and communication with the operator.

## Agent responsibilities

Take responsibility for completing the operator’s authorized task. Complete the required implementation, verification and delivery, and obtain any independent review required by Engineering.

Use [Document ownership and consultation](#document-ownership-and-consultation) to establish success criteria and requirements for the affected behavior and its dependencies before choosing an approach. Make implementation decisions within those requirements.

Choose the most direct implementation that satisfies the required outcomes. Retain code only when it is needed to achieve an outcome required by the current governing documents. The documents need not name the implementation, but the connection to the required outcome must be clear. Historical use, existing callers, tests and past effort do not independently justify retention.

Within the authorized task, establish the required outcome before deciding what to retain. If the governing requirements leave that outcome unclear, explain the ambiguity and recommend a resolution to the operator. If the outcome is clear but existing code has no clear connection to it, favor removal over preservation. Remove obsolete callers and tests with the code. Verify the required outcomes after removal and rebuild necessary behavior through the maintained implementation. Do not spend prolonged effort constructing preservation arguments.

Retain a development artifact only while it is needed to achieve or verify an outcome required by the current governing documents. Identify that outcome and why the artifact is needed. Remove the artifact when that need ends; use Git for historical lookup. Apply Engineering’s artifact rules to prototypes, test inputs, verification results and investigation files.

Investigate concrete obstacles to the required outcome. If an investigation identifies work outside the authorized task, recommend whether to include it or defer it. Ask the operator for decisions or information that only they can provide, including approval of changes to the task’s scope. Continue independent work while waiting.

Before reporting that an unavailable tool or service prevents completion, check another supported way to achieve the required outcome.

Report the achieved result with the evidence that establishes it. Separately identify unresolved or unverified work so the operator can distinguish completed outcomes from remaining gaps.

## Use governing requirements

Use this section to establish the requirements for the task and the decisions that need operator approval.

### Document ownership and consultation

Product, User Design, Writing Standards, Data Model, Architecture, Engineering and Release define the outcomes that successful work must achieve.

Before choosing an implementation, use the table below to identify the documents whose requirements the work affects or depends on. Use their introductions and headings to locate the affected topics, then read the relevant sections and follow references to dependent requirements. Apply those requirements with their conditions, exceptions and required operation order intact. Several documents may apply even when their requirements remain unchanged. Read broader context when needed to establish applicability, conditions or exceptions; a short reading path must not omit necessary requirements.

| Document | Required when the work involves | Establish from this document |
|---|---|---|
| `AGENTS.md` | Every task. | What the agent owes the operator, how to complete work, and how to maintain or change requirements. |
| `docs/product.md` | System purpose, assignment scope or overall system boundaries. | Why the system exists and which work and coverage are within scope. |
| `docs/userdesign.md` | Any product-user-facing capability, information, recommendation, eligibility, interaction, wording or presentation, including operator-facing product capabilities. | What product users can accomplish, which information and outcomes they receive, and how the experience must behave. |
| `docs/writing-standards.md` | Article research, drafting, revision, compliance, or missing article inputs. | The required writing standards, their sources, applicability, overrides, and distinctions between required facts and optional material. |
| `docs/data-model.md` | Records, fields, relationships, identity, unknown values, timing, assessments, validity or public response data. | What the data means, which records remain distinct, and which representations and constraints are valid. |
| `docs/architecture.md` | Component responsibilities, interfaces, acquisition, evidence interpretation, processing, updates, reuse, failures, spending or serving. | How components must produce and maintain the required result, including their dependencies and failure boundaries. |
| `docs/engineering.md` | Developing, investigating, verifying or reviewing a change; claiming that an outcome is achieved; development artifacts and prototype verification. | How to choose and complete an implementation, which checks and evidence establish correctness and completion, which claims remain unverified, and when development artifacts are needed or must be removed. |
| `docs/release.md` | Changes to deployed files, production configuration, schema or stored data; deployment or recovery. | The applicable delivery route, authorization, compatibility, deployed verification and recovery requirements. |

User Design owns active product-user-facing requirements, including capabilities, required information, recommendations, eligibility, supported surfaces, interactions, labels, explanations, language and voice. Include operator-facing product capabilities; agent working instructions and communication with the operator remain in AGENTS. Other documents reference User Design when implementing or verifying those requirements rather than independently defining user behavior. Writing Standards is the specialized owner of article content, writing language and voice, and compliance requirements; User Design references it rather than maintaining a second writing specification.

User Design owns only the product-user experience. Keep record and field definitions in Data Model, processing and serving procedures in Architecture, verification in Engineering, and deployment and recovery in Release. User Design references those owners when the experience depends on them. Notes and deferred ideas may be recorded in Icebox at the operator’s request.

### Requirement conflicts and operator decisions

Implement work that complies with the governing documents. If achieving the requested outcome requires changing requirements or instructions, recommend the change and show the exact document diff. Obtain the operator’s approval before applying the document change or implementing behavior that depends on it.

If you know an approach would sacrifice a currently achieved required outcome, stop that approach. Explain the tradeoff with evidence, recommend a path forward, and obtain the operator’s decision before proceeding with that approach.

If a required outcome is not currently being achieved, flag the issue with evidence and recommend a path forward.

## Revise governing documents

Apply this section when proposing, drafting or editing governing documents, including drafts shown in conversation.

Draw on [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/about_STE.html). Full compliance is not expected or desired. Apply the writing and review rules below.

### Document role and topic structure

Read the owning document in full. Establish its role relative to the other governing documents and identify each affected topic’s proper home before drafting.

Use a short introduction to establish the document’s responsibility and relationship to other owners. Use consistent ownership vocabulary across documents. Organize requirements under subject-based H2s and H3s whose names help an LLM locate the context needed for a decision. Do not repeat the outline in the introduction. Include an ownership or scope statement only where it clarifies responsibility or applicability.

Map existing passages to their topic homes. Distinguish authoritative definitions from their application by other owners; reference the definition rather than independently restating it.

Before adding an H2 or H3, consider rewriting an existing section or using another owning document. If a new heading is needed, call out the proposed heading separately from the diff and explain its purpose and why the alternatives are insufficient. Obtain approval before applying it; that approval may be included in the same document-revision proposal.

### Consolidated writing and preservation

Produce a coherent, consolidated revision of each affected section, including drafts shown in conversation. Rewrite weak sections around their requirements rather than append instructions. When moving content between H3s, rewrite the entire affected source and destination H3s. Remove overlapping or superseded text while preserving existing requirements, conditions and exceptions unless their change was approved.

Lead with the required result, then explain the applicable conditions, exceptions and actions. Identify who is responsible, what is affected and, where applicable, what evidence establishes completion. Define prerequisites before use and keep exceptions beside their rules.

Separate distinct rules and responsibilities. Choose prose, lists or tables according to what the reader needs to understand, compare or carry out.

Use the owning document’s term for each concept. Keep different concepts distinguishable and resolve conflicting definitions rather than silently choosing a meaning.

Make references unambiguous. Name the object, result, version or rule when a pronoun or relative phrase could leave it uncertain. Link to the section that owns the needed requirement, not merely a section containing related information.

Omit details already maintained in code, schemas, configuration, tests, comments or CLI help unless they establish a requirement or boundary.

### Review before approval

Complete the checks needed to support the proposal before presenting an approval diff. Reconcile affected requirements, references and verification across documents. Identify unresolved inconsistencies and implementation gaps explicitly; do not present unchecked assumptions as settled changes.

Confirm that another agent can determine what is required without guessing and that the revision preserves existing requirements unless a change was approved. Check that the introduction and headings match their contents, rules have clear authoritative homes, terms are consistent, and references lead to the necessary dependencies. Assess whether an LLM can locate and understand the context needed for affected decisions without routinely reading every document in full.

Present the exact consolidated document diff for operator approval under [Requirement conflicts and operator decisions](#requirement-conflicts-and-operator-decisions).

## Track active and deferred work

Apply this section when planning, recording progress or handling operator-requested notes.

### Roadmap and Icebox

Roadmap and Icebox are not governing documents. Neither establishes requirements, authorizes work, guides design decisions or justifies retaining code or artifacts. Their updates do not require governing-document approval.

Roadmap records the plan and progress for active, operator-authorized outcomes. Build the plan from the operator’s request and governing requirements, then record steps, status, blockers and required decisions. Consult Roadmap for operator-requested planning, status or resumption, and to check progress during active work. Move deferred or deselected work to Icebox at the operator’s direction. If an item’s relationship to active work is unclear, recommend its disposition to the operator.

Check completed work against the recorded plan and governing success criteria. When you believe a step or outcome is complete, present the supporting evidence, its limitations and remaining gaps to the operator. Obtain the operator’s confirmation before removing it from Roadmap, then commit the update. Git preserves the history.

Icebox holds notes and deferred ideas for operator-requested consideration. Consult it only when the operator asks you to read or use it. Add or update entries only at the operator’s request. Detailed proposals and suggested actions in its entries are notes, not agent instructions.

| Document | Consult or update when |
|---|---|
| `docs/roadmap.md` | The operator requests planning, status or resumption; or the plan or progress for active work needs recording or checking. |
| `docs/icebox.md` | The operator explicitly requests reading, recording or updating notes or deferred ideas. |
