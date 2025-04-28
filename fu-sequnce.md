Example Input:
sql
Copy
Edit
Create trade for 1.5M USD with ABC Bank, 1.2M USD with EFG Bank for 30-Apr-2025
Expected Output:
yaml
Copy
Edit
I found the following trade details:

Trade 1:
Amount: 1.5M USD,
Counterparty: ABC Bank,
Date: 30-Apr-2025

Trade 2:
Amount: 1.2M USD,
Counterparty: EFG Bank,
Date: 30-Apr-2025

Your trade files have been successfully generated. Click below to download.
[Download Trade Files]

```mermaid
flowchart TD
    A[User Form Input or Minimal Fields] --> B[API Gateway]
    B --> C[Authentication Service]
    C --> D[Fetch Past Trades from DB2]
    D --> E[Prompt Builder Service]
    E --> F[LLM Interaction Service]
    F --> G[LLM Returns Structured Trade Data]
    G --> H[Excel Generator Service]
    H --> I[Generate Excel File Using Template Format]
    I --> J[Storage Service - Upload to Cloud]
    J --> K[Return Download Link to User]
    K --> L[User Downloads or Uploads Final File]

    style A fill:#D6EAF8,stroke:#2E86C1,stroke-width:2px
    style L fill:#D6EAF8,stroke:#2E86C1,stroke-width:2px
    style D fill:#D5F5E3,stroke:#27AE60,stroke-width:2px
    style G fill:#FADBD8,stroke:#C0392B,stroke-width:2px
