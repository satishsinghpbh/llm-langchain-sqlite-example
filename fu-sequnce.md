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
