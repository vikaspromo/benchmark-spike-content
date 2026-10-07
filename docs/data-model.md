# Data Model

Data Model owns record meanings, identity and validity. It defines which records remain distinct, what their fields mean, which representations are valid, and how provenance and history are preserved.

Read the sections governing the affected records, relationships and responses. Product owns system purpose and scope; User Design owns product-user behavior, language and voice; Writing Standards owns article content and writing standards; Architecture owns component responsibilities, processing and serving; Engineering owns implementation discipline and verification; Release owns deployment and recovery; AGENTS owns agent responsibilities, authorization and governing-document changes.

Data Model defines the information and constraints those owners use. Architecture defines how records are created, updated and served; User Design defines what product users receive.

## Client Information

Client information must accommodate multiple websites and physical locations. It must distinguish physical locations from article target geography, and treatments from bookable appointments. Provider roles, credentials, and treatment associations must refer to the correct person.

[User Design](userdesign.md#article-content-and-writing-standards) defines how articles reflect client information and make missing or conflicting information visible.

## Article Research Material

Article research material records identify useful source material for a particular article, the evidence it provides, and its intended use. A record belongs to the article's assignment and remains distinct from a practice-wide catalog. Material types and content eligibility are owned by [Writing Standards](writing-standards.md#practice-research-and-provider-coverage).

Each item must remain distinguishable within the article's research and carry the following information:

| Information | Meaning |
|---|---|
| Material type | The applicable kind or kinds of material defined in Writing Standards. A case and its image may be associated without treating either as a complete account of the other. |
| Source and available material | The source page and the passage, caption, or asset being considered. An image includes its asset location as well as the page providing context. |
| Supported facts and associations | What the source establishes, including relevant person, treatment, product, technology, or practice associations. Source statements remain distinguishable from the agent's interpretation. |
| Relevance | How the item could help answer this article's question or explain the patient experience. |
| Limits and unresolved facts | What the source does not establish, conflicting evidence, and specific unknowns that affect use. An unknown association is not a confirmed association. |
| Selection and reason | Whether use is undecided, selected, or omitted, with the reason once decided. Selection is an editorial decision, not confirmation of factual support. |
| Planned use | For selected material, the intended section and contribution. Selected images also have an intended placement and proposed caption. |

Discovery, factual support, and selection remain distinct. A source image's presence on the website does not establish that it depicts the practice or its work. Evidence for practice use of one product does not establish use of another formulation or device model. These associations retain their supporting evidence or remain unresolved under Writing Standards.

[Architecture](architecture.md#understand-the-practice) defines acquisition and interpretation; [Build the Outline](architecture.md#build-the-outline) defines selection and planned use. These records describe proposed use, not proof that material appears in the final article.

## Assignments and Article Status

The assignment prompt number remains fixed through revisions. [User Design](userdesign.md#assignment-delivery-and-tracking) defines its presentation in article filenames and the batch Sheet.

Article status has the following meanings, using the labels defined in [User Design](userdesign.md#assignment-delivery-and-tracking):

- Drafting: The article is being prepared for Alex’s review.
- Needs Information: A draft is available with required facts still missing.
- Ready for Review: Required facts are resolved, and the article is ready for Alex’s editorial review.
- Revising: Alex’s information or editorial feedback is being incorporated.
- Accepted: Alex has confirmed that the completed article meets his expectations, with no unresolved required facts.

[User Design](userdesign.md#review-revision-and-writing-feedback) defines the customer review interactions and status changes.
