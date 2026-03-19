# GigShield — AI-Powered Microinsurance for Gig & Delivery Workers

A full-stack AI-driven microinsurance platform that protects gig economy delivery workers from income loss caused by environmental disruptions — bad weather, traffic congestion, poor air quality, and zone restrictions. It uses real-time external data to automatically assess risk, trigger claims, detect fraud, and process instant payouts.

## Features

- **Real-time AI Disruption Index (ADI)** scoring using live weather, traffic, AQI, and delivery demand data
- **Automatic claim triggering** when disruption exceeds thresholds — zero manual input from workers
- **5-layer AI fraud detection** with GPS validation, activity checks, duplicate detection, pattern analysis, and API verification
- **Instant UPI payouts** via Razorpay — approved claims are paid out in minutes
- **Worker dashboard** with real-time ADI scores, active policies, claim history, and payout tracking
- **Policy management** with affordable microinsurance plans designed for gig workers

## Repository Layout

```
GigShield/
├── client/                    — React.js frontend (worker dashboard & web app)
├── server/                    — Node.js / Express backend (API & business logic)
│   ├── controllers/           — Route handlers
│   ├── models/                — MongoDB schemas
│   ├── routes/                — API endpoints
│   └── services/
│       ├── adiService.js      — ADI score calculation
│       ├── fraudService.js    — Fraud detection engine
│       └── payoutService.js   — Razorpay integration
├── ai-engine/                 — Python ML models
│   ├── adi_model.py           — Disruption Index model
│   └── fraud_model.py         — Fraud detection model
├── docs/                      — Architecture diagrams
└── README.md
```

Key backend files:

- `server/server.js` — application entry
- `server/services/adiService.js` — ADI score computation from external APIs
- `server/services/fraudService.js` — multi-layer fraud detection logic
- `server/services/payoutService.js` — Razorpay payment processing

Frontend entry:

- `client/src/App.js`

## Prerequisites

- Node.js 18+ and npm
- MongoDB
- Python 3.9+
- Razorpay Sandbox Account
- API keys for OpenWeatherMap, AQICN, TomTom Traffic

## Backend Setup

1. Install dependencies:
   ```bash
   cd server
   npm install
   ```

2. Configure environment variables:
   Create a `.env` file in the `server/` directory:
   ```env
   PORT=5000
   MONGODB_URI=mongodb://localhost:27017/gigshield
   RAZORPAY_KEY_ID=your_razorpay_key
   RAZORPAY_SECRET=your_razorpay_secret
   WEATHER_API_KEY=your_openweathermap_key
   AQI_API_KEY=your_aqicn_key
   TRAFFIC_API_KEY=your_tomtom_key
   JWT_SECRET=your_jwt_secret
   ```

3. Run the backend (development):
   ```bash
   npm run dev
   ```

## Frontend Setup

1. Install dependencies and run the React app:
   ```bash
   cd client
   npm install
   npm start
   ```

2. Open the app at `http://localhost:3000`.

## AI Engine Setup

1. Install Python dependencies:
   ```bash
   cd ai-engine
   pip install -r requirements.txt
   ```

2. Run the AI engine:
   ```bash
   python adi_model.py
   ```

## Running End-to-End

1. Start MongoDB.
2. Start the backend (see Backend Setup).
3. Start the frontend (see Frontend Setup).
4. Start the AI engine (see AI Engine Setup).

## Architecture

This project is organised as a full-stack AI-powered insurance platform with clear separation of concerns:

**Client (Frontend):**

- React.js app (`client/`) provides the worker dashboard, policy views, claim history, and real-time ADI score display.

**Server (Backend):**

- Express app (`server/server.js`) handles REST API routes, user authentication, and coordinates between AI engine, database, and payment gateway.
- `adiService.js` fetches real-time data from external APIs (Weather, AQI, Traffic, Demand) and computes the AI Disruption Index.
- `fraudService.js` runs 5-layer fraud detection — GPS validation, worker activity check, duplicate claim detection, historical pattern analysis, and API data verification.
- `payoutService.js` integrates with Razorpay/UPI for instant payouts.

**AI Engine:**

- Python-based ML models compute the ADI score (0–100) from real-time features.
- Fraud detection model scores claims as Low / Medium / High risk.

**Data & Flow:**

1. External APIs (Weather, AQI, Traffic, Delivery Demand, Zone Restrictions) feed real-time data into the system.
2. The AI engine processes these into an **ADI score (0–100)**.
3. When ADI exceeds the threshold (60 for partial, 75 for full payout), a claim is automatically triggered.
4. Every claim passes through the **Fraud Detection Engine** — validated against GPS, activity logs, duplicates, historical patterns, and real API data.
5. Approved claims trigger **instant UPI payouts** via Razorpay to the worker's account.

### ADI Score Thresholds

| ADI Range   | Condition         | Action                            |
|-------------|-------------------|-----------------------------------|
| 0 – 59      | Normal            | No claim triggered                |
| 60 – 75     | High Disruption   | Partial compensation payout       |
| 75 – 100    | Severe Disruption | Full payout automatically triggered |

### Fraud Risk Scoring

| Risk Level     | Action                    |
|----------------|---------------------------|
| Low Risk       | Auto-approve → Instant payment |
| Medium Risk    | Flag for manual review    |
| High Risk      | Reject claim              |

## Architecture Diagrams

**System Architecture:**

![System Architecture](System_Architecture_Diagram.png)

**ADI Model Flow:**

![ADI Model Flow](ADI%20Model%20Flow%20Diagram.png)

**Fraud Detection Pipeline:**

![Fraud Detection Pipeline](Fraud%20Detection%20Pipeline%20Diagram.png)

## Development Notes

- API routes are in `server/routes/` and controller logic in `server/controllers/`.
- ADI computation logic lives in `server/services/adiService.js` and the Python model in `ai-engine/adi_model.py`.
- Fraud detection checks are modular — each layer (GPS, activity, duplicate, pattern, API) can be independently toggled.
- MongoDB stores user profiles, policies, claims, transactions, and audit logs.
- Payment integration uses Razorpay Sandbox for development; switch to production keys for deployment.

## Team

**Team STARK** — Built for the Guidewire Hackathon

## Contributing

Feel free to open issues or pull requests. For local contributions:

- Follow the setup steps above for backend, frontend, and AI engine
- Run linting and tests (add test commands as project grows)
