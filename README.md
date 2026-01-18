# Milana-backend (AKSI)

⚠ **Proprietary Project — All Rights Reserved © 2025 Alfiia Bashirova (AKSI Project)**\
Unauthorized use or reproduction is strictly prohibited.

Integrated platform combining the Milana web portal, AKSI DevOps AI Connector, and backend services.

## Overview

This repository integrates functionality from multiple AKSI projects:
- **Milana Web Portal** (`frontend/`): Interactive web interface with 21 AI-powered applications
- **AKSI Signing Infrastructure** (`.aksi/`, `.github/workflows/`): Cryptographic signing for releases
- **Backend API Services**: FastAPI endpoints for AKSI/Milana services

## 🌐 Milana Web Portal

The frontend provides a comprehensive AI superintelligence hub with:

### Core Features
- **Milana Super GPTb**: Free-tier AI engine combining memory, internet orchestration, and GPT integration
- **GPT Integration**: OpenAI API integration with local key storage
- **Long-term Memory**: Persistent conversation memory vault
- **Knowledge Hub**: Multi-source internet data aggregation (Wikipedia, Hacker News, Open Library)

### 21 Interactive Applications

1. **moodmirror** - Mood detection and reflection
2. **mindmirror** - Thought journaling with AI advice
3. **mindlink** - Brain-computer interface simulation
4. **healthscan** - Basic health analysis (pulse, blood pressure)
5. **mentor** - Motivational AI advisor
6. **family** - Family event organizer
7. **aura** - Aura and mood color detection
8. **aksilove** - AI-powered matchmaking
9. **moodradio** - Mood-based music playlists
10. **aksishopping** - Simple shopping cart
11. **aistylist** - Personal style recommendations
12. **ecogaze** - Environmental metrics analyzer
13. **dreamjournal** - Dream diary with local storage
14. **aksicompanion** - Virtual companion with interactions
15. **dressupar** - AR clothes try-on (web demo)
16. **globalid** - Digital ID card generator
17. **aksichat** - Main GPT-powered chat interface
18. **lifescan** - BMI calculator
19. **timecapsule** - Time capsule message creator
20. **telehelp** - Emergency SOS service
21. **storyai** - AI story generator

### Frontend Structure
```
frontend/
├── index.html              # Main portal interface
├── package.json            # Node.js dependencies
├── vitest.config.js        # Test configuration
├── .gitignore             # Frontend-specific ignores
├── scripts/
│   ├── main.js            # Application orchestrator
│   ├── gpt.js             # GPT integration module
│   ├── free-tier.js       # Free-tier engine
│   ├── knowledge.js       # Knowledge hub connectors
│   └── memory.js          # Long-term memory vault
├── styles/
│   └── main.css           # Purple-themed UI styles
├── assets/
│   ├── favicon.svg        # Site icon
│   └── site.webmanifest   # PWA manifest
└── tests/
    ├── gpt.test.js
    ├── free-tier.test.js
    ├── knowledge.test.js
    └── memory.test.js
```

### Running the Frontend
```bash
cd frontend
npm install
npm test                    # Run tests
# Serve index.html with any static server
python -m http.server 8000  # Example
```

## 🔐 AKSI Signing Infrastructure

Cryptographic signing system for release verification (Ed25519 algorithm).

### Files
- `.aksi/manifest.json` - AKSI connector manifest with UID and signing metadata
- `.github/workflows/verify.yml` - GitHub Actions signature verification
- `CODEOWNERS` - Repository ownership (@MILANA808 approval required)
- `NOTICE` - All Rights Reserved notice
- `SECURITY.md` - Security policy and reporting
- `PRIMER.md` - Legal and signing bootstrap documentation

### Signature Verification
GitHub Actions automatically verify signatures on push/PR using:
```bash
python scripts/verify_release.py --root . \
  --pub .aksi/aksi_public_ed25519.pem \
  --sig signature.json
```

⚠️ **Note**: Private key (`~/.aksi/aksi_private_ed25519.pem`) must be stored securely and never committed.

## 🚀 Backend API Endpoints

FastAPI backend for AKSI/Milana services:

### Health & Monitoring
- `GET /health` - Service health check
- `GET /version` - Version information
- `POST /echo` - Echo test endpoint

### AKSI Services
- `GET /aksi/metrics` - System metrics
- `GET /aksi/proof` - AKSI proof retrieval
- `POST /aksi/proof/stable` - Stable proof submission
- `GET /aksi/logs` - Log retrieval
- `POST /aksi/logs/append` - Log appending
- `GET /aksi/logs/export` - Log export

## 📁 Repository Structure

```
.
├── frontend/              # Milana web portal (static site)
├── .aksi/                 # AKSI signing infrastructure
├── .github/workflows/     # CI/CD automation
├── LICENSE                # Proprietary license
├── README.md             # This file
├── NOTICE                # Copyright notice
├── SECURITY.md           # Security policy
├── PRIMER.md             # AKSI bootstrap documentation
└── CODEOWNERS            # Code ownership rules
```

## 🎨 Design Philosophy

The Milana portal features a distinctive **purple superintelligence theme**:
- Deep purple gradients with cosmic aesthetics
- Glassmorphism and backdrop blur effects
- Responsive design optimized for desktop and mobile
- Accessibility-first approach with ARIA labels

## 🧠 Technology Stack

### Frontend
- **Vanilla JavaScript** (ES6 modules)
- **HTML5** with semantic markup
- **CSS3** with custom properties
- **Vitest** for testing
- **Progressive Web App** capabilities

### Knowledge Sources
- Wikipedia (Russian) - Encyclopedic knowledge
- Hacker News - Tech trends and startup news
- Open Library - Books and publications

### GPT Integration
- OpenAI API compatible
- Free-tier fallback mode
- Local key storage (browser localStorage)
- Memory-enhanced conversations

## 📜 License & Contact

**Proprietary License** - All Rights Reserved © 2025 Alfiia Bashirova (AKSI Project)

Unauthorized use, reproduction, or distribution is strictly prohibited.

**Contact**: 716elektrik@mail.ru (Alfiia Bashirova)
For licensing and business inquiries.

## 🔧 Development

### Testing Frontend
```bash
cd frontend
npm install
npm test
```

### Code Ownership
All changes require approval from @MILANA808 (see CODEOWNERS).

### Security
Report security vulnerabilities to: 716elektrik@mail.ru

---

🤖 **Integrated by AI** - Combining milana_site, AKSI-, and Milana-backend repositories into a unified platform.
