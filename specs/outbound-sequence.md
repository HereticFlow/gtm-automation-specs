# Specification: Multi-Channel Outbound Sequence

## 1. Objective
To systematically generate qualified meetings for Account Executives (AEs) by executing a multi-channel outbound sequence targeting [European fintech and SaaS leaders].

## 2. Ideal Customer Profile (ICP)
- **Company Size:** [Ex: 50 - 500 employees]
- **Sector:** [Ex: B2B SaaS, Fintech]
- **Geography:** [Ex: France, Benelux]
- **Target Personas:** [VP of Sales, Head of RevOps, CEO]

## 3. The Sequence Logic (The Machine)
The sequence runs over [14] days, using three channels. We stop the sequence immediately if a prospect replies.

*   **Day 1: LinkedIn View + Connection Request**
    *   *Action:* View profile, send blank connection request or a short note.
*   **Day 2: Email 1 (The Hook)**
    *   *Goal:* Grab attention, identify a pain point.
    *   *Logic:* Personalized opening line based on recent company news or LinkedIn activity. 
*   **Day 4: LinkedIn Message 1**
    *   *Goal:* Soft touch. "Thanks for connecting, saw you're working on X..."
*   **Day 7: Email 2 (The Value)**
    *   *Goal:* Share a relevant case study, metric, or asset (e.g., "How [Similar Company] reduced integration time by 40%").
*   **Day 10: Phone Call + Voicemail**
    *   *Goal:* Direct attempt. Voicemail is short (under 20 seconds).
*   **Day 14: Email 3 (The Breakup)**
    *   *Goal:* Polite close. "Assuming this isn't a priority right now, I'll stop reaching out. Feel free to ping me when it makes sense."

## 4. Data & Tooling Stack
- **Data Enrichment:** [Ex: Clay / Apollo / LinkedIn Sales Navigator]
- **Sequencing Tool:** [Ex: HubSpot / LaGrowthMachine / Lemlist]
- **CRM:** [Ex: HubSpot]

## 5. Metrics & KPIs
To evaluate the health of this sequence, we track:
- **Open Rate:** Target > [60%]
- **Reply Rate:** Target > [5%]
- **Meeting Booked Rate:** Target > [2%]
- **Cost per Meeting:** [Calculated based on tool costs + time]

## 6. The Feedback Loop (Marketing to Sales)
How do we know what works?
- **Objection Handling:** Every objection an AE hears on a call is logged in a shared Notion/HubSpot doc.
- **Iteration:** Every [2 weeks], we review the reply rates. If a specific pain point mentioned in Email 1 gets a 10% reply rate, we write Email 2 about that same pain point. 
- **Data Hygiene:** Leads that bounce or mark as spam are automatically removed from the sequence and sent to a "Do Not Contact" list to protect domain reputation.
