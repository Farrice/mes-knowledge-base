# Angle Map + Message-Market-Fit Client Room — Founding Proof

This is the non-confidential cold-start fixture for the V1 Client Delivery
Room. Farrice Cain is the intended reader and The Angle Map is the subject.

The fixture proves the system can:

1. validate a complete intake and source inventory;
2. preserve a candid private working room;
3. create a separate client-facing brief without internal paths or system
   language;
4. apply an explicit release gate;
5. render Farrice Cain Premium Minimal branding;
6. create private and client ZIPs; and
7. verify hashes, local links, portability, and outward-language rules.

It does **not** prove customer demand, message-market fit, campaign performance,
or a qualified market segment. The segment and message directions remain
`PROVISIONAL` until direct customer evidence and real market exposure exist.

## Run

```bash
python3 execution/client_delivery_room.py check \
  deliverables/client-rooms/angle-map-message-market-fit-v1 --release

python3 execution/client_delivery_room.py build \
  deliverables/client-rooms/angle-map-message-market-fit-v1 \
  --output /tmp/angle-map-client-room-v1

python3 execution/client_delivery_room.py verify /tmp/angle-map-client-room-v1
```
