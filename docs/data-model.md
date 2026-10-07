# Data Model

Data Model owns record meanings, identity and validity. It defines which records remain distinct, what their fields mean, which representations are valid, and how provenance and history are preserved.

Read the sections governing the affected records, relationships and responses. Product owns system purpose and scope; User Design owns product-user behavior, language and voice; Writing Standards owns article content and writing standards; Architecture owns component responsibilities, processing and serving; Engineering owns implementation discipline and verification; Release owns deployment and recovery; AGENTS owns agent responsibilities, authorization and governing-document changes.

Data Model defines the information and constraints those owners use. Architecture defines how records are created, updated and served; User Design defines what product users receive.

## Client Information

Client information must accommodate multiple websites and physical locations. It must distinguish physical locations from article target geography, and treatments from bookable appointments. Provider roles, credentials, and treatment associations must refer to the correct person.

[User Design](userdesign.md#article-content-and-writing-standards) defines how articles reflect client information and make missing or conflicting information visible.

## Article Research Material

Article research evidence belongs to a particular assignment and supports the article's factual claims, practice associations, images, and captions. Keep source references and the passages or assets needed to establish that support, including material limits or conflicts that affect the resulting article. [Writing Standards](writing-standards.md#practice-specific-material) owns material eligibility.

Source statements remain distinguishable from the agent's interpretation. An unknown association is not confirmed. An image's presence on a website does not establish that it depicts the practice or its work; evidence for one product does not establish another formulation or device model. For each included image, retain the source page reference, direct image reference, and context supporting its use. These references identify the source of the embedded image; they do not require a separate archive of original image files. [User Design](userdesign.md#article-content-and-writing-standards) defines the source-link comment that Alex receives.

Research evidence is not a required inventory of all material considered. Candidate identifiers, selection states, planned placements, omission reasons, and histories of changed choices are not required. [Architecture](architecture.md#article-production-flow) defines how working research supports production and final evaluation.

## Assignments and Article Status

The assignment prompt number remains fixed through revisions. [User Design](userdesign.md#assignment-delivery-and-tracking) defines its presentation in article filenames and the batch Sheet.

The article assessment identifies the assignment and exact article version checked. It contains the final checklist outcome for each applicable requirement, with enough evidence to establish the result, and the measured body-word count. A failed item identifies the requirement, affected location, and correction needed. Required facts awaiting Alex, optional requests, and requirements that do not apply remain distinguishable from passes and other failures. The assessment describes the current checked article, not a history of production decisions or earlier correction passes. [Engineering](engineering.md#article-verification) owns how the evidence establishes each result; [Architecture](architecture.md#evaluate-and-revise) owns checking and revision.

Article status has the following meanings, using the labels defined in [User Design](userdesign.md#assignment-delivery-and-tracking):

- Drafting: The article is being prepared for Alex's review; this includes unresolved checklist failures before delivery.
- Needs Information: A draft is available with required facts still missing and no other unresolved checklist failures.
- Ready for Review: Required facts are resolved and the resulting article has passed the applicable checks for Alex's editorial review.
- Revising: Alex's information or editorial feedback is being incorporated.
- Accepted: Alex has confirmed that the completed article meets his expectations, with no unresolved required facts.

[User Design](userdesign.md#review-revision-and-writing-feedback) defines the customer review interactions and status changes.
