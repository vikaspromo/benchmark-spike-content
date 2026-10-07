# Data Model

Data Model owns record meanings, identity and validity. It defines which records remain distinct, what their fields mean, which representations are valid, and how provenance and history are preserved.

Read the sections governing the affected records, relationships and responses. Product owns system purpose and scope; User Design owns product-user behavior, language and voice; Writing Standards owns article content and writing standards; Architecture owns component responsibilities, processing and serving; Engineering owns implementation discipline and verification; Release owns deployment and recovery; AGENTS owns agent responsibilities, authorization and governing-document changes.

Data Model defines the information and constraints those owners use. Architecture defines how records are created, updated and served; User Design defines what product users receive.

## Client Information

Client information must accommodate multiple websites and physical locations. It must distinguish physical locations from article target geography, and treatments from bookable appointments. Provider roles, credentials, and treatment associations must refer to the correct person.

[User Design](userdesign.md#article-content-and-writing-standards) defines how articles reflect client information and make missing or conflicting information visible.

## Assignments and Article Status

The assignment prompt number remains fixed through revisions. [User Design](userdesign.md#assignment-delivery-and-tracking) defines its presentation in article filenames and the batch Sheet.

Article status has the following meanings, using the labels defined in [User Design](userdesign.md#assignment-delivery-and-tracking):

- Drafting: The article is being prepared for Alex’s review.
- Needs Information: A draft is available with required facts still missing.
- Ready for Review: Required facts are resolved, and the article is ready for Alex’s editorial review.
- Revising: Alex’s information or editorial feedback is being incorporated.
- Accepted: Alex has confirmed that the completed article meets his expectations, with no unresolved required facts.

[User Design](userdesign.md#review-revision-and-writing-feedback) defines the customer review interactions and status changes.
