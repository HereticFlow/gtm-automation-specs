# gtm-automation-specs
Description : Technical specifications and Python automations for building an AI-native GTM engine.
# GTM Automation Specs

This repository contains the technical specifications, logic, and Python automations for building an AI-native Go-To-Market (GTM) engine. 

It is designed as a practical portfolio demonstrating how to bridge the gap between marketing demand and sales execution: capturing signals, qualifying leads, routing them, and feeding data back into the loop.

## Repository Structure

- `/specs` — Markdown specifications for outbound sequences, lead scoring, and attribution.
- `/automations` — Python scripts for lead enrichment, scoring, and routing.
- `/tests` — Unit tests for the automation logic.
- `/data` — Synthetic CSV data used for testing.

## Core Philosophy

The core philosophy here is **"builder mentality"**: spend a week building the system once, rather than two weeks running it by hand every time.

## Running Tests
To run the unit tests for the lead scoring automation, execute:
`python -m unittest discover tests`
