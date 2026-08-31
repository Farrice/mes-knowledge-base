# Working Demonstration

This is a local, deterministic demonstration using synthetic `.test` records. It shows the workflow behavior without calling an AI model, CRM, email service, or client system.

Run it:

```bash
python3 lead_to_proposal.py
python3 -m unittest discover -s tests
```

What it demonstrates:

- inquiry capture and duplicate detection;
- qualification summary and confidence;
- missing and conflicting information flags;
- proposal draft from supplied facts;
- follow-up task and CRM-ready record;
- exception routing for sensitive data, integration failure, and unsupported claims;
- a non-bypassable human hold on every external send.

What it does not demonstrate:

- a live integration;
- AI model quality;
- client adoption;
- revenue impact;
- a paid pilot.
