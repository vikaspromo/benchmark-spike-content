# Data Model

## Client Information

Client information must accommodate multiple websites and physical locations. It must distinguish physical locations from article target geography, and treatments from bookable appointments. Clinician roles, credentials, and treatment associations must refer to the correct person.

[User Design](userdesign.md#article-content-and-writing-standards) defines how articles reflect client information and make missing or conflicting information visible.

## Article Research Material

Keep source links and the passages needed to verify the resulting article's factual claims and practice associations in its support-and-check record under [Assignments and Article Status](#assignments-and-article-status). Retain material limits or conflicts when they affect those claims or unresolved issues. Sources can support several passages; do not repeat the same evidence for each occurrence. [Writing Standards](writing-standards.md#content-types) owns material eligibility.

Distinguish source statements from interpretation and unknown associations from confirmed ones. Evidence for one product does not establish another formulation or device model.

## Assignments and Article Status

The assignment prompt number remains fixed through revisions. [User Design](userdesign.md#assignment-delivery-and-tracking) defines its presentation in article filenames and the review index.

Retain two items for each article version: the article, including its customer comments, and one compact support-and-check record. The record contains:

- **Identity:** A reference to the original assignment, the exact article version checked and the customer Doc URL once the Doc exists.
- **Article status:** The current status under the meanings below.
- **Production inputs:** The **agent version** is the repository commit used for production. It is distinct from the article version. If relevant inputs were uncommitted, include their exact diff; the commit alone does not identify those inputs.
- **Claim support:** The source evidence required by [Article Research Material](#article-research-material).
- **Final checks:** The outcome for every applicable requirement, concise evidence sufficient to establish each result, and the measured body-word count. A failure identifies the requirement, location, and correction needed. Keep required facts awaiting Alex, optional requests, and inapplicable requirements distinct from passes and other failures. Identify unperformed or unverified checks explicitly.
- **Unresolved issues:** Only issues that still affect verification, revision, or delivery. While comments have not been posted to the article Doc, keep their text and anchors here so they can be transferred accurately.

The article assessment is the final-check portion of this record. [Engineering](engineering.md#article-verification) owns how evidence establishes each result; [Architecture](architecture.md#evaluate-and-revise) owns checking and revision.

Briefs, plans, outlines, investigation notes, intermediate checks, and transfer files are working material. They do not require separate retention after the article and support-and-check record contain the needed evidence and unresolved issues. Do not retain production histories or duplicate research, assessment, and provenance records. Preserve reviewed article versions; replacing working material does not authorize deleting those versions.

Article status has the following meanings, using the labels defined in [User Design](userdesign.md#assignment-delivery-and-tracking):

- Drafting: The article is being prepared for Alex's review; this includes unresolved checklist failures before delivery.
- Needs Information: A draft is available with required facts still missing and no other unresolved checklist failures.
- Ready for Review: Required facts are resolved and the resulting article has passed the applicable checks for Alex's editorial review.
- Revising: Alex's information or editorial feedback is being incorporated.
- Accepted: Alex has confirmed that the completed article meets his expectations, with no unresolved required facts.

[User Design](userdesign.md#review-revision-and-writing-feedback) defines the customer review interactions and status changes.
