# CapitalBench Private Eval Sprint - Private Audit Packet Delivery Method

Private audit packets are delivered through a client-approved channel after final scoring and report review.

## Default Method

- Package files into a single ZIP.
- Include `evaluation_manifest.yaml` and `hash_manifest.txt`.
- Compute a SHA-256 hash for the ZIP.
- Deliver through a client-approved file-transfer method.
- Send the package hash separately in the delivery email or report.

## Delivery Record

Record:

- Packet filename
- Packet SHA-256 hash
- Delivery channel
- Delivery date and time
- Recipient names or email addresses
- Retention period
- Any client-specific deletion requirements

## Assurance Limits

Customer-executed results are clearly identified because CapitalBench did not directly control execution. They may be useful internally, but they provide weaker independent execution assurance.
